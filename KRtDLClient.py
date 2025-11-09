from logging import Logger
import dolphin_memory_engine
import subprocess
import Utils
import asyncio
import multiprocessing
import subprocess
import traceback
import zipfile
import time
import json
import struct
from enum import Enum
from typing import Any, Dict, List, Optional, cast
from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, logger, server_loop, gui_enabled
from NetUtils import ClientStatus, NetworkItem
from .Items import ItemData, item_table

HEADER_ID_ADDRESS = 0x80000000
HUD_MESSAGE_ADDRESS = 0x80EB0BE0
HUD_MESSAGE_DURATION = 10.0
HUD_MAX_MESSAGE_SIZE = 194

INHALE_ADDRESS = 0x8052a448 # Default value is 40820088, 48000088 for disable
FLOAT_ADDRESS = 0x80520ab4 # Default value is 4bfcef51, change to 4bfcef51 for dedede to have it but not kirby, 4bfcef2d to disable only dedede's float and 38600000 to disable both
METAKNIGHT_FLOAT_ADDRESS = 0x805b7d84 # Default value is 41820068, 48000068 for disable
BANDANADEE_FLOAT_ADDRESS = 0x80519598 # Default value is 41820050, 48000050 for disable
SLIDEKICK_ADDRESS = 0x80527cf0 # Default value is 40820010, 48000010 for disable

# ^^^^ these addresses are all redundant due to the Wii's memory system, need to find address chains in order to find consistent addresses for the game's data

BaseLocationID = 24102011 + 40

class ConnectionState(Enum):
    DISCONNECTED = 0
    IN_GAME = 1
    IN_MENU = 2
    MULTIPLE_DOLPHIN_INSTANCES = 3

status_messages = {
    ConnectionState.DISCONNECTED: "Unable to connect to the Dolphin instance. Retrying...",
    ConnectionState.IN_GAME: "Connected to Kirby's Return to Dream Land.",
    ConnectionState.IN_MENU: "Connected to game, waiting for game to start...",
    ConnectionState.MULTIPLE_DOLPHIN_INSTANCES: "Warning: Multiple Dolphin instances detected, client may not function correctly."
}

class NotificationManager:
    notification_queue = []
    time_since_last_message: int = 0
    last_message_time: int = 0
    message_duration: int = None
    send_notification_func = None

    def __init__(self, message_duration, send_notification_func):
        self.message_duration = message_duration / 2  # If there are multiple messages, the duration is shorter
        self.send_notification_func = send_notification_func

    def queue_notification(self, message):
        self.notification_queue.append(message)

    def handle_notifications(self):
        self.time_since_last_message = time.time() - self.last_message_time
        if len(self.notification_queue) > 0 and self.time_since_last_message >= self.message_duration:
            notification = self.notification_queue[0]
            result = self.send_notification_func(notification)
            if result:
                self.notification_queue.pop(0)
                self.last_message_time = time.time()
                self.time_since_last_message = 0

class KRtDLCommandProcessor(ClientCommandProcessor):
    ctx: "KRtDLContext"
    
    def __init__(self, ctx: "KRtDLContext"):
        super().__init__(ctx)

    def _cmd_test_message(self, *args):
        """Send a message to the game interface."""
        self.ctx.notification_manager.queue_notification(' '.join(map(str, args)))

    def _cmd_status(self, *args):
        """Display the current dolphin connection status."""
        logger.info(f"Connection status: {status_messages[self.ctx.connection_state]}")

    def _cmd_deathlink(self):
        """Toggle deathlink from client. Overrides default setting."""
        self.ctx.death_link_enabled = not self.ctx.death_link_enabled
        Utils.async_start(
            self.ctx.update_death_link(self.ctx.death_link_enabled),
            name="Update Deathlink",
        )
        message = (
            f"Deathlink {'enabled' if self.ctx.death_link_enabled else 'disabled'}"
        )
        logger.info(message)
        self.ctx.notification_manager.queue_notification(message)

class InventoryItemData(ItemData):
    """Class used to track the player's current items and their quantities"""
    current_amount: int
    current_capacity: int

    def __init__(self, item_data: ItemData, current_amount: int, current_capacity: int) -> None:
        super().__init__(item_data.name, item_data.id,
                         item_data.classification, item_data.max_capacity)
        self.current_amount = current_amount
        self.current_capacity = current_capacity

class DolphinException(Exception):
    pass

class DolphinInstance:
    dolphin: dolphin_memory_engine
    logger: Logger
    
    def __init__(self, logger):
        self.dolphin = dolphin_memory_engine
        self.logger = logger

    def is_connected(self):
        try:
            self.__assert_connected()
            return True
        except Exception:
            return False

    def connect(self):
        if not self.dolphin.is_hooked():
            self.dolphin.hook()
        if not self.dolphin.is_hooked():
            raise DolphinException("Verify that you have the game running in Dolphin. Retrying...")

    def disconnect(self):
        if self.dolphin.is_hooked():
            self.dolphin.un_hook()

    def __assert_connected(self):
        """Custom assert function that returns a DolphinException instead of a generic RuntimeError if the connection is lost"""
        try:
            self.dolphin.assert_hooked()
            # For some reason the dolphin_memory_engine.is_hooked() function doesn't recognize when the game is closed, checking if memory is available will assert the connection is alive
            self.dolphin.read_bytes(HEADER_ID_ADDRESS, 0)
        except RuntimeError as e:
            self.disconnect()
            raise DolphinException(e)

    def verify_target_address(self, target_address: int, read_size: int):
        """Ensures that the target address is within the valid range for GC memory"""
        if target_address < 0x80000000 or (target_address + read_size > 0x81800000 and target_address + read_size < 0x90000000) or target_address + read_size > 0x93FFFFF0:
            raise DolphinException(
                f"{target_address:x} -> {target_address + read_size:x} is not a valid memory address. Please write between the range of 0x80000000 and 0x81800000 and 0x90000000 and 0x93FFFFF0."
            )

    def read_pointer(self, pointer, offset, byte_count):
        self.__assert_connected()

        address = None
        try:
            address = self.dolphin.follow_pointers(pointer, [0])
        except RuntimeError:
            return None

        if not self.dolphin.is_hooked():
            self.logger.info(f"Dolphin no longer connected.")
            raise DolphinException("Dolphin no longer connected")

        address += offset
        return self.read_address(address, byte_count)

    def read_address(self, address, bytes_to_read):
        self.__assert_connected()
        self.verify_target_address(address, bytes_to_read)
        result = self.dolphin.read_bytes(address, bytes_to_read)
        return result

    def write_pointer(self, pointer, offset, data):
        self.__assert_connected()
        address = None
        try:
            address = self.dolphin.follow_pointers(pointer, [0])
        except RuntimeError:
            return None

        if not self.dolphin.is_hooked():
            self.logger.info(f"Dolphin no longer connected.")
            raise DolphinException("Dolphin no longer connected.")

        address += offset
        return self.write_address(address, data)

    def write_address(self, address, data):
        self.__assert_connected()
        result = self.dolphin.write_bytes(address, data)
        return result

class DolphinBridge:
    dolphin_client: DolphinInstance
    connection_status: str
    logger: Logger
    _previous_message_size: int = 0
    # game_state_pointer
    # cstate_manager_global
    # cplayer_vtable: None
    game_id_error: str = None
    current_game: str = None

    def __init__(self, logger) -> None:
        self.logger = logger
        self.dolphin_client = DolphinInstance(logger)

    def connect_to_game(self):
        """Initializes the connection to dolphin and verifies it is connected to Kirby's Return to Dream Land"""
        try:
            self.dolphin_client.connect()
            self.logger.info("Connected to Dolphin Emulator.")
            game_id = ""
            # The first read of the address will be null if the client is faster than the emulator
            self.dolphin_client.read_address(HEADER_ID_ADDRESS, 0)
            game_id = self.dolphin_client.read_address(HEADER_ID_ADDRESS, 6).decode("utf-8")
            self.current_game = None
            if game_id == "SUKE01":
                self.current_game = game_id
                self.logger.info("Successfully found SUKE01.")
            else:
                self.logger.warn(
                    f"Strange header detected. Please provide a blank US RVZ of Return to Dream Land.")
                self.game_id_error = game_id
        except DolphinException:
            pass

    def disconnect_from_game(self):
        self.dolphin_client.disconnect()
        self.logger.info("Disconnected from Dolphin Emulator.")

    def get_item(self, item_id: int) -> InventoryItemData:
        for item in item_table.values():
            if item.id == item_id:
                return self.get_item(item)
        return None

    def get_current_inventory(self) -> dict[str, InventoryItemData]:
        MAX_VANILLA_ITEM_ID = 39
        inventory: dict[str, InventoryItemData] = {}
        for item in item_table.values():
            if item.id <= MAX_VANILLA_ITEM_ID:
                inventory[item.name] = self.get_item(item)
        return inventory
    
    def get_connection_state(self):
        try:
            connected = self.dolphin_client.is_connected()
            if not connected or self.current_game is None:
                return ConnectionState.DISCONNECTED
            elif self.is_in_playable_state():
                return ConnectionState.IN_GAME
            else:
                return ConnectionState.IN_MENU
        except DolphinException:
            return ConnectionState.DISCONNECTED

    def is_in_playable_state(self) -> bool:
        """ Check if the player is in the actual game rather than the main menu """
        return True # for now just assume that the menu is it and it's all good cuz setting this up needs some RAM addresses

    def send_hud_message(self, message: str) -> bool:
        message = f"&just=center;{message}"
        current_value = self.dolphin_client.read_address(HUD_MESSAGE_ADDRESS, 1)
        if current_value == b"\x01":
            return False
        self._save_message_to_memory(message)
        self.dolphin_client.write_address(HUD_MESSAGE_ADDRESS, b"\x01")
        return True

    def _save_message_to_memory(self, message: str):
        encoded_message = message.encode(
            "utf-16_be")[: HUD_MAX_MESSAGE_SIZE]

        if len(encoded_message) == self._previous_message_size:
            encoded_message += b"\x00 "  # Add a space to the end of the message to force the game to update the message if it is the same size

        self._previous_message_size = len(encoded_message)

        encoded_message += b"\x00\x00"  # Game expects a null terminator at the end of the message

        if len(encoded_message) & 3:
            # Ensure the size is a multiple of 4
            num_to_align = (len(encoded_message) | 3) - \
                len(encoded_message) + 1
            encoded_message += b"\x00" * num_to_align

        self.dolphin_client.write_address(HUD_MESSAGE_ADDRESS, encoded_message)

    def reset_relay_tracker_cache(self):
        self.relay_trackers = None

class KRtDLContext(CommonContext):
    game = "Kirby's Return to Dream Land"
    command_processor = KRtDLCommandProcessor
    notification_manager: NotificationManager
    dolphin_bridge: DolphinBridge
    items_handling = 0b111
    dolphin_sync_task = Optional[asyncio.Task[Any]] = None
    connection_state = ConnectionState.DISCONNECTED
    slot_data: Dict[str, Utils.Any] = {}
    death_link_enabled = False
    slot_name: Optional[str] = None
    last_error_message: Optional[str] = None
    krtdl_file: Optional[str] = None

    def __init__(self, server_address: str, password: str, krtdl_file: Optional[str] = None):
        super().__init__(server_address, password)
        self.game_interface = DolphinBridge(logger)
        self.notification_manager = NotificationManager(HUD_MESSAGE_DURATION, self.game_interface.send_hud_message)
        self.krtdl_file = krtdl_file
    
    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(KRtDLContext, self).server_auth(password_requested)
        await self.get_username()
        self.tags = set()
        await self.send_connect()

    def on_deathlink(self, data: Utils.Dict[str, Utils.Any]) -> None:
        super().on_deathlink(data)
        # fire the death call here
    
    def on_package(self, cmd: str, args: Dict[str, Any]) -> None:
        if cmd == "Connected":
            self.slot_data = args["slot_data"]
            if "death_link" in args["slot_data"]:
                self.death_link_enabled = bool(args["slot_data"]["death_link"])
                Utils.async_start(self.update_death_link(bool(args["slot_data"]["death_link"])))
    
    def run_gui(self):
        from kvui import GameManager

        class KRtDLManager(GameManager):
            logging_pairs = [("Client", "Archipelago")]
            base_title = "Archipelago Kirby's Return to Dream Land Client"

        self.ui = KRtDLManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

def update_connection_status(ctx: KRtDLContext, status):
    if ctx.connection_state == status:
        return
    else:
        logger.info(status_messages[status])
        if get_num_dolphin_instances() > 1:
            logger.info(status_messages[ConnectionState.MULTIPLE_DOLPHIN_INSTANCES])
        ctx.connection_state = status

def assert_no_running_dolphin() -> bool:
    """Only checks on windows for now, verifies no existing instances of dolphin are running."""
    if Utils.is_windows:
        if get_num_dolphin_instances() > 0:
            return False
    return True


def get_num_dolphin_instances() -> int:
    """Only checks on windows for now, kind of brittle so if it causes problems then just ignore it"""
    try:
        if Utils.is_windows:
            output = subprocess.check_output("tasklist", shell=True).decode()
            lines = output.strip().split("\n")
            count = sum("Dolphin.exe" in line for line in lines)
            return count
        return 0
    except:
        return 0

async def dolphin_sync_task(ctx: KRtDLContext):
    try:
        # This will not work if the client is running from source
        version = get_apworld_version()
        logger.info(f"Using krtdl.apworld version: {version}")
    except:
        pass

    if ctx.krtdl_file:
        Utils.async_start(patch_and_run_game(ctx.krtdl_file))

    logger.info("Starting Dolphin Connector, attempting to connect to emulator...")

    while not ctx.exit_event.is_set():
        try:
            connection_state = ctx.DolphinBridge.get_connection_state()
            update_connection_status(ctx, connection_state)
            if connection_state == ConnectionState.IN_MENU:
                await handle_check_goal_complete(
                    ctx
                )  # It will say the player is in menu sometimes
            if connection_state == ConnectionState.IN_GAME:
                await _handle_game_ready(ctx)
            else:
                await _handle_game_not_ready(ctx)
                await asyncio.sleep(1)
        except Exception as e:
            if isinstance(e, DolphinException):
                logger.error(str(e))
            else:
                logger.error(traceback.format_exc())
            await asyncio.sleep(3)
            continue

def inventory_item_by_network_id(network_id: int, current_inventory: dict[str, InventoryItemData]) -> InventoryItemData:

    for item in current_inventory.values():
        if item.code == network_id:
            return item

    # Handle custom items like missile launcher and main power bomb
    # for key, value in custom_suit_upgrade_table.items():
    #     if value.code == network_id:
    #         return InventoryItemData(value, 0, 0)
    return None

async def handle_receive_items(ctx: 'KRtDLContext', current_items: dict[str, InventoryItemData]):
    logger.info("unfinished handle items")
    for network_item in ctx.items_received:
        item_data = inventory_item_by_network_id(
            network_item.item, current_items)
        if item_data is None:
            continue
        # if item_data.name == "Missile Launcher":
            # continue
        # elif item_data.name == "Power Bomb (Main)":
            # continue

        # Handle Single Item Upgrades
        if item_data.max_capacity == 1 and item_data.current_amount == 0:
            ctx.dolphin_bridge.give_item_to_player(item_data.id, 1, 1)
            if network_item.player != ctx.slot:
                receipt_message = "online" # receipt_message = "online" if not item_data.name.startswith("Artifact") else "received"
                ctx.notification_manager.queue_notification(f"{item_data.name} {receipt_message} ({ctx.player_names[network_item.player]})")
        elif item_data.max_capacity > 1:
            continue

    # Handle repeat pickups

    # await handle_receive_missiles(ctx, current_items)
    # await handle_receive_power_bombs(ctx, current_items)
    # await handle_receive_energy_tanks(ctx, current_items)

    # Handle Artifacts
    # ctx.game_interface.sync_artifact_layers()

async def handle_checked_location(ctx: KRtDLContext, current_inventory: dict[str, InventoryItemData]):
    """Uses the current amount of UnknownItem1 in inventory as an indicator of which location was checked. This will break if the player collects more than one pickup without having the AP client hooked to the game and server"""
    logger.info("unfinished location handler")
    # unknown_item1 = current_inventory["UnknownItem1"]
    # if (unknown_item1.current_capacity == 0):
    #     return
    # checked_location_id = BaseLocationID + \
    #     unknown_item1.current_capacity - 1
    # await ctx.send_msgs([{"cmd": "LocationChecks", "locations": [checked_location_id]}])
    # ctx.dolphin_bridge.give_item_to_player(unknown_item1.id, 0, 0)

async def handle_check_goal_complete(ctx: KRtDLContext):
    # if ctx.game_interface.current_game is not None:
        # need to find the memory locations in RAM for states I can work with for this

    logger.info(f"yippee cool you win I haven't actually made this do anything yet")
    
        # current_level = ctx.game_interface.get_current_level()
        # if current_level == MetroidPrimeLevel.End_of_Game:
            # await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])

async def handle_check_deathlink(ctx: KRtDLContext):
    # need to find the memory locations in RAM for states I can work with for this

    logger.info(f"are you dead yet")
    
    # health = ctx.game_interface.get_current_health()
    # if health <= 0 and ctx.is_pending_death_link_reset == False:
        # await ctx.send_death(ctx.player_names[ctx.slot] + " ran out of energy.")
        # ctx.is_pending_death_link_reset = True
    # elif health > 0 and ctx.is_pending_death_link_reset == True:
        # ctx.is_pending_death_link_reset = False

async def _handle_game_ready(ctx: KRtDLContext):
    if ctx.server:
        if not ctx.slot:
            await asyncio.sleep(1)
            return
        current_inventory = ctx.dolphin_bridge.get_current_inventory()
        await handle_receive_items(ctx, current_inventory)
        ctx.notification_manager.handle_notifications()
        await handle_checked_location(ctx, current_inventory)
        await handle_check_goal_complete(ctx)

        if ctx.death_link_enabled:
            await handle_check_deathlink(ctx)
        await asyncio.sleep(0.5)
    else:
        logger.info("Waiting for player to connect to server.")
        await asyncio.sleep(1)


async def _handle_game_not_ready(ctx: KRtDLContext):
    """If the game is not connected or not in a playable state, this will attempt to retry connecting to the game."""
    ctx.dolphin_bridge.reset_relay_tracker_cache()
    if ctx.connection_state == ConnectionState.DISCONNECTED:
        ctx.dolphin_bridge.connect_to_game()
    elif ctx.connection_state == ConnectionState.IN_MENU:
        await asyncio.sleep(3)


async def run_game(romfile):
    auto_start = Utils.get_options()["krtdl_options"].get("rom_start", True)

    if auto_start is True and assert_no_running_dolphin():
        import webbrowser
        webbrowser.open(romfile)
    elif os.path.isfile(auto_start) and assert_no_running_dolphin():
        subprocess.Popen(
            [str(auto_start), romfile],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

def get_version_from_rvz(path: str) -> str:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Couldn't get version for rvz {path}!")
    with open(path, "rb") as f:
        game_id = f.read(0).decode("utf-8")
        if game_id == "SUKE01":
            return "SUKE01"
        else:
            raise Exception("Strange header detected. Ensure you are using a blank US RVZ of Return to Dream Land.")

async def patch_and_run_game(krtdl_file: str):
    krtdl_file = os.path.abspath(krtdl_file)
    input_rvz_path = Utils.get_options()["krtdl_options"]["rom_file"]
    game_version = get_version_from_rvz(input_rvz_path)
    base_name = os.path.splitext(krtdl_file)[0]
    output_path = base_name + '.rvz'

    if not os.path.exists(output_path):
        if not zipfile.is_zipfile(krtdl_file):
            raise Exception(f"Invalid krtdl file: {krtdl_file}")

        config_json_file = None
        if zipfile.is_zipfile(krtdl_file):
            for name in zipfile.ZipFile(krtdl_file).namelist():
                if name == 'config.json':
                    config_json_file = name
                    break

        config_json = None
        with zipfile.ZipFile(krtdl_file) as zip_file:
            with zip_file.open(config_json_file) as file:
                config_json = file.read().decode("utf-8")
                config_json = json.loads(config_json)

        # config_json["gameConfig"]["updateHintStateReplacement"] = construct_hud_message_patch(game_version)

    
        # this is the point where the RVZ must be patched                    py_randomprime.patch_iso(input_rvz_path, output_path, config_json, notifier)
    

    Utils.async_start(run_game(output_path))


def launch():
    Utils.init_logging("Kirby's Return to Dream Land Client")

    async def main():
        multiprocessing.freeze_support()
        logger.info("main")
        parser = get_base_parser()
        parser.add_argument('krtdl_file', default="", type=str, nargs="?",
                            help='Path to an krtdl file')
        args = parser.parse_args()

        ctx = KRtDLContext(args.connect, args.password)
        
        if args.krtdl_file:
            logger.info("KRTDL file supplied, beginning patching process...")
            Utils.async_start(patch_and_run_game(args.krtdl_file))
            
        logger.info("Connecting to server...")
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="Server Loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        logger.info("Running game...")
        ctx.dolphin_sync_task = asyncio.create_task(dolphin_sync_task(ctx), name="Dolphin Sync")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await ctx.shutdown()

        if ctx.dolphin_task:
            await asyncio.sleep(3)
            await ctx.dolphin_sync_task

    import colorama

    colorama.init()

    asyncio.run(main())
    colorama.deinit()


if __name__ == '__main__':
    launch()

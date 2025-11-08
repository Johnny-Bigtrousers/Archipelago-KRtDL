# HEY BIG DOOFUS YOU NEED TO MAKE THE KRTDL FOLDER THAT ALL OF THIS IS IN TO BE INSIDE OF ANOTHER FOLDER CALLED KRTDL AND THEN TURN IT INTO A ZIP ARCHIVE THEN CHANGE THE EXTENSION TO .APWORLD

import os
import settings
import struct
import zipfile
import typing
from typing import TYPE_CHECKING, Any, Dict, List, Optional
from logging import info
from .Items import KRtDLItems, item_table
from .Locations import KRtDLLocations, composite_location
from .Options import KRtDLOptions, krtdl_option_groups
from .Config import make_config
from worlds.AutoWorld import World, WebWorld
from worlds.Files import APPlayerContainer
from worlds.LauncherComponents import Component, SuffixIdentifier, Type, icon_paths, components, launch_subprocess
from BaseClasses import MultiWorld, Region, Location, Entrance, Item, Tutorial, ItemClassification
from Utils import local_path

BaseID = 24102011

if TYPE_CHECKING:
    from ppc_asm.assembler.ppc import GeneralRegister  # type: ignore

class MultiworldWithPassthrough(MultiWorld):
    re_gen_passthrough: Dict[str, Dict[str, Any]] = {}

def run_client(url: Optional[str] = None):
    from .KRtDLClient import launch
    launch_subprocess(launch, name="KRtDLClient")

components.append(
    Component("Kirby's Return to Dream Land Client", func=run_client, component_type=Type.CLIENT, icon='krtdlicon',
              file_identifier=SuffixIdentifier(".krtdl"))
)

icon_paths['krtdlicon'] = f"ap:{__name__}/krtdlicon.png"

class KRtDLSettings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the Kirby's Return to Dream Land RVZ"""
        description = "KRtDL RVZ file"
        copy_to = "Kirby's Return to Dream Land (USA) (En,Fr,Es).rvz"

    class RomStart(str):
        """
        Set this to false to never autostart an rvz (such as after patching),
        Set it to true to have the operating system default program open the rvz
        Alternatively, set a path to Dolphin to open the .rvz file with.
        """

    rom_file: RomFile = RomFile(RomFile.copy_to)
    rom_start: typing.Union[RomStart, bool] = False

class KRtDLWeb(WebWorld):
    theme = "grassFlowers"
    rich_text_options_doc = True
    option_groups = krtdl_option_groups
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Kirby's Return to Dream Land for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Trodgy"]
    )]

class KRtDLContainer(APPlayerContainer):
    game: str = "Kirby's Return to Dream Land"

    def __init__(
        self, 
        config_json: str, 
        options_json: str, 
        outfile_name: str, 
        output_directory: str,
        player: Optional[int] = None, 
        player_name: str = "", 
        server: str = ""):
            
        self.config_json = config_json
        self.config_path = "config.json"
        self.options_path = "options.json"
        self.options_json = options_json
        container_path = os.path.join(output_directory, outfile_name + ".krtdl")
        super().__init__(container_path, player, player_name, server)

    def write_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        opened_zipfile.writestr(self.config_path, self.config_json)
        opened_zipfile.writestr(self.options_path, self.options_json)
        super().write_contents(opened_zipfile)

class KRtDLWorld(World):
    """
    Also known as Kirby's Adventure Wii in PAL regions.
    
    The tough puff Kirby is back for a 1-4 player platforming adventure across Planet Popstar. 
    Help the mysterious far-flung traveler Magolor rebuild his ship and return to his home planet of Halcandra.
    """

    game = "Kirby's Return to Dream Land"
    web = KRtDLWeb()
    required_client_version = (0, 6, 4)
    options_dataclass = KRtDLOptions
    options: KRtDLOptions
    topology_present = True
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = composite_location

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)

    def generate_output(self, output_directory: str) -> None:
        # if self.options.randomize_suit_colors:
            # options: List[VariaSuitColorOverride] = [self.options.power_suit_color, self.options.varia_suit_color, self.options.gravity_suit_color, self.options.phazon_suit_color]
            # for option in options:
                # if option.value == 0:
                    # option.value = self.random.randint(1, 35) * 10

        import json
        configjson = make_config(self)
        configjsons = json.dumps(configjson, indent=4)
        # Check if the environment variable 'DEBUG' is set to 'True'
        if os.environ.get('DEBUG') == 'True':
            with open("test_config.json", "w") as f:
                f.write(configjsons)

        # convert configjson to json
        
        options_json = json.dumps(options_dict, indent=4)
        outfile_name = self.multiworld.get_out_file_name_base(self.player)
        krtdl = KRtDLContainer(configjsons, options_json, outfile_name, output_directory, player=self.player, player_name=self.player_name)
        krtdl.write()

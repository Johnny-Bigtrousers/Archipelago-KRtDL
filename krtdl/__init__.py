# HEY BIG DOOFUS YOU NEED TO MAKE THE KRTDL FOLDER THAT ALL OF THIS IS IN TO BE INSIDE OF ANOTHER FOLDER CALLED KRTDL AND THEN TURN IT INTO A ZIP ARCHIVE THEN CHANGE THE EXTENSION TO .APWORLD

from worlds.LauncherComponents import Component, SuffixIdentifier, Type, components, launch_subprocess
import settings
import struct
import typing
from typing import Any, Dict, List, Optional
from logging import info
import os
from .Items import KRtDLItems
from .Locations import KRtDLLocations, composite_location
from .Options import KRtDLOptions, create_option_groups
from worlds.AutoWorld import World, WebWorld
from worlds.Files import APContainer
from BaseClasses import Region, Location, Entrance, Item, Tutorial, ItemClassification

BaseID = 24102011

def run_client(url: Optional[str] = None):
    from .KRtDLClient import launch
    launch_subprocess(launch, name="KRtDLClient")

components.append(
    Component("Kirby's Return to Dream Land Client", func=run_client, component_type=Type.CLIENT,
              file_identifier=SuffixIdentifier(".krtdl"))
)

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
    option_groups = create_option_groups()
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Kirby's Return to Dream Land for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Trodgy"]
    )]

class KRtDLContainer(APContainer):
    game: str = "Kirby's Return to Dream Land"

    def __init__(self, config_json: str, outfile_name: str, output_directory: str,
                 player=None, player_name: str = "", server: str = ""):
        self.config_json = config_json
        self.config_path = "config.json"
        container_path = os.path.join(output_directory, outfile_name + ".apmp1")
        super().__init__(container_path, player, player_name, server)

    def write_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        opened_zipfile.writestr(self.config_path, self.config_json)
        super().write_contents(opened_zipfile)

class KRtDLWorld(World):
    """
    Also known as Kirby's Adventure Wii in PAL regions.
    The tough puff Kirby is back for a 1-4 player platforming adventure across Planet Popstar. 
    Help the mysterious cosmic traveler Magolor rebuild his ship and return to his home planet Halcandra.
    """

    game = "Kirby's Return to Dream Land"
    web = KRtDLWeb
    options_dataclass = KRtDLOptions
    options: KRtDLOptions
    topology_present = True
    location_name_to_id = composite_location

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

        outfile_name = self.multiworld.get_out_file_name_base(self.player)
        krtdl = KRtDLContainer(configjsons, outfile_name, output_directory, player=self.player, player_name=self.multiworld.get_player_name(self.player))
        krtdl.write()

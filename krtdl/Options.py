from typing import List, TYPE_CHECKING, Dict, Any
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, Range, Toggle, DeathLink, DefaultOnToggle, OptionGroup, OptionSet

def create_option_groups() -> List[OptionGroup]:
    option_group_list: List[OptionGroup] = []
    for name, options in krtdl_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list

class Goal(Choice):
    """Determines the goal for your run.
    
    Main Complete - Complete the Main mode by defeating the final boss.
    The Arena - Complete The Arena.
    Extra Complete - Complete the Extra mode by defeating the EX final boss.
    The True Arena - Complete The True Arena.
    Energy Sphere Hunt - Collect a set number of Energy Spheres.
    Perfectionist - Obtain every available check. [Adapts to Sanity options]"""
    display_name = "Goal"
    default = 0
    option_main_complete = 0
    option_the_arena = 1
    option_extra_complete = 2
    option_the_true_arena = 3
    option_energy_sphere_hunt = 4
    option_perfectionist = 5

class EnergySphereHuntRequirement(Range):
    """Determines how many Energy Spheres are necessary to achieve the Energy Sphere Hunt goal.
    [Note that setting the goal over 120 will require playing through Extra mode]
    [Will force Energy Spheres in Extra mode to become checks if over 120 regardless of Extrasanity status]"""
    display_name = "Energy Sphere Hunt Requirement"
    range_start = 1
    range_end = 240
    default = 80

class ShuffleCookieCountry(DefaultOnToggle):
    """If enabled, allows Cookie Country to be shuffled with other worlds."""
    display_name = "Shuffle Cookie Country"

class ShuffleRaisinRuins(DefaultOnToggle):
    """If enabled, allows Raisin Ruins to be shuffled with other worlds."""
    display_name = "Shuffle Raisin Ruins"

class ShuffleOnionOcean(DefaultOnToggle):
    """If enabled, allows Onion Ocean to be shuffled with other worlds."""
    display_name = "Shuffle Onion Ocean"

class ShuffleWhiteWafers(DefaultOnToggle):
    """If enabled, allows White Wafers to be shuffled with other worlds."""
    display_name = "Shuffle White Wafers"

class ShuffleNuttyNoon(DefaultOnToggle):
    """If enabled, allows Nutty Noon to be shuffled with other worlds."""
    display_name = "Shuffle Nutty Noon"

class ShuffleEggEngines(DefaultOnToggle):
    """If enabled, allows Egg Engines to be shuffled with other worlds."""
    display_name = "Shuffle Egg Engines"

class ShuffleDangerousDinner(DefaultOnToggle):
    """If enabled, allows Dangerous Dinner to be shuffled with other worlds."""
    display_name = "Shuffle Dangerous Dinner"

class StartingWorld(Choice):
    """Determines the first world of your run. Default is Cookie Country."""
    display_name = "Starting World"
    default = 0
    option_cookie_country = 0
    option_raisin_ruins = 1
    option_onion_ocean = 2
    option_white_wafers = 3
    option_nutty_noon = 4
    option_egg_engines = 5
    option_dangerous_dinner = 6

class UnlockWorlds(Toggle):
    """Unlocks all of the worlds from the start.
    [Some worlds may be locked out by Lor Starcutter access]"""
    display_name = "Unlock Worlds"

class ShuffleStages(Choice):
    """Shuffles the game's stages around.
    
    Light - Shuffles stages within a given world.
    Intense - Shuffles all of the game's stages with eachother."""
    display_name = "Shuffle Stages"
    default = 0
    option_off = 0
    option_light = 1
    option_intense = 2

class UnlockStages(Toggle):
    """Unlocks all of the non-boss stages from the start. Beating all of a level's stages unlocks the boss stage slot."""
    display_name = "Unlock Worlds"

class ShuffleBossStages(Toggle):
    """Shuffles the game's boss stages around.
    [If Shuffle Stages is turned on to Intense then boss stages can possibly end up in other worlds]"""
    display_name = "Shuffle Boss Stages"

class ShuffleBosses(Choice):
    """Shuffles the game's bosses around excluding Another Dimension.
    
    Light - Bosses will be shuffled with eachother.
    Anomalous - Randomizes boss fights out of the game's possible ones."""
    display_name = "Shuffle Bosses"
    default = 0
    option_off = 0
    option_light = 1
    option_anomalous = 2

class ShuffleEnemies(Choice):
    """Shuffles the game's enemies around excluding Another Dimension.
    
    Light - Enemies will be shuffled with eachother within a given stage's pool.
    Intense - Enemies will be shuffled with eachother within the entire game's pool.
    Anomalous - Randomizes enemies out of the game's possible ones. [CREATES HARDER SEEDS]"""
    display_name = "Shuffle Enemies"
    default = 0
    option_off = 0
    option_light = 1
    option_intense = 2
    option_anomalous = 3

class ShuffleCopyAbilities(Toggle):
    """Shuffles what enemies give what copy abilities."""
    display_name = "Shuffle Copy Abilities"

class RandomizeCopyAbilities(Toggle):
    """Requires individual Copy Abilities to be unlocked to be able to obtain them."""
    display_name = "Randomize Copy Abilities"

class RandomizeLandia(Toggle):
    """Requires you to find Landia in order to enter Another Dimension."""
    display_name = "Randomize Landia"

class RandomizeMoves(Toggle):
    """If enabled, requires some of Kirby's basic moves to be unlocked to be able to use them."""
    display_name = "Randomize Moves"

class RandomizeItems(Toggle):
    """Requires items such as Invincibility Candy or the Crackler to be unlocked to be able to obtain them."""
    display_name = "Randomize Items"

class EnergySphereSanity(Toggle):
    """Turns all Energy Spheres into checks.
    [Total checks added: 120]"""
    display_name = "Energy Spheresanity"

class PartSphereSanity(Toggle):
    """Turns all Part Spheres into checks.
    [May cause BKs related to the Lor Starcutter]
    [Total checks added: 5]"""
    display_name = "Part Spheresanity"

class StarSanity(Toggle):
    """Turns all guaranteed Gold Stars (ones not gained from Flowers) into checks.
    [WARNING: ADDS A GIGANTIC NUMBER OF CHECKS AND CREATES SOME VERY HARD SEEDS]
    [MAY RESULT IN FRIENDS YELLING AT YOU FOR PICKING UP HUNDREDS OF STARS IN THEIR WORLD]"""
    display_name = "Starsanity"

class RedStarSanity(Toggle):
    """Turns all Red Stars into checks."""
    display_name = "Red Starsanity"

class BlueStarSanity(Toggle):
    """Turns all Blue Stars into checks."""
    display_name = "Blue Starsanity"

class FoodSanity(Toggle):
    """Turns all guaranteed Food items (ones not gained from Flowers and exluding Maxim Tomatoes) into checks."""
    display_name = "Foodsanity"

class OneUpSanity(Toggle):
    """Turns all 1-Ups into checks."""
    display_name = "1-Upsanity"

class MaximSanity(Toggle):
    """Turns all Maxim Tomatoes into checks."""
    display_name = "Maximsanity"

class ExtraSanity(Toggle):
    """Effectively doubles the number of checks by replicating all of Main mode's checks to Extra Mode uniquely.
    [WARNING: ADDS AN OBSCENE NUMBER OF EXTRA CHECKS AND MAY REQUIRE TWO FULL PLAYTHROUGHS OF THE GAME]
    [MAY RESULT IN A GRUELING ENDURANCE TEST]"""
    display_name = "Extrasanity"

class TrapChance(Range):
    """The chance for any junk item in the pool to be replaced by a trap."""
    display_name = "Trap Chance"
    range_start = 0
    range_end = 100
    default = 0

class SleepWeight(Range):
    """The weight of Sleep traps in the trap pool.
    Forces all players to use Sleep if possible."""
    display_name = "Sleep Weight"
    range_start = 0
    range_end = 100
    default = 40

class EjectWeight(Range):
    """The weight of Eject traps in the trap pool.
    Forces all players to eject their abilities."""
    display_name = "Eject Weight"
    range_start = 0
    range_end = 100
    default = 20

class MouthfulWeight(Range):
    """The weight of Mouthful traps in the trap pool.
    Puts a junk item in Kirby's mouth which disables some of his moves."""
    display_name = "Mouthful Weight"
    range_start = 0
    range_end = 100
    default = 40


@dataclass
class KRtDLOptions(PerGameCommonOptions):
    Goal:                         Goal
    EnergySphereHuntRequirement:  EnergySphereHuntRequirement
    ShuffleCookieCountry:         ShuffleCookieCountry
    ShuffleRaisinRuins:           ShuffleRaisinRuins
    ShuffleOnionOcean:            ShuffleOnionOcean
    ShuffleWhiteWafers:           ShuffleWhiteWafers
    ShuffleNuttyNoon:             ShuffleNuttyNoon
    ShuffleEggEngines:            ShuffleEggEngines
    ShuffleDangerousDinner:       ShuffleDangerousDinner
    StartingWorld:                StartingWorld
    UnlockWorlds:                 UnlockWorlds

    ShuffleStages:            ShuffleStages
    ShuffleBossStages:        ShuffleBossStages
    ShuffleBosses:            ShuffleBosses
    ShuffleEnemies:           ShuffleEnemies
    
    ShuffleCopyAbilities:     ShuffleCopyAbilities
    RandomizeCopyAbilities:   RandomizeCopyAbilities
    RandomizeLandia: RandomizeLandia
    RandomizeMoves:           RandomizeMoves
    RandomizeItems:           RandomizeItems

    StarSanity:               StarSanity
    RedStarSanity:            RedStarSanity
    BlueStarSanity:           BlueStarSanity
    FoodSanity:               FoodSanity
    OneUpSanity:              OneUpSanity
    MaximSanity:              MaximSanity

    TrapChance:               TrapChance
    SleepWeight:              SleepWeight
    EjectWeight:              EjectWeight
    MouthfulWeight:           MouthfulWeight

    death_link:               DeathLink

krtdl_option_groups: Dict[str, List[Any]] = {
    "Basic Options": [Goal, EnergySphereHuntRequirement, ShuffleCookieCountry, ShuffleRaisinRuins, ShuffleOnionOcean, ShuffleWhiteWafers, ShuffleNuttyNoon, ShuffleEggEngines, ShuffleDangerousDinner, StartingWorld, UnlockWorlds],

    "Stage Options": [ShuffleStages, ShuffleBossStages, ShuffleBosses, ShuffleEnemies],

    "Item Options": [ShuffleCopyAbilities, RandomizeCopyAbilities, RandomizeLandia, RandomizeMoves, RandomizeItems],

    "Sanity Options": [StarSanity, RedStarSanity, BlueStarSanity, FoodSanity, OneUpSanity, MaximSanity],

    "Trap Options": [TrapChance, SleepWeight, EjectWeight, MouthfulWeight]
}

data_options: List[str] = [
    "Goal",
    "EnergySphereHuntRequirement",
    "ShuffleCookieCountry",
    "ShuffleRaisinRuins",
    "ShuffleOnionOcean",
    "ShuffleWhiteWafers",
    "ShuffleNuttyNoon",
    "ShuffleEggEngines",
    "ShuffleDangerousDinner",
    "StartingWorld",
    "UnlockWorlds",
    "ShuffleStages",
    "ShuffleBossStages",
    "ShuffleBosses",
    "ShuffleEnemies",
    "ShuffleCopyAbilities",
    "RandomizeCopyAbilities",
    "RandomizeLandia",
    "RandomizeMoves",
    "RandomizeItems",
    "StarSanity",
    "RedStarSanity",
    "BlueStarSanity",
    "FoodSanity",
    "OneUpSanity",
    "MaximSanity",

    "death_link",
]

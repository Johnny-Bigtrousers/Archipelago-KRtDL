from BaseClasses import Item, ItemClassification
from enum import Enum

class ItemNames(Enum):
    gold_star = "Gold Star"
    red_star = "Red Star"
    blue_star = "Blue Star"
    one_up = "1-Up"
    food_pickup = "Food Pickup"
    m_tomato = "Maxim Tomato"
    energy_sphere = "Energy Sphere"
    part_sphere = "Part Sphere"
    energy_sphere_ex = "Extra Energy Sphere"
    part_sphere_ex = "Extra Part Sphere"
    sleep_trap = "Sleep Trap"
    eject_trap = "Eject Trap"
    mouthful_trap = "Mouthful Trap"


BaseID = 24102011

class KRtDLItems(Item):
    game: str = "Kirby's Return to Dream Land"

class ItemData:
    name: str
    code: int
    classification: ItemClassification
    max_capacity: int
    id: int

    def __init__(self, name: str, id: int, progression: ItemClassification, max_capacity: int = 1) -> None:
        self.name = name
        self.id = id
        self.code = id + BaseID
        self.classification = progression
        self.max_capacity = max_capacity

item_table: dict[str, ItemData] = {
    # junk items
    ItemNames.gold_star.value: ItemData(ItemNames.gold_star.value, 0, ItemClassification.filler),
    ItemNames.red_star.value: ItemData(ItemNames.red_star.value, 1, ItemClassification.filler),
    ItemNames.blue_star.value: ItemData(ItemNames.blue_star.value, 2, ItemClassification.filler),

    # useful items
    ItemNames.one_up.value: ItemData(ItemNames.one_up.value, 3, ItemClassification.useful),
    ItemNames.food_pickup.value: ItemData(ItemNames.food_pickup.value, 13, ItemClassification.useful),
    ItemNames.m_tomato.value: ItemData(ItemNames.m_tomato.value, 14, ItemClassification.useful),

    # progression items
    ItemNames.energy_sphere.value: ItemData(ItemNames.energy_sphere.value, 24, ItemClassification.progression, 120),
    ItemNames.part_sphere.value: ItemData(ItemNames.part_sphere.value, 25, ItemClassification.progression, 5),
    ItemNames.energy_sphere_ex.value: ItemData(ItemNames.energy_sphere_ex.value, 26, ItemClassification.progression, 120),
    ItemNames.part_sphere_ex.value: ItemData(ItemNames.part_sphere_ex.value, 27, ItemClassification.progression, 5),

    # trap items
    ItemNames.sleep_trap.value: ItemData(ItemNames.sleep_trap.value, 37, ItemClassification.trap),
    ItemNames.eject_trap.value: ItemData(ItemNames.eject_trap.value, 38, ItemClassification.trap),
    ItemNames.mouthful_trap.value: ItemData(ItemNames.mouthful_trap.value, 39, ItemClassification.trap),
}

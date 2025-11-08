from .GameNames import ItemNames
from BaseClasses import Item, ItemClassification

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
    ItemNames.energy_sphere_ex.value: ItemData(ItemNames.energy_sphere_ex.value, 25, ItemClassification.progression, 120),
    ItemNames.lor_oars.value: ItemData(ItemNames.lor_oars.value, 26, ItemClassification.progression, 1),
    ItemNames.lor_rwing.value: ItemData(ItemNames.lor_rwing.value, 27, ItemClassification.progression, 1),
    ItemNames.lor_lwing.value: ItemData(ItemNames.lor_lwing.value, 28, ItemClassification.progression, 1),
    ItemNames.lor_emblem.value: ItemData(ItemNames.lor_emblem.value, 29, ItemClassification.progression, 1),
    ItemNames.lor_mast.value: ItemData(ItemNames.lor_mast.value, 30, ItemClassification.progression, 1),
    ItemNames.lor_oars_ex.value: ItemData(ItemNames.lor_oars_ex.value, 31, ItemClassification.progression, 1),
    ItemNames.lor_rwing_ex.value: ItemData(ItemNames.lor_rwing_ex.value, 32, ItemClassification.progression, 1),
    ItemNames.lor_lwing_ex.value: ItemData(ItemNames.lor_lwing_ex.value, 33, ItemClassification.progression, 1),
    ItemNames.lor_emblem_ex.value: ItemData(ItemNames.lor_emblem_ex.value, 34, ItemClassification.progression, 1),
    ItemNames.lor_mast_ex.value: ItemData(ItemNames.lor_mast_ex.value, 35, ItemClassification.progression, 1),

    # trap items
    ItemNames.sleep_trap.value: ItemData(ItemNames.sleep_trap.value, 37, ItemClassification.trap),
    ItemNames.eject_trap.value: ItemData(ItemNames.eject_trap.value, 38, ItemClassification.trap),
    ItemNames.mouthful_trap.value: ItemData(ItemNames.mouthful_trap.value, 39, ItemClassification.trap),
}

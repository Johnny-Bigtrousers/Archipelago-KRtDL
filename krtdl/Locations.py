import typing
from BaseClasses import Location
from .GameNames import LocationNames

BaseID = 24102011

class KRtDLLocations(Location):
    game: str = "Kirby's Return to Dream Land"

stage_completion_table = {
    # not entirely sure how to handle this yet.
    LocationNames.stage1_1_complete.value: BaseID + 40,
    LocationNames.stage1_2_complete.value: BaseID + 40 + 1,
    LocationNames.stage1_3_complete.value: BaseID + 40 + 2,
    LocationNames.stage1_4_complete.value: BaseID + 40 + 3,
    LocationNames.stage1_5_complete.value: BaseID + 40 + 4,
    LocationNames.stage2_1_complete.value: BaseID + 40 + 5,
    LocationNames.stage2_2_complete.value: BaseID + 40 + 6,
    LocationNames.stage2_3_complete.value: BaseID + 40 + 7,
    LocationNames.stage2_4_complete.value: BaseID + 40 + 8,
    LocationNames.stage2_5_complete.value: BaseID + 40 + 9,
    LocationNames.stage3_1_complete.value: BaseID + 40 + 10,
    LocationNames.stage3_2_complete.value: BaseID + 40 + 11,
    LocationNames.stage3_3_complete.value: BaseID + 40 + 12,
    LocationNames.stage3_4_complete.value: BaseID + 40 + 13,
    LocationNames.stage3_5_complete.value: BaseID + 40 + 14,
    LocationNames.stage4_1_complete.value: BaseID + 40 + 15,
    LocationNames.stage4_2_complete.value: BaseID + 40 + 16,
    LocationNames.stage4_3_complete.value: BaseID + 40 + 17,
    LocationNames.stage4_4_complete.value: BaseID + 40 + 18,
    LocationNames.stage4_5_complete.value: BaseID + 40 + 19,
    LocationNames.stage4_6_complete.value: BaseID + 40 + 20,
    LocationNames.stage5_1_complete.value: BaseID + 40 + 21,
    LocationNames.stage5_2_complete.value: BaseID + 40 + 22,
    LocationNames.stage5_3_complete.value: BaseID + 40 + 23,
    LocationNames.stage5_4_complete.value: BaseID + 40 + 24,
    LocationNames.stage5_5_complete.value: BaseID + 40 + 25,
    LocationNames.stage5_6_complete.value: BaseID + 40 + 26,
    LocationNames.stage6_1_complete.value: BaseID + 40 + 27,
    LocationNames.stage6_2_complete.value: BaseID + 40 + 28,
    LocationNames.stage6_3_complete.value: BaseID + 40 + 29,
    LocationNames.stage6_4_complete.value: BaseID + 40 + 30,
    LocationNames.stage6_5_complete.value: BaseID + 40 + 31,
    LocationNames.stage6_6_complete.value: BaseID + 40 + 32,
    LocationNames.stage7_1_complete.value: BaseID + 40 + 33,
    LocationNames.stage7_2_complete.value: BaseID + 40 + 34,
    LocationNames.stage7_3_complete.value: BaseID + 40 + 35,
    LocationNames.stage7_4_complete.value: BaseID + 40 + 36,
    LocationNames.stage8_3_complete.value: BaseID + 40 + 37,
    LocationNames.stage8_4_complete.value: BaseID + 40 + 38
}

energy_sphere_table = {
    # not entirely sure how to handle this yet.
    # LocationNames.stage1_1_complete.value: BaseID + 1
}

part_sphere_table = {
    # not entirely sure how to handle this yet.
    # LocationNames.stage1_1_complete.value: BaseID + 1
}

flower_table = {
    # not entirely sure how to handle this yet.
    # LocationNames.stage1_1_complete.value: BaseID + 1
}

gold_star_table = {
    # not entirely sure how to handle this yet.
    # LocationNames.stage1_1_complete.value: BaseID + 1
}

red_star_table = {
    # not entirely sure how to handle this yet.
    # LocationNames.stage1_1_complete.value: BaseID + 1
}

blue_star_table = {
    # not entirely sure how to handle this yet.
    # LocationNames.stage1_1_complete.value: BaseID + 1
}

one_up_table = {
    # not entirely sure how to handle this yet.
    # LocationNames.stage1_1_complete.value: BaseID + 1
}

health_pickup_table = {
    # not entirely sure how to handle this yet.
    # LocationNames.stage1_1_complete.value: BaseID + 1
}

maxim_tomato_table = {
    # not entirely sure how to handle this yet.
    # LocationNames.stage1_1_complete.value: BaseID + 1
}

composite_location: dict[str, int] = {
    **stage_completion_table,
    **energy_sphere_table,
    **part_sphere_table,
    **flower_table,
    **gold_star_table,
    **red_star_table,
    **blue_star_table,
    **one_up_table,
    **health_pickup_table,
    **maxim_tomato_table
}

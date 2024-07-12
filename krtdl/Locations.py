import typing
from BaseClasses import Location
from .GameNames import LocationNames

BaseLocationID = 24102011 + 40

class KRtDLLocations(Location):
    game: str = "Kirby's Return to Dream Land"

stage_completion_table = {
    # not entirely sure how to handle this yet.
    LocationNames.stage1_1_complete.value: BaseLocationID,
    LocationNames.stage1_2_complete.value: BaseLocationID + 1,
    LocationNames.stage1_3_complete.value: BaseLocationID + 2,
    LocationNames.stage1_4_complete.value: BaseLocationID + 3,
    LocationNames.stage1_5_complete.value: BaseLocationID + 4,
    LocationNames.stage2_1_complete.value: BaseLocationID + 5,
    LocationNames.stage2_2_complete.value: BaseLocationID + 6,
    LocationNames.stage2_3_complete.value: BaseLocationID + 7,
    LocationNames.stage2_4_complete.value: BaseLocationID + 8,
    LocationNames.stage2_5_complete.value: BaseLocationID + 9,
    LocationNames.stage3_1_complete.value: BaseLocationID + 10,
    LocationNames.stage3_2_complete.value: BaseLocationID + 11,
    LocationNames.stage3_3_complete.value: BaseLocationID + 12,
    LocationNames.stage3_4_complete.value: BaseLocationID + 13,
    LocationNames.stage3_5_complete.value: BaseLocationID + 14,
    LocationNames.stage4_1_complete.value: BaseLocationID + 15,
    LocationNames.stage4_2_complete.value: BaseLocationID + 16,
    LocationNames.stage4_3_complete.value: BaseLocationID + 17,
    LocationNames.stage4_4_complete.value: BaseLocationID + 18,
    LocationNames.stage4_5_complete.value: BaseLocationID + 19,
    LocationNames.stage4_6_complete.value: BaseLocationID + 20,
    LocationNames.stage5_1_complete.value: BaseLocationID + 21,
    LocationNames.stage5_2_complete.value: BaseLocationID + 22,
    LocationNames.stage5_3_complete.value: BaseLocationID + 23,
    LocationNames.stage5_4_complete.value: BaseLocationID + 24,
    LocationNames.stage5_5_complete.value: BaseLocationID + 25,
    LocationNames.stage5_6_complete.value: BaseLocationID + 26,
    LocationNames.stage6_1_complete.value: BaseLocationID + 27,
    LocationNames.stage6_2_complete.value: BaseLocationID + 28,
    LocationNames.stage6_3_complete.value: BaseLocationID + 29,
    LocationNames.stage6_4_complete.value: BaseLocationID + 30,
    LocationNames.stage6_5_complete.value: BaseLocationID + 31,
    LocationNames.stage6_6_complete.value: BaseLocationID + 32,
    LocationNames.stage7_1_complete.value: BaseLocationID + 33,
    LocationNames.stage7_2_complete.value: BaseLocationID + 34,
    LocationNames.stage7_3_complete.value: BaseLocationID + 35,
    LocationNames.stage7_4_complete.value: BaseLocationID + 36,
    LocationNames.stage8_3_complete.value: BaseLocationID + 37,
    LocationNames.stage8_4_complete.value: BaseLocationID + 38
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

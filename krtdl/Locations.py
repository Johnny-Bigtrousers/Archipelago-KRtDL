import typing
from BaseClasses import Location
from .GameNames import LocationNames

BaseID = 24102011

class KRtDLLocations(Location):
    game: str = "Kirby's Return to Dream Land"

stage_completion_table = {
    # not entirely sure how to handle this yet.
    LocationNames.stage1_1_complete.value: BaseID + 1
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

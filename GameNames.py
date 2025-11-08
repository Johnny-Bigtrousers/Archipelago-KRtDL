from enum import Enum

class ItemNames(Enum):
    gold_star = "Gold Star"
    red_star = "Red Star"
    blue_star = "Blue Star"
    one_up = "1-Up"
    food_pickup = "Food Pickup"
    m_tomato = "Maxim Tomato"
    gold_star_ex = "EX Gold Star"
    red_star_ex  = "EX Red Star"
    blue_star_ex  = "EX Blue Star"
    one_up_ex  = "EX 1-Up"
    food_pickup_ex  = "EX Food Pickup"
    m_tomato_ex  = "EX Maxim Tomato"
    energy_sphere = "Energy Sphere"
    energy_sphere_ex = "EX Energy Sphere"
    lor_oars = "Lor Starcutter Oars"
    lor_rwing = "Lor Starcutter Right Wing"
    lor_lwing = "Lor Starcutter Left Wing"
    lor_emblem = "Lor Starcutter Emblem"
    lor_mast = "Lor Starcutter Mast"
    lor_oars_ex = "EX Lor Starcutter Oars"
    lor_rwing_ex = "EX Lor Starcutter Right Wing"
    lor_lwing_ex = "EX Lor Starcutter Left Wing"
    lor_emblem_ex = "EX Lor Starcutter Emblem"
    lor_mast_ex = "EX Lor Starcutter Mast"
    sleep_trap = "Sleep Trap"
    eject_trap = "Eject Trap"
    mouthful_trap = "Mouthful Trap"

class StageNames(Enum):
    stage1_1 = "Cookie Country Stage 1"
    stage1_2 = "Cookie Country Stage 2"
    stage1_3 = "Cookie Country Stage 3"
    stage1_4 = "Cookie Country Stage 4"
    stage1_5 = "Cookie Country Stage 5"
    stage2_1 = "Raisin Ruins Stage 1"
    stage2_2 = "Raisin Ruins Stage 2"
    stage2_3 = "Raisin Ruins Stage 3"
    stage2_4 = "Raisin Ruins Stage 4"
    stage2_5 = "Raisin Ruins Stage 5"
    stage3_1 = "Onion Ocean Stage 1"
    stage3_2 = "Onion Ocean Stage 2"
    stage3_3 = "Onion Ocean Stage 3"
    stage3_4 = "Onion Ocean Stage 4"
    stage3_5 = "Onion Ocean Stage 5"
    stage4_1 = "White Wafers Stage 1"
    stage4_2 = "White Wafers Stage 2"
    stage4_3 = "White Wafers Stage 3"
    stage4_4 = "White Wafers Stage 4"
    stage4_5 = "White Wafers Stage 5"
    stage4_6 = "White Wafers Stage 6"
    stage5_1 = "Nutty Noon Stage 1"
    stage5_2 = "Nutty Noon Stage 2"
    stage5_3 = "Nutty Noon Stage 3"
    stage5_4 = "Nutty Noon Stage 4"
    stage5_5 = "Nutty Noon Stage 5"
    stage5_6 = "Nutty Noon Stage 6"
    stage6_1 = "Egg Engines Stage 1"
    stage6_2 = "Egg Engines Stage 2"
    stage6_3 = "Egg Engines Stage 3"
    stage6_4 = "Egg Engines Stage 4"
    stage6_5 = "Egg Engines Stage 5"
    stage6_6 = "Egg Engines Stage 6"
    stage7_1 = "Dangerous Dinner Stage 1"
    stage7_2 = "Dangerous Dinner Stage 2"
    stage7_3 = "Dangerous Dinner Stage 3"
    stage7_4 = "Dangerous Dinner Stage 4"
    stage8_1 = "Another Dimension Part 1"
    stage8_2 = "Another Dimension Part 2"
    stage8_3 = "Another Dimension Boss"
    stage8_4 = "Another Dimension Final Boss"

class LocationNames(Enum):
    stage1_1_esphere_1 = (StageNames.stage1_1.value + " - Energy Sphere 1")
    stage1_1_esphere_2 = (StageNames.stage1_1.value + " - Energy Sphere 2")
    stage1_1_esphere_3 = (StageNames.stage1_1.value + " - Energy Sphere 3")
    stage1_1_complete = (StageNames.stage1_1.value + " - Complete")
    extra_stage1_1_esphere_1 = ("EX " + StageNames.stage1_1.value + " - Energy Sphere 1")
    extra_stage1_1_esphere_2 = ("EX " + StageNames.stage1_1.value + " - Energy Sphere 2")
    extra_stage1_1_esphere_3 = ("EX " + StageNames.stage1_1.value + " - Energy Sphere 3")
    extra_stage1_1_complete = ("EX " + StageNames.stage1_1.value + " - Complete")

    stage1_2_esphere_1 = (StageNames.stage1_2.value + " - Energy Sphere 1")
    stage1_2_esphere_2 = (StageNames.stage1_2.value + " - Energy Sphere 2")
    stage1_2_esphere_3 = (StageNames.stage1_2.value + " - Energy Sphere 3")
    stage1_2_complete = (StageNames.stage1_2.value + " - Complete")
    extra_stage1_2_esphere_1 = ("EX " + StageNames.stage1_2.value + " - Energy Sphere 1")
    extra_stage1_2_esphere_2 = ("EX " + StageNames.stage1_2.value + " - Energy Sphere 2")
    extra_stage1_2_esphere_3 = ("EX " + StageNames.stage1_2.value + " - Energy Sphere 3")
    extra_stage1_2_complete = ("EX " + StageNames.stage1_2.value + " - Complete")

    stage1_3_esphere_1 = (StageNames.stage1_3.value + " - Energy Sphere 1")
    stage1_3_esphere_2 = (StageNames.stage1_3.value + " - Energy Sphere 2")
    stage1_3_esphere_3 = (StageNames.stage1_3.value + " - Energy Sphere 3")
    stage1_3_complete = (StageNames.stage1_3.value + " - Complete")
    extra_stage1_3_esphere_1 = ("EX " + StageNames.stage1_3.value + " - Energy Sphere 1")
    extra_stage1_3_esphere_2 = ("EX " + StageNames.stage1_3.value + " - Energy Sphere 2")
    extra_stage1_3_esphere_3 = ("EX " + StageNames.stage1_3.value + " - Energy Sphere 3")
    extra_stage1_3_complete = ("EX " + StageNames.stage1_3.value + " - Complete")

    stage1_4_esphere_1 = (StageNames.stage1_4.value + " - Energy Sphere 1")
    stage1_4_esphere_2 = (StageNames.stage1_4.value + " - Energy Sphere 2")
    stage1_4_esphere_3 = (StageNames.stage1_4.value + " - Energy Sphere 3")
    stage1_4_esphere_4 = (StageNames.stage1_4.value + " - Energy Sphere 4")
    stage1_4_complete = (StageNames.stage1_4.value + " - Complete")
    extra_stage1_4_esphere_1 = ("EX " + StageNames.stage1_4.value + " - Energy Sphere 1")
    extra_stage1_4_esphere_2 = ("EX " + StageNames.stage1_4.value + " - Energy Sphere 2")
    extra_stage1_4_esphere_3 = ("EX " + StageNames.stage1_4.value + " - Energy Sphere 3")
    extra_stage1_4_esphere_4 = ("EX " + StageNames.stage1_4.value + " - Energy Sphere 4")
    extra_stage1_4_complete = ("EX " + StageNames.stage1_4.value + " - Complete")
    
    stage1_5_part = (StageNames.stage1_5.value + " - " + ItemNames.lor_oars.value)
    extra_stage1_5_part = ("EX " + StageNames.stage1_5.value + " - " + ItemNames.lor_oars_ex.value)
  
 
    stage2_1_esphere_1 = (StageNames.stage2_1.value + " - Energy Sphere 1")
    stage2_1_esphere_2 = (StageNames.stage2_1.value + " - Energy Sphere 2")
    stage2_1_esphere_3 = (StageNames.stage2_1.value + " - Energy Sphere 3")
    stage2_1_complete = (StageNames.stage2_1.value + " - Complete")
    extra_stage2_1_esphere_1 = ("EX " + StageNames.stage2_1.value + " - Energy Sphere 1")
    extra_stage2_1_esphere_2 = ("EX " + StageNames.stage2_1.value + " - Energy Sphere 2")
    extra_stage2_1_esphere_3 = ("EX " + StageNames.stage2_1.value + " - Energy Sphere 3")
    extra_stage2_1_complete = ("EX " + StageNames.stage2_1.value + " - Complete")

    stage2_2_esphere_1 = (StageNames.stage2_2.value + " - Energy Sphere 1")
    stage2_2_esphere_2 = (StageNames.stage2_2.value + " - Energy Sphere 2")
    stage2_2_esphere_3 = (StageNames.stage2_2.value + " - Energy Sphere 3")
    stage2_2_esphere_4 = (StageNames.stage2_2.value + " - Energy Sphere 4")
    stage2_2_complete = (StageNames.stage2_2.value + " - Complete")
    extra_stage2_2_esphere_1 = ("EX " + StageNames.stage2_2.value + " - Energy Sphere 1")
    extra_stage2_2_esphere_2 = ("EX " + StageNames.stage2_2.value + " - Energy Sphere 2")
    extra_stage2_2_esphere_3 = ("EX " + StageNames.stage2_2.value + " - Energy Sphere 3")
    extra_stage2_2_esphere_4 = ("EX " + StageNames.stage2_2.value + " - Energy Sphere 4")
    extra_stage2_2_complete = ("EX " + StageNames.stage2_2.value + " - Complete")

    stage2_3_esphere_1 = (StageNames.stage2_3.value + " - Energy Sphere 1")
    stage2_3_esphere_2 = (StageNames.stage2_3.value + " - Energy Sphere 2")
    stage2_3_esphere_3 = (StageNames.stage2_3.value + " - Energy Sphere 3")
    stage2_3_esphere_4 = (StageNames.stage2_3.value + " - Energy Sphere 4")
    stage2_3_complete = (StageNames.stage2_3.value + " - Complete")
    extra_stage2_3_esphere_1 = ("EX " + StageNames.stage2_3.value + " - Energy Sphere 1")
    extra_stage2_3_esphere_2 = ("EX " + StageNames.stage2_3.value + " - Energy Sphere 2")
    extra_stage2_3_esphere_3 = ("EX " + StageNames.stage2_3.value + " - Energy Sphere 3")
    extra_stage2_3_esphere_4 = ("EX " + StageNames.stage2_3.value + " - Energy Sphere 4")
    extra_stage2_3_complete = ("EX " + StageNames.stage2_3.value + " - Complete")

    stage2_4_esphere_1 = (StageNames.stage2_4.value + " - Energy Sphere 1")
    stage2_4_esphere_2 = (StageNames.stage2_4.value + " - Energy Sphere 2")
    stage2_4_esphere_3 = (StageNames.stage2_4.value + " - Energy Sphere 3")
    stage2_4_esphere_4 = (StageNames.stage2_4.value + " - Energy Sphere 4")
    stage2_4_esphere_5 = (StageNames.stage2_4.value + " - Energy Sphere 5")
    stage2_4_complete = (StageNames.stage2_4.value + " - Complete")
    extra_stage2_4_esphere_1 = ("EX " + StageNames.stage2_4.value + " - Energy Sphere 1")
    extra_stage2_4_esphere_2 = ("EX " + StageNames.stage2_4.value + " - Energy Sphere 2")
    extra_stage2_4_esphere_3 = ("EX " + StageNames.stage2_4.value + " - Energy Sphere 3")
    extra_stage2_4_esphere_4 = ("EX " + StageNames.stage2_4.value + " - Energy Sphere 4")
    extra_stage2_4_esphere_5 = ("EX " + StageNames.stage2_4.value + " - Energy Sphere 5")
    extra_stage2_4_complete = ("EX " + StageNames.stage2_4.value + " - Complete")
    
    stage2_5_part = (StageNames.stage2_5.value + " - " + ItemNames.lor_rwing.value)
    extra_stage2_5_part = ("EX " + StageNames.stage2_5.value + " - " + ItemNames.lor_rwing_ex.value)

    
    stage3_1_esphere_1 = (StageNames.stage3_1.value + " - Energy Sphere 1")
    stage3_1_esphere_2 = (StageNames.stage3_1.value + " - Energy Sphere 2")
    stage3_1_esphere_3 = (StageNames.stage3_1.value + " - Energy Sphere 3")
    stage3_1_complete = (StageNames.stage3_1.value + " - Complete")
    extra_stage3_1_esphere_1 = ("EX " + StageNames.stage3_1.value + " - Energy Sphere 1")
    extra_stage3_1_esphere_2 = ("EX " + StageNames.stage3_1.value + " - Energy Sphere 2")
    extra_stage3_1_esphere_3 = ("EX " + StageNames.stage3_1.value + " - Energy Sphere 3")
    extra_stage3_1_complete = ("EX " + StageNames.stage3_1.value + " - Complete")

    stage3_2_esphere_1 = (StageNames.stage3_2.value + " - Energy Sphere 1")
    stage3_2_esphere_2 = (StageNames.stage3_2.value + " - Energy Sphere 2")
    stage3_2_esphere_3 = (StageNames.stage3_2.value + " - Energy Sphere 3")
    stage3_2_esphere_4 = (StageNames.stage3_2.value + " - Energy Sphere 4")
    stage3_2_complete = (StageNames.stage3_2.value + " - Complete")
    extra_stage3_2_esphere_1 = ("EX " + StageNames.stage3_2.value + " - Energy Sphere 1")
    extra_stage3_2_esphere_2 = ("EX " + StageNames.stage3_2.value + " - Energy Sphere 2")
    extra_stage3_2_esphere_3 = ("EX " + StageNames.stage3_2.value + " - Energy Sphere 3")
    extra_stage3_2_esphere_4 = ("EX " + StageNames.stage3_2.value + " - Energy Sphere 4")
    extra_stage3_2_complete = ("EX " + StageNames.stage3_2.value + " - Complete")

    stage3_3_esphere_1 = (StageNames.stage3_3.value + " - Energy Sphere 1")
    stage3_3_esphere_2 = (StageNames.stage3_3.value + " - Energy Sphere 2")
    stage3_3_esphere_3 = (StageNames.stage3_3.value + " - Energy Sphere 3")
    stage3_3_esphere_4 = (StageNames.stage3_3.value + " - Energy Sphere 4")
    stage3_3_complete = (StageNames.stage3_3.value + " - Complete")
    extra_stage3_3_esphere_1 = ("EX " + StageNames.stage3_3.value + " - Energy Sphere 1")
    extra_stage3_3_esphere_2 = ("EX " + StageNames.stage3_3.value + " - Energy Sphere 2")
    extra_stage3_3_esphere_3 = ("EX " + StageNames.stage3_3.value + " - Energy Sphere 3")
    extra_stage3_3_esphere_4 = ("EX " + StageNames.stage3_3.value + " - Energy Sphere 4")
    extra_stage3_3_complete = ("EX " + StageNames.stage3_3.value + " - Complete")

    stage3_4_esphere_1 = (StageNames.stage3_4.value + " - Energy Sphere 1")
    stage3_4_esphere_2 = (StageNames.stage3_4.value + " - Energy Sphere 2")
    stage3_4_esphere_3 = (StageNames.stage3_4.value + " - Energy Sphere 3")
    stage3_4_esphere_4 = (StageNames.stage3_4.value + " - Energy Sphere 4")
    stage3_4_esphere_5 = (StageNames.stage3_4.value + " - Energy Sphere 5")
    stage3_4_complete = (StageNames.stage3_4.value + " - Complete")
    extra_stage3_4_esphere_1 = ("EX " + StageNames.stage3_4.value + " - Energy Sphere 1")
    extra_stage3_4_esphere_2 = ("EX " + StageNames.stage3_4.value + " - Energy Sphere 2")
    extra_stage3_4_esphere_3 = ("EX " + StageNames.stage3_4.value + " - Energy Sphere 3")
    extra_stage3_4_esphere_4 = ("EX " + StageNames.stage3_4.value + " - Energy Sphere 4")
    extra_stage3_4_esphere_5 = ("EX " + StageNames.stage3_4.value + " - Energy Sphere 5")
    extra_stage3_4_complete = ("EX " + StageNames.stage3_4.value + " - Complete")
    
    stage3_5_part = (StageNames.stage3_5.value + " - " + ItemNames.lor_lwing.value)
    extra_stage3_5_part = ("EX " + StageNames.stage3_5.value + " - " + ItemNames.lor_lwing_ex.value)
    
    
    stage4_1_esphere_1 = (StageNames.stage4_1.value + " - Energy Sphere 1")
    stage4_1_esphere_2 = (StageNames.stage4_1.value + " - Energy Sphere 2")
    stage4_1_esphere_3 = (StageNames.stage4_1.value + " - Energy Sphere 3")
    stage4_1_complete = (StageNames.stage4_1.value + " - Complete")
    extra_stage4_1_esphere_1 = ("EX " + StageNames.stage4_1.value + " - Energy Sphere 1")
    extra_stage4_1_esphere_2 = ("EX " + StageNames.stage4_1.value + " - Energy Sphere 2")
    extra_stage4_1_esphere_3 = ("EX " + StageNames.stage4_1.value + " - Energy Sphere 3")
    extra_stage4_1_complete = ("EX " + StageNames.stage4_1.value + " - Complete")

    stage4_2_esphere_1 = (StageNames.stage4_2.value + " - Energy Sphere 1")
    stage4_2_esphere_2 = (StageNames.stage4_2.value + " - Energy Sphere 2")
    stage4_2_esphere_3 = (StageNames.stage4_2.value + " - Energy Sphere 3")
    stage4_2_esphere_4 = (StageNames.stage4_2.value + " - Energy Sphere 4")
    stage4_2_complete = (StageNames.stage4_2.value + " - Complete")
    extra_stage4_2_esphere_1 = ("EX " + StageNames.stage4_2.value + " - Energy Sphere 1")
    extra_stage4_2_esphere_2 = ("EX " + StageNames.stage4_2.value + " - Energy Sphere 2")
    extra_stage4_2_esphere_3 = ("EX " + StageNames.stage4_2.value + " - Energy Sphere 3")
    extra_stage4_2_esphere_4 = ("EX " + StageNames.stage4_2.value + " - Energy Sphere 4")
    extra_stage4_2_complete = ("EX " + StageNames.stage4_2.value + " - Complete")

    stage4_3_esphere_1 = (StageNames.stage4_3.value + " - Energy Sphere 1")
    stage4_3_esphere_2 = (StageNames.stage4_3.value + " - Energy Sphere 2")
    stage4_3_esphere_3 = (StageNames.stage4_3.value + " - Energy Sphere 3")
    stage4_3_esphere_4 = (StageNames.stage4_3.value + " - Energy Sphere 4")
    stage4_3_complete = (StageNames.stage4_3.value + " - Complete")
    extra_stage4_3_esphere_1 = ("EX " + StageNames.stage4_3.value + " - Energy Sphere 1")
    extra_stage4_3_esphere_2 = ("EX " + StageNames.stage4_3.value + " - Energy Sphere 2")
    extra_stage4_3_esphere_3 = ("EX " + StageNames.stage4_3.value + " - Energy Sphere 3")
    extra_stage4_3_esphere_4 = ("EX " + StageNames.stage4_3.value + " - Energy Sphere 4")
    extra_stage4_3_complete = ("EX " + StageNames.stage4_3.value + " - Complete")

    stage4_4_esphere_1 = (StageNames.stage4_4.value + " - Energy Sphere 1")
    stage4_4_esphere_2 = (StageNames.stage4_4.value + " - Energy Sphere 2")
    stage4_4_esphere_3 = (StageNames.stage4_4.value + " - Energy Sphere 3")
    stage4_4_esphere_4 = (StageNames.stage4_4.value + " - Energy Sphere 4")
    stage4_4_complete = (StageNames.stage4_4.value + " - Complete")
    extra_stage4_4_esphere_1 = ("EX " + StageNames.stage4_4.value + " - Energy Sphere 1")
    extra_stage4_4_esphere_2 = ("EX " + StageNames.stage4_4.value + " - Energy Sphere 2")
    extra_stage4_4_esphere_3 = ("EX " + StageNames.stage4_4.value + " - Energy Sphere 3")
    extra_stage4_4_esphere_4 = ("EX " + StageNames.stage4_4.value + " - Energy Sphere 4")
    extra_stage4_4_complete = ("EX " + StageNames.stage4_4.value + " - Complete")

    stage4_5_esphere_1 = (StageNames.stage4_5.value + " - Energy Sphere 1")
    stage4_5_esphere_2 = (StageNames.stage4_5.value + " - Energy Sphere 2")
    stage4_5_esphere_3 = (StageNames.stage4_5.value + " - Energy Sphere 3")
    stage4_5_esphere_4 = (StageNames.stage4_5.value + " - Energy Sphere 4")
    stage4_5_complete = (StageNames.stage4_5.value + " - Complete")
    extra_stage4_5_esphere_1 = ("EX " + StageNames.stage4_5.value + " - Energy Sphere 1")
    extra_stage4_5_esphere_2 = ("EX " + StageNames.stage4_5.value + " - Energy Sphere 2")
    extra_stage4_5_esphere_3 = ("EX " + StageNames.stage4_5.value + " - Energy Sphere 3")
    extra_stage4_5_esphere_4 = ("EX " + StageNames.stage4_5.value + " - Energy Sphere 4")
    extra_stage4_5_complete = ("EX " + StageNames.stage4_5.value + " - Complete")
    
    stage4_6_part = (StageNames.stage4_6.value + " - " + ItemNames.lor_emblem.value)
    extra_stage4_6_part = ("EX " + StageNames.stage4_6.value + " - " + ItemNames.lor_emblem_ex.value)
    
    
    stage5_1_esphere_1 = (StageNames.stage5_1.value + " - Energy Sphere 1")
    stage5_1_esphere_2 = (StageNames.stage5_1.value + " - Energy Sphere 2")
    stage5_1_esphere_3 = (StageNames.stage5_1.value + " - Energy Sphere 3")
    stage5_1_esphere_4 = (StageNames.stage5_1.value + " - Energy Sphere 4")
    stage5_1_complete = (StageNames.stage5_1.value + " - Complete")
    extra_stage5_1_esphere_1 = ("EX " + StageNames.stage5_1.value + " - Energy Sphere 1")
    extra_stage5_1_esphere_2 = ("EX " + StageNames.stage5_1.value + " - Energy Sphere 2")
    extra_stage5_1_esphere_3 = ("EX " + StageNames.stage5_1.value + " - Energy Sphere 3")
    extra_stage5_1_esphere_4 = ("EX " + StageNames.stage5_1.value + " - Energy Sphere 4")
    extra_stage5_1_complete = ("EX " + StageNames.stage5_1.value + " - Complete")

    stage5_2_esphere_1 = (StageNames.stage5_2.value + " - Energy Sphere 1")
    stage5_2_esphere_2 = (StageNames.stage5_2.value + " - Energy Sphere 2")
    stage5_2_esphere_3 = (StageNames.stage5_2.value + " - Energy Sphere 3")
    stage5_2_esphere_4 = (StageNames.stage5_2.value + " - Energy Sphere 4")
    stage5_2_complete = (StageNames.stage5_2.value + " - Complete")
    extra_stage5_2_esphere_1 = ("EX " + StageNames.stage5_2.value + " - Energy Sphere 1")
    extra_stage5_2_esphere_2 = ("EX " + StageNames.stage5_2.value + " - Energy Sphere 2")
    extra_stage5_2_esphere_3 = ("EX " + StageNames.stage5_2.value + " - Energy Sphere 3")
    extra_stage5_2_esphere_4 = ("EX " + StageNames.stage5_2.value + " - Energy Sphere 4")
    extra_stage5_2_complete = ("EX " + StageNames.stage5_2.value + " - Complete")

    stage5_3_esphere_1 = (StageNames.stage5_3.value + " - Energy Sphere 1")
    stage5_3_esphere_2 = (StageNames.stage5_3.value + " - Energy Sphere 2")
    stage5_3_esphere_3 = (StageNames.stage5_3.value + " - Energy Sphere 3")
    stage5_3_esphere_4 = (StageNames.stage5_3.value + " - Energy Sphere 4")
    stage5_3_complete = (StageNames.stage5_3.value + " - Complete")
    extra_stage5_3_esphere_1 = ("EX " + StageNames.stage5_3.value + " - Energy Sphere 1")
    extra_stage5_3_esphere_2 = ("EX " + StageNames.stage5_3.value + " - Energy Sphere 2")
    extra_stage5_3_esphere_3 = ("EX " + StageNames.stage5_3.value + " - Energy Sphere 3")
    extra_stage5_3_esphere_4 = ("EX " + StageNames.stage5_3.value + " - Energy Sphere 4")
    extra_stage5_3_complete = ("EX " + StageNames.stage5_3.value + " - Complete")

    stage5_4_esphere_1 = (StageNames.stage5_4.value + " - Energy Sphere 1")
    stage5_4_esphere_2 = (StageNames.stage5_4.value + " - Energy Sphere 2")
    stage5_4_esphere_3 = (StageNames.stage5_4.value + " - Energy Sphere 3")
    stage5_4_esphere_4 = (StageNames.stage5_4.value + " - Energy Sphere 4")
    stage5_4_complete = (StageNames.stage5_4.value + " - Complete")
    extra_stage5_4_esphere_1 = ("EX " + StageNames.stage5_4.value + " - Energy Sphere 1")
    extra_stage5_4_esphere_2 = ("EX " + StageNames.stage5_4.value + " - Energy Sphere 2")
    extra_stage5_4_esphere_3 = ("EX " + StageNames.stage5_4.value + " - Energy Sphere 3")
    extra_stage5_4_esphere_4 = ("EX " + StageNames.stage5_4.value + " - Energy Sphere 4")
    extra_stage5_4_complete = ("EX " + StageNames.stage5_4.value + " - Complete")

    stage5_5_esphere_1 = (StageNames.stage5_5.value + " - Energy Sphere 1")
    stage5_5_esphere_2 = (StageNames.stage5_5.value + " - Energy Sphere 2")
    stage5_5_esphere_3 = (StageNames.stage5_5.value + " - Energy Sphere 3")
    stage5_5_esphere_4 = (StageNames.stage5_5.value + " - Energy Sphere 4")
    stage5_5_complete = (StageNames.stage5_5.value + " - Complete")
    extra_stage5_5_esphere_1 = ("EX " + StageNames.stage5_5.value + " - Energy Sphere 1")
    extra_stage5_5_esphere_2 = ("EX " + StageNames.stage5_5.value + " - Energy Sphere 2")
    extra_stage5_5_esphere_3 = ("EX " + StageNames.stage5_5.value + " - Energy Sphere 3")
    extra_stage5_5_esphere_4 = ("EX " + StageNames.stage5_5.value + " - Energy Sphere 4")
    extra_stage5_5_complete = ("EX " + StageNames.stage5_5.value + " - Complete")
    
    stage5_6_part = (StageNames.stage5_6.value + " - " + ItemNames.lor_mast.value)
    extra_stage5_6_part = ("EX " + StageNames.stage5_6.value + " - " + ItemNames.lor_mast_ex.value)
    

    stage6_1_esphere_1 = (StageNames.stage6_1.value + " - Energy Sphere 1")
    stage6_1_esphere_2 = (StageNames.stage6_1.value + " - Energy Sphere 2")
    stage6_1_esphere_3 = (StageNames.stage6_1.value + " - Energy Sphere 3")
    stage6_1_complete = (StageNames.stage6_1.value + " - Complete")
    extra_stage6_1_esphere_1 = ("EX " + StageNames.stage6_1.value + " - Energy Sphere 1")
    extra_stage6_1_esphere_2 = ("EX " + StageNames.stage6_1.value + " - Energy Sphere 2")
    extra_stage6_1_esphere_3 = ("EX " + StageNames.stage6_1.value + " - Energy Sphere 3")
    extra_stage6_1_complete = ("EX " + StageNames.stage6_1.value + " - Complete")

    stage6_2_esphere_1 = (StageNames.stage6_2.value + " - Energy Sphere 1")
    stage6_2_esphere_2 = (StageNames.stage6_2.value + " - Energy Sphere 2")
    stage6_2_esphere_3 = (StageNames.stage6_2.value + " - Energy Sphere 3")
    stage6_2_esphere_4 = (StageNames.stage6_2.value + " - Energy Sphere 4")
    stage6_2_complete = (StageNames.stage6_2.value + " - Complete")
    extra_stage6_2_esphere_1 = ("EX " + StageNames.stage6_2.value + " - Energy Sphere 1")
    extra_stage6_2_esphere_2 = ("EX " + StageNames.stage6_2.value + " - Energy Sphere 2")
    extra_stage6_2_esphere_3 = ("EX " + StageNames.stage6_2.value + " - Energy Sphere 3")
    extra_stage6_2_esphere_4 = ("EX " + StageNames.stage6_2.value + " - Energy Sphere 4")
    extra_stage6_2_complete = ("EX " + StageNames.stage6_2.value + " - Complete")

    stage6_3_esphere_1 = (StageNames.stage6_3.value + " - Energy Sphere 1")
    stage6_3_esphere_2 = (StageNames.stage6_3.value + " - Energy Sphere 2")
    stage6_3_esphere_3 = (StageNames.stage6_3.value + " - Energy Sphere 3")
    stage6_3_esphere_4 = (StageNames.stage6_3.value + " - Energy Sphere 4")
    stage6_3_complete = (StageNames.stage6_3.value + " - Complete")
    extra_stage6_3_esphere_1 = ("EX " + StageNames.stage6_3.value + " - Energy Sphere 1")
    extra_stage6_3_esphere_2 = ("EX " + StageNames.stage6_3.value + " - Energy Sphere 2")
    extra_stage6_3_esphere_3 = ("EX " + StageNames.stage6_3.value + " - Energy Sphere 3")
    extra_stage6_3_esphere_4 = ("EX " + StageNames.stage6_3.value + " - Energy Sphere 4")
    extra_stage6_3_complete = ("EX " + StageNames.stage6_3.value + " - Complete")

    stage6_4_esphere_1 = (StageNames.stage6_4.value + " - Energy Sphere 1")
    stage6_4_esphere_2 = (StageNames.stage6_4.value + " - Energy Sphere 2")
    stage6_4_esphere_3 = (StageNames.stage6_4.value + " - Energy Sphere 3")
    stage6_4_esphere_4 = (StageNames.stage6_4.value + " - Energy Sphere 4")
    stage6_4_esphere_5 = (StageNames.stage6_4.value + " - Energy Sphere 5")
    stage6_4_complete = (StageNames.stage6_4.value + " - Complete")
    extra_stage6_4_esphere_1 = ("EX " + StageNames.stage6_4.value + " - Energy Sphere 1")
    extra_stage6_4_esphere_2 = ("EX " + StageNames.stage6_4.value + " - Energy Sphere 2")
    extra_stage6_4_esphere_3 = ("EX " + StageNames.stage6_4.value + " - Energy Sphere 3")
    extra_stage6_4_esphere_4 = ("EX " + StageNames.stage6_4.value + " - Energy Sphere 4")
    extra_stage6_4_esphere_5 = ("EX " + StageNames.stage6_4.value + " - Energy Sphere 5")
    extra_stage6_4_complete = ("EX " + StageNames.stage6_4.value + " - Complete")

    stage6_5_esphere_1 = (StageNames.stage6_5.value + " - Energy Sphere 1")
    stage6_5_esphere_2 = (StageNames.stage6_5.value + " - Energy Sphere 2")
    stage6_5_esphere_3 = (StageNames.stage6_5.value + " - Energy Sphere 3")
    stage6_5_esphere_4 = (StageNames.stage6_5.value + " - Energy Sphere 4")
    stage6_5_esphere_5 = (StageNames.stage6_5.value + " - Energy Sphere 5")
    stage6_5_complete = (StageNames.stage6_5.value + " - Complete")
    extra_stage6_5_esphere_1 = ("EX " + StageNames.stage6_5.value + " - Energy Sphere 1")
    extra_stage6_5_esphere_2 = ("EX " + StageNames.stage6_5.value + " - Energy Sphere 2")
    extra_stage6_5_esphere_3 = ("EX " + StageNames.stage6_5.value + " - Energy Sphere 3")
    extra_stage6_5_esphere_4 = ("EX " + StageNames.stage6_5.value + " - Energy Sphere 4")
    extra_stage6_5_esphere_5 = ("EX " + StageNames.stage6_5.value + " - Energy Sphere 5")
    extra_stage6_5_complete = ("EX " + StageNames.stage6_5.value + " - Complete")
    
    stage6_6_complete = (StageNames.stage6_6.value + " - Complete")
    extra_stage6_6_complete = ("EX " + StageNames.stage6_6.value + " - Complete")
    
    
    stage7_1_esphere_1 = (StageNames.stage7_1.value + " - Energy Sphere 1")
    stage7_1_esphere_2 = (StageNames.stage7_1.value + " - Energy Sphere 2")
    stage7_1_esphere_3 = (StageNames.stage7_1.value + " - Energy Sphere 3")
    stage7_1_esphere_4 = (StageNames.stage7_1.value + " - Energy Sphere 4")
    stage7_1_esphere_5 = (StageNames.stage7_1.value + " - Energy Sphere 5")
    stage7_1_complete = (StageNames.stage7_1.value + " - Complete")
    extra_stage7_1_esphere_1 = ("EX " + StageNames.stage7_1.value + " - Energy Sphere 1")
    extra_stage7_1_esphere_2 = ("EX " + StageNames.stage7_1.value + " - Energy Sphere 2")
    extra_stage7_1_esphere_3 = ("EX " + StageNames.stage7_1.value + " - Energy Sphere 3")
    extra_stage7_1_esphere_4 = ("EX " + StageNames.stage7_1.value + " - Energy Sphere 4")
    extra_stage7_1_esphere_5 = ("EX " + StageNames.stage7_1.value + " - Energy Sphere 5")
    extra_stage7_1_complete = ("EX " + StageNames.stage7_1.value + " - Complete")

    
    stage7_2_esphere_1 = (StageNames.stage7_2.value + " - Energy Sphere 1")
    stage7_2_esphere_2 = (StageNames.stage7_2.value + " - Energy Sphere 2")
    stage7_2_esphere_3 = (StageNames.stage7_2.value + " - Energy Sphere 3")
    stage7_2_esphere_4 = (StageNames.stage7_2.value + " - Energy Sphere 4")
    stage7_2_esphere_5 = (StageNames.stage7_2.value + " - Energy Sphere 5")
    stage7_2_complete = (StageNames.stage7_2.value + " - Complete")
    extra_stage7_2_esphere_1 = ("EX " + StageNames.stage7_2.value + " - Energy Sphere 1")
    extra_stage7_2_esphere_2 = ("EX " + StageNames.stage7_2.value + " - Energy Sphere 2")
    extra_stage7_2_esphere_3 = ("EX " + StageNames.stage7_2.value + " - Energy Sphere 3")
    extra_stage7_2_esphere_4 = ("EX " + StageNames.stage7_2.value + " - Energy Sphere 4")
    extra_stage7_2_esphere_5 = ("EX " + StageNames.stage7_2.value + " - Energy Sphere 5")
    extra_stage7_2_complete = ("EX " + StageNames.stage7_2.value + " - Complete")

    stage7_3_esphere_1 = (StageNames.stage7_3.value + " - Energy Sphere 1")
    stage7_3_esphere_2 = (StageNames.stage7_3.value + " - Energy Sphere 2")
    stage7_3_esphere_3 = (StageNames.stage7_3.value + " - Energy Sphere 3")
    stage7_3_esphere_4 = (StageNames.stage7_3.value + " - Energy Sphere 4")
    stage7_3_esphere_5 = (StageNames.stage7_3.value + " - Energy Sphere 5")
    stage7_3_complete = (StageNames.stage7_3.value + " - Complete")
    extra_stage7_3_esphere_1 = ("EX " + StageNames.stage7_3.value + " - Energy Sphere 1")
    extra_stage7_3_esphere_2 = ("EX " + StageNames.stage7_3.value + " - Energy Sphere 2")
    extra_stage7_3_esphere_3 = ("EX " + StageNames.stage7_3.value + " - Energy Sphere 3")
    extra_stage7_3_esphere_4 = ("EX " + StageNames.stage7_3.value + " - Energy Sphere 4")
    extra_stage7_3_esphere_5 = ("EX " + StageNames.stage7_3.value + " - Energy Sphere 5")
    extra_stage7_3_complete = ("EX " + StageNames.stage7_3.value + " - Complete")
    
    stage7_4_complete = (StageNames.stage7_4.value + " - Complete")
    extra_stage7_4_complete = ("EX " + StageNames.stage7_4.value + " - Complete")

    
    stage8_3_complete = (StageNames.stage8_3.value + " - Complete")
    extra_stage8_3_complete = ("EX " + StageNames.stage8_3.value + " - Complete")
    
    stage8_4_complete = (StageNames.stage8_4.value + " - Complete")
    extra_stage8_4_complete = ("EX " + StageNames.stage8_4.value + " - Complete")

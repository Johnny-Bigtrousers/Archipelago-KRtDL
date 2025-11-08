import typing
from BaseClasses import Location
from .GameNames import LocationNames

BaseLocationID = 24102011 + 40

class KRtDLLocations(Location):
    game: str = "Kirby's Return to Dream Land"

stage_completion_table = {
    LocationNames.stage1_1_complete.value: BaseLocationID,
    LocationNames.stage1_2_complete.value: BaseLocationID + 1,
    LocationNames.stage1_3_complete.value: BaseLocationID + 2,
    LocationNames.stage1_4_complete.value: BaseLocationID + 3,
    LocationNames.stage2_1_complete.value: BaseLocationID + 5,
    LocationNames.stage2_2_complete.value: BaseLocationID + 6,
    LocationNames.stage2_3_complete.value: BaseLocationID + 7,
    LocationNames.stage2_4_complete.value: BaseLocationID + 8,
    LocationNames.stage3_1_complete.value: BaseLocationID + 9,
    LocationNames.stage3_2_complete.value: BaseLocationID + 10,
    LocationNames.stage3_3_complete.value: BaseLocationID + 11,
    LocationNames.stage3_4_complete.value: BaseLocationID + 12,
    LocationNames.stage4_1_complete.value: BaseLocationID + 13,
    LocationNames.stage4_2_complete.value: BaseLocationID + 14,
    LocationNames.stage4_3_complete.value: BaseLocationID + 15,
    LocationNames.stage4_4_complete.value: BaseLocationID + 16,
    LocationNames.stage4_5_complete.value: BaseLocationID + 17,
    LocationNames.stage5_1_complete.value: BaseLocationID + 18,
    LocationNames.stage5_2_complete.value: BaseLocationID + 19,
    LocationNames.stage5_3_complete.value: BaseLocationID + 20,
    LocationNames.stage5_4_complete.value: BaseLocationID + 21,
    LocationNames.stage5_5_complete.value: BaseLocationID + 22,
    LocationNames.stage6_1_complete.value: BaseLocationID + 23,
    LocationNames.stage6_2_complete.value: BaseLocationID + 24,
    LocationNames.stage6_3_complete.value: BaseLocationID + 25,
    LocationNames.stage6_4_complete.value: BaseLocationID + 26,
    LocationNames.stage6_5_complete.value: BaseLocationID + 27,
    LocationNames.stage6_6_complete.value: BaseLocationID + 28,
    LocationNames.stage7_1_complete.value: BaseLocationID + 29,
    LocationNames.stage7_2_complete.value: BaseLocationID + 30,
    LocationNames.stage7_3_complete.value: BaseLocationID + 31,
    LocationNames.stage7_4_complete.value: BaseLocationID + 32,
    LocationNames.stage8_3_complete.value: BaseLocationID + 33,
    LocationNames.stage8_4_complete.value: BaseLocationID + 34,
    
    LocationNames.extra_stage1_1_complete.value: BaseLocationID + 35,
    LocationNames.extra_stage1_2_complete.value: BaseLocationID + 36,
    LocationNames.extra_stage1_3_complete.value: BaseLocationID + 37,
    LocationNames.extra_stage1_4_complete.value: BaseLocationID + 38,
    LocationNames.extra_stage2_1_complete.value: BaseLocationID + 39,
    LocationNames.extra_stage2_2_complete.value: BaseLocationID + 40,
    LocationNames.extra_stage2_3_complete.value: BaseLocationID + 41,
    LocationNames.extra_stage2_4_complete.value: BaseLocationID + 42,
    LocationNames.extra_stage3_1_complete.value: BaseLocationID + 43,
    LocationNames.extra_stage3_2_complete.value: BaseLocationID + 44,
    LocationNames.extra_stage3_3_complete.value: BaseLocationID + 45,
    LocationNames.extra_stage3_4_complete.value: BaseLocationID + 46,
    LocationNames.extra_stage4_1_complete.value: BaseLocationID + 47,
    LocationNames.extra_stage4_2_complete.value: BaseLocationID + 48,
    LocationNames.extra_stage4_3_complete.value: BaseLocationID + 49,
    LocationNames.extra_stage4_4_complete.value: BaseLocationID + 50,
    LocationNames.extra_stage4_5_complete.value: BaseLocationID + 51,
    LocationNames.extra_stage5_1_complete.value: BaseLocationID + 52,
    LocationNames.extra_stage5_2_complete.value: BaseLocationID + 53,
    LocationNames.extra_stage5_3_complete.value: BaseLocationID + 54,
    LocationNames.extra_stage5_4_complete.value: BaseLocationID + 55,
    LocationNames.extra_stage5_5_complete.value: BaseLocationID + 56,
    LocationNames.extra_stage6_1_complete.value: BaseLocationID + 57,
    LocationNames.extra_stage6_2_complete.value: BaseLocationID + 58,
    LocationNames.extra_stage6_3_complete.value: BaseLocationID + 59,
    LocationNames.extra_stage6_4_complete.value: BaseLocationID + 60,
    LocationNames.extra_stage6_5_complete.value: BaseLocationID + 61,
    LocationNames.extra_stage6_6_complete.value: BaseLocationID + 62,
    LocationNames.extra_stage7_1_complete.value: BaseLocationID + 63,
    LocationNames.extra_stage7_2_complete.value: BaseLocationID + 64,
    LocationNames.extra_stage7_3_complete.value: BaseLocationID + 65,
    LocationNames.extra_stage7_4_complete.value: BaseLocationID + 66,
    LocationNames.extra_stage8_3_complete.value: BaseLocationID + 67,
    LocationNames.extra_stage8_4_complete.value: BaseLocationID + 68
}

energy_sphere_table = {
    LocationNames.stage1_1_esphere_1.value: BaseLocationID + 69,
    LocationNames.stage1_1_esphere_2.value: BaseLocationID + 70,
    LocationNames.stage1_1_esphere_3.value: BaseLocationID + 71,
    LocationNames.stage1_2_esphere_1.value: BaseLocationID + 72,
    LocationNames.stage1_2_esphere_2.value: BaseLocationID + 73,
    LocationNames.stage1_2_esphere_3.value: BaseLocationID + 74,
    LocationNames.stage1_3_esphere_1.value: BaseLocationID + 75,
    LocationNames.stage1_3_esphere_2.value: BaseLocationID + 76,
    LocationNames.stage1_3_esphere_3.value: BaseLocationID + 77,
    LocationNames.stage1_4_esphere_1.value: BaseLocationID + 78,
    LocationNames.stage1_4_esphere_2.value: BaseLocationID + 79,
    LocationNames.stage1_4_esphere_3.value: BaseLocationID + 80,
    LocationNames.stage1_4_esphere_4.value: BaseLocationID + 81,
    
    LocationNames.stage2_1_esphere_1.value: BaseLocationID + 82,
    LocationNames.stage2_1_esphere_2.value: BaseLocationID + 83,
    LocationNames.stage2_1_esphere_3.value: BaseLocationID + 84,
    LocationNames.stage2_2_esphere_1.value: BaseLocationID + 85,
    LocationNames.stage2_2_esphere_2.value: BaseLocationID + 86,
    LocationNames.stage2_2_esphere_3.value: BaseLocationID + 87,
    LocationNames.stage2_2_esphere_4.value: BaseLocationID + 88,    
    LocationNames.stage2_3_esphere_1.value: BaseLocationID + 89,
    LocationNames.stage2_3_esphere_2.value: BaseLocationID + 90,
    LocationNames.stage2_3_esphere_3.value: BaseLocationID + 91,
    LocationNames.stage2_3_esphere_4.value: BaseLocationID + 92,    
    LocationNames.stage2_4_esphere_1.value: BaseLocationID + 93,
    LocationNames.stage2_4_esphere_2.value: BaseLocationID + 94,
    LocationNames.stage2_4_esphere_3.value: BaseLocationID + 95,
    LocationNames.stage2_4_esphere_4.value: BaseLocationID + 96,
    LocationNames.stage2_4_esphere_5.value: BaseLocationID + 97,
    
    LocationNames.stage3_1_esphere_1.value: BaseLocationID + 98,
    LocationNames.stage3_1_esphere_2.value: BaseLocationID + 99,
    LocationNames.stage3_1_esphere_3.value: BaseLocationID + 100,
    LocationNames.stage3_2_esphere_1.value: BaseLocationID + 101,
    LocationNames.stage3_2_esphere_2.value: BaseLocationID + 102,
    LocationNames.stage3_2_esphere_3.value: BaseLocationID + 103,
    LocationNames.stage3_2_esphere_4.value: BaseLocationID + 104,
    LocationNames.stage3_3_esphere_1.value: BaseLocationID + 105,
    LocationNames.stage3_3_esphere_2.value: BaseLocationID + 106,
    LocationNames.stage3_3_esphere_3.value: BaseLocationID + 107,
    LocationNames.stage3_3_esphere_4.value: BaseLocationID + 108,
    LocationNames.stage3_4_esphere_1.value: BaseLocationID + 109,
    LocationNames.stage3_4_esphere_2.value: BaseLocationID + 110,
    LocationNames.stage3_4_esphere_3.value: BaseLocationID + 111,
    LocationNames.stage3_4_esphere_4.value: BaseLocationID + 112,
    LocationNames.stage3_4_esphere_5.value: BaseLocationID + 113,
    
    LocationNames.stage4_1_esphere_1.value: BaseLocationID + 114,
    LocationNames.stage4_1_esphere_2.value: BaseLocationID + 115,
    LocationNames.stage4_1_esphere_3.value: BaseLocationID + 116,
    LocationNames.stage4_2_esphere_1.value: BaseLocationID + 117,
    LocationNames.stage4_2_esphere_2.value: BaseLocationID + 118,
    LocationNames.stage4_2_esphere_3.value: BaseLocationID + 119,
    LocationNames.stage4_2_esphere_4.value: BaseLocationID + 120,
    LocationNames.stage4_3_esphere_1.value: BaseLocationID + 121,
    LocationNames.stage4_3_esphere_2.value: BaseLocationID + 122,
    LocationNames.stage4_3_esphere_3.value: BaseLocationID + 123,
    LocationNames.stage4_3_esphere_4.value: BaseLocationID + 124,
    LocationNames.stage4_4_esphere_1.value: BaseLocationID + 125,
    LocationNames.stage4_4_esphere_2.value: BaseLocationID + 126,
    LocationNames.stage4_4_esphere_3.value: BaseLocationID + 127,
    LocationNames.stage4_4_esphere_4.value: BaseLocationID + 128,
    LocationNames.stage4_5_esphere_1.value: BaseLocationID + 129,
    LocationNames.stage4_5_esphere_2.value: BaseLocationID + 130,
    LocationNames.stage4_5_esphere_3.value: BaseLocationID + 131,
    LocationNames.stage4_5_esphere_4.value: BaseLocationID + 132,
    
    LocationNames.stage5_1_esphere_1.value: BaseLocationID + 133,
    LocationNames.stage5_1_esphere_2.value: BaseLocationID + 134,
    LocationNames.stage5_1_esphere_3.value: BaseLocationID + 135,
    LocationNames.stage5_1_esphere_4.value: BaseLocationID + 136,
    LocationNames.stage5_2_esphere_1.value: BaseLocationID + 137,
    LocationNames.stage5_2_esphere_2.value: BaseLocationID + 138,
    LocationNames.stage5_2_esphere_3.value: BaseLocationID + 139,
    LocationNames.stage5_2_esphere_4.value: BaseLocationID + 140,
    LocationNames.stage5_3_esphere_1.value: BaseLocationID + 141,
    LocationNames.stage5_3_esphere_2.value: BaseLocationID + 142,
    LocationNames.stage5_3_esphere_3.value: BaseLocationID + 143,
    LocationNames.stage5_3_esphere_4.value: BaseLocationID + 144,
    LocationNames.stage5_4_esphere_1.value: BaseLocationID + 145,
    LocationNames.stage5_4_esphere_2.value: BaseLocationID + 146,
    LocationNames.stage5_4_esphere_3.value: BaseLocationID + 147,
    LocationNames.stage5_4_esphere_4.value: BaseLocationID + 148,
    LocationNames.stage5_5_esphere_1.value: BaseLocationID + 149,
    LocationNames.stage5_5_esphere_2.value: BaseLocationID + 150,
    LocationNames.stage5_5_esphere_3.value: BaseLocationID + 151,
    LocationNames.stage5_5_esphere_4.value: BaseLocationID + 152,
    
    LocationNames.stage6_1_esphere_1.value: BaseLocationID + 153,
    LocationNames.stage6_1_esphere_2.value: BaseLocationID + 154,
    LocationNames.stage6_1_esphere_3.value: BaseLocationID + 155,
    LocationNames.stage6_2_esphere_1.value: BaseLocationID + 156,
    LocationNames.stage6_2_esphere_2.value: BaseLocationID + 157,
    LocationNames.stage6_2_esphere_3.value: BaseLocationID + 158,
    LocationNames.stage6_2_esphere_4.value: BaseLocationID + 159,
    LocationNames.stage6_3_esphere_1.value: BaseLocationID + 160,
    LocationNames.stage6_3_esphere_2.value: BaseLocationID + 161,
    LocationNames.stage6_3_esphere_3.value: BaseLocationID + 162,
    LocationNames.stage6_3_esphere_4.value: BaseLocationID + 163,
    LocationNames.stage6_4_esphere_1.value: BaseLocationID + 164,
    LocationNames.stage6_4_esphere_2.value: BaseLocationID + 165,
    LocationNames.stage6_4_esphere_3.value: BaseLocationID + 166,
    LocationNames.stage6_4_esphere_4.value: BaseLocationID + 167,
    LocationNames.stage6_4_esphere_5.value: BaseLocationID + 168,
    LocationNames.stage6_5_esphere_1.value: BaseLocationID + 169,
    LocationNames.stage6_5_esphere_2.value: BaseLocationID + 170,
    LocationNames.stage6_5_esphere_3.value: BaseLocationID + 171,
    LocationNames.stage6_5_esphere_4.value: BaseLocationID + 172,
    LocationNames.stage6_5_esphere_5.value: BaseLocationID + 173,

    LocationNames.stage7_1_esphere_1.value: BaseLocationID + 174,
    LocationNames.stage7_1_esphere_2.value: BaseLocationID + 175,
    LocationNames.stage7_1_esphere_3.value: BaseLocationID + 176,
    LocationNames.stage7_1_esphere_4.value: BaseLocationID + 177,
    LocationNames.stage7_1_esphere_5.value: BaseLocationID + 178,
    LocationNames.stage7_2_esphere_1.value: BaseLocationID + 179,
    LocationNames.stage7_2_esphere_2.value: BaseLocationID + 180,
    LocationNames.stage7_2_esphere_3.value: BaseLocationID + 181,
    LocationNames.stage7_2_esphere_4.value: BaseLocationID + 182,
    LocationNames.stage7_2_esphere_5.value: BaseLocationID + 183,
    LocationNames.stage7_3_esphere_1.value: BaseLocationID + 184,
    LocationNames.stage7_3_esphere_2.value: BaseLocationID + 185,
    LocationNames.stage7_3_esphere_3.value: BaseLocationID + 186,
    LocationNames.stage7_3_esphere_4.value: BaseLocationID + 187,
    LocationNames.stage7_3_esphere_5.value: BaseLocationID + 189,


    LocationNames.extra_stage1_1_esphere_1.value: BaseLocationID + 190,
    LocationNames.extra_stage1_1_esphere_2.value: BaseLocationID + 191,
    LocationNames.extra_stage1_1_esphere_3.value: BaseLocationID + 192,
    LocationNames.extra_stage1_2_esphere_1.value: BaseLocationID + 193,
    LocationNames.extra_stage1_2_esphere_2.value: BaseLocationID + 194,
    LocationNames.extra_stage1_2_esphere_3.value: BaseLocationID + 195,
    LocationNames.extra_stage1_3_esphere_1.value: BaseLocationID + 196,
    LocationNames.extra_stage1_3_esphere_2.value: BaseLocationID + 197,
    LocationNames.extra_stage1_3_esphere_3.value: BaseLocationID + 198,
    LocationNames.extra_stage1_4_esphere_1.value: BaseLocationID + 199,
    LocationNames.extra_stage1_4_esphere_2.value: BaseLocationID + 200,
    LocationNames.extra_stage1_4_esphere_3.value: BaseLocationID + 201,
    LocationNames.extra_stage1_4_esphere_4.value: BaseLocationID + 202,
    
    LocationNames.extra_stage2_1_esphere_1.value: BaseLocationID + 203,
    LocationNames.extra_stage2_1_esphere_2.value: BaseLocationID + 204,
    LocationNames.extra_stage2_1_esphere_3.value: BaseLocationID + 205,
    LocationNames.extra_stage2_2_esphere_1.value: BaseLocationID + 206,
    LocationNames.extra_stage2_2_esphere_2.value: BaseLocationID + 207,
    LocationNames.extra_stage2_2_esphere_3.value: BaseLocationID + 208,
    LocationNames.extra_stage2_2_esphere_4.value: BaseLocationID + 209,    
    LocationNames.extra_stage2_3_esphere_1.value: BaseLocationID + 210,
    LocationNames.extra_stage2_3_esphere_2.value: BaseLocationID + 211,
    LocationNames.extra_stage2_3_esphere_3.value: BaseLocationID + 212,
    LocationNames.extra_stage2_3_esphere_4.value: BaseLocationID + 213,    
    LocationNames.extra_stage2_4_esphere_1.value: BaseLocationID + 214,
    LocationNames.extra_stage2_4_esphere_2.value: BaseLocationID + 215,
    LocationNames.extra_stage2_4_esphere_3.value: BaseLocationID + 216,
    LocationNames.extra_stage2_4_esphere_4.value: BaseLocationID + 217,
    LocationNames.extra_stage2_4_esphere_5.value: BaseLocationID + 218,
    
    LocationNames.extra_stage3_1_esphere_1.value: BaseLocationID + 219,
    LocationNames.extra_stage3_1_esphere_2.value: BaseLocationID + 220,
    LocationNames.extra_stage3_1_esphere_3.value: BaseLocationID + 221,
    LocationNames.extra_stage3_2_esphere_1.value: BaseLocationID + 222,
    LocationNames.extra_stage3_2_esphere_2.value: BaseLocationID + 223,
    LocationNames.extra_stage3_2_esphere_3.value: BaseLocationID + 224,
    LocationNames.extra_stage3_2_esphere_4.value: BaseLocationID + 225,
    LocationNames.extra_stage3_3_esphere_1.value: BaseLocationID + 226,
    LocationNames.extra_stage3_3_esphere_2.value: BaseLocationID + 227,
    LocationNames.extra_stage3_3_esphere_3.value: BaseLocationID + 228,
    LocationNames.extra_stage3_3_esphere_4.value: BaseLocationID + 229,
    LocationNames.extra_stage3_4_esphere_1.value: BaseLocationID + 230,
    LocationNames.extra_stage3_4_esphere_2.value: BaseLocationID + 231,
    LocationNames.extra_stage3_4_esphere_3.value: BaseLocationID + 232,
    LocationNames.extra_stage3_4_esphere_4.value: BaseLocationID + 233,
    LocationNames.extra_stage3_4_esphere_5.value: BaseLocationID + 234,
    
    LocationNames.extra_stage4_1_esphere_1.value: BaseLocationID + 235,
    LocationNames.extra_stage4_1_esphere_2.value: BaseLocationID + 236,
    LocationNames.extra_stage4_1_esphere_3.value: BaseLocationID + 237,
    LocationNames.extra_stage4_2_esphere_1.value: BaseLocationID + 238,
    LocationNames.extra_stage4_2_esphere_2.value: BaseLocationID + 239,
    LocationNames.extra_stage4_2_esphere_3.value: BaseLocationID + 240,
    LocationNames.extra_stage4_2_esphere_4.value: BaseLocationID + 241,
    LocationNames.extra_stage4_3_esphere_1.value: BaseLocationID + 242,
    LocationNames.extra_stage4_3_esphere_2.value: BaseLocationID + 243,
    LocationNames.extra_stage4_3_esphere_3.value: BaseLocationID + 244,
    LocationNames.extra_stage4_3_esphere_4.value: BaseLocationID + 245,
    LocationNames.extra_stage4_4_esphere_1.value: BaseLocationID + 246,
    LocationNames.extra_stage4_4_esphere_2.value: BaseLocationID + 247,
    LocationNames.extra_stage4_4_esphere_3.value: BaseLocationID + 248,
    LocationNames.extra_stage4_4_esphere_4.value: BaseLocationID + 249,
    LocationNames.extra_stage4_5_esphere_1.value: BaseLocationID + 250,
    LocationNames.extra_stage4_5_esphere_2.value: BaseLocationID + 251,
    LocationNames.extra_stage4_5_esphere_3.value: BaseLocationID + 252,
    LocationNames.extra_stage4_5_esphere_4.value: BaseLocationID + 253,
    
    LocationNames.extra_stage5_1_esphere_1.value: BaseLocationID + 254,
    LocationNames.extra_stage5_1_esphere_2.value: BaseLocationID + 255,
    LocationNames.extra_stage5_1_esphere_3.value: BaseLocationID + 256,
    LocationNames.extra_stage5_1_esphere_4.value: BaseLocationID + 257,
    LocationNames.extra_stage5_2_esphere_1.value: BaseLocationID + 258,
    LocationNames.extra_stage5_2_esphere_2.value: BaseLocationID + 259,
    LocationNames.extra_stage5_2_esphere_3.value: BaseLocationID + 260,
    LocationNames.extra_stage5_2_esphere_4.value: BaseLocationID + 261,
    LocationNames.extra_stage5_3_esphere_1.value: BaseLocationID + 262,
    LocationNames.extra_stage5_3_esphere_2.value: BaseLocationID + 263,
    LocationNames.extra_stage5_3_esphere_3.value: BaseLocationID + 264,
    LocationNames.extra_stage5_3_esphere_4.value: BaseLocationID + 265,
    LocationNames.extra_stage5_4_esphere_1.value: BaseLocationID + 266,
    LocationNames.extra_stage5_4_esphere_2.value: BaseLocationID + 267,
    LocationNames.extra_stage5_4_esphere_3.value: BaseLocationID + 268,
    LocationNames.extra_stage5_4_esphere_4.value: BaseLocationID + 269,
    LocationNames.extra_stage5_5_esphere_1.value: BaseLocationID + 270,
    LocationNames.extra_stage5_5_esphere_2.value: BaseLocationID + 271,
    LocationNames.extra_stage5_5_esphere_3.value: BaseLocationID + 272,
    LocationNames.extra_stage5_5_esphere_4.value: BaseLocationID + 273,
    
    LocationNames.extra_stage6_1_esphere_1.value: BaseLocationID + 274,
    LocationNames.extra_stage6_1_esphere_2.value: BaseLocationID + 275,
    LocationNames.extra_stage6_1_esphere_3.value: BaseLocationID + 276,
    LocationNames.extra_stage6_2_esphere_1.value: BaseLocationID + 277,
    LocationNames.extra_stage6_2_esphere_2.value: BaseLocationID + 278,
    LocationNames.extra_stage6_2_esphere_3.value: BaseLocationID + 279,
    LocationNames.extra_stage6_2_esphere_4.value: BaseLocationID + 280,
    LocationNames.extra_stage6_3_esphere_1.value: BaseLocationID + 281,
    LocationNames.extra_stage6_3_esphere_2.value: BaseLocationID + 282,
    LocationNames.extra_stage6_3_esphere_3.value: BaseLocationID + 283,
    LocationNames.extra_stage6_3_esphere_4.value: BaseLocationID + 284,
    LocationNames.extra_stage6_4_esphere_1.value: BaseLocationID + 285,
    LocationNames.extra_stage6_4_esphere_2.value: BaseLocationID + 286,
    LocationNames.extra_stage6_4_esphere_3.value: BaseLocationID + 287,
    LocationNames.extra_stage6_4_esphere_4.value: BaseLocationID + 288,
    LocationNames.extra_stage6_4_esphere_5.value: BaseLocationID + 289,
    LocationNames.extra_stage6_5_esphere_1.value: BaseLocationID + 290,
    LocationNames.extra_stage6_5_esphere_2.value: BaseLocationID + 291,
    LocationNames.extra_stage6_5_esphere_3.value: BaseLocationID + 292,
    LocationNames.extra_stage6_5_esphere_4.value: BaseLocationID + 293,
    LocationNames.extra_stage6_5_esphere_5.value: BaseLocationID + 294,

    LocationNames.extra_stage7_1_esphere_1.value: BaseLocationID + 295,
    LocationNames.extra_stage7_1_esphere_2.value: BaseLocationID + 296,
    LocationNames.extra_stage7_1_esphere_3.value: BaseLocationID + 297,
    LocationNames.extra_stage7_1_esphere_4.value: BaseLocationID + 298,
    LocationNames.extra_stage7_1_esphere_5.value: BaseLocationID + 299,
    LocationNames.extra_stage7_2_esphere_1.value: BaseLocationID + 300,
    LocationNames.extra_stage7_2_esphere_2.value: BaseLocationID + 301,
    LocationNames.extra_stage7_2_esphere_3.value: BaseLocationID + 302,
    LocationNames.extra_stage7_2_esphere_4.value: BaseLocationID + 303,
    LocationNames.extra_stage7_2_esphere_5.value: BaseLocationID + 304,
    LocationNames.extra_stage7_3_esphere_1.value: BaseLocationID + 305,
    LocationNames.extra_stage7_3_esphere_2.value: BaseLocationID + 306,
    LocationNames.extra_stage7_3_esphere_3.value: BaseLocationID + 307,
    LocationNames.extra_stage7_3_esphere_4.value: BaseLocationID + 308,
    LocationNames.extra_stage7_3_esphere_5.value: BaseLocationID + 309
}

part_sphere_table = {
    # not entirely sure how to handle this yet.
    # LocationNames.stage1_1_complete.value: BaseID + 1
    LocationNames.stage1_5_part.value: BaseLocationID + 310,
    LocationNames.stage2_5_part.value: BaseLocationID + 311,
    LocationNames.stage3_5_part.value: BaseLocationID + 312,
    LocationNames.stage4_6_part.value: BaseLocationID + 313,
    LocationNames.stage5_6_part.value: BaseLocationID + 314,
    LocationNames.extra_stage1_5_part.value: BaseLocationID + 315,
    LocationNames.extra_stage2_5_part.value: BaseLocationID + 316,
    LocationNames.extra_stage3_5_part.value: BaseLocationID + 317,
    LocationNames.extra_stage4_6_part.value: BaseLocationID + 318,
    LocationNames.extra_stage5_6_part.value: BaseLocationID + 319
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

subgame_table = {
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
    **maxim_tomato_table,
    **subgame_table
}

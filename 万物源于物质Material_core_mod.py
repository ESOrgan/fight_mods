"""
Material_core 万物源于物质
核心模组
"""
class_name = "MaterialCore"


class MaterialCore:
    def __init__(self):
        self.GUI = False
        self.LOAD_GUI = False
        self.PRELOAD_ITEM = True
        self.ITEM_PREFIX = "Mat"
        self.NEED_BASE_MOD = False
        self.ITEMS = {
            "1": "物质I",
            "2": "物质II",
            "3": "物质III",
            "4": "物质IV",
            "5": "物质V",
            "6": "B级物质",
            "7": "A级物质",
            "8": "S级物质",
                      }
        self.ITEMS_PROPERTY = {
            "1": {"type": "m", "sell": 5, "description": "1级物质，泛着黯淡的灰色", "mat_flag": None},
            "2": {"type": "m", "sell": 10, "description": "2级物质，泛着稍亮的浅灰色", "mat_flag": None},
            "3": {"type": "m", "sell": 40, "description": "3级物质，泛着明亮的的白色", "mat_flag": None},
            "4": {"type": "m", "sell": 160, "description": "4级物质，泛着令人愉悦的的天蓝色", "mat_flag": None},
            "5": {"type": "m", "sell": 800, "description": "5级物质，泛着深邃的深蓝色", "mat_flag": None},
            "6": {"type": "m", "sell": 9000, "description": "新的里程碑！此前的1~5级物质为C级物质，且合成B级及以上物质将获得价值加成"
                                                            "\nB级物质，泛着幽幽的紫色，物质内似乎有暗流涌动", "mat_flag": None},
            "7": {"type": "m", "sell": 130000, "description": "史诗里程碑！15个B级物质的精华！\nA级物质，泛着令人激动的橙色，"
                                                              "物质内明显有暗流涌动", "mat_flag": None},
            "8": {"type": "m", "sell": 7000000, "description": "传说里程碑！50个A级物质的精华！\nS级物质，泛着神圣的金色，"
                                                               "物质外散发着金色的光波和涌动的流体金色物质\n它能自身悬空，"
                                                               "同时这个物质本身也是一个微型引力场，但引力很小，"
                                                               "只能把物质周围的流体S级物质吸引在周围涌动", "mat_flag": None},
        }

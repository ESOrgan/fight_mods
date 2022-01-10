import random

import easygui as g

class_name = "LeftAndRight"


def get_key(value, dict_obj):
    for key, val in dict_obj.items():
        if val == value:
            return key


class LeftAndRight:
    def __init__(self):
        self.name = "left and right"
        self.GUI = True
        self.LOAD_GUI = False
        self.version = "0.0.1"
        self.NEED_BASE_MOD = False
        self.PRELOAD_ITEM = True
        self.things = ["", "你死了", "你去玩的时候不小心摔了一跤，头上有了一个大包", "这段记忆不知怎的消失了", "你喜欢上了隔壁的一个人", "请的家教天天教你1+1=2", "你学会了骂人",
                       "你被父母打了一次", "你用父母的手机玩王者荣耀", "腾讯与网易打起了官司，\n笑死，屁用没有", "笑死，没什么事发生", "", "", "", "", "", "", "", "",
                       "", ""]
        self.year = 0
        self.thing = 0
        self.ITEM_PREFIX = "LAR"
        self.ITEMS = {
            "lstone": "左之石", "rstone": "右之石"
        }
        self.ITEMS_PROPERTY = {
            "lstone": {"atk": [30, 30], "type": "wep", "skill": [51], "description": "神奇的石头,功能未知",
                       "sell": 2000},
            "rstone": {"atk": [20, 20], "type": "wep", "skill": [51], "description": "神奇的石头,来之不易,先别卖掉吧",
                       "sell": 4000}
        }

    def main(self, **kwargs):
        g.msgbox(f"{self.name}\n"
                 "┌───────────────┐\n"
                 "│      Energy Studio           │\n"
                 "└───────────────┘\n")
        while True:
            choose = g.indexbox(f"{self.name}\n"
                                "制作左之石和右之石",
                                choices=["左之石", "右之石", "关于", "使用左之石", "使用右之石"])

            if choose is None:
                break

            if choose == 0:
                while True:
                    self.thing = random.randint(1, 10)
                    if self.year == 0:
                        g.msgbox("你出生了。")

                    if self.year == 20:
                        kwargs["pocket"]["inventory"].append("LARlstone")

                    g.msgbox(f"{self.year}岁:{self.things[self.thing]}")

                    if self.thing == 1 or self.thing == 11 or self.thing == 21 or self.year == 30:
                        self.year = 0
                        break

                    self.year += 1

            if choose == 1:
                if kwargs["player_property"]["hp"] <= 100 or kwargs["player_property"]["gold"] <= 1000:
                    g.msgbox("你的状态不够，不可获得")
                else:
                    kwargs["pocket"]["inventory"].append("LARrstone")
                    kwargs["player_property"]["hp"] -= 100
                    kwargs["player_property"]["gold"] -= 1000

            if choose == 2:
                g.msgbox("暂无......")
                g.msgbox("自己探究吧......")
                pass
            if choose == 3:
                inv_dis = []
                for i in kwargs["pocket"]["inventory"]:
                    inv_dis.append(kwargs["item_namespaces"][i])
                while len(inv_dis) < 2:
                    inv_dis.append("无")

                it_select = g.choicebox(
                    "sssssssss", choices=inv_dis)
                it_select = get_key(it_select, kwargs["item_namespaces"])
                if it_select == "LARlstone":
                    inv.remove("LARlstone")
                    kwargs["player_property"]["hp"] += 100
                    if kwargs["player_property"]["hp"] > kwargs["player_property"]["max_hp"]:
                        kwargs["player_property"]["hp"] = kwargs["player_property"]["max_hp"]
            if choose == 4:
                inv_dis = []
                for i in kwargs["pocket"]["inventory"]:
                    inv_dis.append(kwargs["item_namespaces"][i])
                while len(inv_dis) < 2:
                    inv_dis.append("无")

                it_select = g.choicebox(
                    "sssssssss", choices=inv_dis)
                it_select = get_key(it_select, kwargs["item_namespaces"])
                if it_select == "LARrstone":
                    kwargs["pocket"]["inventory"].remove("LARrstone")
                    kwargs["player_property"]["mana"] += 100
                    kwargs["player_property"]["str"] += 100
                    if kwargs["player_property"]["mana"] > kwargs["player_property"]["max_mana"]:
                        kwargs["player_property"]["mana"] = kwargs["player_property"]["max_mana"]

                    if kwargs["player_property"]["str"] > kwargs["player_property"]["max_str"]:
                        kwargs["player_property"]["str"] = kwargs["player_property"]["max_str"]
                    if kwargs["player_property"]["hp"] > kwargs["player_property"]["max_hp"]:
                        kwargs["player_property"]["hp"] = kwargs["player_property"]["max_hp"]
        return kwargs

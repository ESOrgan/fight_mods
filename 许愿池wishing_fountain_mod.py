import easygui as g
import time
import random

class_name = "WishingFountain"


class WishingFountain:
    def __init__(self):
        self.possibility = []
        self.FOUNTAIN_BLACKLIST = [640, 632, 622, 621, 637]
        self.GUI = True
        self.LOAD_GUI = True
        self.PRELOAD_ITEM = True
        self.NEED_BASE_MOD = False
        self.ITEM_PREFIX = "WF_wishing_fountain"
        self.ITEMS = {
            "Fountain_reset_poison": "许愿池重置剂"
        }
        self.ITEMS_PROPERTY = {
            "Fountain_reset_poison": {"type": "m", "description": "神奇的药水，可以重置许愿池的消费累计（骗 过 神 明）",
                                      "sell": 600}
        }
        self.name = "许愿池"
        self.version = "0.0.2"

    def info_print(self, msg):
        print(time.strftime(f"[%H:%M:%S][INFO][WF{self.version}]", time.localtime()) + msg)

    def load(self, **kwargs):
        self.info_print("Start preloading")
        self.info_print("adding possibility list")
        for i in kwargs["item_property"].keys():
            if str(i)[0] == "6" and i not in self.FOUNTAIN_BLACKLIST:
                self.possibility.append(i)
        for i in range(100):
            self.possibility.append(0)
        self.info_print("done")
        self.info_print("preload finished")
        self.info_print(f"""
----------------------------
|     Wishing  Fountain    |
|          v0.0.2          |
|   From  Infinity-Energy  |
----------------------------
        """)

    def main(self, **kwargs):
        if "wf_gold_num" not in kwargs["player_property"].keys():
            kwargs["player_property"]["wf_gold_num"] = 0
        while True:
            f_choice = g.indexbox("许愿池边金光闪耀", choices=["许愿", "许愿池商店", "使用许愿池重置剂"])
            if f_choice is None:
                break
            if f_choice == 0:
                while True:
                    need_gold = int(kwargs["player_property"]["wf_gold_num"] / 5 + 1) * 5
                    if not g.ccbox("你要许愿吗？", choices=[f"是的({need_gold}$)", "不了"]):
                        break
                    if kwargs["player_property"]["gold"] < need_gold:
                        g.msgbox("你没有足够的钱")
                        break
                    kwargs["player_property"]["gold"] -= need_gold
                    wish = random.choice(self.possibility)
                    if wish == 0:
                        g.msgbox("什么事也没有发生")
                    else:
                        kwargs["pocket"]["inventory"].append(wish)
                        g.msgbox(f"你获得了{kwargs['item_namespaces'][wish]}")
                    kwargs["player_property"]["wf_gold_num"] += 1
            elif f_choice == 1:
                while True:
                    if g.ccbox("神秘的店员：你可以在这里买到许愿池重置剂", choices=["购买(600$)", "不了"]):
                        kwargs["player_property"]["gold"] -= 600
                        kwargs["pocket"]["inventory"].append("WF_wishing_fountainFountain_reset_poison")
                        g.msgbox("购买成功")
                    else:
                        break
            elif f_choice == 2:
                if g.ccbox("你要向许愿池使用许愿池重置剂吗？", choices=["是的", "不了"]):
                    if "WF_wishing_fountainFountain_reset_poison" in kwargs["pocket"]["inventory"]:
                        kwargs["player_property"]["wf_gold_num"] = 0
                        kwargs["pocket"]["inventory"].remove("WF_wishing_fountainFountain_reset_poison")
                        g.msgbox("已重置")
        return kwargs

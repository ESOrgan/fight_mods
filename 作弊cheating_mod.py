import easygui as g
class_name = "Cheating"


class Cheating:
    def __init__(self):
        self.name = "作弊"
        self.GUI = True
        self.LOAD_GUI = False
        self.version = "0.0.1"
        self.NEED_BASE_MOD = False
        self.PRELOAD_ITEM = False

    def main(self, **kwargs):
        while True:
            choice = g.indexbox(f"{self.name}\n警告：此行为会对你的存档造成正常情况下不可逆的作弊标记，谨慎使用！",
                                choices=["加经验", "增加金币"])
            if choice is None:
                break
            elif choice == 0:
                while True:
                    breaking = False
                    up_num = g.enterbox("你要加多少经验？")
                    if up_num is None:
                        breaking = True
                        break
                    try:
                        up_num = int(up_num)
                    except ValueError:
                        continue
                    else:
                        break
                if breaking:
                    continue
                if not kwargs["player_property"]["cheating"]:
                    if not g.ccbox("请注意：此行为会对你的存档造成正常情况下不可逆的作弊标记，是否继续？", choices=["是的", "不了"]):
                        continue
                    kwargs["player_property"]["cheating"] = True
                kwargs["player_property"]["exp"] += up_num
                g.msgbox("已增加")
            elif choice == 1:
                while True:
                    breaking = False
                    up_num = g.enterbox("你要加多少钱？")
                    if up_num is None:
                        breaking = True
                        break
                    try:
                        up_num = int(up_num)
                    except ValueError:
                        continue
                    else:
                        break
                if breaking:
                    continue
                if not kwargs["player_property"]["cheating"]:
                    if not g.ccbox("请注意：此行为会对你的存档造成正常情况下不可逆的作弊标记，是否继续？", choices=["是的", "不了"]):
                        continue
                    kwargs["player_property"]["cheating"] = True
                kwargs["player_property"]["gold"] += up_num
                g.msgbox("已增加")
        return kwargs

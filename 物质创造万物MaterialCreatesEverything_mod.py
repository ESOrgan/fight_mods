"""
MaterialCreatesEverything 物质创造万物
前置模组：万物源于物质Material_core
"""
import easygui as g
import collections
class_name = "MaterialCreation"
craft_expr = {
    "木棍 * 2 -> 物质I": "2 * 11 -> Mat1",
    "小石子 * 10 -> 物质I": "10 * 61 -> Mat1",
    "物质I * 2 -> 物质II": "2 * Mat1 -> Mat2",
    "物质II * 4 -> 物质III": "4 * Mat2 -> Mat3",
    "物质III * 4 -> 物质IV": "4 * Mat3 -> Mat4",
    "物质IV * 5 -> 物质V": "5 * Mat4 -> Mat5",
    "物质V * 10 -> B级物质": "10 * Mat5 -> Mat6",
    "B级物质 * 15 -> A级物质": "15 * Mat6 -> Mat7",
    "A级物质 * 50 -> S级物质": "50 * Mat7 -> Mat8",
}


class MaterialCreation:
    def __init__(self):
        self.GUI = True
        self.LOAD_GUI = False
        self.name = "物质创造万物"
        self.PRELOAD_ITEM = False
        self.NEED_BASE_MOD = True
        self.BASE_MOD_LIST = ["MaterialCore"]

    @staticmethod
    def main(**kwargs):
        def craft_expr_interpreter(expr):
            materials_namespace = []
            expr = expr.split("->")
            expr[0] = expr[0].split(";")
            for materials in expr[0]:
                materials = materials.split("*")
                for i in range(int(materials[0])):
                    try:
                        materials_namespace.append(int(materials[1]))
                    except ValueError:
                        materials_namespace.append(materials[1])
            try:
                return materials_namespace, int(expr[1])
            except ValueError:
                return materials_namespace, expr[1].strip()

        def inventory_sort(inventory: list):
            for i in range(len(inventory) - 1):
                for j in range(len(inventory) - i - 1):
                    if str(inventory[j]) > str(inventory[j + 1]):
                        inventory[j], inventory[j + 1] = inventory[j + 1], inventory[j]
            return inventory

        def get_key(value, dict_obj=None):
            if dict_obj is None:
                dict_obj = kwargs["item_namespaces"]
            for key, val in dict_obj.items():
                if val == value:
                    return key

        if "ecf" not in kwargs["player_property"].keys():
            kwargs["player_property"]["ecf"] = 0
        if "mat_learn" not in kwargs["player_property"].keys():
            kwargs["player_property"]["mat_learn"] = []
        ecf = kwargs["player_property"]["ecf"]
        learn = kwargs["player_property"]["mat_learn"]
        while True:
            choice = g.indexbox("万物源于物质，物质创造万物！", choices=["物质打造台", "ECF转换台", "教程"])
            kwargs["pocket"]["inventory"] = inventory_sort(kwargs["pocket"]["inventory"])
            if choice == 0:
                while True:
                    craft_display = []
                    for craft_key in craft_expr.keys():
                        craft_display.append(craft_key)
                    crafting_item = g.choicebox(f"请选择你要合成的物品", choices=craft_display)
                    if crafting_item is None:
                        break
                    elif craft_expr[crafting_item] is None:
                        continue
                    craft_materials = craft_expr_interpreter(craft_expr[crafting_item])
                    materials_collections = collections.Counter(craft_materials[0])
                    pocket_collections = collections.Counter(kwargs["pocket"]["inventory"])
                    cyn = False
                    for mat in materials_collections.keys():
                        try:
                            mat_s = mat.strip()
                        except AttributeError:
                            mat_s = mat
                        if mat_s not in pocket_collections:
                            g.msgbox("你没有足够的材料")
                            cyn = True
                            break
                        elif pocket_collections[mat_s] < materials_collections[mat]:
                            g.msgbox("你没有足够的材料")
                            cyn = True
                            break
                    if cyn:
                        continue
                    while True:
                        breaking_craft_num = False
                        craft_num = g.enterbox("请输入你要合成的数量")
                        if craft_num is None:
                            breaking_craft_num = True
                            break
                        try:
                            craft_num = int(craft_num)
                        except ValueError:
                            continue
                        else:
                            break
                    if breaking_craft_num:
                        continue
                    craft_count = 0
                    while craft_count < craft_num:
                        pocket_collections = collections.Counter(kwargs["pocket"]["inventory"])
                        cyn = False
                        for mat in materials_collections.keys():
                            try:
                                mat_s = mat.strip()
                            except AttributeError:
                                mat_s = mat
                            if mat_s not in pocket_collections:
                                cyn = True
                                break
                            elif pocket_collections[mat_s] < materials_collections[mat]:
                                cyn = True
                                break
                        if cyn:
                            break
                        for mat in craft_materials[0]:
                            try:
                                mat = mat.strip()
                            except AttributeError:
                                mat_s = mat
                            kwargs["pocket"]["inventory"].remove(mat_s)
                        kwargs["pocket"]["inventory"].append(craft_materials[1])
                        craft_count += 1
                    if cyn:
                        g.msgbox(f"由于你的材料不够，你只合成了{craft_count} * {kwargs['item_namespaces'][craft_materials[1]]}")
                    else:
                        g.msgbox(f"你合成了{craft_count} * {kwargs['item_namespaces'][craft_materials[1]]}")

            elif choice == 1:
                while True:
                    ecf_choice = g.indexbox(f"""
                    {kwargs["player"]}
                    ECF: {ecf}
                    """, choices=["将物质转化为ECF/学习物品", "将ECF转化为物品"])
                    if ecf_choice is None:
                        break
                    if ecf_choice == 0:
                        while True:
                            inventory_display = []
                            for item in kwargs["pocket"]["inventory"]:
                                inventory_display.append(kwargs["item_namespaces"][item])
                            trans = get_key(g.choicebox("请选择要转化的物质或要学习的物品", choices=inventory_display))
                            if trans is None:
                                break
                            if "mat_flag" in kwargs["item_property"][trans].keys():
                                ecf_get = int(kwargs["item_property"][trans]["sell"] / 2)
                                while True:
                                    breaking_craft_num = False
                                    craft_num = g.enterbox("请输入你要转化的数量")
                                    if craft_num is None:
                                        breaking_craft_num = True
                                        break
                                    try:
                                        craft_num = int(craft_num)
                                    except ValueError:
                                        continue
                                    else:
                                        break
                                if breaking_craft_num:
                                    continue
                                craft_count = 0
                                cyn = False
                                while craft_count < craft_num:
                                    if trans not in kwargs["pocket"]["inventory"]:
                                        cyn = True
                                        break
                                    kwargs["pocket"]["inventory"].remove(trans)
                                    ecf += ecf_get
                                    craft_count += 1
                                if cyn:
                                    g.msgbox(f"由于你的物品不够，你只转化了{craft_count * ecf_get}ECF")
                                else:
                                    g.msgbox(f"你转化了{craft_count * ecf_get}ECF")
                            else:
                                if trans in learn:
                                    g.msgbox("此物品已学习过！")
                                    continue
                                learn.append(trans)
                                g.msgbox("已学习")
                    else:
                        while True:
                            trans_display = []
                            for item in learn:
                                trans_display.append(kwargs["item_namespaces"][item] + " " +
                                                     str(int(kwargs["item_property"][item]["sell"] / 2)) + "ECF")
                            trans_display = inventory_sort(trans_display)
                            while len(trans_display) < 2:
                                trans_display.append("未学习")
                            trans_item = g.choicebox("请选择你要转化的物品", choices=trans_display)
                            if trans_item is None:
                                break
                            if trans_item == "未学习":
                                g.msgbox("此槽位还未学习")
                                continue
                            trans_item = get_key(trans_item.split(" ")[0])
                            ecf_lose = int(kwargs["item_property"][trans_item]["sell"] / 2)
                            if ecf_lose <= 0:
                                ecf_lose = 1
                            while True:
                                breaking_craft_num = False
                                craft_num = g.enterbox("请输入你要转化的数量")
                                if craft_num is None:
                                    breaking_craft_num = True
                                    break
                                try:
                                    craft_num = int(craft_num)
                                except ValueError:
                                    continue
                                else:
                                    break
                            if breaking_craft_num:
                                continue
                            craft_count = 0
                            cyn = False
                            if ecf < ecf_lose:
                                g.msgbox("你没有足够的ECF")
                                continue
                            while craft_count < craft_num:
                                kwargs["pocket"]["inventory"].append(trans_item)
                                ecf -= ecf_lose
                                craft_count += 1
                                if kwargs["player_property"]["ecf"] < ecf_lose:
                                    cyn = True
                                    break
                            if cyn:
                                g.msgbox(f"由于你的物品不够，你只转化了{craft_count} * {kwargs['item_namespeces'][trans_item]}")
                            else:
                                g.msgbox(f"你转化了{craft_count} * {kwargs['item_namespeces'][trans_item]}")
            elif choice == 2:
                g.msgbox("""
    一、打造物质
    打开“物质打造台”，选择任意一项合成即可。
    所有的物质都由一级物质合成，一级物质可以由木棍或小石子合成。
    其中，合成B级及以上物质时，物质的价值（无论是fight原生金钱还是ECF）会有加成
                """)
                g.msgbox("""
    二、获得ECF
    物质可以转化为ECF，但物品不能
    打开“ECF转化台”并进入“将物质转化为ECF/学习物品”，在弹出的页面中选择一种物质即可
    其中，转化的比例是2：1（向下取整），例如，价值为10的二级物质可以获得 5 ECF，价值为5的一级物质可以获得 2 ECF
    附物质价值表：
    等级    价值    ECF
    I      5       2
    II     10      5
    III    40      20
    IV     160     80
    V      800     400
    B      9000    4500
    A      130000  65000
    S      7000000 3500000
                """)
                g.msgbox("""
    三、学习物品并将ECF转化为物品
    1.学习物品
    打开“ECF转化台”并进入“学习物品/将物质转化为ECF”，在弹出的页面中选择一种物品即可
    学习过的物品无需重复学习
                """)
                g.msgbox("""
    2.将ECF转化为物品
    打开“ECF转化台”并进入“将ECF转化为物品”，在弹出的页面中选择一种要转化的物品即可
    要转化的物品需提前学习
    转化物品需要的ECF将标注在物品旁，消耗的ECF为2：1（向下取整，且最低为1）例如，价值3000的电路板需要 1500 ECF转化，价值1的小石子需要 1 ECF转化
                """)
            elif choice is None:
                kwargs["player_property"]["ecf"] = ecf
                kwargs["player_property"]["mat_learn"] = learn
                return kwargs

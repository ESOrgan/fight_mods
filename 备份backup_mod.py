import easygui as g
import time
import base64
class_name = "Backup"


def info(func):
    def wrapper(*args, **kwargs):
        print(time.strftime("[%H:%M:%S][INFO]", time.localtime()), end="")
        func(*args, **kwargs)
    return wrapper


@info
def info_print(msg):
    print(msg)


class Backup:
    def __init__(self):
        self.GUI = True
        self.name = "备份"
        self.version = "0.0.1"
        self.LOAD_GUI = True
        self.PRELOAD_ITEM = False
        self.NEED_BASE_MOD = False

    @staticmethod
    def load(**kwargs):
        info_print("Backup mod loading finished")

    @staticmethod
    def main(**kwargs):
        path = g.diropenbox("请选择备份的文件夹")
        if path is None:
            return kwargs
        with open(kwargs["player"]) as save_obj:
            save_txt = save_obj.read().rstrip().encode()
            save_txt = base64.b64decode(save_txt).decode()
        fd = open(path + f"\\{kwargs['player']}_备份", mode="w", encoding="utf-8")
        fd.write(save_txt)
        fd.close()
        g.msgbox(f"备份成功，备份路径为{path}\\{kwargs['player']}_备份")
        return kwargs

import ctypes
import platform
import json
from typing import Dict, List, Union
from calc_best_n import calc_best_n
from level_tsv2json import level_tsv2json
from calc_rks import calc_rks
from improving_suggestion import improving_suggestion


system = platform.system()
if system == "Windows":
    lib_name = "Library/phigros.dll"
elif system == "Linux":
    lib_name = "Library/libphigros-64.so"
else:
    raise OSError("Unsupported operating system")


try:
    phigros = ctypes.CDLL(lib_name)
except FileNotFoundError:
    raise FileNotFoundError(
        "Error: Failed to load phigros.dll or libphigros-64.so"
        "Please see ./Library/README.md and ./Library/PhigrosLibrary.md or for more information. You should compile the library yourself. See also https://github.com/7aGiven/PhigrosLibrary."
    )
else:
    phigros.get_handle.argtypes = [ctypes.c_char_p]
    phigros.get_handle.restype = ctypes.c_void_p
    phigros.free_handle.argtypes = [ctypes.c_void_p]
    phigros.get_summary.argtypes = [ctypes.c_void_p]
    phigros.get_summary.restype = ctypes.c_char_p
    phigros.get_save.argtypes = [ctypes.c_void_p]
    phigros.get_save.restype = ctypes.c_char_p
    phigros.load_difficulty.argtypes = [ctypes.c_char_p]
    phigros.get_b19.argtypes = [ctypes.c_void_p]
    phigros.get_b19.restype = ctypes.c_char_p

# 先加载定数数据
phigros.load_level_data = phigros.load_difficulty  # 重命名函数
phigros.load_level_data(bytes("Library/level_data.tsv", "utf-8"))


class PhigrosGet:
    def __init__(self, sessionToken: str | bytes):
        if isinstance(sessionToken, str):  # 如果sessionToken是字符串，则将其转换为bytes
            self.sessionToken = bytes(sessionToken, "utf-8")  # 使用utf-8编码
        else:
            self.sessionToken = sessionToken  # 如果sessionToken已经是bytes，则直接使用

        self.handle = phigros.get_handle(self.sessionToken)  # 获取handle
        if not self.handle:  # 如果handle获取失败，则抛出异常
            raise RuntimeError("Failed to get handle")

        # 获取数据
        self.b19 = json.loads(phigros.get_b19(self.handle).decode("utf-8"))
        self.summary = json.loads(phigros.get_summary(self.handle).decode("utf-8"))
        self.rks = self.summary["rankingScore"]
        self.save = json.loads(phigros.get_save(self.handle).decode("utf-8"))

        # 加载数据
        self.game_record = None
        self.get_game_record()

        self.chart_level_data = level_tsv2json("Library/level_data.tsv")

    def get_summary(self) -> dict:
        """返回用户概览数据"""
        return self.summary

    def get_save(self) -> dict:
        """返回用户存档数据"""
        return self.save

    def get_b19(self) -> dict:
        """返回用户 B19 数据"""
        return self.b19

    def get_game_record(self) -> Dict[str, Dict[str, Dict[str, Union[int, float]]]]:
        """返回经整理过的用户游戏记录数据

        Returns:
            Dict[str, List[Dict[str, Union[int, float]]]]: 游戏记录
            - 键: 曲目名称 (str)
            - 值: 难度记录列表 (Dict[str, Dict])
                - 每个难度记录是一个字典 (Dict)
                    - score: 分数 (int)
                    - acc: 准确度 (float)
                    - fc: 是否FC (int)

        Example:
        {
            "song_name": {
                "ez": {
                    "score": 100000,
                    "acc": 100.0,
                    "fc": 1
                },
                "hd": {
                    ...
                },
                "in": {
                    ...
                },
                "at": {
                    ...
                },

            }
        }
        """
        if self.game_record:  # 如果游戏记录已经存在，则直接返回，避免重复计算
            return self.game_record

        game_record: Dict[str, Dict[str, Dict[str, Union[int, float]]]] = {}

        for song_name, records in self.save["gameRecord"].items():
            game_record[song_name] = {}
            # 每3个元素是一个难度的记录（分数、准确度、是否FC），包裹在字典中
            for i in range(0, len(records), 3):
                score, acc, fc = records[i : i + 3]
                difficulty_map = {0: "ez", 3: "hd", 6: "in", 9: "at"}
                difficulty = difficulty_map[i]
                game_record[song_name][difficulty] = {
                    "score": score,
                    "acc": acc,
                    "fc": fc,
                }
        self.game_record = game_record

    def improving_suggestion(self, rks_wanted: float = 0.01, song_num: int = 1) -> dict:  # TODO @Xingyuan55  See #2
        return improving_suggestion(self, rks_wanted, song_num)

    def best_n(self, phi_n: int = 3, best_n: int = 27) -> dict:
        return calc_best_n(self, phi_n, best_n)

    def __del__(self):
        if hasattr(self, "handle") and self.handle:
            try:
                phigros.free_handle(self.handle)
            except:
                pass


# Example usage
if __name__ == "__main__":
    # user = PhigrosGet("ztl8rh36krtgro724jo83f3o5")  # KRK
    user = PhigrosGet("41dtbqsivitthcmrfhn817ntl")  # Xingyuan55
    # print(user.game_record)
    # with open("b191.json", "w", encoding="utf-8") as f:
    #     json.dump(user.b19, f, indent=4, ensure_ascii=False)
    # with open("game_record2.json", "w", encoding="utf-8") as f:
    #     json.dump(user.game_record, f, indent=4, ensure_ascii=False)】
    b30 = user.best_n()
    print("自行计算", calc_rks(b30))
    print("API获取", user.summary["rankingScore"])
    # with open("bestn1.json", "w", encoding="utf-8") as f:
    #     json.dump(b30, f, indent=4, ensure_ascii=False)
    with open("improving_suggestion24Xingyuan55.json", "w", encoding="utf-8") as f:
        json.dump(user.improving_suggestion(0.01, 1), f, indent=4, ensure_ascii=False)
    # print("1首歌：")
    # result1 = user.improving_suggestion(3, 1)
    # print(result1["ATHAZA.LeaF"]["in"])

    # print("30首歌：")
    # result30 = user.improving_suggestion(1, 20)
    # print(result30["ATHAZA.LeaF"]["in"])


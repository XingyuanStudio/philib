import ctypes
import platform
import json
from typing import Dict, List, Union


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



class PhigrosGet:
    def __init__(self, sessionToken: str|bytes):
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
        self.save = json.loads(phigros.get_save(self.handle).decode("utf-8"))
        
        # self.game_record = self.get_game_record()
        # self.b27 = self.get_b27()

    def get_summary(self) -> dict:
        """返回用户概览数据"""
        self.summary = json.loads(phigros.get_summary(self.handle).decode("utf-8"))
        return self.summary

    def get_save(self) -> dict:
        """返回用户存档数据"""
        return self.save

    def get_b19(self) -> dict:
        """返回用户 B19 数据"""
        return self.b19
    
    def calc_b27(self) -> dict:
        """返回用户 B27 数据"""
        b27 = dict()
        for i in self.save["gameRecord"]:
            pass  # TODO: 实现 B27 计算
        
    def get_game_record(self) -> Dict[str, List[Dict[str, Union[int, float]]]]:
        """返回经整理过的用户游戏记录数据
        
        Returns:
            Dict[str, List[Dict[str, Union[int, float]]]]: 游戏记录
            - 键: 曲目名称 (str)
            - 值: 难度记录列表 (List[4])
                - 每个难度记录是一个字典 (Dict)
                    - score: 分数 (int)
                    - acc: 准确度 (float)
                    - fc: 是否FC (int)
        """
        game_record: Dict[str, List[Dict[str, Union[int, float]]]] = {}
        
        for song_name, records in self.save["gameRecord"].items():
            game_record[song_name] = []
            # 每3个元素是一个难度的记录（分数、准确度、是否FC）
            for i in range(0, len(records), 3):  
                score, acc, fc = records[i:i+3]
                game_record[song_name].append({  
                    "score": score,
                    "acc": acc,
                    "fc": fc
                })
        
        return game_record

    def __del__(self):
        if hasattr(self, "handle") and self.handle:
            try:
                phigros.free_handle(self.handle)
            except:
                pass


# Example usage
if __name__ == "__main__":
    user = PhigrosGet("Your sessionToken")
    print(user.get_save())

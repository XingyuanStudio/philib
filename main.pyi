from typing import Dict, List, Union, Optional
from ctypes import CDLL, c_char_p, c_void_p

class PhigrosGet:
    sessionToken: bytes
    handle: c_void_p
    b19: dict
    summary: dict
    save: dict
    game_record: Optional[Dict[str, Dict[str, Dict[str, Union[int, float]]]]]
    chart_level_data: Dict[str, Dict[str, float]]

    def __init__(self, sessionToken: str | bytes) -> None: ...

    def get_summary(self) -> dict: ...

    def get_save(self) -> dict: ...

    def get_b19(self) -> dict: ...

    def get_game_record(self) -> Dict[str, Dict[str, Dict[str, Union[int, float]]]]: ...

    def get_rks_suggest(self, rks_wanted: float = 0.01) -> dict: ...

    def __del__(self) -> None: ...


# 全局变量和函数
phigros: CDLL

# 函数签名设置
phigros.get_handle.argtypes = [c_char_p]
phigros.get_handle.restype = c_void_p
phigros.free_handle.argtypes = [c_void_p]
phigros.get_summary.argtypes = [c_void_p]
phigros.get_summary.restype = c_char_p
phigros.get_save.argtypes = [c_void_p]
phigros.get_save.restype = c_char_p
phigros.load_level_data.argtypes = [c_char_p]
phigros.get_b19.argtypes = [c_void_p]
phigros.get_b19.restype = c_char_p

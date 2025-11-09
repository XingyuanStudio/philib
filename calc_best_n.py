try:
    from .calc_chart_rks import *
except:
    from calc_chart_rks import *


def calc_best_n(self, phi_n, best_n):
    """计算用户最佳成绩

    Args:
        phi_n: phi值数量（通常为3，即Pure Perfect的数量）
        best_n: 最佳成绩数量（通常为27，与phi_n组成B30）

    Returns:
        Dict[str, List[Dict[str, Union[str, float]]]]: 包含phi_list和best_list的字典
        - phi_list: Pure Perfect成绩列表
            - song_name: 曲目名称
            - level: 难度等级(ez/hd/in/at)
            - difficulty: 谱面定数
            - acc: 准确度
            - rks: 单曲Rating
        - best_list: 最佳成绩列表（结构同上）

    Note:
        返回的成绩列表已按rks降序排序
        
    Return Example:
     {
        "phi_list":[
            {
                "song_name": 曲目名称,
                "level": 谱面等级 [ez|hd|in|at],
                "rks": 谱面rks
                "difficulty": 谱面定数
                "acc": 准确度
            }
            ...
        ],
        "best_list":[
            {
                "song_name": 曲目名称,
                "level": 谱面等级 [ez|hd|in|at],
                "rks": 谱面rks
                "level": 谱面定数
                "acc": 准确度
            }
            ...
        ]
    }
    """
    level_list = ["ez", "hd", "in", "at"]
    all_list = []
    phi_list = []
    best_list = []
    for every in self.game_record.items():
        for level in level_list:
            if every[1][level]["score"] == 1000000:
                phi_list.append(
                    {
                        "song_name": every[0],
                        "level": level,
                        "level": self.chart_level_data[every[0]][level],
                        "acc": every[1][level]["acc"],
                        "rks": calc_chart_rks(every[1][level]["acc"], self.chart_level_data[every[0]][level]),
                    }
                )
            all_list.append(
                {
                    "song_name": every[0],
                    "level": level,
                    "level": self.chart_level_data[every[0]][level],
                    "acc": every[1][level]["acc"],
                    "rks": calc_chart_rks(every[1][level]["acc"], self.chart_level_data[every[0]][level]),
                }
            )

    phi_list.sort(key=lambda x: x["rks"], reverse=True)
    all_list.sort(key=lambda x: x["rks"], reverse=True)
    phi_list = phi_list[:phi_n]
    best_list = all_list[:best_n]
    return {
        "phi_list": phi_list,
        "best_list": best_list,
    }


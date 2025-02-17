from calc_chart_score import *


def calc_best_n(self, phi_n, best_n):
    """
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
                        "rks": calc_chart_score(
                            every[1][level]["acc"],
                            self.chart_level_data[every[0]][level],
                        ),
                    }
                )
            all_list.append(
                {
                    "song_name": every[0],
                    "level": level,
                    "level": self.chart_level_data[every[0]][level],
                    "acc": every[1][level]["acc"],
                    "rks": calc_chart_score(
                        every[1][level]["acc"],
                        self.chart_level_data[every[0]][level],
                    ),
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


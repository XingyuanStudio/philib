def calc_best_n(self, phi_n: int = 3, best_n: int = 27) -> dict:  # TODO @machenxiu
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
                    "difficulty": 谱面定数
                    "acc": 准确度
                }
                ...
            ]
        }
        """

        self这个参数，会把main.PhigrosGet的实例传进来
 
def improving_suggestion(self, rks_wanted: float = 0.01):
    """推分建议

    TODO  @Xingyuan55  See #2

    Args:
        self: main.PhigrosGet 实例
        rks_wanted: 想要提升的rks数

    Returns:
        返回符合的每张谱面的最低aac
        Dict[str, Dict[str, float]]

        Examples:
            {
                "song_name":{
                    ez: 1.0000,
                    hd: 0.6974,
                    ...
                },
                ...
            }
    """


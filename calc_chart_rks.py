def calc_chart_rks(acc: float, level: float = None) -> float:
    """计算单谱面rks分数

    Args:
        acc: 准确度（百分比，范围0-100）
        level: 谱面定数

    Returns:
        float: 单曲Rating分数
            - acc < 70% 时返回0
    """
    return 0 if acc < 0.7 else ((acc - 55) / 45) * ((acc - 55) / 45) * level

def calc_chart_rks(acc: float, level: float = None) -> float:
    """计算谱面rks
    
    Args:
        acc: 准确度
        level: 谱面定数
        
    Returns:
        float: 计算谱面rks
    """
    return 0 if acc < 0.7 else ((acc - 55) / 45) * ((acc - 55) / 45) * level
 
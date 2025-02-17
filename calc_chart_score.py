def calc_chart_score(acc: float, level: float = None) -> float:
    """计算谱面rks
    
    Args:
        acc: 准确度
        level: 谱面定数
        
    Returns:
        float: 计算谱面rks
    """
    return ((acc - 55) / 45) * ((acc - 55) / 45) * level
 
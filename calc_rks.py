def calc_rks(best_n: dict):
    """计算总RKS分数

    Args:
        best_n: 包含phi_list和best_list的字典
            结构同calc_best_n()的返回值

    Returns:
        float: 总Rating分数（所有最佳成绩的平均值）

    Note:
        总Rating计算方式为：(phi_list + best_list)所有歌曲rks的算术平均值
    """
    phi_list = best_n["phi_list"]
    best_list = best_n["best_list"]
    rks_list = []

    for phi in phi_list:
        rks_list.append(phi["rks"])

    for best in best_list:
        rks_list.append(best["rks"])

    return sum(rks_list) / len(rks_list)

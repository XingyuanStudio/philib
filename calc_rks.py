def calc_rks(best_n: dict):
    phi_list = best_n["phi_list"]
    best_list = best_n["best_list"]
    rks_list = []

    for phi in phi_list:
        rks_list.append(phi["rks"])

    for best in best_list:
        rks_list.append(best["rks"])

    return sum(rks_list) / len(rks_list)

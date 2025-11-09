import math
from typing import Dict

try:
    from .calc_chart_rks import *
except ImportError:
    from calc_chart_rks import *


def improving_suggestion(self, rks_wanted: float = 0.01, song_num: int = 1) -> Dict[str, Dict[str, float]]:
    """推分建议算法
    
    计算每个谱面需要达到的最低acc，以达到期望的 RKS 提升。
    
    Args:
        rks_wanted: 期望提升的 RKS 数值
        song_num: 期望通过几首歌提升 RKS
        
    Returns:
        Dict[str, Dict[str, float]]: 推分建议
        - 键: 曲目名称
        - 值: 难度建议字典
            - ez/hd/in/at: 最低需要的acc（None表示无法通过此难度提升）
            
    Example:
        >>> user.improving_suggestion(0.01, 1)
        {
            "Glaciaxion": {
                "ez": None,  # 无法通过此难度提升
                "hd": 95.2,  # acc需要达到95.2%
                "in": None,
                "at": 92.1
            }
        }
        
    Note:
        - 如果某难度已经达到或超过建议acc，将返回 None
        - 如果某难度即使100%也无法达到目标，将返回 None
        - 对于高定数谱面，如果定数足够高，可能建议尝试100%
        
    代码借鉴：
        [phi-plugin](https://github.com/Catrong/phi-plugin) 的
        [model/class/Save.js](https://github.com/Catrong/phi-plugin/blob/main/model/class/Save.js#L386)
    """
    suggestions: Dict[str, Dict[str, float]] = {}

    # 获取当前 B30 (B27 + 3phi)
    current_b30 = self.best_n()
    b27_rks = current_b30["best_list"][26]["rks"] if len(current_b30["best_list"]) > 26 else 0

    # 获取最高 phi 分
    phi_list = [song for song in current_b30["phi_list"] if song]
    b0_rks = max((song["rks"] for song in phi_list), default=0) if phi_list else 0

    # 计算最小提升量（考虑四舍五入）
    current_rks = self.rks
    min_up_rks = math.floor(current_rks * 100) / 100 + 0.005 - current_rks
    if min_up_rks < 0:
        min_up_rks += 0.01

    # 使用最小提升量和目标提升量中的较大值
    rks_wanted = max(rks_wanted, min_up_rks)

    # 计算每首歌需要提升的基础 RKS（不含 *30）
    single_rks_base = rks_wanted / song_num

    # 遍历所有谱面
    for song_name, levels in self.chart_level_data.items():
        suggestions[song_name] = {}

        # 获取当前成绩
        current_scores = {}
        if song_name in self.game_record:
            for diff, data in self.game_record[song_name].items():
                current_scores[diff] = data["acc"]

        # 对每个难度计算
        for diff, level in levels.items():
            if level <= 0:
                suggestions[song_name][diff] = None
                continue

            # 获取当前 RKS
            current_acc = current_scores.get(diff, 0)
            if current_acc > 0:
                current_rks = ((current_acc / 100 - 0.55) / 0.45) ** 2 * level
            else:
                current_rks = 0

            # 计算目标 RKS：使用当前 RKS 和 B27 最低分中的较大值
            target_rks = max(b27_rks, current_rks) + single_rks_base * 30

            # 计算所需 acc
            needed_acc = 45 * math.sqrt(target_rks / level) + 55

            # 如果需要的 acc 不合理或者低于当前 acc，就不推荐
            if needed_acc > 100 or (current_acc > 0 and needed_acc <= current_acc):
                # 对于高定数谱面，如果定数足够高，建议尝试 100%
                if level > b0_rks + single_rks_base * 30:
                    suggestions[song_name][diff] = 100.0
                else:
                    suggestions[song_name][diff] = None
            else:
                suggestions[song_name][diff] = needed_acc
    
    return suggestions

def remove_unavailable(suggestions_dict) -> dict:
    result_dict = suggestions_dict.copy()
    
    for song in list(result_dict.keys()):
        for level in list(result_dict[song].keys()):
            if result_dict[song][level] is None:
                result_dict[song].pop(level)
        if not result_dict[song]:
            result_dict.pop(song)
            
    return result_dict
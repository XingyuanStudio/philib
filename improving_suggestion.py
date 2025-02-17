from typing import Dict
import math


def improving_suggestion(self, rks_wanted: float = 0.01, song_num: int = 1) -> Dict[str, Dict[str, float]]:
    """推分建议

    TODO  @Xingyuan55  See #2

    Args:
        self: main.PhigrosGet 实例
        rks_wanted: 想要提升的总 RKS 数值
        song_num: 希望通过几首歌来提升 RKS（默认为1）

    Returns:
        Dict[str, Dict[str, float]]: 每个谱面需要达到的最低acc
        - 键: 曲目名称
        - 值: 难度acc字典
            - ez/hd/in/at: 最低需要的acc

    Example:
        >>> user.improving_suggestion(0.01)
        {
            "Glaciaxion": {
                "ez": 97.5,  # 表示ez难度至少要打到97.5%
                "hd": 95.2,
                "in": None,  # None 表示即使100%也无法达到目标
                "at": 92.1
            },
            ...
        }
    """
    suggestions: Dict[str, Dict[str, float]] = {}
    
    # 获取当前 B30 (B27 + 3phi)
    current_b30 = self.best_n()
    b27_rks = current_b30["best_list"][26]["rks"] if len(current_b30["best_list"]) > 26 else 0
    
    # 计算最小需要提升的 RKS
    min_up_rks = rks_wanted
    
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
                current_rks = ((current_acc/100 - 0.55)/0.45)**2 * level
            else:
                current_rks = 0
            
            # 计算目标 RKS：使用当前 RKS 和 B27 最低分中的较大值
            target_rks = max(b27_rks, current_rks) + min_up_rks * 30
            
            # 计算所需 acc
            needed_acc = 45 * math.sqrt(target_rks/level) + 55
            
            # 如果需要的 acc 不合理或者低于当前 acc，就不推荐
            if needed_acc > 100 or (current_acc > 0 and needed_acc <= current_acc):
                suggestions[song_name][diff] = None
            else:
                suggestions[song_name][diff] = needed_acc
    
    return suggestions


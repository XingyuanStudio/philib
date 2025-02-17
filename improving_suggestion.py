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
    
    # 获取当前 b30
    current_b30 = self.best_n()
    lowest_rks = min(song["rks"] for song in current_b30["best_list"])
    
    # 计算每首歌需要提升的 RKS
    single_rks_needed = (rks_wanted * 30) / song_num
    
    # 计算每个谱面需要的 acc
    for song_name, levels in self.chart_level_data.items():
        suggestions[song_name] = {}
        
        # 获取当前成绩
        current_scores = {}
        if song_name in self.game_record:
            for diff, data in self.game_record[song_name].items():
                current_scores[diff] = data["acc"]
        
        for diff, level in levels.items():
            if level <= 0:
                suggestions[song_name][diff] = None
                continue
            
            # 获取当前 RKS
            current_acc = current_scores.get(diff, 0)
            current_rks = ((current_acc/100 - 0.55)/0.45)**2 * level
            
            # 计算目标 RKS：基于当前 RKS 或 B30 最低分（取较大值）
            target_single_rks = max(current_rks, lowest_rks) + single_rks_needed
            
            # 计算所需 acc
            min_acc = 45 * math.sqrt(target_single_rks/level) + 55
            
            # 如果目标 acc 超过 100，就不需要推分
            if min_acc > 100:
                suggestions[song_name][diff] = None
            else:
                suggestions[song_name][diff] = min_acc
            
    return suggestions


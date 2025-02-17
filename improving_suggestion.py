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
    
    return suggestions


from typing import Dict, Optional

def improving_suggestion(
    self,
    rks_wanted: float = 0.01,
    song_num: int = 1
) -> Dict[str, Dict[str, Optional[float]]]: ... 


def remove_unavailable(
    suggestions_dict
) -> Dict[str, Dict[str, Optional[float]]]: ... 
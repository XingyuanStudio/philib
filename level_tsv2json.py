import json 
import csv
from typing import Dict

def level_tsv2json(tsv_path: str, complete_width: int = 5) -> Dict[str,Dict[str,float]]:
    """将谱面定数数据 tsv 转换为字典格式
    
    Args:
        tsv_path: tsv 文件路径
        complete_width: 补全宽度，默认为5（包含曲名和4个难度）
        
    Returns:
        Dict[str, Dict[str, float]]: 谱面定数数据
        - 键: 曲目名称 (str)
        - 值: 难度定数字典
            - ez: EZ 难度的定数 (float)
            - hd: HD 难度的定数 (float)
            - in: IN 难度的定数 (float)
            - at: AT 难度的定数 (float 或 0.0)

    Example:
        TSV input:
        Glaciaxion.SunsetRay    3.0    7.0    13.8
        ...

        JSON output:
        {
            "Glaciaxion.SunsetRay": 
                {
                    "ez": 3.0,
                    "hd": 7.0,
                    "in": 13.8,
                    "at": 0.0
                }
        }

    """
    data: Dict[str,Dict[str,float]] = {}
    with open(tsv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:  # 一曲的定数信息
            if len(row) < complete_width:  # 补全定数信息
                row.append(0)
                
            data[row[0]] = {
                "ez": float(row[1]),
                "hd": float(row[2]),
                "in": float(row[3]),
                "at": float(row[4]),
            }
    return data

if __name__ == "__main__":
    with open("level_data.json", "w", encoding="utf-8") as f:
        json.dump(level_tsv2json("Library/level_data.tsv"), f, indent=4, ensure_ascii=False)


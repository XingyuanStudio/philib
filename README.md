# Philib

Philib 是一个用于获取 Phigros 玩家云存档数据的 Python 模块。本模块基于 [PhigrosLibrary](https://github.com/7aGiven/PhigrosLibrary) 开发，目的是封装一个更易用的接口，便于 Phigros 玩家查询自己的数据。

> [!WARNING]
> **严禁使用本项目或相关项目进行对Phigros数据库的攻击行为**，包括但不限于:
> - 大规模查分对鸽游服务器进行DDOS

## 环境要求

本项目需要以下环境：

1. **Python**: 任意现代版本

如果需要自行编译核心库，则需要以下环境：

2. **CMake**: 用于编译核心库

- 从 [CMake 官网](https://cmake.org/download/) 下载安装

3. **NMake**: 用于 Windows 环境下的编译
   - 方案 1: 安装 Visual Studio（包含 NMake）
   - 方案 2: 使用项目提供的独立 NMake
     - 在 `Librarys/` 目录下找到 `NMake.exe`
     - 将其添加到系统 PATH 环境变量

## 核心库准备

项目依赖 PhigrosLibrary 的核心库文件：

- Windows: `phigros.dll`
- Linux: `libphigros-64.so`

获取核心库有以下方式：

1. 直接使用

   - 在 `Library/` 目录下包含对应文件

2. 下载编译好的版本

   - 访问 [PhigrosLibrary Releases](https://github.com/7aGiven/PhigrosLibrary/releases)
   - 下载对应平台的文件

3. 自行编译
   - 参考 [Library/PhigrosLibrary.md](Library/PhigrosLibrary.md) 的编译说明（或查看 [PhigrosLibrary GitHub](https://github.com/7aGiven/PhigrosLibrary/blob/main/PhigrosLibrary.md)）

## 项目主要结构

```bash
philib
├── Library/
│   ├── python/         # Python 示例代码
│   ├── src/            # 核心库源码
│   ├── script-py/      # 支持脚本
│   │   Phigros.dll         # 支持库(Windows)
│   │   libphigros-64.so         # 支持库(Linux)
│  .gitignore
│  main.py  # 主程序
│  improving_suggestion.py  # 推分建议算法
│  calc_best_n.py  # 最佳成绩计算
│  calc_chart_rks.py  # 单谱面rks计算
│  calc_rks.py  # 总rks计算
│  level_tsv2json.py  # 谱面定数数据转换
│  README.md
│  __init__.py
```

为方便开发，我们保留了 PhigrosLibrary 的部分支持文件，您可以：

- 参考示例代码：[Library/python/example.py](Library/python/example.py)
- Phigros 游戏数据：
  - 谱面定数数据：[Library/level_data.tsv](Library/level_data.tsv)
  - 收集品数据: [Library/collection.tsv](Library/collection.tsv)
  - 曲目与谱面信息：[Library/info.tsv](Library/info.tsv)
- PhigrosLibrary 说明文件: [Library/PhigrosLibrary.md](Library/PhigrosLibrary.md)

  等等。

PhigrosLibrary 使用了 GNU GPLv3 许可证，据此，Philib 也使用 GNU GPLv3 许可证。

## 使用方式与API接口

```bash
git clone git@github.com:XingyuanStudio/philib.git
```

我们暂时不提供pip库的安装方式，您需要手动下载、复制项目源码到您的项目中来使用。

### 1. 初始化

```python
user = PhigrosGet(sessionToken: str | bytes)
```

### 2. 基础数据获取

```python
# 获取用户概览数据
summary = user.get_summary() -> dict

# 获取用户存档数据
save = user.get_save() -> dict

# 获取用户 B19 数据
b19 = user.get_b19() -> dict

# 获取用户游戏记录
game_record = user.get_game_record() -> Dict[str, Dict[str, Dict[str, Union[int, float]]]]
```

### 3. 成绩计算

```python
# 计算用户最佳成绩 (B30 = phi_n + best_n)
best_n = user.best_n(phi_n: int = 3, best_n: int = 27) -> dict

# 计算单谱面 RKS
rks = calc_chart_rks(acc: float, level: float) -> float

# 计算总 RKS
rks = calc_rks(best_n: dict) -> float
```

### 4. 推分建议

```python
# 获取推分建议
suggestions = user.improving_suggestion(
    rks_wanted: float = 0.01,  # 期望提升的 RKS
    song_num: int = 1  # 要通过几首歌提升
) -> Dict[str, Dict[str, float]]
```

## 更新资源

当您发现Phigros已经更新，而Philib尚未更新时，您可以手动更新资源:

> [!TIP]
> 资源来源：[PhigrosLibrary](https://github.com/7aGiven/PhigrosLibrary)

1. [头像id](https://github.com/7aGiven/PhigrosLibrary/blob/main/avatar.txt)

2. [收藏品id](https://github.com/7aGiven/PhigrosLibrary/blob/main/collection.tsv)

3. 定数表和曲绘请使用项目[Phigros_Resource](https://github.com/7aGiven/Phigros_Resource/)从apk文件中提取

## 项目贡献

本项目欢迎任何形式的贡献，包括但不限于：

- 提交问题报告
- 提交代码

欢迎在[Bilibili@小星圆55](https://space.bilibili.com/525310961)上关注我们！
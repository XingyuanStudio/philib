# Philib

![License](https://img.shields.io/github/license/XingyuanStudio/philib)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Update Status](https://img.shields.io/badge/status-maintained-green)

Philib 是一个用于获取 Phigros 玩家云存档数据的 Python 模块。本模块基于 [PhigrosLibrary](https://github.com/7aGiven/PhigrosLibrary) 开发，目的是封装一个更易用的接口，便于 Phigros 玩家查询自己的数据。

> [!WARNING] > **严禁使用本项目或相关项目进行对 Phigros 数据库的攻击行为**，包括但不限于:
>
> - 大规模查分对鸽游服务器进行 DDOS

## 🚀 快速开始 基本示例

1. 克隆项目：

```bash
git clone git@github.com:XingyuanStudio/philib.git
```

2. 准备环境：

```python
# 确保您有 Python 环境，无需额外依赖
# 将项目目录添加到 Python 路径
```

3. 开始使用：

```python
from philib import PhigrosGet

# 初始化（使用您的会话令牌）
user = PhigrosGet("Your_Session_Token")

# 获取基本信息
print(f"当前 RKS: {user.summary['rankingScore']}")

# 获取 B30 成绩
best_30 = user.best_n(phi_n=3, best_n=27)
print(f"B30 成绩: {calc_rks(best_30)}")

# 获取推分建议
suggestions = user.improving_suggestion(rks_wanted=0.1)
print(f"推分建议: {suggestions}")
```

## 📋 环境要求

### 基本要求

**Python**: 3.6 或更高版本

### 编译核心库需要（可选）

- **CMake**: [下载地址](https://cmake.org/download/)

**Windows 特需**:

- **NMake**:
  - 方案 1: 安装 Visual Studio（包含 NMake）
  - 方案 2: 使用项目提供的独立 NMake
    - 在 `Librarys/` 目录下找到 `NMake.exe`
    - 将其添加到系统 PATH 环境变量

## 🔧 核心库准备

项目依赖 PhigrosLibrary 核心库：

| 平台    | 文件名             |
| ------- | ------------------ |
| Windows | `phigros.dll`      |
| Linux   | `libphigros-64.so` |

获取方式：

1. **直接使用**：`Library/` 目录下已包含
2. **下载编译版**：[PhigrosLibrary Releases](https://github.com/7aGiven/PhigrosLibrary/releases)
3. **自行编译**：参考 [编译说明](Library/PhigrosLibrary.md)（或查看 [PhigrosLibrary GitHub 说明](https://github.com/7aGiven/PhigrosLibrary/blob/main/PhigrosLibrary.md)）

## 📁 项目结构

```bash
philib/
├── Library/                    # 核心库及支持文件
│   ├── python/                # Python 示例代码
│   ├── src/                   # 核心库源码
│   ├── script-py/             # 支持脚本
│   ├── phigros.dll           # Windows 支持库
│   └── libphigros-64.so      # Linux 支持库
├── main.py                    # 主程序
├── improving_suggestion.py    # 推分建议算法
├── calc_best_n.py            # 最佳成绩计算
├── calc_chart_rks.py         # 单谱面 RKS 计算
├── calc_rks.py               # 总 RKS 计算
├── level_tsv2json.py         # 谱面定数数据转换
└── __init__.py
```

为方便开发，我们保留了 PhigrosLibrary 的部分支持文件，您可以：

- 参考示例代码：[Library/python/example.py](Library/python/example.py)
- Phigros 游戏数据：
  - 谱面定数数据：[Library/level_data.tsv](Library/level_data_old.tsv)
  - 收集品数据: [Library/collection.tsv](Library/collection.tsv)
  - 曲目与谱面信息：[Library/info.tsv](Library/info.tsv)
- PhigrosLibrary 说明文件: [Library/PhigrosLibrary.md](Library/PhigrosLibrary.md)

  等等。

PhigrosLibrary 使用了 GNU GPLv3 许可证，据此，Philib 也使用 GNU GPLv3 许可证。

## 📖 API 详细说明

```bash
git clone git@github.com:XingyuanStudio/philib.git
```

我们暂时不提供 pip 库的安装方式，您需要手动下载、复制项目源码到您的项目中来使用。

### 1. 初始化

```python
# sessionToken: 游戏会话令牌，可以是字符串或字节类型
# level_data_path: 难度数据文件路径（可选）
PhigrosGet(sessionToken: str | bytes, level_data_path: str = None)
```

### 2. 数据获取

在初始化时，系统会自动获取并缓存以下基础数据，您可以通过类属性直接访问：

```python
# 用户概览数据（包含用户基本信息和 RKS 等）
PhigrosGet().summary: dict

# 用户存档数据（包含所有原始未经整理的游戏记录）
PhigrosGet().save: dict

# 用户 B19 数据（包含 B19 榜单信息）
PhigrosGet().b19: dict

# 用户游戏记录（经过整理的所有曲目成绩数据）
PhigrosGet().game_record: dict
```

> [!TIP]
> 以上数据在初始化时已经获取并缓存，直接通过属性访问可以避免重复计算。如果需要刷新数据，可以使用对应的方法：
>
> ```python
> user.get_summary()   # 获取最新用户概览
> user.get_save()      # 获取最新存档
> user.get_b19()       # 获取最新 B19
> user.get_game_record() # 获取最新游戏记录
> ```

### 3. 成绩计算功能

```python
# 计算用户最佳成绩 (Best_n = phi_n + best_n)
# phi_n: Phi 曲目数量（默认3）
# best_n: 最佳曲目数量（默认27）
PhigrosGet().best_n(phi_n: int = 3, best_n: int = 27) -> dict

# 获取推分建议
# rks_wanted: 期望提升的 RKS（默认0.01）
# song_num: 要通过几首歌提升（默认1）
PhigrosGet().improving_suggestion(
    rks_wanted: float = 0.01,
    song_num: int = 1
) -> dict

# 计算单谱面 RKS（独立函数）
calc_chart_rks(acc: float, level: float) -> float

# 计算总 RKS（独立函数）
calc_rks(best_n: dict) -> float

```

## 🔄 更新资源

当您发现 Phigros 已经更新，而 Philib 尚未更新时，您可以手动更新资源:

> [!TIP]
> 资源来源：[PhigrosLibrary](https://github.com/7aGiven/PhigrosLibrary)

1. **头像**: [avatar.txt](https://github.com/7aGiven/PhigrosLibrary/blob/main/avatar.txt)
2. **收藏品**: [collection.tsv](https://github.com/7aGiven/PhigrosLibrary/blob/main/collection.tsv)
3. **定数表和曲绘**: 使用 [Phigros_Resource](https://github.com/7aGiven/Phigros_Resource/) 从 APK 提取

> [!TIP]
> 如果您在初始化`phigrosGet()`后报错`Windows Error 0xe06d7363`，是定数表版本与账号版本不一致的问题。
> 请您更新[**定数表**文件](https://github.com/7aGiven/Phigros_Resource/blob/info/difficulty.tsv)至与账号云端存档版本相同。
> 下载新的定数表文件后，将文件路径传入`phigrosGet`的`level_data_path`参数
> （或是放在`Library/`文件夹下并更改源代码[`main.py`](main.py)的第 70 行`）

## 🤝 参与贡献

本项目欢迎任何形式的贡献，包括但不限于：

- 🐛 提交 Bug 报告
- ✨ 提交新功能建议
- 📝 改进文档
- 💻 提交代码

## 📱 联系我们

- 欢迎在[Bilibili@小星圆 55](https://space.bilibili.com/525310961)上关注我们！
- 提交 Issue 或 PR

## 📄 许可证

本项目基于 GNU GPLv3 许可证开源。

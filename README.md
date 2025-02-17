# Philib

Philib 是一个用于获取 Phigros 玩家云存档数据的 Python 模块。本模块基于 [PhigrosLibrary](https://github.com/7aGiven/PhigrosLibrary) 开发，目的是封装一个更易用的接口，便于 Phigros 玩家查询自己的数据。

## 环境要求

本项目需要以下环境：

1. **Python**: 任意现代版本

如果需要自行编译核心库，则需要以下环境： 2. **CMake**: 用于编译核心库

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

   - 在 `Library/` 目录下查找对应文件

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
│  main.py
│  README.md
│  __init__.py
```

为方便开发，我们保留了 PhigrosLibrary 的完整支持文件，您可以：

- 参考示例代码：[Library/python/example.py](Library/python/example.py)
- 查看或修改源码：`Library/src/` 目录
- 查看、使用或修改支持工具：`Library/script-py/` 目录

### 提交规范

本项目使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范进行代码提交。提交信息的格式如下：

```
<type>: <description>
[optional body]
```

提交类型（type）必须是以下之一：

- `init`: 项目初始化
- `feat`: 新功能
- `fix`: 修复 bug
- `docs`: 文档更新
- `style`: 代码格式修改（不影响代码运行的变动）
- `refactor`: 代码重构（既不是新增功能，也不是修复 bug）
- `perf`: 性能优化
- `test`: 测试相关
- `build`: 构建系统或外部依赖修改
- `ci`: CI 配置修改
- `chore`: 其他修改（不添加功能但在做项目维护性工作）
- `revert`: 回退或重提以前的提交
- `wip`: 工作进行中，包含未完成的功能

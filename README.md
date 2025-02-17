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

## Git 远程协作指南

### 1. 基本概念

- `origin`: 远程仓库的默认名称
- `master`: 主分支
- `HEAD`: 当前分支的最新提交

### 2. 日常工作流程

#### 2.1 开始工作前

```bash
# 1. 拉取最新代码
git pull origin master

# 2. 创建功能分支（可选）
git checkout -b feature/your-feature
```

#### 2.2 提交更改

```bash
# 1. 查看更改
git status

# 2. 添加更改
git add main.py                  # 添加单个文件
git add .                        # 添加所有更改

# 3. 提交更改
git commit -m "feat: 添加新功能"  # 遵循提交规范
```

#### 2.3 推送到远程

```bash
# 推送到主分支
git push origin master

# 如果使用功能分支
git push origin feature/your-feature
```

### 3. 常见问题处理

#### 3.1 合并冲突

```bash
# 1. 保存当前工作
git stash save "我的更改"

# 2. 拉取最新代码
git pull origin master

# 3. 恢复工作
git stash pop

# 4. 解决冲突后提交
git add .
git commit -m "merge: 解决冲突"
git push origin master
```

#### 3.2 撤销更改

```bash
# 撤销未提交的更改
git checkout -- main.py

# 撤销最后一次提交
git reset --soft HEAD^

# 撤销已推送的提交（谨慎使用）
git revert <commit-id>
```

#### 一次冲突的解决实例

1. 先保存你的本地更改：`git stash save "添加 Issue 引用到 TODO 注释"`
2. 拉取远程更改：`git pull origin master`
3. 恢复你的更改：`git stash pop`
4. 如果有冲突，解决后：

```bash
git add .
git commit -m "docs: 添加 Issue 引用到 TODO 注释"
git push origin master
```

解释：
git stash 会暂时保存你的更改
git pull 会更新你的本地代码
git stash pop 会恢复你保存的更改
如果有冲突，需要手动解决

### 4. 最佳实践

1. **经常同步**

   - 每天开始工作前先 `pull`
   - 完成一个功能就提交一次

2. **清晰的提交信息**

   - 使用规范的提交类型
   - 简要说明改动内容
   - 必要时添加详细说明

3. **分支管理**

   - 重要功能使用单独分支
   - 及时合并已完成的分支
   - 删除不再使用的分支

4. **文件管理**
   - 使用 `.gitignore` 忽略临时文件
   - 不提交编译产物和个人配置
   - 保持仓库整洁

### 5. 提交规范示例

```bash
# 新功能
git commit -m "feat: 添加游戏记录格式化功能"

# 修复 bug
git commit -m "fix: 修复难度解析错误"

# 文档更新
git commit -m "docs: 更新 README.md"

# 重构代码
git commit -m "refactor: 优化数据结构"

# 进行中的工作
git commit -m "wip: 添加 calc_best_n 框架"
```

# Philib

Philib 是一个用于获取 Phigros 玩家云存档数据的 Python 模块。

本模块基于 [PhigrosLibrary](https://github.com/7aGiven/PhigrosLibrary) 开发。目的是封装一个有更多功能的接口，便于 Phigros 玩家查询自己的数据。

## 项目准备

因为 PhigrosLibrary 是 C 语言编写的，所以需要先安装 CMake（包含 NMake 的）。同时，您还必须安装好了 Python。

CMake 的安装方法：

- 您可以前往[CMake 官网](https://cmake.org/download/)下载安装包。

NMake 的安装方法：

- NMake 是集成在 Visual Studio 中的，如果您知道如何配置并使用 Visual Studio，那么您可以跳过此步骤。

- 在`Librarys/`文件夹下，您可以找到`NMake.exe`文件，这是被分离好的 NMake。您可以将其放在您希望放置的地方，并添加到 PATH 环境变量中。

> [Tips]:
> AI 说，您可以前往[NMake 官网](https://sourceforge.net/projects/gnuwin32/files/make/)下载安装包。但是，我不知道此网址是否是我们需要的，也不知道此网址是否是正确的 NMake 官网。

PhigrosLibrary 的核心是`phigros.dll`文件（或`libphigros-64.so`文件，在 Linux 环境下）。您可以在将`Library/`文件夹下找到此文件。

> 如果找不到或报错，您可以前往[Releases - PhigrosLibrary](https://github.com/7aGiven/PhigrosLibrary/releases)查看。

> 此外，您也可以自行构建`phigros.dll`文件或`libphigros-64.so`文件。请参阅[Library/PhigrosLibrary.md](Library/PhigrosLibrary.md)，在[PhigrosLibrary 的 GitHub 仓库](https://github.com/7aGiven/PhigrosLibrary/blob/main/PhigrosLibrary.md)中也可以查看。

编写代码时，请参阅[PhigrosLibrary 的示例代码](Library/python/example.py)。

为了保证`PhigrosLibrary`能够正常运行且您能够自行更改我们的代码，`PhigrosLibrary`提供的源码、游戏信息及支持库等文件我们并没有删去。

`PhigrosLibrary`的源码、游戏信息及支持库等文件在`Library/`文件夹下。

##

### 提交规范

本项目使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范进行代码提交。提交信息的格式如下：

```
<type>: <description>
[optional body]
[optional footer(s)]
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

# 01. Python 安装

## 1. 选择 Python 版本

新项目应使用 Python 3。优先选择 Python 官方仍支持的稳定版本，并确认项目依赖兼容该版本。不要随意卸载 Linux 发行版自带的 Python：部分系统工具依赖它。

验证已有安装：

```bash
python --version
python3 --version
```

Windows 还可以使用 Python 启动器：

```powershell
py --version
py -0p
```

## 2. Windows

1. 从 [python.org/downloads](https://www.python.org/downloads/) 下载 Windows 安装程序。
2. 启动安装程序。初学者可勾选 **Add python.exe to PATH**，再选择安装。
3. 打开新的 PowerShell 或命令提示符验证：

```powershell
py --version
py -m pip --version
```

推荐使用 `py -m pip`，它能明确使用 Python 启动器选定的解释器对应的 pip。

如果提示找不到命令，检查安装时的 PATH 选项，或使用启动器 `py`。修改 PATH 后需新开终端；不要把不可信目录加入 PATH。

## 3. macOS

macOS 可能带有系统用途的 Python 组件，不建议修改或删除系统文件。可从 Python 官方安装包安装，或使用组织认可的包管理器。安装后检查：

```bash
python3 --version
python3 -m pip --version
```

通常使用 `python3` 命令。项目中建议创建虚拟环境，而不是向系统解释器写入依赖。

## 4. Linux

优先使用发行版包管理器安装 Python 3 和 venv 支持。包名因发行版而异。不要用 `sudo pip install` 覆盖系统管理的 Python 包，也不要删除 `/usr/bin/python3`。

### Debian / Ubuntu

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version
python3 -m pip --version
```

若发行版将某些 Python 包标记为系统管理，安装项目依赖时请使用虚拟环境，不要强行绕过系统保护机制。

### Fedora

```bash
sudo dnf install python3 python3-pip
python3 --version
python3 -m pip --version
```

### Arch Linux

```bash
sudo pacman -Syu python python-pip
python --version
python -m pip --version
```

### openSUSE（示例）

```bash
sudo zypper install python3 python3-pip
python3 --version
```

实际包名和可用版本可能随发行版版本变化，请优先参考对应发行版文档。

## 5. 从源码构建（进阶）

只有在确实需要特定版本或发行版未提供合适版本时才考虑源码构建。通常应安装到独立前缀，不要覆盖系统 Python。源码构建涉及编译器和开发头文件，依赖项依发行版而异；请遵循 Python 官方构建文档和发行版说明。不要直接将 `/usr/local/bin/python3` 替换成系统解释器。

## 6. 安装后验证和问题排查

运行一段代码：

```bash
python3 -c "print('Python 已就绪')"
```

Windows：

```powershell
py -c "print('Python 已就绪')"
```

���看解释器路径：

```bash
python3 -c "import sys; print(sys.executable)"
```

常见问题：

- **命令不存在**：检查安装是否完成、PATH 是否更新，重新打开终端。
- **pip 对应错解释器**：用 `python -m pip` 或 `python3 -m pip`，不要单独猜测 `pip` 指向。
- **权限错误**：项目依赖使用虚拟环境，不要默认用管理员权限安装。
- **Linux 系统组件异常**：不要删除或替换系统 Python；优先修复发行版包或使用隔离环境。

# 02. Python 环境与工具配置

## 1. 虚拟环境

虚拟环境为单个项目隔离解释器包。进入项目目录后创建：

```bash
python3 -m venv .venv
```

Windows：

```powershell
py -m venv .venv
```

激活环境：

```bash
# Linux / macOS
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows 命令提示符
.venv\Scripts\activate.bat
```

激活后通常可见 `(.venv)`。退出：

```bash
deactivate
```

PowerShell 执行策略可能阻止脚本激活；可遵循组织的安全策略，或直接调用 `.venv\Scripts\python.exe`。不要为方便而无差别放宽系统安全策略。

## 2. 安装和检查依赖

```bash
python -m pip install --upgrade pip
python -m pip install requests
python -m pip show requests
python -m pip list
```

生成传统 requirements 文件：

```bash
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

`pip freeze` 会记录当前环境中的全部已安装包，不一定等同于精心维护的直接依赖列表。小项目可手动维护依赖；团队项目可选择 `pyproject.toml` 配合适合的打包/依赖工具。

## 3. `.gitignore`

通常不应提交虚拟环境、缓存或密钥：

```gitignore
.venv/
__pycache__/
*.py[cod]
.pytest_cache/
.coverage
.env
```

提交依赖声明和项目代码；不要把密码、令牌、私钥或含敏感信息的 `.env` 上传到仓库。

## 4. 解释器和 PATH

- `PATH` 是操作系统搜索可执行程序的目录列表。
- `sys.executable` 可显示当前 Python 解释器路径。
- 多版本环境中，优先使用 `python -m pip`，保证 pip 与当前解释器匹配。
- IDE 中要选择项目 `.venv` 里的解释器，而不是全局解释器。

```python
import sys
print(sys.version)
print(sys.executable)
```

## 5. 编辑器与代码质量工具

可选择 VS Code、PyCharm 或其他支持 Python 的编辑器。基本配置包括��选择正确解释器、启用语法提示、配置项目工作目录、运行测试。

常见工具（按项目需要选择）：

- `ruff`：快速 lint 和格式化（功能与规则由配置决定）。
- `black`：代码格式化。
- `pytest`：测试。
- `mypy` 或 `pyright`：静态类型检查。

例如，在虚拟环境安装并运行：

```bash
python -m pip install ruff pytest
ruff check .
ruff format .
pytest
```

团队应统一工具版本和配置，避免每个人本地规则不同。

## 6. 项目结构示例

```text
my_project/
├── .venv/                 # 本地环境，不提交
├── src/
│   └── my_project/
│       └── __init__.py
├── tests/
│   └── test_example.py
├── pyproject.toml         # 项目与工具配置（可选）
├── README.md
└── .gitignore
```

小型脚本不必一开始就采用复杂结构。随着代码增长，再拆分模块并增加测试。

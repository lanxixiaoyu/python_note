# Python 笔记

面向初学者与日常开发者的 Python 学习资料，涵盖安装、环境配置、语言基础、标准库、工程实践与常见应用。示例以 Python 3 为主，建议使用仍受支持的 Python 3 版本。

## 学习路线

1. [安装 Python](docs/01-installation.md)：Windows、macOS、Linux 安装和验证。
2. [环境与工具配置](docs/02-environment.md)：虚拟环境、pip、编辑器、格式化和常见配置。
3. [Python 基础语法](docs/03-basics.md)：数据类型、流程控制、函数、模块、异常和面向对象。
4. [常用标准库与进阶知识](docs/04-standard-library-and-advanced.md)：文件、路径、日期、JSON、迭代器、生成器、装饰器和类型提示。
5. [开发实践与常用生态](docs/05-development-and-ecosystem.md)：测试、调试、日志、依赖管理、网络、数据库和数据处理入门。
6. [速查表与练习](docs/06-cheatsheet-and-exercises.md)：高频语法速查及循序渐进的练习题。

## 快速开始

```python
name = input("请输入你的名字：")
print(f"你好，{name}！")
```

在终端运行脚本：

```bash
python hello.py
```

如果系统中 `python` 指向其他版本，可尝试 `python3 hello.py`（Linux/macOS）或 `py hello.py`（Windows）。

## 建议

- 使用 Python 3，不要开始新的 Python 2 项目。
- 每个项目使用独立虚拟环境，避免全局依赖互相影响。
- 先掌握语法和标准库，再按实际项目选择第三方框架。
- 示例用于学习；生产环境还需考虑输入校验、安全、错误处理和测试。

## 目录

```text
.
├── README.md
└── docs
    ├── 01-installation.md
    ├── 02-environment.md
    ├── 03-basics.md
    ├── 04-standard-library-and-advanced.md
    ├── 05-development-and-ecosystem.md
    └── 06-cheatsheet-and-exercises.md
```

欢迎通过 Issue 或 Pull Request 补充内容、修正错误或添加练习答案。

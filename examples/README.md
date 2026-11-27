# 配套 Python 示例代码

这些脚本对应 `docs/` 中的笔记章节，可使用 Python 3 直接运行：

```bash
python examples/01_installation_check.py
```

Linux/macOS 如果系统使用 `python3` 命令，请将命令中的 `python` 替换为 `python3`。示例不需要安装第三方依赖，除非代码注释另有说明。

| 笔记 | 示例代码 | 内容 |
| --- | --- | --- |
| [安装 Python](../docs/01-installation.md) | [01_installation_check.py](01_installation_check.py) | 检查解释器、平台和 pip |
| [环境与工具配置](../docs/02-environment.md) | [02_environment_demo.py](02_environment_demo.py) | 查看虚拟环境、解释器路径和项目路径 |
| [Python 基础语法](../docs/03-basics.md) | [03_basics_demo.py](03_basics_demo.py) | 类型、容器、流程控制、函数、异常和类 |
| [标准库与进阶知识](../docs/04-standard-library-and-advanced.md) | [04_standard_library_demo.py](04_standard_library_demo.py) | pathlib、JSON、生成器、装饰器和日期时间 |
| [开发实践与常用生态](../docs/05-development-and-ecosystem.md) | [05_development_demo.py](05_development_demo.py) | 日志、SQLite 参数化查询和测试示例 |
| [速查表与练习](../docs/06-cheatsheet-and-exercises.md) | [06_exercises_solutions.py](06_exercises_solutions.py) | 部分练习的参考实现 |

示例以教学清晰为目标。正式项目还需按实际需求补充输入验证、错误处理、测试和安全措施。

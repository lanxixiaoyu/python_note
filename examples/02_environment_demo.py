"""演示如何检查当前项目使用的 Python 环境。"""

from pathlib import Path
import sys


def main() -> None:
    project_dir = Path(__file__).resolve().parent.parent
    interpreter = Path(sys.executable).resolve()
    in_virtual_environment = sys.prefix != getattr(sys, "base_prefix", sys.prefix)

    print(f"项目目录: {project_dir}")
    print(f"Python 版本: {sys.version.split()[0]}")
    print(f"解释器: {interpreter}")
    print(f"是否运行在虚拟环境中: {'是' if in_virtual_environment else '否'}")

    # 虚拟环境解释器路径通常位于项目的 .venv 目录中。
    if ".venv" in interpreter.parts or "venv" in interpreter.parts:
        print("提示：当前解释器路径看起来来自虚拟环境。")
    else:
        print("提示：运行 python -m venv .venv 可为项目创建虚拟环境。")


if __name__ == "__main__":
    main()

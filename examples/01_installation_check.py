"""检查 Python 安装信息；仅使用 Python 标准库。"""

import platform
import shutil
import subprocess
import sys


def main() -> None:
    print(f"Python 版本: {sys.version.split()[0]}")
    print(f"解释器路径: {sys.executable}")
    print(f"操作系统: {platform.platform()}")

    pip = shutil.which("pip") or shutil.which("pip3")
    print(f"PATH 中的 pip: {pip or '未找到（可尝试 python -m pip）'}")

    # 通过当前解释器查询 pip，避免系统中多个 Python 版本导致 pip 指向错误。
    result = subprocess.run(
        [sys.executable, "-m", "pip", "--version"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode == 0:
        print(result.stdout.strip())
    else:
        print("当前解释器中未能运行 pip。可按对应平台文档安装 pip。")
        if result.stderr.strip():
            print(result.stderr.strip())


if __name__ == "__main__":
    main()

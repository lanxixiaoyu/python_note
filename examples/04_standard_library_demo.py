"""常用标准库和进阶语法演示。"""

from datetime import datetime, timezone
from functools import wraps
import json
from pathlib import Path
from typing import Iterable, Iterator


def nonempty_lines(lines: Iterable[str]) -> Iterator[str]:
    """惰性地产生非空、去除首尾空白的行。"""
    for line in lines:
        cleaned = line.strip()
        if cleaned:
            yield cleaned


def announce(func):
    """一个保留原函数元数据的简单装饰器。"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@announce
def total(values: Iterable[int]) -> int:
    return sum(values)


def main() -> None:
    # pathlib 用于跨平台路径操作。示例只在内存中演示，不创建文件。
    notes_path = Path("notes") / "python.txt"
    print("示例路径:", notes_path)
    print("路径后缀:", notes_path.suffix)

    # JSON 序列化与反序列化
    record = {"language": "Python", "active": True, "version": 3}
    encoded = json.dumps(record, ensure_ascii=False)
    decoded = json.loads(encoded)
    print("JSON:", encoded)
    print("还原的数据:", decoded)

    # 生成器按需产生值
    lines = ["  第一行  ", "", " 第二行"]
    print("非空行:", list(nonempty_lines(lines)))

    # 装饰器
    print("总和:", total([1, 2, 3, 4]))

    # 使用带时区的 UTC 时间
    now_utc = datetime.now(timezone.utc)
    print("UTC 时间:", now_utc.isoformat())


if __name__ == "__main__":
    main()

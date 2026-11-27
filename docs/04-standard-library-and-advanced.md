# 04. 标准库与进阶知识

Python 标准库随解释器提供。优先熟悉标准库，再决定是否引入第三方依赖。

## 1. 文件与路径

文本文件推荐明确编码，并用 `with` 自动关闭文件：

```python
from pathlib import Path

path = Path("notes.txt")
path.write_text("Python 笔记\n", encoding="utf-8")
content = path.read_text(encoding="utf-8")
print(content)
```

大文件应逐行读取，而不是一次性读入全部内容：

```python
with Path("large.txt").open(encoding="utf-8") as file:
    for line in file:
        process_line = line.rstrip("\n")
        print(process_line)
```

文件操作前检查路径和权限；处理用户提供的路径时注意目录穿越风险，不要拼接后就盲目读写。

## 2. JSON、CSV 和命令行

```python
import json

record = {"name": "Ada", "active": True}
serialized = json.dumps(record, ensure_ascii=False)
restored = json.loads(serialized)
```

CSV：

```python
import csv

with open("people.csv", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        print(row)
```

命令行参数可用 `argparse`：为参数提供帮助文字、类型和默认值，便于维护脚本接口。

## 3. 日期、时间与随机数

```python
from datetime import datetime, timezone

now_utc = datetime.now(timezone.utc)
print(now_utc.isoformat())
```

存储时间时优先使用带时区的 UTC 时间，展示时再转换为本地时间。随机抽样可使用 `random`；涉及密码、令牌等安全用途时，应使用 `secrets`，不能使用 `random`。

## 4. 迭代器与生成器

可迭代对象能被 `for` 遍历；迭代器逐个产生值。生成器能延迟计算，适合处理流式数据：

```python
def read_nonempty(lines):
    for line in lines:
        value = line.strip()
        if value:
            yield value
```

生成器通常减少一次性保存大量中间结果的内存开销。

## 5. 装饰器与上下文管理器

装饰器可包装函数行为。使用 `functools.wraps` 保留被装饰函数信息：

```python
from functools import wraps

def announce(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("开始")
        return func(*args, **kwargs)
    return wrapper
```

上下文管理器通过 `with` 管理资源生命周期，例如文件、锁和临时资源。自定义上下文管理器可实现 `__enter__`/`__exit__`，或使用 `contextlib.contextmanager`。

## 6. 类型提示

```python
def average(values: list[float]) -> float:
    if not values:
        raise ValueError("values 不能为空")
    return sum(values) / len(values)
```

类型提示用于沟通意图和静态分析，不会自动在运行时强制类型。复杂类型可从 `typing` 使用 `Iterable`、`Sequence`、`TypedDict`、`Protocol` 等；也可根据目标 Python 版本选择合适写法。

## 7. 并发概念

- `threading`：适合大量等待网络或磁盘的 I/O 工作；共享数据时需要考虑锁和竞态。
- `multiprocessing`：可利用多进程处理 CPU 密集任务，但进程间通信有成本。
- `asyncio`：用协程处理大量异步 I/O；需要使用兼容的异步库，避免在事件循环中执行长时间阻塞操作。

选择方案前先测量瓶颈。并发会增加复杂度，不能保证程序更快。

## 8. 性能与内存

- 先使用 `timeit`、`cProfile` 或内存分析工具定位瓶颈，再优化。
- 避免过早优化；选择清晰的数据结构和算法往往最重要。
- 用生成器逐条处理大型输入；避免不必要的复制。
- 缓存只适用于结果可安全复用的场景，并考虑缓存失效和内存占用。

## 9. 常用标准库速览

- `collections`：`Counter`、`defaultdict`、`deque`。
- `itertools`：高效迭代器组合工具。
- `functools`：`lru_cache`、`partial`、`wraps`。
- `re`：正则表达式；复杂文本处理先考虑普通字符串方法。
- `logging`：分级日志记录。
- `subprocess`：调用外部程序；避免把不可信输入直接拼接到 shell 命令。
- `sqlite3`：内置 SQLite 数据库接口。
- `unittest`：标准库测试框架。

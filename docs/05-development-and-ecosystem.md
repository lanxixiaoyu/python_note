# 05. 开发实践与常用生态

## 1. 测试

测试验证程序行为。测试函数应关注可观察结果，而不是实现细节。

```python
# calculator.py
def add(a, b):
    return a + b
```

```python
# test_calculator.py
from calculator import add

def test_adds_two_numbers():
    assert add(2, 3) == 5
```

可使用标准库 `unittest` 或第三方 `pytest`。测试正常输入、边界条件和预期错误；测试应可重复运行，并尽量不依赖外部网络或真实生产数据。

## 2. 调试和日志

简单调试可使用断点或编辑器调试器；标准库 `pdb` 也能逐步检查程序。

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("处理任务 %s", "daily")
```

日志级别通常包括 DEBUG、INFO、WARNING、ERROR、CRITICAL。避免记录密码、访问令牌、个人敏感信息；异常日志应保留足够上下文但不泄露机密。

## 3. 网络请求

使用第三方 HTTP 库前先安装并查阅其文档。请求应设置合理超时，检查状态码，并处理网络失败：

```python
# 伪代码风格示意：具体异常类型以所选 HTTP 库文档为准
response = http_client.get(url, timeout=10)
response.raise_for_status()
data = response.json()
```

不要关闭 TLS 证书验证来“修复”连接问题。不要把令牌硬编码到源码或提交到版本控制；通过安全的环境变量或密钥管理系统配置。

## 4. 数据库

关系型数据库使用 SQL 表达查询。参数化查询可以避免 SQL 注入：

```python
import sqlite3

with sqlite3.connect("app.db") as connection:
    connection.execute(
        "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT)"
    )
    connection.execute("INSERT INTO items(name) VALUES (?)", ("笔记",))
```

不要用字符串拼接构造包含用户输入的 SQL。真实服务还需要设计事务、索引、迁移、备份和访问权限。

## 5. Web 开发与数据分析方向

根据目标选择生态：

- Web：Django、Flask、FastAPI 等；理解 HTTP、路由、输入校验和认证授权。
- 数据分析：NumPy、pandas、Matplotlib 等；先学习数据清洗、缺失值和图表表达。
- 自动化：标准库、命令行工具和任务调度；限制权限并验证输入。
- 机器学习：先掌握 Python、数据处理、统计与模型评估，再选合适框架。

框架的 API 和版本会变化，查阅项目所用版本的官方文档，不要把演示代码直接当成生产方案。

## 6. 项目打包与配置

现代 Python 项目可使用 `pyproject.toml` 声明项目元信息及工具配置。根据团队规模选用依赖锁定和打包工具；固定依赖有利于复现，但升级时要评估兼容性与安全公告。

配置与代码分离：开发、测试、生产环境可使用不同配置；机密信息通过安全渠道注入。不要把生产凭据写进示例文件或日志。

## 7. Git 与协作

- 小步提交，每次提交说明一个逻辑变更。
- 提交源代码、测试和依赖配置；忽略虚拟环境、缓存、构建产物。
- 代码评审关注正确性、可读性、安全性和测试覆盖。
- 文档中的命令要在干净环境验证，并说明平台差异。

## 8. 常见错误清单

- 把 `=`（赋值）与 `==`（比较）混淆。
- 混淆可变对象别名与复制。
- 忘记 `input()` 得到的是字符串。
- 误用 `is` 比较值相等；普通比较使用 `==`。
- 捕获所有异常或忽略错误。
- 在系统 Python 中全局安装项目依赖。
- 依赖当前工作目录导致文件路径在 IDE 和终端中表现不同；需要时用 `pathlib` 和明确的项目路径。
- 直接执行不可信的 shell 命令或 SQL 字符串拼接。

"""开发实践演示：日志、SQLite 参数化查询和单元测试。"""

import logging
import sqlite3
import unittest

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def add(a: int, b: int) -> int:
    return a + b


def demo_database() -> None:
    # 使用内存数据库，运行后不会在项目目录留下数据库文件。
    with sqlite3.connect(":memory:") as connection:
        connection.execute(
            "CREATE TABLE tasks (id INTEGER PRIMARY KEY, title TEXT NOT NULL)"
        )
        title = "学习 Python"
        # 使用 ? 占位符绑定参数，不要拼接用户输入来构造 SQL。
        connection.execute("INSERT INTO tasks(title) VALUES (?)", (title,))
        row = connection.execute(
            "SELECT id, title FROM tasks WHERE title = ?", (title,)
        ).fetchone()
        logger.info("查询到任务: %s", row)


class AddTests(unittest.TestCase):
    def test_adds_positive_numbers(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_adds_negative_number(self) -> None:
        self.assertEqual(add(-1, 1), 0)


def main() -> None:
    logger.info("开始演示")
    demo_database()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(AddTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)


if __name__ == "__main__":
    main()

"""Python 基础语法演示。"""


def describe_number(number: int) -> str:
    """返回数字的简单描述。"""
    if number % 2 == 0:
        return f"{number} 是偶数"
    return f"{number} 是奇数"


def safe_divide(numerator: float, denominator: float) -> float | None:
    """演示异常处理；除数为零时返回 None。"""
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("不能除以零。")
        return None


class Student:
    """一个简单的学生类。"""

    def __init__(self, name: str, scores: list[int]) -> None:
        self.name = name
        self.scores = scores

    def average(self) -> float:
        return sum(self.scores) / len(self.scores) if self.scores else 0.0


def main() -> None:
    # 基本类型、字符串和 f-string
    name = "小林"
    age = 18
    print(f"{name}，{age} 岁")

    # 列表、字典和集合
    numbers = [1, 2, 2, 3, 4]
    unique_numbers = set(numbers)
    profile = {"name": name, "age": age}
    print("去重后的数字:", sorted(unique_numbers))
    print("字典中的姓名:", profile.get("name", "未知"))

    # 循环、条件和推导式
    for number in range(1, 5):
        print(describe_number(number))
    squares = [number**2 for number in range(5)]
    print("平方:", squares)

    # 函数和异常
    print("10 / 2 =", safe_divide(10, 2))
    print("10 / 0 =", safe_divide(10, 0))

    # 类和实例
    student = Student("小林", [90, 85, 95])
    print(f"{student.name} 的平均分: {student.average():.1f}")


if __name__ == "__main__":
    main()

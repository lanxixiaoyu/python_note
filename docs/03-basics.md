# 03. Python 基础语法

## 1. 语句、缩进和注释

Python 使用缩进表示代码块，通常每级缩进 4 个空格；同一代码块保持一致。

```python
# 单行注释
if True:
    print("缩进表示代码块")
```

文档字符��通常用三引号编写，用于模块、类和函数说明。

## 2. 变量与基本类型

变量名绑定到对象，不需要预先声明类型。变量名区分大小写，推荐使用 `snake_case`。

```python
name = "Ada"            # str
age = 20                 # int
height = 1.68            # float
is_student = True        # bool
nothing = None           # NoneType
```

检查类型和类型转换：

```python
print(type(age))
number = int("42")
text = str(42)
```

`input()` 返回字符串；进行数值运算前需要转换并处理无效输入。

## 3. 字符串

```python
language = "Python"
print(language[0])       # P
print(language[0:3])     # Pyt，左闭右开
print(f"我正在学习 {language}")
print(" a,b ".strip().split(","))
```

字符串不可变。需要拼接大量片段时，可将片段放入列表再用 `"".join(parts)`。

## 4. 容器

### 列表 `list`：有序、可变

```python
numbers = [3, 1, 2]
numbers.append(4)
numbers.sort()
first, *rest = numbers
```

### 元组 `tuple`：有序、不可变

```python
point = (10, 20)
x, y = point
```

### 字典 `dict`：键值映射

```python
user = {"name": "Lin", "age": 18}
user["city"] = "上海"
for key, value in user.items():
    print(key, value)
```

字典键必须可哈希；用 `dict.get(key, default)` 可提供默认值。

### 集合 `set`：唯一元素

```python
tags = {"python", "linux", "python"}
print(tags)  # 重复项会被去重
```

集合适合去重、成员测试和交并差运算。

## 5. 运算符

- 算术：`+ - * / // % **`；`/` 为真除法，`//` 为整除。
- 比较：`== != < <= > >=`；对象身份使用 `is`，不要用 `is` 比较普通数值或字符串相等性。
- 逻辑：`and or not`，具备短路特性。
- 成员：`in`、`not in`。
- 赋值：`=`, `+=` 等。

## 6. 条件和循环

```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"

for number in range(3):
    print(number)

while score < 100:
    score += 1
```

`break` 结束循环，`continue` 跳过本轮。循环可配合 `else`：只有循环没有通过 `break` 结束时才执行。

## 7. 推导式

```python
squares = [n * n for n in range(6)]
even_squares = {n: n * n for n in range(6) if n % 2 == 0}
unique_lengths = {len(word) for word in ["cat", "python"]}
```

推导式适用于简单转换；逻辑过于复杂时使用普通循环提高可读性。

## 8. 函数

```python
def greet(name: str, punctuation: str = "!") -> str:
    """返回问候语。"""
    return f"你好，{name}{punctuation}"

print(greet("小明"))
```

参数可有位置参数、关键字参数、默认值、可变位置参数 `*args` 和可变关键字参数 `**kwargs`。避免使用可变对象作为默认值：

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

函数没有显式 `return` 时返回 `None`。优先让函数职责清晰、输入输出明确。

## 9. 模块、包和入口

一个 `.py` 文件就是模块。用 `import math` 或 `from pathlib import Path import ...` 导入模块/名称。避免用与标准库同名的文件（例如 `random.py`），否则可能遮蔽标准库。

```python
def main():
    print("程序入口")

if __name__ == "__main__":
    main()
```

包通常由目录组织；现代 Python 支持命名空间包，但初学项目可通过 `__init__.py` 明确包边界。

## 10. 异常

```python
try:
    value = int(input("输入整数："))
except ValueError:
    print("输入格式不正确")
else:
    print(value * 2)
finally:
    print("本段始终执行")
```

只捕获能够合理处理的异常，避免裸 `except:`。需要抛出异常时使用 `raise`；不要悄悄吞掉错误。

## 11. 面向对象

```python
class Dog:
    species = "犬科"  # 类属性

    def __init__(self, name: str):
        self.name = name  # 实例属性

    def speak(self) -> str:
        return f"{self.name}：汪！"

my_dog = Dog("小白")
print(my_dog.speak())
```

理解实例、属性、方法、继承和组合。很多时候组合比复杂继承更简单。双下划线方法（如 `__init__`）是 Python 数据模型的一部分。

## 12. 可变性与复制

列表、字典和集合可变；整数、字符串和元组通常不可变（元组中的对象仍可能可变）。赋值通常只是创建另一个引用。必要时使用 `copy.copy()` 浅拷贝或 `copy.deepcopy()` 深拷贝，并理解嵌套对象行为。

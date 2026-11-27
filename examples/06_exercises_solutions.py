"""第 06 章部分练习的参考实现。"""

from collections import Counter
import re
from typing import Iterable


def word_counts(text: str) -> dict[str, int]:
    """统计英文单词频次，忽略大小写和常见标点。"""
    words = re.findall(r"[\w']+", text.casefold())
    return dict(Counter(words))


def unique_in_order(values: Iterable[int]) -> list[int]:
    """去重并保留元素首次出现的顺序。"""
    seen: set[int] = set()
    result: list[int] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def is_palindrome(text: str) -> bool:
    """忽略大小写和非字母数字字符后判断回文。"""
    normalized = "".join(char.casefold() for char in text if char.isalnum())
    return normalized == normalized[::-1]


def primes_below(limit: int):
    """逐个产生小于 limit 的素数（试除法，适合学习用的小范围）。"""
    for candidate in range(2, limit):
        is_prime = True
        for divisor in range(2, int(candidate**0.5) + 1):
            if candidate % divisor == 0:
                is_prime = False
                break
        if is_prime:
            yield candidate


def main() -> None:
    print("词频:", word_counts("Python is fun; Python is clear."))
    print("保序去重:", unique_in_order([3, 1, 3, 2, 1]))
    print("回文:", is_palindrome("A man, a plan, a canal: Panama!"))
    print("小于 20 的素数:", list(primes_below(20)))


if __name__ == "__main__":
    main()

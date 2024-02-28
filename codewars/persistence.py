# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python
from typing import Optional
import functools


lst = [f for f in dir(str) if "__" not in f]
print(lst)


def persistence(n):
    out = 0
    while len(str(n)) > 1:
        n = functools.reduce(lambda a, b: int(a) * int(b), str(n))
        out += 1
    return out


print(persistence(999))

print("hello", "james")

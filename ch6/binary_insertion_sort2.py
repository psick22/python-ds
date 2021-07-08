import bisect
from typing import MutableSequence


def binary_insert_sort(a: MutableSequence) -> None:
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)

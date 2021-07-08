from typing import MutableSequence


def shell_sort(a: MutableSequence) -> None:
    h = len(a) // 2
    while h > 0:
        for start in range(h):
            gap_insertion_sort(a, start, h)
        print(a)
        h //= 2


def gap_insertion_sort(a: MutableSequence, start: int, gap: int) -> None:
    for i in range(start + gap, len(a), gap):
        temp = a[i]
        pos = i
        while pos >= gap and a[pos - gap] > temp:
            a[pos] = a[pos - gap]
            pos -= gap

        a[pos] = temp


a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(a)
print(f'a = {a}')

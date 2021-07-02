from typing import Any, Sequence
import copy


def seq_search(a: Sequence, key: Any) -> int:
    i = 0
    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1


def seq_search_2(a: Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1


def search_sentinel(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq)
    a.append(key)

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1

    return -1 if i == len(seq) else i


if __name__ == "__main__":

    num = int(input("원소 수를 입력하세요 : "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    key = int(input("검색할 값을 입력 : "))

    idx = seq_search(x, key)

    if idx == -1:
        print("없음")
    else:
        print(f'x[{idx}]')

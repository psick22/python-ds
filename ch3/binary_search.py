# 이진 검색 활용을 위해서는 데이터가 정렬되어있어야함

from typing import Any, Sequence


def bin_search(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a) - 1

    while pl <= pr:
        pc = (pr + pl) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
    return -1


if __name__ == "__main__":
    num = int(input("원소 수를 입력 : "))
    x = [None] * num

    print("오름차순으로 입력하세요")

    x[0] = int(input('x[0] : '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}] : '))
            if x[i] >= x[i - 1]:
                break

    key = int(input("검색 할 값 : "))

    idx = bin_search(x, key)

    if idx == -1:
        print("없음")

    else:
        print(f'검색값은 x[{idx}] 에 있습니다')

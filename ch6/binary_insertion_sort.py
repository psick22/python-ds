from typing import MutableSequence


def binary_insert_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0
        pr = i - 1
        while pl <= pr:
            pc = (pl + pr) // 2
            if a[pc] == key:
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1

        pd = pl + 1 if pl <= pr else pr + 1

        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = key


if __name__ == "__main__":
    print(' -- 이진 삽입 정렬 -- ')
    num = int(input("원소 수를 입력하세요 >> "))
    x = [None] * num
    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    binary_insert_sort(x)

    print('---- 오름차순 정렬 결과 ----')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

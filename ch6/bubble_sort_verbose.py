from typing import MutableSequence


def bubble_sort(a: MutableSequence) -> None:
    ccnt = 0  # 비교 횟수
    scnt = 0  # 교환 횟수
    n = len(a)
    for i in range(n - 1):
        print(f'[ pass {i + 1} ]')
        for j in range(n - 1, i, -1):
            for m in range(0, n - 1):
                print(f'{a[m]:2}' + ('  ' if m != j - 1 else ' +' if a[j - 1] > a[j] else ' -'), end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]

        for m in range(0, n - 1):
            print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')
    print(f'비교 횟수 : {ccnt} 회 ')
    print(f'교환 횟수 : {scnt} 회 ')


if __name__ == "__main__":
    print(' -- 버블 정렬 -- ')
    num = int(input("원소 수를 입력하세요 >> "))
    x = [None] * num
    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    bubble_sort(x)

    print('---- 오름차순 정렬 결과 ----')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

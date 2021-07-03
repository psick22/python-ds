from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu', ['인큐', '디큐', '피크', '검색', '덤프', '종료'])


def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)


q = FixedQueue(64)


while True:
    print(f'현재 데이터 갯수: {len(q)} / {q.capacity}')
    menu = select_menu()

    if menu == Menu.인큐:
        value = int(input("인큐할 데이터를 입력하세요: "))
        try:
            q.enqueue(value)
        except FixedQueue.Full:
            print("큐가 가득 찼습니다")

    elif menu == Menu.디큐:
        try:
            value = q.dequeue()
            print(f'디큐한 데이터는 {value} 입니다')
        except FixedQueue.Empty:
            print("큐가 비어있습니다")

    elif menu == Menu.피크:
        try:
            value = q.peek()
            print(f'피크한 데이터는 {value} 입니다')
        except FixedQueue.Empty:
            print("큐가 비어있습니다")

    elif menu == Menu.검색:
        value = int(input("검색할 값을 입력하세요: "))
        if value in q:
            print(f'{q.count(value)} 개 있으며, 맨 앞의 인덱스는 {q.find(value)} 입니다')
        else:
            print('검색값을 찾을 수 없습니다')

    elif menu == Menu.덤프:
        q.dump()

    else:
        break





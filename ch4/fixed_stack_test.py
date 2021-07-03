from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu', ['푸시', '팝', '피크', '검색', '덤프', '종료'])


def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)


stack = FixedStack(64)


while True:
    print(f'현재 데이터 갯수 : {len(stack)} / {stack.capacity}')
    menu = select_menu()

    if menu == Menu.푸시:
        value = int(input('푸시할 데이터를 입력하세요 >> '))
        try:
            stack.push(value)
        except FixedStack.Full:
            print(' >> 스택이 가득 차있습니다.')

    elif menu == Menu.팝:
        try:
            value = stack.pop()
            print(f' >>팝한 데이터는 {value} 입니다')
        except FixedStack.Empty:
            print(' >> 스택이 비어있습니다')

    elif menu == Menu.피크:
        try:
            value = stack.peek()
            print(f' >> 피크한 데이터는 {value} 입니다')
        except FixedStack.Empty:
            print(' >> 스택이 비어있습니다')

    elif menu == Menu.검색:
        value = int(input('검색할 값을 입력하세요: '))
        if value in stack:
            print(f' >> {value}는 스택에 {stack.count(value)} 개 있으면, 맨 앞의 위치는 {stack.find(value)} 입니다')
        else:
            print(' >> 없습니다')

    elif menu == Menu.덤프:
        stack.dump()

    else:
        break




from ch4.stack import Stack


def recur(n: int) -> int:
    stk = Stack(n)

    while True:
        if n > 0:
            stk.push(n)
            n = n - 1
            continue
        if not stk.is_empty():
            n = stk.pop()
            print(n)
            n = n - 2
            continue
        break

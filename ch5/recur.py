def recur(n: int) -> None:
    while n > 0:
        recur(n - 1)
        print(n)
        n = n - 2


recur(5)

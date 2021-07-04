def factorial(num: int) -> int:
    if num > 0:
        return num * factorial(num - 1)
    elif num == 0:
        return 1
    else:
        raise ValueError


if __name__ == "__main__":
    n = int(input("출력할 팩토리얼 값을 입력하세요 : "))
    print(f"{n}! = {factorial(n)}")

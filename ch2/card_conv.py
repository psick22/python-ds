## 10진수 정수값 -> (2~36) n진수로 출력

def card_conv(number: int, n: int) -> str:
    res = ''
    charset = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while number > 0:
        res += charset[number % n]
        number = number // n

    return res[::-1]


if __name__ == "__main__":
    print("10진수를 n진수로 변환")

    while True:
        while True:
            number = int(input("변환할 값으로 음이 아닌 정수를 입력하세요 : "))
            if number > 0:
                break

        while True:
            n = int(input("변환할 진수를 입력하세요 (2~36) >> "))
            if 2 <= n <= 36:
                break

        print(f'{n}진수 변환값: {card_conv(number, n)}')

        retry = input("한번 더 하시겠습니까? (Y / N) >>함 ")
        if retry in {'N','n'}:
            break


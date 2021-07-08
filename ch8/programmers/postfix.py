# 피연산자이면 그냥 출력
# ( -> 스택에 push
# ) 이면 ( 이나올때 까지 스택에서 pop해서 출력
# 연산자이면 스택에서 이보다 높거나 같은 우선순위를 pop해서 출력하고 이 연산자는 스택에 push
# 남아있는 스택은 모두 pop 이후 출력

class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        if len(self.data) == 0:
            return False
        return self.data[len(self.data) - 1]


prec = {
    "*": 3, "/": 3, "+": 2, "-": 2, "(": 1
}


def solution(S):
    opStack = ArrayStack()
    answer = ''

    for char in S:
        if char.isalpha():
            answer += char
        else:
            if opStack.isEmpty():
                opStack.push(char)
            else:
                if char == "(":
                    opStack.push(char)
                elif char == ")":
                    while opStack.peek() != '(':
                        answer += opStack.pop()
                    opStack.pop()
                else:
                    while opStack.size() > 0 and prec[opStack.peek()] >= prec[char]:
                        answer += opStack.pop()
                    opStack.push(char)

    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer


print(solution("A+B+C"))

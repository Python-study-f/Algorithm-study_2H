# 후위 표기식 1918 백준

a = input()
stack = []
res = ""

for x in a:
    if x.isalpha():
        res += x
    else:
        if x == "(":
            stack.append(x)
        elif x == "*" or x == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                res += stack.pop()
            stack.append(x)
        elif x == "+" or x == "-":
            # + - 는 어느 문자보다 우선순위가 낮기때문에 "("" 전까지 다 빼서 res 에 넣는다
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.append(x)
        elif x == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()

print(res)

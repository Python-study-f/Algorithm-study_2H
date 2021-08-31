def pri(a):
    if a == "*" or a == "/":
        return 2
    if a == "+" or a == "-":
        return 1
    if a == "(":
        return 0


a = input()
stack = []
temp = ''

for k in a:
    if k == '(':
        stack.append(k)
    elif k == ')':
        while stack and stack[-1] != '(':
            temp += stack.pop()
        stack.pop()
    elif k == '*' or k == '/' or k == '+' or k == '-':
        while stack and pri(stack[-1]) >= pri(k):
            temp += stack.pop()
        stack.append(k)
    else:
        temp += k

while stack:
    temp += stack.pop()

print(temp)

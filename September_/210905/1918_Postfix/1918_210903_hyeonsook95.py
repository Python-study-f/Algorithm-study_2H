import sys

input = sys.stdin.readline


def solution(EXP):
    prior = {"(": -1, "+": 1, "-": 1, "*": 2, "/": 2}
    stack = []
    for char in EXP:
        if char.isalpha():
            print(char, end="")
            continue

        # 괄호
        if char == ")":
            while stack and stack[-1] != "(":
                print(stack.pop(), end="")
            stack.pop()
        # 연산자
        else:
            while stack and prior[char] > 0 and prior[stack[-1]] >= prior[char]:
                print(stack.pop(), end="")
            stack.append(char)

    while stack:
        if stack[-1] == "(":
            stack.pop()
        else:
            print(stack.pop(), end="")


solution(input().strip())

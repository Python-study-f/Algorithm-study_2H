# 짝을 맞춰 닫혀있는 괄호들은 모두 올바른 문자열이다.
# A, B가 올바른 괄호 문자열이라면, AB도 올바른 괄호 문자열이다.
# 문자열 s가 매개변수로 주어진다.
# s를 왼쪽으로 x칸만큼 회전시켰을 때, s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하라.

# s, 1 <= len(s) <= 1,000
# x, 0 <= x < len(s)

from collections import deque


def solution(s):
    cnt = 0
    paren = {"[": None, "]": "[", "(": None, ")": "(", "{": None, "}": "{"}

    def is_valid(dq):
        stack = []
        while dq:
            if stack and stack[-1] == paren[dq[0]]:
                stack.pop()
                dq.popleft()
            else:
                stack.append(dq.popleft())
        return len(stack) == 0

    for m in range(len(s)):
        dq = deque(s)
        dq.rotate(m)
        if is_valid(dq):
            cnt += 1
    return cnt

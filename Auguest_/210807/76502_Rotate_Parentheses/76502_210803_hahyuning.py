# 1000 * 1000 = 10 ** 6
# 회전 시킬때마다 올바른 괄호열인지 확인

def solution(s):
    ans = 0
    for _ in range(len(s)):
        s = s[1:] + s[0]
        if check(s):
            ans += 1
    return ans

def check(s):
    stack = []
    pairs = {"(": ")", "[": "]", "{": "}"}
    for x in s:
        if x in pairs.keys():
            stack.append(x)
            continue

        if not stack:
            return False
        y = stack.pop()
        if pairs[y] != x:
            return False

    if stack:
        return False
    return True

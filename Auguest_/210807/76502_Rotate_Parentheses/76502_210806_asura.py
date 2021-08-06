def valid_parentheses(check):
    dic = {
        "}" : "{",
        "]" : "[",
        ")" : "("
    }
    st = []
    for i in check:
        if i not in dic.keys():
            st.append(i)
        elif not st or dic[i] != st.pop():
            return False

    return len(st) == 0

def solution(s):
    stack = list(s)
    cnt = 0

    for k in range(len(s)):
        if valid_parentheses(''.join(stack)):
            cnt += 1
        stack.append(stack.pop(0))

    return cnt
from collections import deque
def chkpar(st):
    dq = deque()
    for ch in st:
        if ch == '[' or ch == '{' or ch == '(':
            dq.append(ch)
        elif ch == ']' or ch == '}' or ch == ')':
            if not dq:
                return 0
            elif (ch ==']' and dq[-1]=='[') or (ch=='}' and dq[-1] == '{') or (ch ==')' and dq[-1] == '('):
                dq.pop()
            else:
                return 0
    if dq:
        return 0
    else:
        return 1
    
def solution(ss):
    answer = 0
    s = deque(ss)
    for i in range(len(s)):
        answer += chkpar(s)
        a = s.popleft()
        s.append(a)
    return answer

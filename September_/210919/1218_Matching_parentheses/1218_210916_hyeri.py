from collections import deque

paren = {'{': '}', '<': '>', '[': ']', '(': ')'}

for t in range(1, 11):
    N = int(input())
    sentence = input()
    dq = deque()
    answer = 0
    for c in sentence:
        if c in paren:
            dq.append(c)
        else:
            if dq:
                l = dq[-1]
                if paren[l] != c:
                    break
                else:
                    dq.pop()
            else:
                break
    else:
        answer = 1
    print("#{} {}".format(t, answer))

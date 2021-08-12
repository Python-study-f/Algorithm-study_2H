import re

def check(x):
    if x[-1] in end:
        x = x[:-1]

    p = re.compile("[A-Z]{1}[a-z]*")
    if p.fullmatch(x):
        return True
    else:
        return False

t = int(input())
for tx in range(1, t + 1):
    n = int(input())
    n_cnt = 0
    end = [".", "?", "!"]

    ans = [0] * n
    cnt = 0

    while True:
        if n_cnt == n:
            break
        tmp = input().split( )
        for x in tmp:
            if check(x):
                cnt += 1

            if x[-1] in end:
                ans[n_cnt] = cnt
                cnt = 0
                n_cnt += 1

    print("#{}".format(tx), end=" ")
    print(*ans)

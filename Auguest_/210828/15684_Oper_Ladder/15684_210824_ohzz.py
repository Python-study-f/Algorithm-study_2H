# 사다리 조작 15684 백준

import sys

input = sys.stdin.readline

n, m, h = map(int, input().split())

if m == 0:
    print(0)
    exit()

ladder = [[0] * n for _ in range(h)]
for _ in range(m):
    x, y = map(int, input().split())
    ladder[x - 1][y - 1] = 1


def check():
    for start in range(n):
        k = start
        for i in range(h):
            if ladder[i][k]:
                k += 1
            elif k > 0 and ladder[i][k - 1]:
                k -= 1
        if start != k:
            return False
    return True


def dfs(cnt, x, y):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt:
        return
    for i in range(x, h):
        if i == x:
            k = y
        else:
            k = 0
        for j in range(k, n - 1):
            if not ladder[i][j] and not ladder[i][j + 1]:

                ladder[i][j] = 1
                dfs(cnt + 1, i, j + 2)
                ladder[i][j] = 0


ans = 4
dfs(0, 0, 0)
if ans < 4:
    print(ans)
else:
    print(-1)

# https://baby-ohgu.tistory.com/3 완전 참고함. 체크하는게 어려웠음

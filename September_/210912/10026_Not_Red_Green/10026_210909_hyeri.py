import sys
sys.setrecursionlimit(10000)


N = int(input())
arr = [list(input()) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, n, ok):
    for d in range(4):
        tx, ty = x + dx[d], y + dy[d]
        if 0 <= tx < N and 0 <= ty < N and visit[tx][ty] != ok:
            if arr[tx][ty] == n:
                visit[tx][ty] = ok
                dfs(tx, ty, n, ok)
            if ok == 2:
                if (arr[x][y] == 'R' or arr[x][y] == 'G') and (arr[tx][ty] == 'R' or arr[tx][ty] == 'G'):
                    visit[tx][ty] = 2
                    dfs(tx, ty, n, ok)


num1 = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] != 1:
            visit[i][j] = 1
            num1 += 1
            dfs(i, j, arr[i][j], 1)

num2 = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] != 2:
            visit[i][j] = 2
            num2 += 1
            dfs(i, j, arr[i][j], 2)

print("{} {}".format(num1, num2))

import sys
sys.setrecursionlimit(10**6)

a = int(input())
array = [list(map(int, input().split())) for _ in range(a)]
visit = [[0] * a for i in range(a)]

dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if visit[x][y] != 0:
        return visit[x][y]
    visit[x][y] = 1
    for b in range(4):
        nx = x + dx[b]
        ny = y + dy[b]
        if 0 <= nx < a and 0 <= ny < a:
            if array[x][y] < array[nx][ny]:
                visit[x][y] = max(visit[x][y], dfs(nx, ny) + 1)
    return visit[x][y]

count = 0
for i in range(a):
    for j in range(a):
        if visit[i][j] == 0:
            count = max(count, dfs(i, j))

print(count)

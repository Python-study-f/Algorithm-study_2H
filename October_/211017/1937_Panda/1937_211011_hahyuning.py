import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(i, j):
    if dist[i][j] != 0:
        return dist[i][j]

    dist[i][j] = 1

    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] > a[i][j]:
                dist[i][j] = max(dist[i][j], dfs(nx, ny) + 1)

    return dist[i][j]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# d[i][j]: (i, j) 에서 최대한 살 수 있는 일수
dist = [[0] * n for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        if dist[i][j] == 0:
            ans = max(dfs(i, j), ans)

print(ans)
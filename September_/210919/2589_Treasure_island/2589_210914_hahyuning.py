from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global ans

    q = deque()
    q.append((x, y))
    visit = [[-1] * m for _ in range(n)]
    visit[x][y] = 0

    while q:
        x, y = q.popleft()
        ans = max(ans, visit[x][y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == -1 and maps[nx][ny] == "L":
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))

n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(input().rstrip())

ans = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == "L":
            bfs(i, j)

print(ans)
from collections import deque
import sys

# 1. 남아있는 빙산의 개수 세기
def bfs(i, j):
    q = deque()
    q.append((i, j))
    dist[i][j] = True

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] != 0 and not dist[nx][ny]:
                    q.append((nx, ny))
                    dist[nx][ny] = True
    return

# 2. 빙산 녹이기
def melt():
    b = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j] != 0:
                cnt = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 0:
                        cnt += 1
                b[i][j] = cnt
    for i in range(n):
        for j in range(m):
            a[i][j] = max(0, a[i][j] - b[i][j])
    return


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0
while True:
    cnt = 0
    dist = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j] != 0 and not dist[i][j]:
                cnt += 1
                bfs(i, j)

    # 빙산이 분리되는 경우
    if cnt >= 2:
        print(ans)
        sys.exit(0)

    # 빙산이 다 녹을 때까지 분리되지 않는 경우
    if cnt == 0:
        print(0)
        break

    ans += 1
    melt()
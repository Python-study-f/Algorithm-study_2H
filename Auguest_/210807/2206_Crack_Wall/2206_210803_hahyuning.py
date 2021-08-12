from collections import deque

n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
# dist[i][j][k]: (0, 0)에서 (i, j)까지 벽을 부순 횟수가 k번 일때의 최단 거리
dist = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
q = deque()
q.append((0, 0, 0))
dist[0][0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    x, y, w = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        # 새로 가는 곳이 빈칸인 경우
        if a[nx][ny] == 0 and dist[nx][ny][w] == -1:
            dist[nx][ny][w] = dist[x][y][w] + 1
            q.append((nx, ny, w))
        # 새로 가는 곳이 벽인 경우
        if a[nx][ny] == 1 and w + 1 <= 1:
            if dist[nx][ny][w + 1] == -1:
                dist[nx][ny][w + 1] = dist[x][y][w] + 1
                q.append((nx, ny, w + 1))

ans = -1
for i in range(2):
    if dist[-1][-1][i] != -1:
        if ans == -1 or dist[-1][-1][i] < ans:
            ans = dist[-1][-1][i]
print(ans)


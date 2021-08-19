from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dist = [[-1] * m for _ in range(n)]
    dist[0][0] = 1
    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    return dist[-1][-1]
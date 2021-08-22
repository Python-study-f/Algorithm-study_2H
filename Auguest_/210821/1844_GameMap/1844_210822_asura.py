from collections import  deque

def solution(maps):

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    N, M = len(maps), len(maps[0])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    dq = deque()
    dq.append((0,0))

    while dq:
        x, y = dq.popleft()

        if x == N-1 and y == M-1:
            return visited[-1][-1]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                dq.append((nx,ny))

    return -1
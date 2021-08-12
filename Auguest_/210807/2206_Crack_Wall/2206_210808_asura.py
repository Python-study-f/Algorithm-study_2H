from collections import deque

N,M = map(int,input().split())
data = [list(map(int, list(input()))) for _ in range(N)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():
    dq = deque()
    dq.append((0, 0, 1))
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)] # 3번째 인덱스 1은 부실 수 있는 벽 1개라는 뜻, 0은 부실 수 없다는 뜻
    visited[0][0][1] = 1

    while dq:
        x, y, wall = dq.popleft()

        if x == N-1 and y == M-1: # 마지막에 닿았을 때,
            return visited[x][y][wall]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny <M:
                if data[nx][ny] == 1 and wall == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    dq.append((nx,ny,0))
                elif data[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    dq.append((nx,ny,wall))
    return -1
print(bfs())

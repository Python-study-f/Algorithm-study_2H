from collections import deque
import sys

input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y,color):

    dq = deque()
    dq.append((x,y))
    visited[x][y] = 1

    while dq:
        x,y = dq.popleft()

        for d in range(4):
            nx,ny = x + dx[d], y + dy[d]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and data[nx][ny] == color:
                dq.append((nx,ny))
                visited[nx][ny] = 1  # 방문체크


N = int(input())
data = [list(input()) for _ in range(N)]

cnt = 0
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i,j,data[i][j])
            cnt += 1
print(cnt,end=' ')

for i in range(N):
    for j in range(N):
        if data[i][j] == "R":
            data[i][j] = "G"

cnt = 0
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i,j,data[i][j])
            cnt += 1
print(cnt)


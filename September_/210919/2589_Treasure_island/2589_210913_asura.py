from collections import deque

"""
접근을 왜 그렇게 했어?
1. 최단거리(0.9) + 상하좌우(0.1) = BFS/DFS
2. 쪼개는 문제가 아니기 때문에 DP가 아니다.
"""

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):

    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1
    num = 0

    dq = deque()
    dq.append((x,y))

    while dq:
        x,y = dq.popleft()

        for a in range(4):
            nx, ny = x + dx[a], y + dy[a]

            if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                num = max(num,visited[nx][ny])
                dq.append((nx,ny))

    return num -1

N,M = map(int,input().split())

data = [list(input()) for _ in range(N)]

max_dist = 0


for i in range(N):
    for j in range(M):
        if data[i][j] =='L':
            max_dist = max(max_dist,bfs(i,j))

print(max_dist)


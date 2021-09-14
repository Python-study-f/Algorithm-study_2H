from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n,m  = map(int,input().split())
graph = [list(map(str, input())) for _ in range(n)]

def bfs(x,y):
    q = deque()
    q.append([x,y])
    tmp = [[0]*m for _ in range(n)]
    tmp[x][y] = 1
    num = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 'L' and tmp[nx][ny] == 0:
                    tmp[nx][ny] = tmp[x][y]+1
                    num = max(num, tmp[nx][ny])
                    q.append([nx,ny])
    return num-1

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            cnt = max(cnt, bfs(i,j))
            
print(cnt)

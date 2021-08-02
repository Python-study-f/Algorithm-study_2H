from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph=[list(map(int, input().strip())) for _ in range(n)]
visited=[[[0] * (2) for _ in range(m)] for _ in range(n)]
visited[0][0] = [1,1]

def bfs():
    q=deque()
    q.append([0,0,0])

    
    while q:
        x,y,z=q.popleft()
        if x==n-1 and y==m-1:
            return visited[x][y][z]
        
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<m and visited[nx][ny][z]==0:
                if graph[nx][ny]==0:
                    visited[nx][ny][z]=visited[x][y][z]+1
                    q.append([nx,ny,z])
                elif z<1:
                    visited[nx][ny][z+1]=visited[x][y][z]+1
                    q.append([nx,ny,z+1])
    return -1

print(bfs())
    

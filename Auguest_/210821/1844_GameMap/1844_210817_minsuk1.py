from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



def solution(graph):
    n=len(graph); m=len(graph[0])    
    
    def bfs(x,y):
        q = deque()
        q.append((x,y))
        while q:
            x,y=q.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                    graph[nx][ny] = graph[x][y]+1                
                    q.append((nx,ny))
        return graph[n-1][m-1] if graph[n-1][m-1]!=1 else -1 

    
    return bfs(0,0)
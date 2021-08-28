from collections import deque

picture=[[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]
n,m = len(picture), len(picture[0])
dx = [0,0,-1,1]
dy = [-1,1,0,0]
visited = [[False]*m for _ in range(n)]
ans1=0
ans2=0


def bfs(x,y,color):
    cnt=0
    q=deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m and picture[nx][ny]==color and not visited[nx][ny]:
                cnt += 1
                visited[nx][ny] = 1
                q.append((nx,ny))
    return cnt

for i in range(n):
    for j in range(m):
        if not visited[i][j] and picture[i][j] != 0:
            tmp=bfs(i,j,picture[i][j])
            ans2 = max(tmp,ans2)
            ans1 += 1

print(ans1,ans2)
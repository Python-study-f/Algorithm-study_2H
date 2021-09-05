from collections import deque

def bfs(x,y,visited):
    q = deque()
    mq = deque()
    q.append((x, y))
    
    visited[x][y] = 1
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    while q:
        ax, ay = q.popleft()
        mcount = 0
        for i in range(4):
            tx, ty = ax + dx[i], ay + dy[i]
            if 0 <= tx < n and 0 <= ty < m and visited[tx][ty] == 0:
                if array[tx][ty] != 0:
                    visited[tx][ty] = 1
                    q.append((tx, ty))
                else:
                    mcount += 1
        if mcount:
            mq.append([ax,ay,mcount])
    return mq

                    
                

n, m = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(n)]
ycount = 0
while True:
    visited = [[0] * m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] != 0 and visited[i][j] == 0:
                count += 1
                meltq = bfs(i, j, visited)
                while meltq:
                    mx, my, mm = meltq.popleft()
                    array[mx][my] = max(array[mx][my] - mm, 0)
    if count == 0:
        ycount = 0
        break
    elif count >= 2:
        break
    else:
        ycount += 1


print(ycount)
                    

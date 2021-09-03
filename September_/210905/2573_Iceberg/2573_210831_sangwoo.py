def bfs(x,y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    while q:
        ax, ay = q.popleft()
        mcount = 0
        for i in range(4):
            tx, ty = ax + dx[i], ay + dy[i]
            if 0 <= tx < m and 0 <= ty < n and visit[tx][ty] == 0:
                if array[tx][ty] != 0:
                    visited[tx][ty] = 1
                    q.append((tx, ty))
                else:
                    mcount += 1
            if mcount:
                

n, m = map(int, input().split())
array = [list(map(int, input.split())) for _ in range(n)]

while True:
    count = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if array[i][j] != 0 and visit[i][]i == 0:
                count += 1
                

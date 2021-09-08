from collections import deque

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append([x,y])
    while q:
        x, y = q.popleft()
        for i in range(4):
           tx = x + dx[i]
           ty = y + dy[i]
           if 0 <= tx < n and 0 <= ty < n:
               if array[tx][ty] == array[x][y] and visit[tx][ty] == 0:
                   q.append([tx, ty])
                   visit[tx][ty] = 1

n = int(input())
array = [list(map(str, input())) for _ in range(n)]
visit = [[0] * n for _ in range(n)]
count = 0
mcount = 0

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i, j)
            count += 1

visit = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if array[i][j] == 'R':
            array[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i, j)
            mcount += 1

print(count, mcount)

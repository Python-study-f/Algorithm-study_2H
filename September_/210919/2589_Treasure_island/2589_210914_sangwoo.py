from collections import deque

def bfs(x, y):
    q = deque()
    q.append([x, y])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    plength = 0
    visitcount = [[0] * m for _ in range(n)]
    visitcount[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < n and 0 <= ty < m:
                if array[tx][ty] == 'L' and visitcount[tx][ty] == 0:
                    visitcount[tx][ty] = visitcount[x][y] + 1
                    plength = max(plength, visitcount[tx][ty])
                    q.append([tx, ty])
    return plength-1



n, m = map(int, input().split())
array = [list(map(str, input())) for _ in range(n)]
length = 0
for i in range(n):
    for j in range(m):
        if array[i][j] == 'L':
            length = max(length, bfs(i, j))
print(length)
            

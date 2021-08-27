from collections import deque

def bfs(pic, x,y):
    q = deque()
    q.append((x, y))
    count = 0
    while q:
        ax, ay = q.popleft()
        for i in range(4):
            tx, ty = ax + dx[i], ay + dy[i]
            if 0<= tx < m and 0<= ty < n:
                if picture[tx][ty] == pic and visited[tx][ty] != 1:
                    visited[tx][ty] = 1
                    q.append((tx, ty))
                    count += 1
    return count

# m, n = 6, 4
# picture =[[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]
visited = [[0 for _ in range(n)] for _ in range(m)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
maxarea = 0
num = 0
for i in range(m):
    for j in range(n):
        if visited[i][j] != 1 and picture[i][j] != 0:
            maxarea = max(bfs(picture[i][j], i, j), maxarea)
            num += 1

print("[{}, {}]".format(num, maxarea))


            




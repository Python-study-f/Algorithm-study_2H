from collections import deque

m,n = 6,4
picture = [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]
N, M = len(picture), len(picture[0])

for pic in picture:
    print(pic)

dx = [0,0,-1,1]
dy = [-1,1,0,0]
visited = [[0] * M for _ in range(N)]
max_area, tot = 0, 0

# 풀이1. DFS
def dfs(x,y,color):
    cnt = 1

    visited[x][y] = 1

    for i in range(4):
        nx,ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and picture[nx][ny] == color and  visited[nx][ny] != 1:
            cnt += dfs(nx,ny,color)

        else:
            continue

    return cnt

for i in range(N):
    for j in range(M):
        if picture[i][j] != 0 and not visited[i][j]:
            check = dfs(i,j,picture[i][j])
            tot += 1
            max_area = max(max_area, check)

print(max_area,tot)

# 풀이2. BFS
def bfs(x,y,color):
    cnt = 0
    q = deque()
    q.append((x,y))
    while q:
        tx, ty = q.popleft()

        for k in range(4):
            nx,ny = tx + dx[k], ty + dy[k]

            if 0 <= nx < N and 0 <= ny < M and picture[nx][ny] == color and visited[nx][ny] != 1:
                cnt += 1
                visited[nx][ny] = 1
                q.append((nx,ny))
    return cnt

for i in range(N):
    for j in range(M):
        if not visited[i][j] and picture[i][j] != 0:
            max_area = max(bfs(i,j,picture[i][j]),max_area)
            tot += 1

print(tot,max_area)
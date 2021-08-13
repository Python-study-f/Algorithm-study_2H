from collections import deque

n, m, fuel = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
start_x, start_y = map(int, input().split())
data = [list(map(int,input().split())) for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0

    while q:
        x1, y1 = q.popleft()

        for i in range(4):
            nx=x1+dx[i]
            ny=y1+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]!=1 and visited[nx][ny]==-1:
                visited[nx][ny] = visited[x1][y1]+1
                q.append((nx, ny))

    return visited


def order(visited, data):
    i = 0
    for p_x, p_y, a_x, a_y in data:
        data[i].append(visited[p_x - 1][p_y - 1])
        i += 1

    data.sort(key=lambda x: (-x[4], -x[0], -x[1]))


def solve(start_x, start_y):
    global fuel
    while data:
        visitied = bfs(start_x-1, start_y-1)
        order(visitied, data)
        s_x, s_y, e_x, e_y, dist = data.pop()

        for i in data:
            i.pop()

        visitied = bfs(s_x-1, s_y-1)
        dist2 = visitied[e_x-1][e_y-1]
        start_x, start_y = e_x, e_y

        if dist == -1 or dist2 == -1:
            print(-1)
            return

        fuel -= dist
        if fuel < 0:
            break

        fuel -= dist2
        if fuel < 0:
            break

        fuel += dist2 * 2

    if fuel < 0:
        print(-1)
    else:
        print(fuel)


solve(start_x, start_y)
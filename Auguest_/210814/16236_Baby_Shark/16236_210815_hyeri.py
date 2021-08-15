from collections import deque

N = int(input())
mp = [list(map(int, input().split())) for _ in range(N)]
sx, sy, sw, ss, dist = 0, 0, 2, 0, 0
fish = []
visit = [[0] * N for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(N):
        if mp[i][j] == 9:
            sx, sy = i, j
            mp[i][j] = 0
        elif mp[i][j] > 0:
            fish.append([i, j])


def bfs():
    global sw, sx, sy
    ret = 0
    for i in range(N):
        for j in range(N):
            visit[i][j] = 0
    dq = deque()
    dq.append([sx, sy])
    visit[sx][sy] = 1
    rx, ry = N, N
    ext = False  # 먹은 물고기가 있는 상태
    while dq:
        qn = len(dq)
        for k in range(qn):
            nk = dq.popleft()
            nx, ny = nk[0], nk[1]
            for i in range(4):
                tx, ty = nx + dx[i], ny + dy[i]
                if tx < 0 or tx >= N or ty < 0 or ty >= N:
                    continue
                if visit[tx][ty] == 0 and mp[tx][ty] <= sw:
                    if mp[tx][ty] != 0 and mp[tx][ty] < sw:
                        ext = True
                        if rx > tx:
                            rx, ry = tx, ty
                        elif rx == tx and ry > ty:
                            rx, ry = tx, ty
                        visit[tx][ty] = 1
                    else:
                        dq.append([tx, ty])
                        visit[tx][ty] = 1
        ret += 1
        if ext:
            break
    if not ext:
        return [0, [N, N]]
    mp[rx][ry] = 0
    return [ret, [rx, ry]]


while True:
    chk = True
    for i in range(len(fish)):
        if 0 < mp[fish[i][0]][fish[i][1]] < sw:
            chk = False
            break
    if chk:
        break
    s = bfs()
    if s[0] == 0:
        break
    dist += s[0]
    sx, sy = s[1][0], s[1][1]
    ss += 1
    if sw == ss:
        sw += 1
        ss = 0

print(dist)

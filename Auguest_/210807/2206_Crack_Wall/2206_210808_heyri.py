from collections import deque

N, M = map(int, input().split())
mp = [list(map(int, list(input()))) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    ret = 1
    dq = deque()
    dq.append([[0, 0], 2])
    visit = [([0] * M) for _ in range(N)]
    visit[0][0] = 1
    while dq:
        qn = len(dq)
        #print(dq, ret)
        for _ in range(qn):
            n = dq.popleft()
            nx = n[0][0]
            ny = n[0][1]
            nk = n[1]
            if nx == N - 1 and ny == M - 1:
                return ret
            for i in range(4):
                tx, ty = nx + dx[i], ny + dy[i]
                if 0 <= tx < N and 0 <= ty < M:
                    if mp[tx][ty] == 0:
                        if visit[tx][ty] == 0:
                            visit[tx][ty] = nk
                            dq.append([[tx, ty], nk])
                        elif nk == 2 and visit[tx][ty] == 1:
                            visit[tx][ty] = nk
                            dq.append([[tx, ty], nk])
                        else:
                            continue
                    elif nk == 2:
                        visit[tx][ty] = 1
                        dq.append([[tx, ty], 1])
                    else:
                        continue
        ret += 1
    return -1


print(bfs())

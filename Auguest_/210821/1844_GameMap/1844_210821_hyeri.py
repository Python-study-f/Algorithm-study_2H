# programmer - basic bfs 

from collections import deque
def solution(maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    N, M = len(maps), len(maps[0])
    visit = [[False]*M for _ in range(N)]
    dq = deque()
    dq.append([0, 0])
    visit[0][0] = 1
    ret = 1
    while dq:
        qs = len(dq)
        for _ in range(qs):
            nq = dq.popleft()
            for i in range(4):
                tx, ty = nq[0] + dx[i], nq[1] + dy[i]
                if 0 <= tx < N and 0 <= ty < M and maps[tx][ty] == 1:
                    if not visit[tx][ty]:
                        visit[tx][ty] = True
                        dq.append([tx, ty])
                        if tx == N-1 and ty == M-1:
                            return ret + 1
    
        ret += 1  
    return -1

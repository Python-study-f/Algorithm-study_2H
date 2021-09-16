from collections import deque

N, M = map(int, input().split())

tm = [input() for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
arr = []

for i in range(N):
    for j in range(M):
        if tm[i][j] == 'L':
            arr.append([i, j])


def bfs(x, y):
    visit = [[0] * M for _ in range(N)]
    dq = deque()
    dq.append([x, y])
    visit[x][y] = 1
    cnt = 0
    while dq:
        qn = len(dq)
        for k in range(qn):
            n = dq.popleft()
            for d in range(4):
                tx, ty = n[0] + dx[d], n[1] + dy[d]
                if 0 <= tx < N and 0 <= ty < M and tm[tx][ty] == 'L' and visit[tx][ty] == 0:
                    visit[tx][ty] = 1
                    dq.append([tx, ty])
        cnt += 1
    return cnt - 1


res = 0
for a in arr:
    res = max(res, bfs(a[0], a[1]))

print(res)

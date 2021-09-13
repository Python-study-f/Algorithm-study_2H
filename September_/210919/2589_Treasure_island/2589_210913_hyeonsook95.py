# python3 시간초과, pypy 통과
import sys, collections

input = sys.stdin.readline

R, C = map(int, input().split())
N, INF = 0, sys.maxsize

maps = []
lands = {}

for r in range(R):
    maps.append(input().strip())
    for c in range(C):
        if maps[-1][c] == "L":
            lands[(r, c)] = N
            N += 1

dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
dist = [[-1 for _ in range(N)] for _ in range(N)]


def bfs(start_v):
    dist = [-1 for _ in range(N)]
    dist[lands[start_v]] = 0
    queue = collections.deque([start_v])

    while queue:
        vr, vc = queue.popleft()
        for d in range(4):
            wr, wc = vr + dr[d], vc + dc[d]
            if -1 < wr < R and -1 < wc < C and maps[wr][wc] == "L":
                if dist[lands[(wr, wc)]] < 0:
                    dist[lands[(wr, wc)]] = dist[lands[(vr, vc)]] + 1
                    queue.append((wr, wc))
    return max(dist)


ans = -1
for v in lands.keys():
    ans = max(ans, bfs(v))
print(ans)

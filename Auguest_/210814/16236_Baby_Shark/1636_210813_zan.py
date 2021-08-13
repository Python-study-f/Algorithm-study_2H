import sys

input = sys.stdin.readline
import collections


def solution(N):
    m = []
    shk_r, shk_c, shk_s, cnt = 0, 0, 2, 0
    graph = collections.defaultdict(list)
    for _ in range(N):
        m.append(list(map(int, input().split())))

    for r in range(N):
        for c in range(N):
            # graph
            if r > 0:
                graph[(r, c)].append((r - 1, c))
            if c > 0:
                graph[(r, c)].append((r, c - 1))
            if c < N - 1:
                graph[(r, c)].append((r, c + 1))
            if r < N - 1:
                graph[(r, c)].append((r + 1, c))

            # 아기상어
            if m[r][c] == 9:
                shk_r, shk_c = r, c
                m[r][c] = 0

    def bfs(shk_r, shk_c, shk_s):
        visited = [[-1 for _ in range(N)] for _ in range(N)]
        queue = collections.deque([(shk_r, shk_c)])
        visited[shk_r][shk_c] = 0
        fishes = []

        while queue:
            v = queue.popleft()
            for r, c in graph[v]:
                if m[r][c] <= shk_s and visited[r][c] == -1:
                    visited[r][c] = visited[v[0]][v[1]] + 1
                    queue.append((r, c))
                    if 0 < m[r][c] < shk_s:
                        fishes.append((visited[r][c], r, c))
        return fishes

    times = []
    fishes = [(shk_r, shk_c)]
    while fishes:
        fishes = bfs(shk_r, shk_c, shk_s)
        if fishes:
            t, r, c = sorted(fishes)[0]
            m[r][c] = 0
            shk_r, shk_c = r, c
            cnt += 1
            if shk_s == cnt:
                cnt = 0
                shk_s += 1
            times.append(t)

    return sum(times)


print(solution(int(input().strip())))

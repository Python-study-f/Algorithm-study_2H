from collections import defaultdict, deque


def solution(maps):
    N, M = len(maps), len(maps[0])
    graph = defaultdict(list)
    for r in range(N):
        for c in range(M):

            if r > 0 and maps[r - 1][c] != 0:
                graph[(r, c)].append((r - 1, c))
            if c > 0 and maps[r][c - 1] != 0:
                graph[(r, c)].append((r, c - 1))
            if r < N - 1 and maps[r + 1][c] != 0:
                graph[(r, c)].append((r + 1, c))
            if c < M - 1 and maps[r][c + 1] != 0:
                graph[(r, c)].append((r, c + 1))

    def bfs(start_v):
        visited = [[0 for _ in range(M)] for _ in range(N)]
        visited[start_v[0]][start_v[1]] = 1
        queue = deque([start_v])

        while queue:
            vr, vc = queue.popleft()
            for wr, wc in graph[(vr, vc)]:
                if visited[wr][wc] == 0:
                    visited[wr][wc] = visited[vr][vc] + 1
                    queue.append((wr, wc))
        return visited[N - 1][M - 1]

    dist = bfs((0, 0))
    if dist == 0:
        return -1
    return dist

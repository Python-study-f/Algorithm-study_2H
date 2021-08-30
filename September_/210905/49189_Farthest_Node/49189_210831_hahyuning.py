from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    dist = [-1] * (n + 1)
    q = deque()
    q.append(1)
    dist[1] = 0

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + 1
                q.append(nxt)

    max_val = max(dist)
    ans = 0
    for x in dist:
        if x == max_val:
            ans += 1
    return ans

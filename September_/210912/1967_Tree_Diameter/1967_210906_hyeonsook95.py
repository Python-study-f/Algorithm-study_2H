import sys

sys.setrecursionlimit(100000000)

input = sys.stdin.readline
N = int(input().strip())
graph = [[] for _ in range(N + 1)]
dist = [-1 for _ in range(N + 1)]

for _ in range(N - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))


def dfs(node, time, visited):
    visited[node] = True

    children = []
    for v, w in graph[node]:
        if not visited[v]:
            d, visited = dfs(v, w, visited)
            children.append(d)

    if not children:
        children = [0]

    children = sorted(children, reverse=True)
    dist[node] = sum(children[:2])
    return max(children) + time, visited


visited = [False for _ in range(N + 1)]
dfs(1, 0, visited)

print(max(dist))

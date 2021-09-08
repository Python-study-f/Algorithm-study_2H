from collections import deque

def bfs(start):
    global ans
    dist = [-1] * (n + 1)
    q = deque()
    q.append(start)
    dist[start] = 0

    while q:
        now = q.popleft()
        for nxt, cost in graph[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + cost
                q.append(nxt)

    ans = max(ans, max(dist))

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

ans = 0
for i in range(1, n + 1):
    bfs(i)
print(ans)
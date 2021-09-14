import heapq

graph = [[] for _ in range(51)]
dist = [-1] * 51

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        cost, now = heapq.heappop(q)

        if dist[now] != -1 and dist[now] > cost:
            continue

        for nxt, nxt_cost in graph[now]:
            nxt_cost += cost

            if dist[nxt] == -1 or nxt_cost < dist[nxt]:
                dist[nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt))

def solution(N, road, K):
    for x in road:
        a, b, c = x
        graph[a].append((b, c))
        graph[b].append((a, c))

    dijkstra(1)

    ans = 0
    for i in range(1, N + 1):
        if dist[i] != -1 and dist[i] <= K:
            ans += 1
    return ans

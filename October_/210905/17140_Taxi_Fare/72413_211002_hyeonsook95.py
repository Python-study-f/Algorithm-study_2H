# 다익스트라
import heapq
from collections import defaultdict


def solution(n, s, a, b, fares):
    graph = defaultdict(list)

    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))

    def dyjkstra(K):
        Q = [(-1, K)]
        dist = defaultdict(list)

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        return dist

    answer = int(1e9)
    s_dist = dyjkstra(s)
    for node in range(1, n + 1):
        n_dist = dyjkstra(node)
        if s_dist[node] and n_dist[a] and n_dist[b]:
            answer = min(answer, s_dist[node] + n_dist[a] + n_dist[b] + 3)

    return answer


# https://programmers.co.kr/learn/courses/30/lessons/72413/solution_groups?language=python3
# 플로이드 와셜
def solution(n, s, a, b, fares):
    dp = [[int(1e9) for _ in range(n)] for _ in range(n)]

    for node in range(n):
        dp[node][node] = 0
    for u, v, w in fares:
        dp[u - 1][v - 1] = w
        dp[v - 1][u - 1] = w

    for k in range(n):
        for u in range(n):
            for v in range(n):
                if dp[u][v] > dp[u][k] + dp[k][v]:
                    dp[u][v] = dp[u][k] + dp[k][v]
    answer = int(1e9)
    for mid in range(n):
        answer = min(answer, dp[s - 1][mid] + dp[mid][a - 1] + dp[mid][b - 1])
    return answer


# 플로이드 와셜
from itertools import product


def solution(n, s, a, b, fares):
    dp = [[int(1e9) for _ in range(n)] for _ in range(n)]

    for node in range(n):
        dp[node][node] = 0
    for u, v, w in fares:
        dp[u - 1][v - 1] = dp[v - 1][u - 1] = w

    for k, u, v in product(range(n), repeat=3):
        if dp[u][v] > (w := dp[u][k] + dp[k][v]):
            dp[u][v] = w
    return min([dp[s - 1][k] + dp[k][a - 1] + dp[k][b - 1] for k in range(n)])

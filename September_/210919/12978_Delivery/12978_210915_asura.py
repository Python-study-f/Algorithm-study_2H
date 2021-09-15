"""
접근을 어떻게 했어?
1. 양방향 통행 => 다익스트라 느낌이
2. N개 마을 중 K 이하 => 전체를 돌려봐야 한다는 것이 다익스트라를 이용하면 간편할거라 생각함.
"""

import heapq


def solution(N, road, K):
    INF = int(1e9)
    data = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)

    for r in road: # 다익스트라 간선 저장. 양방향으로 체크
        a, b, wei = r
        data[a].append((b, wei))
        data[b].append((a, wei))

    def dijkstra(start): # 다익스트라 알고리즘
        q = []
        distance[start] = 0
        heapq.heappush(q, (0, start))

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for i in data[now]:
                cost = dist + i[1]

                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(1)

    return len([d for d in distance if d <= K])
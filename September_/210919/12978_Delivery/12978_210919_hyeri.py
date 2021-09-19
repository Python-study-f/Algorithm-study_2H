import heapq
import sys


def solution(N, road, K):
    answer = 0
    INF = int(1e9)

    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)

    for r in road:
        a, b, c = r
        graph[a].append((b, c))
        graph[b].append((a, c))

    def dijkstra():
        q = []
        heapq.heappush(q, (0, 1))
        distance[1] = 0

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue

            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            for i in graph[now]:
                cost = dist + i[1]
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[i[0]]:
                    heapq.heappush(q, (cost, i[0]))
                    distance[i[0]] = cost

    dijkstra()
    for d in range(N + 1):
        if distance[d] <= K:
            answer += 1
    return answer



# 참고 : https://velog.io/@postivegirl/ 개선된 다익스트라 알고리즘
# 그래프 최단 경로 문제 = 다익스트라

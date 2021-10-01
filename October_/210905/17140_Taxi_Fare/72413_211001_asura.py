# Z를 두 사람이 헤어질 장소라고 하고 A,B를 두 사람이 가야할 장소라고 하면,
# 요금 = 다익스트라(출발점, Z) + 다익스트라(Z, A) + 다익스트라 (Z, B) 이다.

import heapq
def solution(n, s, a, b, fares):
    def dijkstra(first, last):
        table = [INF for _ in range(n + 1)]  # 새 board판 생성
        table[first] = 0
        q = []
        heapq.heappush(q, (0, first))

        while q:
            weight, now = heapq.heappop(q)

            if table[now] < weight: continue

            for items in board[now]:
                nx, ncost = items
                ncost += weight

                if ncost < table[nx]:
                    table[nx] = ncost
                    heapq.heappush(q, (ncost, nx))

        return table[last]

    INF = int(1e9)
    ans = INF
    board = [[] for _ in range(n + 1)]

    for i in range(len(fares)):  # 입력
        start, end, wei = fares[i]
        board[start].append((end, wei))
        board[end].append((start, wei))

    for i in range(1, n + 1):
        ans = min(ans, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))

    return ans



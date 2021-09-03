import sys
from collections import deque

input = sys.stdin.readline


def solution(N, M):
    ice_berg = 0
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def count_ice_berg():
        cnt = 0
        ice_points = []
        visited = [[False for _ in range(M)] for _ in range(N)]
        for r in range(1, N - 1):
            for c in range(1, M - 1):
                if maps[r][c] > 0 and not visited[r][c]:
                    cnt += 1
                    visited[r][c] = True
                    ice_points.append((r, c))
                    queue = deque([(r, c)])
                    while queue:
                        vr, vc = queue.popleft()
                        for d in range(4):
                            wr, wc = vr + dr[d], vc + dc[d]
                            if 0 <= wr < N and 0 <= wc < M and maps[wr][wc] > 0:
                                if not visited[wr][wc]:
                                    visited[wr][wc] = True
                                    queue.append((wr, wc))
                                    ice_points.append((wr, wc))
        return cnt, ice_points

    def melt_ice_berg(ice_points):
        dis = False
        dis_ice_berg = {}
        visited = [[False for _ in range(M)] for _ in range(N)]
        for r, c in ice_points:
            if maps[r][c] > 0 and not visited[r][c]:
                amt = 0
                for d in range(4):
                    wr, wc = r + dr[d], c + dc[d]
                    if 0 <= wr < N and 0 <= wc < M and maps[wr][wc] == 0:
                        amt += 1

                if amt > 0:
                    dis_ice_berg[(r, c)] = amt

        for ice, amt in dis_ice_berg.items():
            ir, ic = ice
            maps[ir][ic] -= amt
            if maps[ir][ic] < 1:
                dis = True
                maps[ir][ic] = 0
        return dis

    ice_berg, ice_points = count_ice_berg()
    if ice_berg > 1:
        return 0

    y = 0
    while ice_berg > 0:
        y += 1
        dis = melt_ice_berg(ice_points)
        if dis:
            ice_berg, ice_points = count_ice_berg()
        if ice_berg > 1:
            return y
    return 0


N, M = map(int, input().split())
print(solution(N, M))

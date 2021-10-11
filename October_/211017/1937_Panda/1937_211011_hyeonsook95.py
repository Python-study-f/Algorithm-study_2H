# top down dfs + memorize
# 34%~36% 시간 초과
import sys


def solution(N):
    maps = [list(map(int, input().strip().split())) for _ in range(N)]
    dist = [[0 for _ in range(N)] for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def dfs(vr, vc, cnt):
        if cnt < dist[vr][vc]:
            return cnt

        dist[vr][vc] = cnt

        for d in range(4):
            wr, wc = vr + dr[d], vc + dc[d]
            if -1 < wr < N and -1 < wc < N:
                if maps[vr][vc] < maps[wr][wc]:
                    cnt = max(cnt, dfs(wr, wc, dist[vr][vc] + 1))
        return cnt

    count = -1
    for r in range(N):
        for c in range(N):
            if dist[r][c] == 0:
                count = max(count, dfs(r, c, 1))
    return count


# bottom up dfs + memorize
# 51140kb 864ms
import sys


def solution(N):
    maps = [list(map(int, input().strip().split())) for _ in range(N)]
    dist = [[0 for _ in range(N)] for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def dfs(vr, vc):
        if dist[vr][vc] > 0:
            return dist[vr][vc]

        dist[vr][vc] = 1

        for d in range(4):
            wr, wc = vr + dr[d], vc + dc[d]
            if -1 < wr < N and -1 < wc < N:
                if maps[vr][vc] < maps[wr][wc]:
                    dist[vr][vc] = max(dist[vr][vc], dfs(wr, wc) + 1)
        return dist[vr][vc]

    count = -1
    for r in range(N):
        for c in range(N):
            if dist[r][c] == 0:
                count = max(count, dfs(r, c))
    return dist


if __name__ == "__main__":
    sys.setrecursionlimit(30000)
    print(solution(int(input().strip())))

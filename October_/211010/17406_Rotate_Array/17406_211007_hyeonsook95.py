# 브루투 포스
# 29860kb 2228ms
from itertools import permutations
from copy import deepcopy


def solution(N, M, K):
    maps = [list(map(int, input().strip().split())) for _ in range(N)]
    rotations = [list(map(int, input().strip().split())) for _ in range(K)]

    dt = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def operation(map):
        ans = []
        for c in map:
            ans.append(sum(c))
        return min(ans)

    def rotate(SV, EV, map):
        sr, sc = SV
        er, ec = EV

        while abs(sr - er) != 0:
            r, c = sr, sc
            tmp, map[r][c] = map[r][c], map[r + 1][c]
            for mr, mc in dt:
                while True:
                    if sr <= r + mr <= er and sc <= c + mc <= ec:
                        r, c = r + mr, c + mc
                        tmp, map[r][c] = map[r][c], tmp
                    else:
                        break
            sr, sc = sr + 1, sc + 1
            er, ec = er - 1, ec - 1
        return map

    ans = []
    for rotation in permutations(rotations, len(rotations)):
        tmp = deepcopy(maps)
        for r, c, s in rotation:
            r, c = r - 1, c - 1
            tmp = rotate((r - s, c - s), (r + s, c + s), tmp)
        ans.append(operation(tmp))
    return min(ans)


# 브루투 포스
# 29860kb 652ms
def solution(N, _, K):
    maps = [list(map(int, input().strip().split())) for _ in range(N)]
    rotations = [list(map(int, input().strip().split())) for _ in range(K)]

    visited = [False] * K
    dt = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def rotate(omaps, vs):
        R, C, S = vs
        sr, sc = R - S - 1, C - S - 1
        er, ec = R + S - 1, C + S - 1
        cmaps = [column[:] for column in omaps]

        while abs(sr - er) != 0:
            r, c = sr, sc
            tmp, cmaps[r][c] = cmaps[r][c], cmaps[r + 1][c]
            for mr, mc in dt:
                while True:
                    if sr <= r + mr <= er and sc <= c + mc <= ec:
                        r, c = r + mr, c + mc
                        tmp, cmaps[r][c] = cmaps[r][c], tmp
                    else:
                        break
            sr, sc = sr + 1, sc + 1
            er, ec = er - 1, ec - 1
        return cmaps

    def dfs(cmaps, result):
        if sum(visited) == K:
            return min(result, min(map(sum, cmaps)))

        for k in range(K):
            if not visited[k]:
                visited[k] = True
                result = min(result, dfs(rotate(cmaps, rotations[k]), result))
                visited[k] = False
        return result

    return dfs(maps, int(1e9))


if __name__ == "__main__":
    N, M, K = map(int, input().strip().split())
    print(solution(N, M, K))


# 브루투포스 + dfs
# 29200kb 360ms
# https://www.acmicpc.net/source/32232515
def solution(N, _, K):
    maps = [list(map(int, input().strip().split())) for _ in range(N)]
    rotations = [tuple(map(int, input().strip().split())) for _ in range(K)]

    visited = [False] * K

    def rotate(cmaps, vs):
        nm = [column[:] for column in cmaps]
        R, C, S = vs

        for t in range(1, S + 1):
            sr, sc = R - t - 1, C - t - 1
            er, ec = R + t - 1, C + t - 1
            for c in range(sc + 1, ec + 1):
                nm[sr][c] = cmaps[sr][c - 1]
            for r in range(sr + 1, er + 1):
                nm[r][ec] = cmaps[r - 1][ec]
            for c in range(sc, ec):
                nm[er][c] = cmaps[er][c + 1]
            for r in range(sr, er):
                nm[r][sc] = cmaps[r + 1][sc]
        return nm

    def dfs(cmaps, result):
        if sum(visited) == K:
            return min(result, min(map(sum, cmaps)))

        for k in range(K):
            if not visited[k]:
                visited[k] = True
                result = min(result, dfs(rotate(cmaps, rotations[k]), result))
                visited[k] = False
        return result

    return dfs(maps, int(1e9))

from copy import deepcopy
from itertools import product

# pypy 1852ms
# python 4492ms
def solution(N, M):
    rotations = {
        1: list(range(4)),
        2: list(range(2)),
        3: list(range(4)),
        4: list(range(4)),
        5: list(range(1)),
    }
    # cctv 종류별 초기 방향 값
    directions = {
        1: [(0, 1)],
        2: [(0, 1), (0, -1)],
        3: [(-1, 0), (0, 1)],
        4: [(0, -1), (0, 1), (-1, 0)],
        5: [(0, 1), (0, -1), (1, 0), (-1, 0)],
    }

    amt = N * M
    maps = []
    cases, cctvs = [], []
    for r in range(N):
        maps.append(list(map(int, input().split())))

        for c in range(M):
            if maps[r][c] != 0:
                amt -= 1
            if 0 < maps[r][c] < 6:
                cctvs.append((maps[r][c], r, c))
                # cctv의 종류별로 의미있는 회전을 할 수 있는 경우를
                # 하나의 list로 cases에 추가
                cases.append(rotations[maps[r][c]])

    # 90도씩 회전시킨 방향값을 리턴하는 함수
    def rotate(loop, direction):
        if loop == 0:
            return direction

        for _ in range(loop):
            tmp = []
            for r, c in direction:
                if r != 0:
                    r *= -1
                r, c = c, r
                tmp.append((r, c))
            direction = tmp[::]
        return direction

    # 주어진 방향으로 #를 기록하고, 기록한 횟수를 반환
    def watch(tmp, r, c, direction):
        cnt = 0
        for mr, mc in direction:
            vr, vc = r + mr, c + mc
            while -1 < vr < N and -1 < vc < M and tmp[vr][vc] != 6:
                if tmp[vr][vc] == 0:
                    cnt += 1

                tmp[vr][vc] = -1
                vr, vc = vr + mr, vc + mc
        return cnt

    ans = 100
    # 모든 cctv들의 방향이 변할 수 있는 모든 경우의 수를 계산
    for case in product(*cases):
        cnt = 0  # '#'의 개수
        tmp = deepcopy(maps)
        for cctv, loop in zip(cctvs, case):
            typ, r, c = cctv  # cctv의 종류, 초기 위치 값
            # loop 만큼 cctv의 방향을 회전
            direction = rotate(loop, directions[typ])
            cnt += watch(tmp, r, c, direction)

        ans = min(ans, amt - cnt)
    return ans


# python 196ms
# https://www.acmicpc.net/source/33822999
def solution(N, M):
    UP, DOWN, LEFT, RIGHT = [-1, 0], [1, 0], [0, -1], [0, 1]
    DIRECTION = {
        1: [[UP], [DOWN], [LEFT], [RIGHT]],
        2: [[UP, DOWN], [LEFT, RIGHT]],
        3: [[RIGHT, UP], [RIGHT, DOWN], [LEFT, DOWN], [LEFT, UP]],
        4: [
            [UP, RIGHT, DOWN],
            [RIGHT, DOWN, LEFT],
            [DOWN, LEFT, UP],
            [UP, LEFT, RIGHT],
        ],
        5: [[UP, DOWN, LEFT, RIGHT]],
    }

    total = 0
    cases = []
    cctvs, maps = [], []
    for r in range(N):
        maps.append(list(map(int, input().split())))
        for c in range(M):
            if maps[r][c] == 0:
                total += 1
            elif 0 < maps[r][c] < 6:
                cases.append([])
                cctvs.append([maps[r][c], r, c])

    def detect(r, c, directions):
        cctv_case = []
        for direction in directions:
            case = set()
            for mr, mc in direction:
                vr, vc = r + mr, c + mc
                while -1 < vr < N and -1 < vc < M and maps[vr][vc] != 6:
                    if maps[vr][vc] == 0:
                        case.add((vr, vc))
                    vr, vc = vr + mr, vc + mc
            cctv_case.append(case)
        return cctv_case

    for idx, cctv in enumerate(cctvs):
        typ, r, c = cctv
        cases[idx] = detect(r, c, DIRECTION[typ])

    ans = 0
    for case in product(*cases):
        sum = set()
        for s in case:
            sum |= s
        ans = max(ans, len(list(sum)))
    return total - ans


if __name__ == "__main__":
    N, M = map(int, input().split())
    print(solution(N, M))

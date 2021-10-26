# pypy
def solution(R, C, M):
    maps = [[-1 for _ in range(C)] for _ in range(R)]
    sharks = []
    for idx in range(M):
        r, c, s, d, z = list(map(int, input().split()))

        # 상어별 기록
        sharks.append([r - 1, c - 1, s, d - 1, z])
        # 맵에 상어 표시
        maps[sharks[-1][0]][sharks[-1][1]] = idx

    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]

    def move(r, c, s, d, z):
        # 시간초과
        # https://www.acmicpc.net/board/view/51649
        m = s

        # 이동 좌표 계산
        while True:
            if d in [0, 1] and -1 < r + (m * dr[d]) < R:
                r = r + (m * dr[d])
                break
            elif d in [2, 3] and -1 < c + (m * dc[d]) < C:
                c = c + (m * dc[d])
                break

            if d == 0:
                d = 1
                m -= r
                r = 0
            elif d == 1:
                d = 0
                m -= R - 1 - r
                r = R - 1
            elif d == 2:
                d = 3
                m -= C - 1 - c
                c = C - 1
            elif d == 3:
                d = 2
                m -= c
                c = 0

        return [r, c, s, d, z]

    def update():
        # 상어 이동
        new_maps = [[[] for _ in range(C)] for _ in range(R)]
        for idx, shark in enumerate(sharks):
            if shark[-1] > 0:
                maps[shark[0]][shark[1]] = -1
                sharks[idx] = move(*shark)
                new_maps[sharks[idx][0]][sharks[idx][1]].append((-shark[-1], idx))
        # 상어 죽이기
        for r in range(R):
            for c in range(C):
                if new_maps[r][c]:
                    # 가장 큰 값을 maps에 넣음
                    maps[r][c] = sorted(new_maps[r][c])[0][1]
                    for _, idx in new_maps[r][c]:
                        if maps[r][c] != idx:
                            sharks[idx][-1] = -1
        return

    # 낚시왕 상어 낚시
    def fish(c):
        size = 0
        for r in range(R):
            if maps[r][c] > -1:
                size = sharks[maps[r][c]][-1]
                sharks[maps[r][c]][-1] = -1
                maps[r][c] = -1
                return size
        return size

    amt = 0
    for c in range(C):
        amt += fish(c)
        update()
    return amt


if __name__ == "__main__":
    R, C, M = map(int, input().split())
    print(solution(R, C, M))

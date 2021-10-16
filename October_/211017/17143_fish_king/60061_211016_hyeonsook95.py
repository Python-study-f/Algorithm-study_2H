# 시간 초과, 틀렸습니다.
def solution(R, C, M):
    maps = [[-1 for _ in range(C)] for _ in range(R)]
    alived = [True] * M
    sharks = []
    for idx in range(M):
        r, c, s, d, z = list(map(int, input().split()))

        sharks.append([r - 1, c - 1, s, d - 1, z])
        maps[sharks[-1][0]][sharks[-1][1]] = idx

    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]

    def move(shark):
        r, c, s, d, z = shark
        # 시간초과
        # https://www.acmicpc.net/board/view/51649
        for _ in range(s):
            wr, wc = r + dr[d], c + dc[d]
            if (wr < 0 or wr >= R) or (wc < 0 or wc >= C):
                # 방향 전환
                d += 1 if d in [0, 2] else -1
                wr, wc = r + dr[d], c + dc[d]
            r, c = wr, wc

        return [r, c, s, d, z]

    def update():
        for idx, shark in enumerate(sharks):
            if alived[idx]:
                maps[shark[0]][shark[1]] = -1

                sharks[idx] = move(shark)
                r, c, s, d, z = sharks[idx]
                # 틀렸습니다.
                if maps[r][c] > -1:
                    if sharks[maps[r][c]][-1] < z:
                        alived[maps[r][c]] = False
                        maps[r][c] = idx
                    else:
                        alived[idx] = False
                else:
                    maps[r][c] = idx
        return

    def fish(c):
        size = 0
        for r in range(R):
            if maps[r][c] > -1:
                size = sharks[maps[r][c]][-1]
                alived[maps[r][c]] = False
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

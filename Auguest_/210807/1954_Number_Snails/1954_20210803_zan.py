# 1954. 달팽이 숫자

# 1 부터 N*N 까지의 숫자가 시계방향으로 이루어져 있다.
# 정수 N을 입력받아 N 크기의 달팽이를 출력하라.

# 입력
# T, 테스트 케이스 수
# N, 1 <= N <= 10

# 출력
# #t 로 시작, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력
# t는 1부터 시작

"""
# 이동 패턴: n -> n-1 -> n-1 -> n-2 -> n-2 -> ...
# scope와 count로 이동 패턴을 맞춤.
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    snail = [[0 for _ in range(N)] for _ in range(N)]

    num = 0
    count, scope = N, 1
    direction = 0
    r, c = 0, -1
    while num < N ** 2:
        for _scp in range(scope):
            for _cnt in range(count):
                if direction == 0:
                    c += 1
                elif direction == 1:
                    r += 1
                elif direction == 2:
                    c -= 1
                elif direction == 3:
                    r -= 1
                num += 1
                snail[r][c] = num
            direction = 0 if direction > 2 else direction + 1
        scope = 2
        count -= 1

    print(f"#{tc}")
    for r in range(len(snail)):
        print(" ".join(map(str, snail[r])))
"""
# REF https://itzjamie96.github.io/2020/11/18/swea-python-1954/
T = int(input())
#    R, D, L, U
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N = int(input())
    snail = [[0 for _ in range(N)] for _ in range(N)]

    x, y = 0, -1
    d = 0
    num = 0
    while num < N * N:

        if (
            -1 < x + dx[d % 4] < N  # 이동할 x 값이 -1 보다 크고, N 보다 작을 경우
            and -1 < y + dy[d % 4] < N  # 이동할 y 값이 -1 보다 크고, N 보다 작을 경우
            and snail[x + dx[d % 4]][y + dy[d % 4]] == 0  # 이동할 snail의 값이 초기화된 값일 경우
        ):
            x = x + dx[d % 4]
            y = y + dy[d % 4]
            num += 1
            snail[x][y] = num
        else:
            d += 1
    print(f"#{tc}")
    for x in range(len(snail)):
        print(*snail[x])

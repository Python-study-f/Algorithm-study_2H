# 1. y 번 원판을 d 방향으로 k 만큼 회전시키는 함수
def rotate(y, d, k):
    if d == 0:
        a[y] = a[y][-k:] + a[y][:-k]
    else:
        a[y] = a[y][k:] + a[y][:k]

# 2. 인접한 수를 확인하고 지우는 함수
# 더 이상 지울 숫자가 없으면 false 리턴
def check():
    # 인접한 수와 같은지 기록
    d = [[False] * m for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(m):
            # 이미 지워진 경우
            if a[i][j] == 0:
                continue

            # 같은 원판 내에서 검사
            if a[i][j] == a[i][(j + 1) % m]:
                d[i][j] = True
                d[i][(j + 1) % m] = True

            # 다른 원판 들과 검사
            if i + 1 <= n and a[i][j] == a[i + 1][j]:
                d[i][j] = True
                d[i + 1][j] = True

    flg = False
    for i in range(1, n + 1):
        for j in range(m):
            if d[i][j] == True:
                flg = True
                a[i][j] = 0
    return flg

# 지울 수 없는 경우 평균을 구해서 숫자를 조정하는 함수
def mean():
    total = 0
    cnt = 0

    for i in range(1, n + 1):
        for j in range(m):
            if a[i][j] != 0:
                total += a[i][j]
                cnt += 1

    # 모든 숫자가 0인 경우
    if cnt == 0:
        return

    for i in range(1, n + 1):
        for j in range(m):
            if a[i][j] != 0:
                # 평균보다 큰 경우
                if total // cnt < a[i][j]:
                    a[i][j] -= 1
                # 평균보다 작은 경우
                elif total // cnt > a[i][j]:
                    a[i][j] += 1

n, m, t = map(int, input().split())
a = [[]] + [list(map(int, input().split())) for _ in range(n)]

for _ in range(t):
    x, d, k = map(int, input().split())
    # x 의 배수인 원판을 d 방향으로 k 칸 회전
    for y in range(x, n + 1, x):
        rotate(y, d, k)

    # 원판에 수가 남아있는지 확인
    if check() == False:
        # 수가 남아있지 않는 경우 평균 구하기
        mean()

ans = 0
for i in range(1, n + 1):
    for j in range(m):
        ans += a[i][j]
print(ans)
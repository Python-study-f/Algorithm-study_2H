# 1. pan_no 번 원판을 direction 방향으로 k 만큼 회전시키는 함수
def rotate(pan_no, direction, k):
    if direction == 0:
        a[pan_no] = a[pan_no][-k:] + a[pan_no][:-k]
    else:
        a[pan_no] = a[pan_no][k:] + a[pan_no][:k]


def duplication_check():
    count = 0
    copy_arr = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            check_num = a[i][j]
            right = a[i][(j + 1) % m]
            if i != n - 1:
                bottom = a[i + 1][j]
            else:
                bottom = 0
            if check_num != 0:
                if check_num == bottom:
                    copy_arr[i][j] = True
                    copy_arr[i + 1][j] = True
                    # a[i][j] = 0
                    # a[i + 1][j] = 0
                    count += 1
                elif check_num == right:
                    copy_arr[i][j] = True
                    copy_arr[i][(j + 1)%m] = True
                    # a[i][j] = 0
                    # a[i][j + 1] = 0
                    count += 1

    for i in range(0, n):
        for j in range(m):
            if copy_arr[i][j]:
                a[i][j] = 0
    return count > 0


def mean():
    total, count = get_total_info()
    mean = total / count

    for i in range(n):
        for j in range(m):
            if a[i][j] != 0:
                if mean < a[i][j]:
                    a[i][j] = a[i][j] - 1
                elif mean > a[i][j]:
                    a[i][j] = a[i][j] + 1


def get_total_info():
    total = 0
    count = 0
    for i in range(n):
        for j in range(m):
            total += a[i][j]
            if a[i][j] != 0:
                count += 1
    return total, count


n, m, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 판 방향바꿔놓기
for _ in range(t):
    x, direction, k = map(int, input().split())
    # x 의 배수인 원판을 direction 방향으로 k 칸 회전
    for y in range(x, n + 1, x):
        rotate(y - 1, direction, k)

    if not duplication_check():
        mean()

ans = 0
for i in range(n):
    for j in range(m):
        ans += a[i][j]
print(ans)

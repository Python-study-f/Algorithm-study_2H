from collections import defaultdict
import sys

r, c, k = map(int, input().split())
r -= 1
c -= 1

# a[r][c] = k 가 되는 최소 시간 구하기
a = [[0] * 100 for _ in range(100)]
for i in range(3):
    tmp = list(map(int, input().split()))
    for j in range(3):
        a[i][j] = tmp[j]

if a[r][c] == k:
    print(0)
    sys.exit(0)

n = 3
m = 3
for t in range(1, 101):
    # 행이 열보다 크거나 같은 경우 R 연산 수행
    if n >= m:
        new_m = m # 바뀌는 열의 갯수

        # 등장 횟수 기록
        for i in range(n):
            d = defaultdict(int)
            for j in range(n):
                if a[i][j] != 0:
                    d[a[i][j]] += 1

            # 정렬
            b = []
            for key, val in d.items():
                b.append((val, key))
            b.sort()

            # 배열의 길이는 최대 100
            limit = min(len(b), 50)
            for j in range(limit):
                a[i][j * 2] = b[j][1]
                a[i][j * 2 + 1] = b[j][0]

            for j in range(limit * 2, 100):
                a[i][j] = 0

            new_m = max(len(b) * 2, new_m)
        m = new_m
    else:
        new_n = n

        # 등장 횟수 기록
        for j in range(m):
            d = defaultdict(int)
            for i in range(m):
                if a[i][j] != 0:
                    d[a[i][j]] += 1

            # 정렬
            b = []
            for key, val in d.items():
                b.append((val, key))
            b.sort()

            # 배열의 길이는 최대 100
            limit = min(len(b), 50)
            for i in range(limit):
                a[i * 2][j] = b[i][1]
                a[i * 2 + 1][j] = b[i][0]
            for i in range(limit * 2, 100):
                a[i][j] = 0

            new_n = max(len(b) * 2, new_n)
        n = new_n

    if a[r][c] == k:
        print(t)
        sys.exit(0)
print(-1)
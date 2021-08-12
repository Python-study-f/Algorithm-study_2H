n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# d[i][j]: a[i][j]에 도착했을 때 가져올 수 있는 사탕의 최대 개수
d = [[0] * m for _ in range(n)]
tmp = 0
for i in range(m):
    tmp += a[0][i]
    d[0][i] = tmp

tmp = 0
for i in range(n):
    tmp += a[i][0]
    d[i][0] = tmp

for i in range(1, n):
    for j in range(1, m):
        d[i][j] = max(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + a[i][j]

print(d[n - 1][m - 1])
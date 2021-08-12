# N*M 크기에 준규가 갇혀있다. 각 방에는 사탕이 놓여져 있다.
# 준규는 (1,1)에 있고, (N, M)으로 이동하려 한다. 각 방을 방문할 때마다 방에 놓여져 있는 사탕을 모두 가져갈 수 있다.
# 준규가 (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수의 최댓값을 구하라.

# 입력
# 1 <= N, M <= 1,000

# https://pacific-ocean.tistory.com/204
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
dp = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = s[i - 1][j - 1] + max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
print(dp[n][m])

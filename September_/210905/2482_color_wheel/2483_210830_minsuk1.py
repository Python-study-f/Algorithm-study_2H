mod = 1000000003
n = int(input())
k = int(input())
dp = [[0]*(1002) for _ in range(1002)]
for i in range(n+1):
    dp[i][1] = i
 #   dp[i][0] = 1
for i in range(2, n+1):
    for j in range(2, k+1):
        if i == n:
            dp[i][j] = dp[i-3][j-1] + dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] + dp[i-2][j-1]
        dp[i][j] %= mod
print(dp[n][k])
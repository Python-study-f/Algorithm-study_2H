N, M = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(M+1) for _ in range(N+1)]

dp[1][1] = mp[0][0]


for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i][j], dp[i-1][j]+mp[i-1][j-1], dp[i][j-1]+mp[i-1][j-1], dp[i-1][j-1]+mp[i-1][j-1])


print(dp[N][M])

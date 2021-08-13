n, m = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        current_candy = maze[i - 1][j - 1]
        dp[i][j] = max(
            dp[i - 1][j - 1] + current_candy,
            dp[i - 1][j] + current_candy,
            dp[i][j - 1] + current_candy,
        )

print(dp[n][m])

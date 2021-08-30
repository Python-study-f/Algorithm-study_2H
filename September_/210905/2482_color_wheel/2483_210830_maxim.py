mod = 1000000003
n = int(input())
k = int(input())
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]


def color_comb(n, k):
    if n / k == 2:
        return 2
    elif k == 1:
        return n
    elif dp[n][k] == 0:
        dp[n][k] = color_comb(n - 1, k) + color_comb(n - 2, k - 1)

    return dp[n][k]


if n / 2 < k:
    print(0)
else:
    print(color_comb(n, k) % mod)

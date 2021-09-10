TC = int(input())
for tc in range(1, TC + 1):
    day, month, months, year = map(int, input().split())
    plan = list(map(int, input().split()))
    dp = [0] * 12
    for idx in range(len(plan)):
        if plan[idx] == 0:
            dp[idx] = dp[idx - 1]
            continue

        dp[idx] = dp[idx - 1] + min(day * plan[idx], month)

        if idx < 3:
            dp[idx] = min(dp[idx], months)
        else:
            dp[idx] = min(dp[idx], dp[idx - 3] + months)

    dp[-1] = min(dp[-1], year, min(dp[-3:]) + months)
    print(f"#{tc} {dp[-1]}")

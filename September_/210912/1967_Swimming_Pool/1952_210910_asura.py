T = int(input())

for tc in range(1,T+1):
    dp = [0 for _ in range(12)]
    data = list(map(int,input().split()))
    month = list(map(int,input().split()))

    dp[0] = min(month[0] * data[0] , data[1])  # 1월
    dp[1] = dp[0] + min(data[0]*month[1], data[1]) # 2월

    for i in range(2,12): # 3월부터 12월까지
        dp[i] = min( dp[i-1] + data[0]*month[i], dp[i-1] + data[1], dp[i-3] + data[2])

    # 마지막 12월 비교
    dp[11] = min(dp[11], data[3])

    print("#{} {}".format(tc,dp[11]))

T = int(input())

for test_case in range(1, T+1):
    data = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    dp = [0]*13
    dp[1] = min(data[2], data[1], plan[0]*data[0])
    dp[2] = min(data[2], data[1]+dp[1], plan[1]*data[0]+dp[1])
    
    for i in range(3, 13):
        dp[i] = min(data[2]+dp[i-3], data[1]+dp[i-1], plan[i-1]*data[0]+dp[i-1])
    
    dp[12] = min(data[3], dp[12])
    
    print("#{} {}".format(test_case, dp[12]))

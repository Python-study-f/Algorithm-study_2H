N = int(input())
data = [0] * 10000
for i in range(N):
    data[i] = int(input())

dp = [0] * 10000 # 전체 테이블 생성
dp[0] = data[0]
dp[1] = data[0] + data[1] # 1
dp[2] = max(dp[1], data[2] + data[0], data[2] + data[1]) # 2

for i in range(3,N): # 점화식
    dp[i] = max(dp[i-1],data[i] + data[i-1] + dp[i-3], data[i] + dp[i-2])

print(max(dp))


"""
1. 마시지 않거나,
2. 지금꺼 마시고, 전전꺼 total 마시거나
3. 지금꺼 마시고, 전에꺼 마시고, 전전전꺼 total 마시고
"""


n = int(input())
data = [0]
for i in range(n):
    data.append(int(input()))
dp = [0]
dp.append(data[1])
if n > 1:
    dp.append(max(data[1] + data[2], data[0]+data[2]))
for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + data[i - 1] + data[i], dp[i - 2] + data[i]))
print(dp[n])
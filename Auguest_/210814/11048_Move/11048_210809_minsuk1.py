n,m=map(int,input().split())
dp = []
for _ in range(n):
    dp.append(list(map(int,input().split())))
    
for i in range(n):
    for j in range(m):
        #위에서 옴
        if i==0:
            up=0
        else:
            up=dp[i-1][j]

        #왼쪽에서 옴
        if j==0:
            left =0 
        else:
            left = dp[i][j-1]

        #대각선에서 옴
        if i == 0 or j==0:
            left_down = 0
        else:
            left_down = dp[i-1][j-1]
            
        dp[i][j] = dp[i][j] + max(up,left,left_down)
        
        
print(dp[n-1][m-1])
from copy import deepcopy

class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        banned = {tuple(mine) for mine in mines}            
        dp = [[0] * N for _ in range(N)]
        
        for i in range(N):
            cnt = 0
            for j in range(N):
                if (i,j) in banned:
                    cnt = 0
                else:
                    cnt += 1
                dp[i][j] = cnt
            cnt = 0
            for j in range(N-1, -1, -1):
                if (i,j) in banned:
                    cnt = 0
                else:
                    cnt += 1
                if cnt < dp[i][j]: 
                    dp[i][j] = cnt
                    
        for j in range(N):
            cnt = 0
            for i in range(N):
                if (i,j) in banned:
                    cnt = 0
                else:
                    cnt += 1
                if cnt < dp[i][j]: 
                    dp[i][j] = cnt
            cnt = 0
            for i in range(N-1, -1, -1):
                if (i,j) in banned:
                    cnt = 0
                else:
                    cnt += 1
                if cnt < dp[i][j]: 
                    dp[i][j] = cnt
                    
        answer = 0
        for i in range(N):
            for j in range(N):
                answer = max(answer, dp[i][j])

        return answer

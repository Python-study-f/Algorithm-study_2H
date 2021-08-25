from collections import deque


# dfs/bfs 구현하다 아래 or 오른쪽으로만 이동할 수 있다는 것을 보고 DP로 바꿈
# 문제 잘 읽어봐야 한다는걸 배움..

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        N, M = len(obstacleGrid), len(obstacleGrid[0])  # N,M 설정

        if obstacleGrid[0][0] == 0 and N == 1 and M == 1:
            return 1

        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        dp = [[0] * (len(obstacleGrid[0]) + 1) for _ in range(len(obstacleGrid) + 1)]
        dp[1][1] = 1

        for i in range(1, N + 1):
            for j in range(1, M + 1):

                if i == 1 and j == 1:
                    continue

                if obstacleGrid[i - 1][j - 1] == 1:
                    continue

                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
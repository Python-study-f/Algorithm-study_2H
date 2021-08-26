class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        visit = [[0]*(n+1) for _ in range(m+1)]
        visit[1][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1] == 1:
                    continue
                visit[i][j] += visit[i-1][j]
                visit[i][j] += visit[i][j-1]

        return visit[m][n]

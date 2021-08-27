class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        obstacleGrid[0][0] == 1
        
        state = 0
        for i in range(1, m):
            if obstacleGrid[i][0] == 0 and state == 0:
                obstacleGrid[i][0] = 1
            else:
                state += 1
                obstacleGrid[i][0] = 0
                
        state = 0
        for j in range(1,n):
            if obstacleGrid[0][j] == 0 and state == 0:
                obstacleGrid[0][j] = 1
            else:
                state += 1
                obstacleGrid[0][j] = 0
                
        for k in range(1,m):
            for t in range(1,n):
                if obstacleGrid[k][t] == 1:
                    obstacleGrid[k][t] = 0
                else:
                    obstacleGrid[k][t] = obstacleGrid[k-1][t] + obstacleGrid[k][t-1]
        
        return obstacleGrid[-1][-1]
                
        

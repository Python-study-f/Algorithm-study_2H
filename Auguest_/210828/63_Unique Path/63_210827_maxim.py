class Solution:
    def uniquePathsWithObstacles(self, m, n):
        area = [n][m]
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    area[i][j] = 1
                else:
                    area[i][j] = area[i - 1][j] + area[i][j - 1]

        return area[n - 1][m - 1]

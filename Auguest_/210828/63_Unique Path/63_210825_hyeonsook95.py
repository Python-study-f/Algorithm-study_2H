from typing import List

# 시간초과
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dr, dc = [1, 0], [0, 1]

        def dfs(start_v=(0, 0)):
            stack = [start_v]
            cnt = 0

            while stack:
                vr, vc = stack.pop()
                if 0 <= vr < M and 0 <= vc < N and obstacleGrid[vr][vc] != 1:
                    if (vr, vc) == (M - 1, N - 1):
                        cnt += 1
                    else:
                        for mv, mc in zip(dr, dc):
                            wr, wc = vr + mv, vc + mc
                            stack.append((wr, wc))
            return cnt

        return dfs()


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
sol = Solution()
print(sol.uniquePathsWithObstacles(obstacleGrid))

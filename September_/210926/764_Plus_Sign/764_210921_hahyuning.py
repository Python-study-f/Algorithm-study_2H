from copy import deepcopy


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:

        if len(mines) == n ** 2:
            return 0

        a = [[1] * n for _ in range(n)]

        for i in range(len(mines)):
            a[mines[i][0]][mines[i][1]] = 0

        left = deepcopy(a)
        right = deepcopy(a)
        up = deepcopy(a)
        down = deepcopy(a)

        for i in range(n):
            for j in range(n - 2, -1, -1):
                if a[i][j] == 1:
                    left[i][j] = left[i][j + 1] + 1
            for j in range(1, n):
                if a[i][j] == 1:
                    right[i][j] = right[i][j - 1] + 1

        for j in range(n):
            for i in range(1, n):
                if a[i][j] == 1:
                    down[i][j] = down[i - 1][j] + 1
            for i in range(n - 2, -1, -1):
                if a[i][j] == 1:
                    up[i][j] = up[i + 1][j] + 1

        ans = 1
        for i in range(n):
            for j in range(n):
                if a[i][j] == 1:
                    ans = max(ans, min(left[i][j], right[i][j], up[i][j], down[i][j]))

        return ans
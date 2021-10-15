class Solution:
    def maxCoins(self, nums) -> int:
        def top_down(i, j):
            if i == j:
                d[i][j] = 0
                return d[i][j]

            tmp = 0
            for k in range(i + 1, j):
                if d[i][k] == -1:
                    top_down(i, k)
                if d[k][j] == -1:
                    top_down(k, j)
                tmp = max(tmp, nums[i] * nums[k] * nums[j] + d[i][k] + d[k][j])
            d[i][j] = tmp

            return d[i][j]

        nums = [1] + nums + [1]
        n = len(nums)
        d = [[-1] * n for _ in range(n)]

        return top_down(0, n - 1)
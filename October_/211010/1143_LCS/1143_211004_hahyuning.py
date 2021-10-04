class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        text1 = " " + text1
        text2 = " " + text2

        # d[i][j]: text1이 i까지 text2가 j까지 있을 때 LCS 길이
        d = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i] == text2[j]:
                    d[i][j] = d[i - 1][j - 1] + 1
                else:
                    d[i][j] = max(d[i - 1][j], d[i][j - 1])

        return d[n][m]
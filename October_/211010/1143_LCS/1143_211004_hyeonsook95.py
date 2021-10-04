# dp
# 22.8mb 805ms
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1) + 1, len(text2) + 1
        dp = [[0 for _ in range(N)] for _ in range(M)]
        for r in range(1, M):
            for c in range(1, N):
                if text1[c - 1] == text2[r - 1]:
                    dp[r][c] = dp[r - 1][c - 1] + 1
                else:
                    dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])
        return dp[-1][-1]


# dp
# 14.2mb 332ms
# https://leetcode.com/problems/longest-common-subsequence/discuss/1497846/Python-A-bit-scary-one-liner
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)
        for char1 in text1:
            cnt = 0
            for idx, char2 in enumerate(text2):
                # cnt == text1[index(char1)-1]에서 text2[idx-1]
                dp[idx], cnt = (
                    cnt + 1 if char1 == char2 else max(dp[idx - 1], dp[idx]),
                    dp[idx],
                )
        return dp[-2]


# dp
# 14.2mb 300ms
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)
        for char1 in text1:
            cnt = 0
            for idx, char2 in enumerate(text2):
                if char1 == char2:
                    dp[idx], cnt = cnt + 1, dp[idx]
                else:
                    dp[idx], cnt = max(dp[idx - 1], dp[idx]), dp[idx]
                """
                # 14.3mb 387ms
                tmp = dp[idx]
                if char1 == char2:
                    dp[idx] = cnt + 1
                else:
                    dp[idx] = max(dp[idx - 1], dp[idx])
                cnt = tmp
                """

        return dp[-2]


# Recursive
# 141.6mb 728ms
# https://leetcode.com/problems/longest-common-subsequence/discuss/350993/Python-dp-and-recursive
import functools


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @funtools.lru_cache(None)
        def recursiveCommon(i, j):
            # 어느 한 쪽 text라도 비교할 문자가 없을 경우
            if i < 0 or j < 0:
                return 0

            if text1[i] == text2[j]:
                return recursiveCommon(i - 1, j - 1) + 1
            return max(recursiveCommon(i - 1, j), recursiveCommon(i, j - 1))

        return recursiveCommon(len(text1) - 1, len(text2) - 1)


# bfs
# 619.5mb 3396ms
# https://leetcode.com/problems/longest-common-subsequence/discuss/465365/Python-BFS-Solution
from collections import deque


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ans = int(-1e9)
        visited = set()
        queue = deque([(text1, text2, 0)])
        while queue:
            str1, str2, count = queue.popleft()
            ans = max(ans, count)
            if str1 and str2 and (str1, str2) not in visited:
                visited.add((str1, str2))
                if str1[0] == str2[0]:
                    queue.append((str1[1:], str2[1:], count + 1))
                else:
                    queue.append((str1[1:], str2, count))
                    queue.append((str1, str2[1:], count))
        return ans

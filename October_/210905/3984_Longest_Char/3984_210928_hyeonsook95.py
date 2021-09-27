from typing import List
from itertools import combinations


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        cnt = 0
        for n in range(len(arr)):
            for sentences in combinations(arr, n + 1):
                tmp = ""
                for sentence in sentences:
                    tmp += sentence
                if len(tmp) == len(set(tmp)):
                    cnt = max(cnt, len(tmp))
        return cnt

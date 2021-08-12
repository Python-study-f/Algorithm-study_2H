# 11. Container with most water

# 음이 아닌 정수들 a1, a2,...,an n개 주어진다.
# n개의 수직선은 (i, a1)-(i, 0)으로 그려진다.
# x 축과 함께 두 개의 라인으로 컨테이너를 만들 때, 물이 가장 많이 들어갈 수 있는 두 개의 라인을 찾아라.

# 입력
# height: List, 0 <= height[i] <= 100000
# n = len(height), 2 <= n <= 1000000

from typing import List

# Brute Force
# Time Limit Exceeded
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for start in range(len(height) - 1):
            for end in range(start + 1, len(height)):
                w = end - start
                h = min(height[start], height[end])
                max_area = max(max_area, w * h)
        return max_area


# Two Point, Greedy
class Solution2:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        start, end = 0, len(height) - 1
        while start < end:
            w = end - start
            h = min(height[start], height[end])
            max_area = max(max_area, w * h)
            # 다음 width에 대해 더 작은 값을 이동시키면
            # 최적의 height가 됨.
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return max_area

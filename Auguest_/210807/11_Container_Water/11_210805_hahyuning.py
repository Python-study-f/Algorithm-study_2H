# n = 10 ** 5 -> O(n)으로 풀이 (투포인터)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        lt = 0
        rt = len(height) - 1

        ans = 0
        while lt < rt:
            # 양쪽 중 더 작은쪽의 높이로 고인 물의 양 계산 후 최대값 갱신
            min_height = min(height[lt], height[rt])
            ans = max(ans, min_height * (rt - lt))

            # 더 낮은쪽 위치 변경
            if height[lt] < height[rt]:
                lt += 1
            else:
                rt -= 1
        return ans
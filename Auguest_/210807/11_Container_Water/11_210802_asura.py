# 풀이 1 - Brute Force
# 가장 기본적인 접근법. 역시 TLE
# 시간 복잡도 : O(n^2)
"""
class Solution(object):
    def maxArea(self, height):
        max_area = 0

        for i in range(len(height)):
            for j in range(i+1,len(height)):
                a,b,vertical = height[i], height[j] , j-i

                cur_area = min(a,b) * vertical
                max_area = max(max_area,cur_area)

        return max_area
"""

# 풀이 2 - Two Point 접근
# O(N) 방식으로, Brute Force 보다 시간을 덜 잡아 먹음

class Solution(object):
    def maxArea(self, height):
        max_area = 0
        ldx, rdx = 0, len(height) - 1

        while ldx < rdx:
            cur_area = (rdx - ldx) * min(height[ldx], height[rdx])
            max_area = max(max_area, cur_area)

            if height[ldx] > height[rdx]:
                rdx -= 1
            else:
                ldx += 1

        return max_area



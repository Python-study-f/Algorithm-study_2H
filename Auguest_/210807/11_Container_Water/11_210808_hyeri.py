class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        l,r = 0, len(height)-1
        while l < r:
            s = (r - l) * min(height[l], height[r])
            answer = max(answer, s)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return answer
        
        

class Solution(object):
    def maxArea(self, height):
        start=0; end=len(height)-1
        ans=0
        while start<end:
            a=end-start; b=min(height[start],height[end])
            ans=max(ans,a*b)

            if height[start]<=height[end]:
                start+=1
            else:
                end-=1
        return ans
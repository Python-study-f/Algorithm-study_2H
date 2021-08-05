class Solution(object):
    def maxArea(self, height):
        # 초기 최대값을 리스트 양끝의 2개의 숫자의 크기로 지정
        pointer1 = 0
        pointer2 = len(height) - 1
        max_Area = (len(height) - 1) * min(height[pointer1], height[pointer2])
        
        # 높이로 지정된 값들을 차례로 하나씩 욺겨가며 넓이를 비교
        for i in range(len(height) - 1):
            width = len(height) - (i + 2) # 가로의 길이를 먼저 계산
            
            # 왼쪽이 오른쪽 보다 작을 경우 
            if height[pointer1] < height[pointer2]:
                # 왼쪽의 포인터를 한칸 오른쪽으로 이동한 후 넓이를 계산하여 원래값과 비교해 큰 값을 저장
                pointer1 += 1
                temp_Area = width * min(height[pointer1], height[pointer2])
                if temp_Area > max_Area:
                    max_Area = temp_Area
                    
            # 오른쪽이 왼쪽보다 작을 경우        
            elif height[pointer1] >= height[pointer2]:
                # 오른쪽의 포인터를 한칸 왼쪽으로 이동한 후 넓이를 계산하여 원래값과 비교해 큰 값을 저장
                pointer2 -= 1
                temp_Area = width * min(height[pointer1], height[pointer2])
                if temp_Area > max_Area:
                    max_Area = temp_Area
        
        return(max_Area)
                    
        

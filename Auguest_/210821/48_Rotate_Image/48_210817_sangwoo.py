import copy

class Solution(object):
    def rotate(self, matrix):
        temp = copy.deepcopy(matrix)
        
        # 행과 열 바꾸기
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = temp[j][i]
                
        temp = copy.deepcopy(matrix)
        
        # 세로 중간줄을 기준으로 바꾸기
        for k in range(len(matrix)):
            for t in range(len(matrix) // 2):
                matrix[k][t] = temp[k][-t-1]
                matrix[k][-t-1] = temp[k][t]

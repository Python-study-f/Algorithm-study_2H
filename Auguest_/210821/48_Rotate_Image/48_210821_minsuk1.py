import copy
class Solution(object):
    def rotate(self, matrix):
        tmp=copy.deepcopy(matrix)
        n=len(matrix[0])
        ans=[[] for _ in range(n)]
        
        
        for i in range(n):
            for j in range(n-1,-1,-1):
                ans[i].append(tmp[j][i])
        for i in range(n):
            for j in range(n):
                matrix[i][j]=ans[i][j]

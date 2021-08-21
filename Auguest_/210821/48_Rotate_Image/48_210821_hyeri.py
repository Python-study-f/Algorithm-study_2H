class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        N = len(matrix)
        answer = [[] for _ in range(N)]
        for j in range(N):
            for i in range(N-1, -1, -1):
                answer[j].append(matrix[i][j])
        for i in range(N):
            for j in range(N):
                matrix[i][j] = answer[i][j]
                
                
        # 왜 matrix = answer 로 하면 안 되는지 아시는분...? 

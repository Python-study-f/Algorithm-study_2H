from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        tmp = list(map(list, list(zip(*matrix[::-1]))))
        for i in range(len(tmp)):
            matrix[i] = tmp[i]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        tmp = [[matrix[r][c] for c in range(n)] for r in range(n)]
        for r in range(n):
            for c in range(n):
                matrix[c][n - r - 1] = tmp[r][c]

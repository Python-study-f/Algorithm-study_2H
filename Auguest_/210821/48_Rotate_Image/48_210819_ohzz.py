# Rotate Image 48 Leetcode


def rotate(matrix):
    rotate_mat = list(zip(*matrix))
    for i in range(len(matrix)):
        matrix[i] = list(rotate_mat[i][::-1])
    return matrix


# matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
# matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(rotate(matrix1))

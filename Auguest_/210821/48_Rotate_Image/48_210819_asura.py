
class Solution(object):
    def rotate(self, matrix):
        for idx, arr in enumerate(zip(*matrix[::-1])):
            matrix[idx] = list(arr)

        print(matrix)

# tmp = []
#
# for i in zip(*matrix):
#     tmp.append(list(reversed(i)))


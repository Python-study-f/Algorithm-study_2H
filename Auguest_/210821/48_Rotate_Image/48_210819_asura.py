matrix = [[1,2,3],[4,5,6],[7,8,9]]

for idx, arr in enumerate(zip(*matrix[::-1])):
    matrix[idx] = list(arr)

print(matrix)

# tmp = []
#
# for i in zip(*matrix):
#     tmp.append(list(reversed(i)))


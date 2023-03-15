import numpy as np
#1
matrix = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
print(matrix)

matrix1 = np.array([[], [], []])
index = 0
# for i in matrix:
#     # for y in i:
#         matrix1[index] = i
#         index+=1
#
# print(matrix1)

matrix = matrix.reshape(-1)
print(matrix)

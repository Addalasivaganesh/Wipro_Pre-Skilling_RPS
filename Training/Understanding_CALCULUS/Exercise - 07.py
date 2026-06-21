import numpy as np

#TRANSPOSE
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

#Find transpose
transpose_matrix = matrix.T
print("Transposed matrix is: ", transpose_matrix)

#print original shape
print("Original shape", matrix.shape)

#print transpose shape
print("Transpose shape", transpose_matrix.shape)

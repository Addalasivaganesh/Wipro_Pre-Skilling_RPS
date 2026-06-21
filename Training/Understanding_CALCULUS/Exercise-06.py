import numpy as np

#matrix multiplication using np.matmul()

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

result = np.matmul(A, B)
print(result)
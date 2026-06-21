import numpy as np

matrix = np.array([
    [80, 70, 90],
    [60, 75, 88],
    [95, 85, 91]
])

#first student marks
print("first student marks", matrix[0])

#print second row
print("second row", matrix[1])

#print third column
print("third row:", matrix[:,2])

#print science marks of student B
print("science marks of student B: ", matrix[1,1])
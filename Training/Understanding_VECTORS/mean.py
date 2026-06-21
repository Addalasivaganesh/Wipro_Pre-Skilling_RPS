import numpy as np

marks = [60, 70, 90, 100, 101]
#mean
print(np.mean(marks))

#median
print(np.median(marks))

#mode
from scipy import stats

data = [1, 2, 2,  2, 3, 4]
result = stats.mode(data)
print("Mode: ",result.mode)
print("count ",result.count)

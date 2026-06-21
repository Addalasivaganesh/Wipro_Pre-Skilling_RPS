import numpy as np

data = [60, 70, 80, 90, 100]

#variance
#if values are close to the mean --> variance is small
#if values are far from the mean --> variance is large
print(np.var(data))

#Standard deviation
#variance in squared units
#standard deviation brings it back to original units
print(np.std(data))
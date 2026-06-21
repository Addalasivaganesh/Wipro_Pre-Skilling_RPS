# normal distribution

import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(50, 10, 1000)

plt.hist(data, bins = 30)
plt.show()
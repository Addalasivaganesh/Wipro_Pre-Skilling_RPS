#ReLU - Rectified linear Unit

import numpy as np

# input values
values = np.array([
    -10, -5, 0, 5, 10
])

#ReLU function
relu_output = np.maximum(0, values)
print("Input", values)
print("ReLU Output:", relu_output)

#01. What is the output
# Input [-10  -5   0   5  10]
# ReLU Output: [ 0  0  0  5 10]

#02. which values become zero
# -10, -5 (All negative values become zero)

#03. why does ReLU removes Negative value
#ReLU formula:
# f(x) = max(0, x)
# It suppresses negative signals and keeps only useful positive activations → helps neural networks learn faster and avoids unnecessary noise.

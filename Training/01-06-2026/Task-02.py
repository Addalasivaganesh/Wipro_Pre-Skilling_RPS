
import numpy as np

# Input scores
scores = np.array([5, 2, 1])

# Softmax function
exp_scores = np.exp(scores)
softmax_output = exp_scores / np.sum(exp_scores)

print("Scores:", scores)
print("Softmax Output:", softmax_output)
print("Sum of probabilities:", np.sum(softmax_output))




#01. Which class has the highest probability
# The score 5 → highest probability ≈ 0.93623955

#02. Do all probabilities add upto 1
# Yes → exactly 1.0


#03. Why Softmax is preferred over raw scores
# Converts raw scores into probabilities
# Makes outputs interpretable (0 to 1 range)
# Useful for classification (clearly shows confidence)

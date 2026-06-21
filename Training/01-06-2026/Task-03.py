import numpy as np

# Target class
target = 1

# Predictions (logits)
A = np.array([1, 8, 1])
B = np.array([8, 1, 1])

# Softmax function
def softmax(x):
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x)

# Cross Entropy Loss
def cross_entropy(pred, target):
    return -np.log(pred[target])

# Compute for A
softmax_A = softmax(A)
loss_A = cross_entropy(softmax_A, target)

# Compute for B
softmax_B = softmax(B)
loss_B = cross_entropy(softmax_B, target)

print("Softmax A:", softmax_A)
print("Loss A:", loss_A)

print("\nSoftmax B:", softmax_B)
print("Loss B:", loss_B)


#01. Which prediction has lower loss?
# Prediction A

#02. Which prediction has higher loss?
# Prediction B

#03. Why?

# Actual class = 1 (Pass)
# Cross Entropy checks how much probability is given to the correct class.
#
# Prediction A:
#
# Gives very high probability (~0.998) to correct class
# So, loss is very small
#
# Prediction B:

# Gives very low probability (~0.0009) to correct class
# So, loss is very high
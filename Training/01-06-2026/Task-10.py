gradient = 1

for i in range(10):
    gradient = gradient * 2
    print(gradient)

# Answers
# 1. What happens to the gradient?
#
# It keeps increasing rapidly
# Becomes very large
#
#
# 2. Why is this dangerous?
#
# Large gradients → huge weight updates
# Model becomes:
#
# Unstable
# Loss may become NaN
# Training diverges
#
#
#
#
# 3. What is Gradient Clipping?
# Gradient Clipping = limiting the size of gradients
# Example:
#
# # torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
#
# If gradient > threshold → reduce it
# Keeps training stable
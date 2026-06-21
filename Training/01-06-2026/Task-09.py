gradient = 1

for i in range(10):
    gradient = gradient * 0.1
    print(f"{gradient:.10f}")

# Answers
# 1. What happens to the gradient?
#
# It keeps becoming smaller
# Eventually → almost zero
#
#
# 2. Why is this a problem?
#
# Gradients are used to update weights
# If gradient ≈ 0:
#
# No learning happens
# Deep layers stop updating
# Training becomes very slow or stops
#
#
#
#
# 3. Which activation function helps reduce this issue?
# ReLU (Rectified Linear Unit)
# Why:
#
# Does not shrink values like sigmoid/tanh
# Keeps gradient active for positive values
import torch
import torch.nn as nn
import torch.optim as optim

# Sample dataset (y = 2x + 3)
X = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[5.0], [7.0], [9.0], [11.0]])

# Linear model
model_sgd = nn.Linear(1, 1)
model_adam = nn.Linear(1, 1)

# Loss function
criterion = nn.MSELoss()

# Optimizers
optimizer_sgd = optim.SGD(model_sgd.parameters(), lr=0.01)
optimizer_adam = optim.Adam(model_adam.parameters(), lr=0.01)

# Training loop
epochs = 100

print("Training with SGD")
for epoch in range(epochs):
    optimizer_sgd.zero_grad()
    output = model_sgd(X)
    loss = criterion(output, y)
    loss.backward()
    optimizer_sgd.step()

    if (epoch+1) % 20 == 0:
        print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

print("\nTraining with Adam")
for epoch in range(epochs):
    optimizer_adam.zero_grad()
    output = model_adam(X)
    loss = criterion(output, y)
    loss.backward()
    optimizer_adam.step()

    if (epoch+1) % 20 == 0:
        print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")



# Answers
# 1. Which optimizer reduces loss faster?
# Adam optimizer
#
# 2. Which optimizer is commonly used in modern Deep Learning?
# Adam optimizer
#
# 3. Why?
# SGD (Stochastic Gradient Descent)
#
# Uses same learning rate for all parameters
# Moves step-by-step → slower convergence
# Can get stuck or oscillate
#
# Adam (Adaptive Moment Estimation)
#
# Uses:
#
# Momentum (past gradients)
# Adaptive learning rates (per parameter)
#
#
# Automatically adjusts learning speed
# Converges faster and more stable



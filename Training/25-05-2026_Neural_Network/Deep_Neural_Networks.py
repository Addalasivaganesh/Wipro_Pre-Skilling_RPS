import torch
import torch.nn as nn
import torch.optim as optim
# Input Data
X = torch.tensor(
    [
        [1, 50],
        [2, 55],
        [3, 60],
        [4, 65],
        [5, 70]
    ],
    dtype=torch.float32
)
# Output Data
y = torch.tensor(
    [
        [40],
        [50],
        [60],
        [70],
        [80]
    ],

    dtype=torch.float32
)
#Create Deep Neural Network
model = nn.Sequential(
    nn.Linear(2, 8),
    nn.ReLU(),#Activation Function
    nn.Linear(8, 4),
    nn.ReLU(),
    nn.Linear(4, 1),
    nn.ReLU()
)
#Loss function
criterion = nn.MSELoss()
#Optimizer
optimizer = optim.SGD(model.parameters(), lr=0.001)
#Training Loop
epochs = 200
for epoch in range(epochs):
    # Forward pass
    predictions = model(X)
    #Loss Calculation
    loss = criterion(predictions, y)
    #Clear Old Gradients
    optimizer.zero_grad()
    #Back propagation
    loss.backward()
    #Update Weights
    optimizer.step()
    #print Progress
    if epoch % 20 == 0:
        print(f"Epoch {epoch}")
        print(f"Loss: {loss.item():.4f}")
        print("----------------------")
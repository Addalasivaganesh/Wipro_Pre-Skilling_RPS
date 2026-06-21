import torch
import torch.nn as nn
import torch.optim as optim

#Input Data
X = torch.tensor(
    [[1], [2], [3], [4], [5]],
    dtype = torch.float32
)

#Output Data
Y = torch.tensor(
    [[40], [50], [60], [70], [80]],
    dtype = torch.float32
)
#Create Neural Network
model = nn.Linear(
    1,
    1
)
#Loss Function
criterion = nn.MSELoss()

#Optimizer
optimizer = optim.SGD(model.parameters(), lr=0.001)

#Training loop

epochs = 100

for epoch in range(epochs):

    #Forward pass
    predictions = model(X)

    #loss calculation
    loss = criterion(predictions, Y)


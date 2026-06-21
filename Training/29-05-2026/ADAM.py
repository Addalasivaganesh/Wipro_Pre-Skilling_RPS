import torch
import torch.nn as nn
import torch.optim as optim

X = torch.tensor(
    [[1.0],
     [2.0],
     [3.0],
     [4.0]]
)
y = torch.tensor(
    [[10.0],
     [20.0],
     [30.0],
     [40.0]]
)
model = nn.Linear(
    1,
    1
)
criterion = nn.MSELoss()
optimizer = optim.Adam(
    model.parameters(),
    lr = 0.01
)

for epoch in range(100):
    predictions = model(X)
    loss = criterion(
        predictions,
        y
    )
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if epoch % 10 == 0:
        print(
            epoch,
            loss.item()
        )
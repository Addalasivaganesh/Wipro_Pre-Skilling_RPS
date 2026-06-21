



import torch

import torch.nn as nn
import torch.optim as optim

X = torch.tensor([
    [0,2],  # good movie
    [3,2],  # amazing movie
    [1,2],  # bad movie
    [4,2]   # terrible movie
])

y = torch.tensor([
    1,
    1,
    0,
    0
])

class SentimentModel(nn.Module):

    def __init__(self):

        super().__init__() # Super - Parent Class -- init = Constructor

        self.embedding = nn.Embedding(
            5,
            4
        )

        self.fc = nn.Linear(
            4,
            2
        )

    def forward(self,x):

        x = self.embedding(x)
        x = x.mean(dim=1)
        x = self.fc(x)
        return x


model = SentimentModel()

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=0.01
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
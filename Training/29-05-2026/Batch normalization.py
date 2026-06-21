import torch
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(4,8),
    nn.BatchNorm1d(8),
    nn.ReLU(),
    nn.Linear(8,3)
)
print(model)
import torch
import torch.nn as nn

X = torch.tensor([
    [10., 20.],
    [30., 40.],
    [50., 60.]
])

bn = nn.BatchNorm1d(2)

output = bn(X)
print(output)
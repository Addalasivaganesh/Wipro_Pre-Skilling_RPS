import torch
import torch.nn as nn
layer = nn.Linear(4, 8)

nn.init.xavier_uniform_(  #This is old  use sigmoid and tanh
    layer.weight
)

print(layer.weight)
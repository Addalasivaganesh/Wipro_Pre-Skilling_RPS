import torch
import torch.nn as nn

layer = nn.Linear(4, 8)

nn.init.kaiming_uniform_(   #This is new updated older was xavier
    layer.weight
)
print(layer.weight)
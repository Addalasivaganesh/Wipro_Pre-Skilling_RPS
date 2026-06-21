import torch
import torch.nn as nn

layer1 = nn.Linear(100,100)
layer2 = nn.Linear(100,100)

nn.init.xavier_uniform_( layer1.weight)
nn.init.kaiming_uniform_( layer2.weight)

print("Xavier")
print(layer1.weight.std())

print("\n kaiming")
print(layer2.weight.std())
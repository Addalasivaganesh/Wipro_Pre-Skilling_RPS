import torch
import torch.nn as nn

dropout = nn.Dropout(0.5)

x = torch.tensor(
    [1., 2., 3., 4., 5.]
)
print("Before")
print(x)

print("\n After")
print(
    dropout(x)
)
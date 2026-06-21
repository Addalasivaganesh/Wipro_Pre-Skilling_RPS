import torch.nn as nn
from torchvision import models

# Load pretrained ResNet18
model = models.resnet18(pretrained=True)

# Print final layer
print("Original final layer:\n", model.fc)

# Replace final layer
model.fc = nn.Linear(512, 2)

print("\nModified final layer:\n", model.fc)

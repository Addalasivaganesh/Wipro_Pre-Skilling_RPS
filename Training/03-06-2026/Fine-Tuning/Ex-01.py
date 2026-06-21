import torch.nn as nn
from torchvision import models

# Load pretrained model
model = models.resnet18(pretrained=True)

# Freeze all layers
for param in model.parameters():
    param.requires_grad = False

# Unfreeze layer4
for param in model.layer4.parameters():
    param.requires_grad = True

# Print trainable layers
for name, param in model.named_parameters():
    if param.requires_grad:
        print(name)

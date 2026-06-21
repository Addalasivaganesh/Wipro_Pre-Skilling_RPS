import torch
import torch.nn as nn
from torchvision import models

# ----------------------------
# Step 1: Load pretrained model
# ----------------------------
model = models.resnet18(pretrained=True)

# ----------------------------
# Step 2: Print original final layer
# ----------------------------
print("Original Final Layer:\n")
print(model.fc)

# ----------------------------
# Step 3: Replace final layer
# ----------------------------
model.fc = nn.Linear(512, 2)

print("\nModified Final Layer:\n")
print(model.fc)

# ----------------------------
# Step 4: Freeze all layers
# ----------------------------
for param in model.parameters():
    param.requires_grad = False

# ----------------------------
# Step 5: Unfreeze final layer
# ----------------------------
for param in model.fc.parameters():
    param.requires_grad = True

# ----------------------------
# Step 6: Check trainable layers
# ----------------------------
print("\nTrainable Layers:\n")
for name, param in model.named_parameters():
    if param.requires_grad:
        print(name)
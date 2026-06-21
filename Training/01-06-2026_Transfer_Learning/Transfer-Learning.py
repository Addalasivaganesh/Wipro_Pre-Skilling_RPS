import torch
import torch.nn as nn
import torch.optim as optim

from torchvision import models


# --------------------------------------------------
# STEP 1
# Load pretrained ResNet18
# --------------------------------------------------

model = models.resnet18(pretrained=True)

print("Original Final Layer")
print(model.fc)


# Original:
#
# Image
#   ↓
# ResNet Feature Extractor
#   ↓
# 512 Features
#   ↓
# FC Layer
#   ↓
# 1000 Classes
#
# fc = nn.Linear(512,1000)


# --------------------------------------------------
# STEP 2
# Freeze all pretrained layers
# --------------------------------------------------

for param in model.parameters():
    param.requires_grad = False


# Meaning:
#
# Do NOT retrain:
#
# Edge Detection
# Shape Detection
# Texture Detection
# Pattern Detection
#
# already learned from ImageNet


# --------------------------------------------------
# STEP 3
# Replace Final Layer
# --------------------------------------------------

model.fc = nn.Linear(
    512,   # 512 features coming from ResNet
    2      # Cat or Dog
)


print("\nNew Final Layer")
print(model.fc)


# Architecture now:
#
# Image
#   ↓
# ResNet Feature Extractor
#   ↓
# 512 Features
#   ↓
# FC Layer
#   ↓
# Cat
# Dog
#
#
# fc = nn.Linear(512,2)


# --------------------------------------------------
# STEP 4
# Loss Function
# --------------------------------------------------

criterion = nn.CrossEntropyLoss()


# Multi-Class Classification Loss
#
# Cat = 0
# Dog = 1


# --------------------------------------------------
# STEP 5
# Optimizer
# --------------------------------------------------

optimizer = optim.Adam(
    model.fc.parameters(),
    lr=0.001
)


# Important:
#
# ONLY final layer gets updated.
#
# Entire ResNet remains frozen.


# --------------------------------------------------
# STEP 6
# Sample Images
# --------------------------------------------------

X = torch.randn(
    4,      # 4 images
    3,      # RGB
    224,    # height
    224     # width
)


# Shape:
#
# Batch Size = 4
# Channels = 3
# Height = 224
# Width = 224


# --------------------------------------------------
# STEP 7
# Labels
# --------------------------------------------------

y = torch.tensor([
    0,  # Cat
    1,  # Dog
    0,  # Cat
    1   # Dog
])


# --------------------------------------------------
# STEP 8
# Training
# --------------------------------------------------

epochs = 5

for epoch in range(epochs):

    # Forward Pass
    outputs = model(X)

    print("\nOutput Shape")
    print(outputs.shape)

    #
    # Shape:
    #
    # [4,2]
    #
    # 4 images
    # 2 class scores
    #

    loss = criterion(
        outputs,
        y
    )

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    print(
        f"Epoch {epoch}"
    )

    print(
        f"Loss = {loss.item()}"
    )


# --------------------------------------------------
# STEP 9
# Prediction
# --------------------------------------------------

with torch.no_grad():

    outputs = model(X)

    print("\nRaw Scores")
    print(outputs)

    predictions = torch.argmax(
        outputs,
        dim=1
    )

    print("\nPredicted Classes")
    print(predictions)


# Example Output:
#
# tensor([0,1,0,1])
#
# Meaning:
#
# Image 1 -> Cat
# Image 2 -> Dog
# Image 3 -> Cat
# Image 4 -> Dog
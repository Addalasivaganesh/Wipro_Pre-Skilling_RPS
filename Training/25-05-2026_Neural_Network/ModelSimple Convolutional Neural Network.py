import torch
import torch.nn as nn
#Create  CNN Model
model = nn.Sequential(
    #Convolutional Layer
    nn.Conv2d(
        in_channels = 1,
        out_channels = 8,
        kernel_size = 3
    ),
    #Activation
    nn.ReLU(),
    #polling
    nn.MaxPool2d(kernel_size = 2),
    #Flatten Layer
    nn.Flatten(), #Convert Feature into Vector
    #Fully Connected Layer
    nn.Linear(
        1352,
        10
    )
)
print(model)
# Given code

import torch
import torch.nn as nn

dropout = nn.Dropout(0.5)

x = torch.tensor([1., 2., 3., 4., 5.])

print(dropout(x))

# Answers
# 1. Why are some values becoming 0?
# Dropout randomly turns OFF neurons during training.
#
# Probability = 0.5
# So, 50% values → set to 0
#
# This helps prevent overfitting.
#
# 2. Why do surviving values increase?
# To maintain the overall scale of data, PyTorch scales remaining values:
# Formula:
# output = input / (1 - dropout_rate)
#
# Here:
# 1 / (1 - 0.5) = 2
#
# So:
#
# Surviving values are multiplied by 2
#
#
# 3. Does Dropout work during prediction?
# No
#
# During training → Dropout is ON
# During testing/prediction → Dropout is OFF
#
# Because:
#
# We want full network strength during prediction


# Code Showing Training vs Evaluation Mode
# import torch
# import torch.nn as nn
#
# dropout = nn.Dropout(0.5)
#
# x = torch.tensor([1., 2., 3., 4., 5.])
#
# # Training mode (default)
# dropout.train()
# print("Training output:", dropout(x))
#
# # Evaluation mode
# dropout.eval()
# print("Evaluation output:", dropout(x))
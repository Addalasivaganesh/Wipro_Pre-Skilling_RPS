import torch
import torch.nn as nn

x = torch.tensor([
    [10., 20.],
    [30., 40.],
    [50., 60.]
])

bn = nn.BatchNorm1d(2)

output = bn(x)

print(output)

#Answers

# 1. Why are outputs centered around 0?
# Because Batch Normalization subtracts the mean:
# x - mean → makes data centered at 0
#
# Then divides by standard deviation → scales it.
#
# 2. What problem does BatchNorm solve?
# Problem: Internal Covariate Shift
# Meaning:
#
# During training, input distribution to each layer keeps changing
# Makes training slow and unstable
#
# BatchNorm Fix:
#
# Normalizes inputs for each layer
# Keeps values stable
# Makes training faster and smoother
#
#
# 3. Does BatchNorm learn patterns or help training?
# It helps training (main purpose)
# But it also has small learnable parameters:
#
# Gamma (scale)
# Beta (shift)
#
# So:
#
#  Helps stabilize training
#  Slightly learns scaling/adjustment
#  Does NOT learn patterns like weights do


# Code Showing Training vs Evaluation Mode

# bn = nn.BatchNorm1d(2)
# # Training mode
# bn.train()
# print("Training Output:\n", bn(x))
#
# # Evaluation mode
# bn.eval()
# print("\nEvaluation Output:\n", bn(x))

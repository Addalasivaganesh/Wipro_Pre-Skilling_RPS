import torch
import torch.nn as nn

embedding = nn.Embedding(10, 5)

# Input word index
word = torch.tensor([0])

# Get embedding
output = embedding(word)

print("Output:\n", output)
print("Shape:", output.shape)
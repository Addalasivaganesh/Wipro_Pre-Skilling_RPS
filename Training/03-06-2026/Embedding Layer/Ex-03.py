import torch
import torch.nn as nn

embedding = nn.Embedding(10, 5)

# Multiple words
words = torch.tensor([0, 1, 2])

# Get embeddings
output = embedding(words)

print("Output:\n", output)
print("Shape:", output.shape)
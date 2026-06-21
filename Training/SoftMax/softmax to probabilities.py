import torch
import torch.nn as nn

#Raw scores(Logits)
scores = torch.tensor(
    [2.5, 1.2, 0.3]
)
#Soft max layer
softmax = nn.Softmax(dim=0)

#convert to probabilities
probabilities = softmax(scores)

print(probabilities)
print("\n Sum ")
print(probabilities.sum())
import torch
import torch.nn.functional as F

# Create vectors
v1 = torch.tensor([1.0, 2.0, 3.0])
v2 = torch.tensor([1.0, 2.0, 3.0])

# Cosine similarity
similarity = F.cosine_similarity(v1, v2, dim=0)

print("Cosine Similarity:", similarity.item())
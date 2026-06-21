import numpy as np
from numpy import dot
from numpy.linalg import norm

# Load embeddings
embeddings = {}

with open("glove.6B.50d.txt", encoding="utf-8") as f:
    for line in f:
        values = line.split()
        word = values[0]
        vector = np.array(values[1:], dtype='float32')
        embeddings[word] = vector

# Cosine similarity
def cosine(a, b):
    return dot(a, b) / (norm(a) * norm(b))

print("doctor vs nurse:", cosine(embeddings["doctor"], embeddings["nurse"]))
print("doctor vs football:", cosine(embeddings["doctor"], embeddings["football"]))
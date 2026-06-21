import numpy as np


# Load GloVe file
glove_file = "glove.6B.50d.txt"

embeddings = {}

with open(glove_file, 'r', encoding='utf-8') as f:
    for line in f:
        values = line.split()
        word = values[0]
        vector = np.array(values[1:], dtype='float32')
        embeddings[word] = vector

# Words to print
words = ["doctor", "nurse", "hospital", "football"]

for word in words:
    print(f"{word} vector:\n", embeddings[word][:5], "...")  # printing first 5 values only
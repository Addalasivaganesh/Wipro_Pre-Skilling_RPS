from gensim.models import Word2Vec

# Training data
data = [
    ["doctor", "hospital"],
    ["nurse", "hospital"],
    ["football", "sport"],
    ["cricket", "sport"]
]

# Train model
model = Word2Vec(sentences=data, vector_size=5, window=2, min_count=1)

# Print vectors
print("Doctor Vector:\n", model.wv["doctor"])
print("\nNurse Vector:\n", model.wv["nurse"])
print("\nFootball Vector:\n", model.wv["football"])
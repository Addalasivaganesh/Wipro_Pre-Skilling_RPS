from gensim.models import Word2Vec

# Step 1: Training data (same as Ex-01)
data = [
    ["doctor", "hospital"],
    ["nurse", "hospital"],
    ["football", "sport"],
    ["cricket", "sport"]
]

# Step 2: Train Word2Vec model
model = Word2Vec(sentences=data, vector_size=5, window=2, min_count=1)

# Step 3: Calculate similarities
sim1 = model.wv.similarity("doctor", "nurse")
sim2 = model.wv.similarity("football", "cricket")
sim3 = model.wv.similarity("doctor", "football")

# Step 4: Print results
print("doctor vs nurse:", sim1)
print("football vs cricket:", sim2)
print("doctor vs football:", sim3)

# Step 5: Identify most and least similar
similarities = {
    "doctor vs nurse": sim1,
    "football vs cricket": sim2,
    "doctor vs football": sim3
}

# Most similar
most_similar = max(similarities, key=similarities.get)

# Least similar
least_similar = min(similarities, key=similarities.get)

print("\nMost similar pair:", most_similar)
print("Least similar pair:", least_similar)
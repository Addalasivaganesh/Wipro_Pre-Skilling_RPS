import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("DATASETS/support_tickets.csv")

# Use ticket messages
documents = df["message"].tolist()

# Fixed input (as per requirement)
user_input = "I cannot login"

# Add input to documents
documents.append(user_input)

# TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

# Cosine similarity
similarity_matrix = cosine_similarity(X)

# Get similarity for input
user_similarity = similarity_matrix[-1][:-1]

# Top 3 results
top_indices = user_similarity.argsort()[-3:][::-1]

print("Input:")
print(user_input)

print("\nTop Similar Tickets:")
for i, idx in enumerate(top_indices, start=1):
    print(f"{i}. {documents[idx]}")

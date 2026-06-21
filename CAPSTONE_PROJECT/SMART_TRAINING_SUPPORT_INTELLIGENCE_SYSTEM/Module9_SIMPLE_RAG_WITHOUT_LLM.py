import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load knowledge base
kb = pd.read_csv("DATASETS/knowledge_base.csv")

questions = kb["question"].tolist()
answers = kb["answer"].tolist()

# User input
user_input = input("Ask a question: ")

# TF-IDF
documents = questions + [user_input]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

# Cosine similarity
similarity = cosine_similarity(X)

# Get similarity with user input
user_sim = similarity[-1][:-1]

# Best match index
best_idx = user_sim.argmax()

# Output
print("\nUser Question:")
print(user_input)

print("\nMatched KB Question:")
print(questions[best_idx])

print("\nAnswer:")
print(answers[best_idx])
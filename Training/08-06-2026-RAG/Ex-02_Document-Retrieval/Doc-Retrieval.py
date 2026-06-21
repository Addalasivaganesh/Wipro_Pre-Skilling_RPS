from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Read documents
documents = []

with open("docs.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            documents.append(line)

# Step 2: TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Step 3: Take one user input
user_question = input("Ask your question: ")

# Step 4: Transform input
user_vector = vectorizer.transform([user_question])

# Step 5: Compute similarity
similarity = cosine_similarity(user_vector, tfidf_matrix)

# Step 6: Get Top 3 results
similarity_scores = similarity.flatten()
top_indices = similarity_scores.argsort()[::-1][:3]

# Step 7: Output
print("\nTop 3 matching documents:")
for i, idx in enumerate(top_indices):
    print(f"{i+1}. {documents[idx]}")
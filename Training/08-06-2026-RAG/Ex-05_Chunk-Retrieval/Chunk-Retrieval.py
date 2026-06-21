from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Read file
with open("doc.txt", "r") as file:
    document = file.read()

# Step 2: Split into chunks
chunks = document.strip().split("\n")

# Step 3: TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(chunks)

print(" Chunk Retrieval System Ready!")

# Step 4: Loop
while True:
    query = input("\nAsk your question (type 'exit' to stop): ")

    # Exit condition
    if query.lower() == "exit":
        print("Exiting system...")
        break

    # Step 5: Transform query
    query_vector = vectorizer.transform([query])

    # Step 6: Similarity
    similarity = cosine_similarity(query_vector, tfidf_matrix)

    # Step 7: Top 2 chunks
    scores = similarity.flatten()
    top_indices = scores.argsort()[::-1][:2]

    # Step 8: Output
    print("\nBest matching chunks:\n")
    for idx in top_indices:
        print(chunks[idx])

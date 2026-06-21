import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Read files
folder_path = "Datasets"

documents = []
file_names = []

for file in os.listdir(folder_path):
    if file.endswith(".txt"):
        with open(os.path.join(folder_path, file), "r") as f:
            documents.append(f.read().strip())
            file_names.append(file)

# Step 2: TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

print(" End-to-End RAG System Ready!")

# Step 3: Loop
while True:
    query = input("\nAsk your question (type 'exit' to stop): ")

    if query.lower() == "exit":
        print("Exiting system...")
        break

    # Step 4: Transform query
    query_vector = vectorizer.transform([query])

    # Step 5: Similarity
    similarity = cosine_similarity(query_vector, tfidf_matrix)

    # Step 6: Top 2 chunks
    scores = similarity.flatten()
    top_indices = scores.argsort()[::-1][:2]

    # Step 7: Output
    print("\nRetrieved Chunks:\n")
    for idx in top_indices:
        print(f"{file_names[idx]} → {documents[idx]}")
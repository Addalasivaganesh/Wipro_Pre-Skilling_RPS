import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#  Step 1: Read resumes
folder_path = "resumes"

resumes = []
file_names = []

for file in os.listdir(folder_path):
    if file.endswith(".txt"):
        with open(os.path.join(folder_path, file), "r") as f:
            resumes.append(f.read().strip())
            file_names.append(file)

#  Step 2: TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(resumes)

print("Resume Retrieval System Ready!")

# Step 3: Loop
while True:
    query = input("\nEnter job role (type 'exit' to stop): ")

    # Exit condition
    if query.lower() == "exit":
        print("Exiting Resume System...")
        break

    # Step 4: Transform
    query_vector = vectorizer.transform([query])

    # Step 5: Similarity
    similarity = cosine_similarity(query_vector, tfidf_matrix)

    # Step 6: Top 2
    scores = similarity.flatten()
    top_indices = scores.argsort()[::-1][:2]

    # Step 7: Output
    print("\nTop matching resumes:")
    for idx in top_indices:
        print(f"{file_names[idx]} → {resumes[idx]}")
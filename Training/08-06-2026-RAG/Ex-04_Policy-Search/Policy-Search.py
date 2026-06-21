import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Read policy files
folder_path = "policies"

policies = []
file_names = []

for file in os.listdir(folder_path):
    if file.endswith(".txt"):
        with open(os.path.join(folder_path, file), "r") as f:
            content = f.read().strip()
            policies.append(content)
            file_names.append(file)

#  Step 2: TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(policies)

print(" Policy Search System Ready!")

# Step 3: Loop for multiple queries
while True:
    query = input("\nAsk your policy question (type 'exit' to stop): ")

    # Exit condition
    if query.lower() == "exit":
        print("Exiting Policy Search...")
        break

    # Step 4: Transform query
    query_vector = vectorizer.transform([query])

    # Step 5: Similarity
    similarity = cosine_similarity(query_vector, tfidf_matrix)

    # Step 6: Best match
    best_index = similarity.argmax()

    # Step 7: Output
    print("\nMatched Policy:")
    print(file_names[best_index])
    print(policies[best_index])
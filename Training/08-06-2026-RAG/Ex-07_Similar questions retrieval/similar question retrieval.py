from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#  Step 1: Read questions
questions = []

with open("questions.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            questions.append(line)

# Step 2: TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(questions)

print(" Similar Question Retrieval Ready!")

#  Step 3: Loop
while True:
    query = input("\nAsk your question (type 'exit' to stop): ")

    # Exit condition
    if query.lower() == "exit":
        print("Exiting system...")
        break

    # Step 4: Transform query
    query_vector = vectorizer.transform([query])

    # Step 5: Similarity
    similarity = cosine_similarity(query_vector, tfidf_matrix)

    # Step 6: Best match
    best_index = similarity.argmax()

    # Step 7: Output
    print("\nMost similar question:")
    print(questions[best_index])
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("faq_data.csv")

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['question'])

query = input("Enter your question: ")

query_vec = vectorizer.transform([query])
scores = cosine_similarity(query_vec, tfidf_matrix)

top_idx = scores[0].argsort()[::-1][:3]

print("\nTop Matches:\n")
for i, idx in enumerate(top_idx):
    print(f"{i+1}. {df['question'][idx]}")
    print(f"Score: {round(scores[0][idx], 2)}\n")

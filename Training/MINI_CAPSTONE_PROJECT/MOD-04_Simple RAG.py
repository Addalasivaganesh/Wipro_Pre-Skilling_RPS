import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("faq_data.csv")

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['question'])

query = input("Ask your question: ")

query_vec = vectorizer.transform([query])
scores = cosine_similarity(query_vec, tfidf_matrix)

best_idx = scores.argmax()

print("\nBest Match:")
print(df['question'][best_idx])

print("\nAnswer:")
print(df['answer'][best_idx])
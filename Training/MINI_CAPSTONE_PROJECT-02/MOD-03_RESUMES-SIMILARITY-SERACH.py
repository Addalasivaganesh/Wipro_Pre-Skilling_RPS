# MODULE 03 - RESUME SIMILARITY (FIXED)

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
df = pd.read_csv("resumes.csv")

# TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['resume'])

# Query
query = input("Enter job search: ")

query_vec = vectorizer.transform([query])
similarity = cosine_similarity(query_vec, tfidf_matrix)[0]

# Top 3 matches
top_indices = similarity.argsort()[-3:][::-1]

for i in top_indices:
    print(f"Candidate {df.iloc[i]['candidate_id']}")
    print(f"Score: {similarity[i]:.2f}")
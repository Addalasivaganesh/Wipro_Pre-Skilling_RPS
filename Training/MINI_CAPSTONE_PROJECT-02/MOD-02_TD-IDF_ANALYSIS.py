# MODULE 02 - TF-IDF ANALYSIS

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load dataset
df = pd.read_csv("resumes.csv")

# TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['resume'])

feature_names = vectorizer.get_feature_names_out()

# Show important words for each resume
for i in range(len(df)):
    print(f"\nResume {i + 1} Important Words:")
    scores = tfidf_matrix[i].toarray()[0]

    for word, score in zip(feature_names, scores):
        if score > 0:
            print(word)
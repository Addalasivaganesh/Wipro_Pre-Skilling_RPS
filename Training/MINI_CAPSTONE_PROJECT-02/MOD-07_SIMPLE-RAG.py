# MODULE 07 - SIMPLE RAG

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
resumes_df = pd.read_csv("resumes.csv")
jobs_df = pd.read_csv("job_descriptions.csv")

# TF-IDF on resumes
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(resumes_df['resume'])

# RAG function
def simple_rag(job_desc):

    job_vec = vectorizer.transform([job_desc])
    similarity = cosine_similarity(job_vec, tfidf_matrix)[0]

    top_indices = similarity.argsort()[-3:][::-1]

    print("\nJob:", job_desc)
    print("Top Candidates:")

    for i in top_indices:
        print(f"Candidate {resumes_df.iloc[i]['candidate_id']} | Score: {similarity[i]:.2f}")


# Run for all jobs
for _, row in jobs_df.iterrows():
    simple_rag(row['job_description'])
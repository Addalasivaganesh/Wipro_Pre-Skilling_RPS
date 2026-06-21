import pandas as pd
import string
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec

# ---------------------------
# LOAD DATA (BOTH FILES)
# ---------------------------
resumes_df = pd.read_csv("resumes.csv")
jobs_df = pd.read_csv("job_descriptions.csv")


# ---------------------------
# MODULE 1: PREPROCESSING
# ---------------------------
def preprocess_text(text):
    text = text.lower()

    for ch in string.punctuation:
        text = text.replace(ch, "")

    return text.split()


resumes_df['tokens'] = resumes_df['resume'].apply(preprocess_text)

# ---------------------------
# MODULE 2: TF-IDF
# ---------------------------
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(resumes_df['resume'])


# ---------------------------
# MODULE 3: SEARCH
# ---------------------------
def search_resume(query):
    query_vec = vectorizer.transform([query])
    similarity = cosine_similarity(query_vec, tfidf_matrix)[0]

    top_indices = similarity.argsort()[-3:][::-1]

    print("\nTop Candidates:")
    for i in top_indices:
        print(f"Candidate {resumes_df.iloc[i]['candidate_id']}, Score: {similarity[i]:.2f}")


# ---------------------------
# MODULE 4: WORD2VEC
# ---------------------------
model = Word2Vec(resumes_df['tokens'].tolist(), vector_size=50, window=2, min_count=1)


def word2vec_demo():
    pairs = [("python", "nlp"), ("java", "spring"), ("react", "angular"), ("sql", "analysis")]

    for w1, w2 in pairs:
        if w1 in model.wv and w2 in model.wv:
            print(f"{w1} vs {w2}: {model.wv.similarity(w1, w2):.2f}")
        else:
            print(f"{w1} or {w2} not found")


# ---------------------------
# MODULE 5: CLASSIFICATION
# ---------------------------
def classify_resume(text):
    text = text.lower()

    if "python" in text and "nlp" in text:
        return "AI Engineer"
    elif "java" in text:
        return "Backend Developer"
    elif "react" in text or "angular" in text:
        return "Frontend Developer"
    elif "sql" in text or "power bi" in text:
        return "Data Analyst"
    return "Unknown"


# ---------------------------
# MODULE 6: NER
# ---------------------------
nlp = spacy.load("en_core_web_sm")


def extract_entities(text):
    doc = nlp(text)
    for ent in doc.ents:
        print(ent.text, "->", ent.label_)


# ---------------------------
# MODULE 7: RAG (USES jobs.csv)
# ---------------------------
def simple_rag():
    print("\n--- JOB MATCHING ---")

    for _, row in jobs_df.iterrows():
        job_desc = row['job_description']

        print(f"\nJob: {job_desc}")
        search_resume(job_desc)


# ---------------------------
# RUN
# ---------------------------
if __name__ == "__main__":
    search_resume("Python NLP Engineer")

    print("\nCategory:", classify_resume("Python NLP Deep Learning"))

    word2vec_demo()

    extract_entities("Rahul Sharma worked at Microsoft in Hyderabad")

    simple_rag()



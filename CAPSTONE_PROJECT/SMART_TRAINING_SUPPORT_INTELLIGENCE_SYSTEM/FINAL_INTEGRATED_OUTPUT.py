# ==========================
# FINAL INTEGRATED SYSTEM (LOOP VERSION)
# ==========================

import pandas as pd
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
tickets = pd.read_csv("DATASETS/support_tickets.csv")
kb = pd.read_csv("DATASETS/knowledge_base.csv")

# Preprocessing
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()

# ==========================
# LOOP (UNLIMITED INPUT)
# ==========================

while True:

    user_input = input("\nEnter your message (type 'quit' to exit): ")

    # Exit condition
    if user_input.lower() == "quit":
        print("\nExiting system...")
        break

    # ==========================
    # PREPROCESSING
    # ==========================
    tokens = preprocess(user_input)

    # ==========================
    # CATEGORY
    # ==========================
    if "login" in tokens or "password" in tokens:
        category = "Login Issue"
    elif "course" in tokens:
        category = "Course Access"
    elif "certificate" in tokens:
        category = "Certificate"
    elif "recording" in tokens:
        category = "Recording"
    elif "class" in tokens or "schedule" in tokens:
        category = "Schedule"
    else:
        category = "General"

    # ==========================
    # SENTIMENT
    # ==========================
    if "cannot" in tokens or "unable" in tokens:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # ==========================
    # SIMILARITY SEARCH
    # ==========================
    docs = tickets["message"].tolist()
    docs.append(user_input)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(docs)

    sim = cosine_similarity(X)
    user_sim = sim[-1][:-1]

    top_indices = user_sim.argsort()[-3:][::-1]
    top_tickets = [docs[i] for i in top_indices]

    # ==========================
    # RAG (KB)
    # ==========================
    kb_questions = kb["question"].tolist()
    kb_answers = kb["answer"].tolist()

    kb_docs = kb_questions + [user_input]
    X_kb = vectorizer.fit_transform(kb_docs)

    sim_kb = cosine_similarity(X_kb)
    best_idx = sim_kb[-1][:-1].argmax()

    answer = kb_answers[best_idx]

    # ==========================
    # NAMED ENTITIES
    # ==========================
    entities = []
    if "lms" in tokens:
        entities.append("LMS -> detected as keyword/domain term")

    # ==========================
    # FINAL OUTPUT
    # ==========================

    print("\n------------------------------------------")
    print("SMART TRAINING SUPPORT INTELLIGENCE SYSTEM")
    print("------------------------------------------\n")

    print("User Message:")
    print(user_input)

    print("\nPreprocessed Tokens:")
    print(tokens)

    print("\nPredicted Category:")
    print(category)

    print("\nPredicted Sentiment:")
    print(sentiment)

    print("\nTop Similar Tickets:")
    for i, t in enumerate(top_tickets, 1):
        print(f"{i}. {t}")

    print("\nSimple RAG Answer:")
    print(answer)

    print("\nNamed Entities:")
    for e in entities:
        print(e)
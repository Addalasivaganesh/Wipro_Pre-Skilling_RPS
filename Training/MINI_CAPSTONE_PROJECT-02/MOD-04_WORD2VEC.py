# MODULE 04 - WORD2VEC (FIXED)

import pandas as pd
from gensim.models import Word2Vec
import string

# Load data
df = pd.read_csv("resumes.csv")

# Preprocess
def preprocess(text):
    text = text.lower()
    for ch in string.punctuation:
        text = text.replace(ch, "")
    return text.split()

df['tokens'] = df['resume'].apply(preprocess)

# Train model
model = Word2Vec(df['tokens'].tolist(), vector_size=50, window=2, min_count=1)

# Comparisons
pairs = [
    ("python", "nlp"),
    ("java", "spring"),
    ("react", "angular"),
    ("sql", "analysis")
]

for w1, w2 in pairs:
    if w1 in model.wv and w2 in model.wv:
        print(f"{w1} vs {w2}: {model.wv.similarity(w1, w2):.2f}")
    else:
        print(f"{w1} or {w2} not found")
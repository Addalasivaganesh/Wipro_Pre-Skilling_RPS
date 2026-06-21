import pandas as pd
import string
from gensim.models import Word2Vec

# Preprocessing function (from Module-01)
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = text.split()
    return tokens

# Load dataset
df = pd.read_csv("DATASETS/support_tickets.csv")

# Apply preprocessing to all messages
df["tokens"] = df["message"].apply(preprocess)

# Prepare sentences for Word2Vec
sentences = df["tokens"].tolist()

# Train Word2Vec model
model = Word2Vec(sentences=sentences, vector_size=50, window=3, min_count=1, workers=4)

# Print vector for "course"
print("\nVector for 'course':")
print(model.wv["course"])

# Print vector for "certificate"
print("\nVector for 'certificate':")
print(model.wv["certificate"])

# Find similar words
print("\nWords similar to 'course':")
print(model.wv.most_similar("course"))

# Compare similarities
print("\nSimilarity between words:")
print("course vs lms:", model.wv.similarity("course", "lms"))
print("certificate vs download:", model.wv.similarity("certificate", "download"))
print("recording vs link:", model.wv.similarity("recording", "link"))
print("trainer vs class:", model.wv.similarity("trainer", "class"))
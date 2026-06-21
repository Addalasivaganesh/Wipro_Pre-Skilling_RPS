import pandas as pd
import string
from gensim.models import Word2Vec

df = pd.read_csv("faq_data.csv")

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.split()

df['tokens'] = df['question'].apply(preprocess_text)

sentences = df['tokens'].tolist()

model = Word2Vec(sentences=sentences, vector_size=50, window=3, min_count=1)

word = input("Enter word: ")

if word in model.wv:
    print(model.wv.most_similar(word))
else:
    print("Word not found")
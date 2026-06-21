import pandas as pd
import string

df = pd.read_csv("faq_data.csv")

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    return tokens

df['tokens'] = df['question'].apply(preprocess_text)

print(df[['question', 'tokens']])
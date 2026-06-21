# MODULE 01 - TEXT PREPROCESSING

import pandas as pd
import string

# Load dataset
df = pd.read_csv("resumes.csv")


# Preprocessing function
def preprocess_text(text):
    text = text.lower()

    for ch in string.punctuation:
        text = text.replace(ch, "")

    tokens = text.split()
    return tokens


# Apply preprocessing
df['tokens'] = df['resume'].apply(preprocess_text)

# Output
print(df[['candidate_id', 'tokens']])
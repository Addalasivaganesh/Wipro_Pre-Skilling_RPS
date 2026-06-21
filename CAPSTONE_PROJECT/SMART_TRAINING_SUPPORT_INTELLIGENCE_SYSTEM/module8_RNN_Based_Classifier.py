import pandas as pd
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load your dataset (main dataset)
df = pd.read_csv("support_tickets.csv")

print("\n--- Named Entity Recognition (Dataset Based) ---\n")

# Using first 5 rows for demo
for i, text in enumerate(df['text'].dropna().head(5)):

    doc = nlp(text)

    print(f"\nSentence {i+1}: {text}")

    for ent in doc.ents:
        print(f"{ent.text} → {ent.label_}")
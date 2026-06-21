import pandas as pd
import spacy

#  Load spaCy model
nlp = spacy.load("en_core_web_sm")

#  Load datasets (optional but good practice)
tickets = pd.read_csv("DATASETS/support_tickets.csv")
kb = pd.read_csv("DATASETS/knowledge_base.csv")

#  Take input
user_input = input("Enter your message: ")

#  Apply NER
doc = nlp(user_input)

#  Output
print("\nMessage:")
print(user_input)

print("\nNamed Entities:")

#  Extract and print entities
for ent in doc.ents:
    print(ent.text, "->", ent.label_)
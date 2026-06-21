# MODULE 06 - NER

import spacy

# Load model
nlp = spacy.load("en_core_web_sm")

# Input
text = "Rahul Sharma worked at Microsoft in Hyderabad."

doc = nlp(text)

# Output
for ent in doc.ents:
    print(ent.text, "->", ent.label_)
import spacy

nlp = spacy.load(
    "en_core_web_sm"
)

text = """
Sivaganesh addala works at wipro hyderabad.
"""

doc = nlp(text)

for entity in doc.ents:
    print(
        entity.text,
        entity.label_
    )
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("faq_data.csv")

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['question'])

print("Vocabulary:")
print(vectorizer.get_feature_names_out())

print("\nMatrix Shape:")
print(tfidf_matrix.shape)

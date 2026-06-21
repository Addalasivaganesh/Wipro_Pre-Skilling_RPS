from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "Python is easy",
    "Python is powerful",
    "Java is powerful"
]

vectorizer = TfidfVectorizer()

tfidf = vectorizer.fit_transform(documents)

print("Features:", vectorizer.get_feature_names_out())
print("\nTF-IDF Matrix:\n", tfidf.toarray())
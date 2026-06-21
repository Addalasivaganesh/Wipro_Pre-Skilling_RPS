from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "I love cricket",
    "I love football",
    "I love sports"
]

vectorizer = TfidfVectorizer(stop_words='english')

tfidf = vectorizer.fit_transform(documents)

print("Features:", vectorizer.get_feature_names_out())
print("\nTF-IDF Matrix:\n", tfidf.toarray())
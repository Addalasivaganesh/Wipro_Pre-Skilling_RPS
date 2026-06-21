from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Extended dataset
texts = [
    "good movie",
    "amazing movie",
    "bad movie",
    "terrible movie",
    "excellent movie",
    "awful movie"
]

labels = [
    "Positive",
    "Positive",
    "Negative",
    "Negative",
    "Positive",
    "Negative"
]

# Vectorize
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train
model = MultinomialNB()
model.fit(X, labels)

# Test
test_text = ["good movie"]
X_test = vectorizer.transform(test_text)

prediction = model.predict(X_test)

print("Prediction:", prediction[0])
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
texts = [
    "good movie",
    "amazing movie",
    "bad movie",
    "terrible movie"
]

labels = [
    "Positive",
    "Positive",
    "Negative",
    "Negative"
]

# Convert text → numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Test prediction
test_text = ["good movie"]
X_test = vectorizer.transform(test_text)

prediction = model.predict(X_test)

print("Prediction:", prediction[0])
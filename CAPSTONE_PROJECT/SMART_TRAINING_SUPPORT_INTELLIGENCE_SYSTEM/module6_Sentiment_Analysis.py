import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
df = pd.read_csv("DATASETS/support_tickets.csv")

# Input column
X = df['message']

# Output columns
y_category = df['category']
y_sentiment = df['sentiment']

# TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X_vector = vectorizer.fit_transform(X)

# Train CATEGORY model
model_category = MultinomialNB()
model_category.fit(X_vector, y_category)

# Train SENTIMENT model (IMPORTANT)
model_sentiment = MultinomialNB()
model_sentiment.fit(X_vector, y_sentiment)

# User input
user_input = input("Enter your message: ")

# Transform input
user_vector = vectorizer.transform([user_input])

# Predictions
category_pred = model_category.predict(user_vector)
sentiment_pred = model_sentiment.predict(user_vector)

# FINAL OUTPUT
print("\nMessage:")
print(user_input)

print("\nPredicted Category:")
print(category_pred[0])

print("\nPredicted Sentiment:")
print(sentiment_pred[0])
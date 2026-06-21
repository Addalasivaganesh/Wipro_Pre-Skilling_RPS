import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load dataset
df = pd.read_csv("DATASETS/support_tickets.csv")

# Take only message column
documents = df['message'].tolist()

# User input
user_input = input("Enter your message: ")

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words='english')

# Fit on dataset
vectorizer.fit(documents)

# Transform only user input
user_vector = vectorizer.transform([user_input])

# Get feature names (words)
features = vectorizer.get_feature_names_out()

# Convert to array
scores = user_vector.toarray()[0]

# Get words with score > 0 (important words)
important_words = [features[i] for i in range(len(scores)) if scores[i] > 0]


print("\nTicket:")
print(user_input)
print("\nImportant Words:")
for word in important_words:
    print(word)
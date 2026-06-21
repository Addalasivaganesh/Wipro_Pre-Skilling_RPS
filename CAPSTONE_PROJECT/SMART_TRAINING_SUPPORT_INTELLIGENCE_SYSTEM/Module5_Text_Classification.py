import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

#  Step 1: Load your dataset
df = pd.read_csv("DATASETS/support_tickets.csv")

#  Step 2: Features and labels
X = df['message']     # input text
y = df['category']    # category output

#  Step 3: TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X_vector = vectorizer.fit_transform(X)

#  Step 4: Train model
model = MultinomialNB()
model.fit(X_vector, y)

#  Step 5: User input
user_input = input("Enter your message: ")

#  Step 6: Transform user input
user_vector = vectorizer.transform([user_input])

#  Step 7: Predict category
prediction = model.predict(user_vector)

#  Step 8: Output (exact format you want)
print("\nMessage:")
print(user_input)

print("\nPredicted Category:")
print(prediction[0])

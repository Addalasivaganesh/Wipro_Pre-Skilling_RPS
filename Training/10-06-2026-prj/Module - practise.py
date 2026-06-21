#Importing all the packages we need

import pandas as pd
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec

#Loading the Dataset
df = pd.read_csv("faq_data.csv")

#Module-01 -- TEXT-PREPROCESSING.
#Function for pre-processing

def preprocessing_text(text):
    text = text.lower()

    #Removing punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    #Tokenization (Splitting into words)
    tokens = text.split()

    #Word counting
    word_count = len(tokens)

    return tokens, word_count

#Apply preprocessing on questions
df['tokens'], df['word_count'] = zip(*df['question'].apply(preprocessing_text))

#Displaying result
print(df[['question', 'tokens', 'word_count']])

# #-------------------------
# #Checking the module is working fine or nor
# def test_preprocessing():
#     sample = input("Enter your query :" )
#     tokens, count = preprocessing_text(sample)
#
#     print("Original", sample)
#     print("Tokens", tokens)
#     print("Word count:", count)
# #Calling the function
# test_preprocessing()
# #---------------------------

#Module-02 -- TF-IDF ANALYSIS.
# Initialize TF-IDF Vectorizer

vectorizer = TfidfVectorizer(stop_words='english')

# Fit and transform questions
tfidf_matrix = vectorizer.fit_transform(df['question'])

# Get vocabulary
vocabulary = vectorizer.get_feature_names_out()

# Print vocabulary
print("Vocabulary:\n", vocabulary)

# Print matrix shape
print("\nTF-IDF Matrix Shape:", tfidf_matrix.shape)

# Convert to DataFrame for better understanding
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vocabulary)

# Display TF-IDF values
print("\nTF-IDF Matrix:\n")
print(tfidf_df)

# Display Top Keywords for each question
print("\nTop Keywords for each question:\n")

for i in range(len(tfidf_df)):
    top_words = tfidf_df.iloc[i].sort_values(ascending=False).head(3)
    print(f"Q{i+1}:", list(top_words.index))

#Module-03 -- SIMILARITY SEARCH ENGINE.
# Function: Search Engine

def search_faq():
    user_query = input("Enter your question: ")

    # Convert query to TF-IDF
    query_vec = vectorizer.transform([user_query])

    # Cosine similarity
    similarity_scores = cosine_similarity(query_vec, tfidf_matrix)

    # Get top 3 matches
    top_indices = similarity_scores[0].argsort()[::-1][:3]

    print("\nTop Matches:\n")

    for i, idx in enumerate(top_indices):
        print(f"{i + 1}. {df['question'][idx]}")
        print(f"   Score: {similarity_scores[0][idx]:.2f}\n")


# Call function
search_faq()

#Module-04 -- SIMPLE RAG- IMPLEMENTATION.
# Preprocessing function

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Apply preprocessing
df['clean_question'] = df['question'].apply(preprocess_text)

# TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['clean_question'])

# RAG function (Retrieval only)
def rag_system():
    user_query = input("Ask your question: ")

    # Preprocess query
    clean_query = preprocess_text(user_query)

    # Convert to vector
    query_vec = vectorizer.transform([clean_query])

    # Cosine similarity
    similarity_scores = cosine_similarity(query_vec, tfidf_matrix)

    # Best match index
    best_index = similarity_scores.argmax()

    # Output
    print("\n Retrieved FAQ:")
    print(df['question'][best_index])

    print("\n Answer:")
    print(df['answer'][best_index])


# Run system
rag_system()


#Module-05 -- FAQ CLASSIFICATION.
# Classification function

def classify_question(question):
    question = question.lower()

    if "password" in question or "login" in question:
        return "Login"

    elif "course" in question or "access" in question:
        return "Course Access"

    elif "certificate" in question:
        return "Certificate"

    elif "recording" in question:
        return "Recordings"

    elif "profile" in question:
        return "Profile"

    elif "class" in question or "schedule" in question:
        return "Schedule"

    else:
        return "Other"


# Apply classification
df['category'] = df['question'].apply(classify_question)

# Display results
print(df[['question', 'category']])


#Module-06 -- WORD2VEC EXPLORATION
# Apply preprocessing
df['tokens'] = df['question'].apply(preprocess_text)

# Prepare sentences for Word2Vec
sentences = df['tokens'].tolist()

# Train Word2Vec model
model = Word2Vec(
    sentences=sentences,
    vector_size=50,   # size of embedding
    window=3,         # context window
    min_count=1,      # include all words
    workers=2
)

# Find similar words
print("Similar words:\n")

words_to_test = ["password", "certificate", "course"]

for word in words_to_test:
    if word in model.wv:
        print(f"{word} -> {model.wv.most_similar(word)}\n")

#Module-07 -- PROMT ENGINEERING
# ZERO SHOT, ONE SHOT, FEW SHOT

#Module-08 -- FINAL INTEGRATION



import pandas as pd
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
from datetime import datetime

# Load dataset
df = pd.read_csv("faq_data.csv")


# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    return text, tokens


# Apply preprocessing
df['clean_question'], df['tokens'] = zip(*df['question'].apply(preprocess_text))

# TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['clean_question'])


# Classification (Module 5)
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

# Word2Vec (Module 6)
sentences = df['tokens'].tolist()

word2vec_model = Word2Vec(
    sentences=sentences,
    vector_size=50,
    window=3,
    min_count=1,
    workers=2
)

# BONUS: Search history
search_history = []


# BONUS: Keyword highlighting
def highlight_keywords(query, text):
    query_words = set(query.split())
    words = text.split()

    highlighted = []
    for w in words:
        if w in query_words:
            highlighted.append(w.upper())  # highlight
        else:
            highlighted.append(w)

    return " ".join(highlighted)


# MAIN MENU SYSTEM
def menu():
    while True:
        print("\n==============================")
        print("INTELLIGENT FAQ SYSTEM")
        print("==============================")
        print("1. Search FAQ (Top 3 Answers)")  # Modified
        print("2. Show Top 3 Similar Questions")
        print("3. View TF-IDF Keywords")
        print("4. Show Categories")
        print("5. Word2Vec Similar Words")
        print("6. View Search History")  # New
        print("7. Exit")  # Updated

        choice = input("Enter your choice: ")

        # 1. Top 3 Answers + Scores + Highlight
        if choice == '1':
            user_query = input("\nEnter Question: ")
            clean_query, _ = preprocess_text(user_query)

            query_vec = vectorizer.transform([clean_query])
            similarity_scores = cosine_similarity(query_vec, tfidf_matrix)

            top_indices = similarity_scores[0].argsort()[::-1][:3]

            print("\nTop 3 Answers:\n")

            for i, idx in enumerate(top_indices):
                question = df['question'][idx]
                answer = df['answer'][idx]
                score = round(similarity_scores[0][idx], 2)

                highlighted_q = highlight_keywords(clean_query, question.lower())

                print(f"{i + 1}. {question}")
                print(f"   Highlight: {highlighted_q}")
                print(f"   Score: {score}")
                print(f"   Answer: {answer}")
                print(f"   Category: {df['category'][idx]}\n")

            # Save history with timestamp
            search_history.append((datetime.now(), user_query))

        # 2. Top 3 Matches
        elif choice == '2':
            user_query = input("\nEnter Question: ")
            clean_query, _ = preprocess_text(user_query)

            query_vec = vectorizer.transform([clean_query])
            similarity_scores = cosine_similarity(query_vec, tfidf_matrix)

            top_indices = similarity_scores[0].argsort()[::-1][:3]

            print("\nTop 3 Matches:\n")

            for i, idx in enumerate(top_indices):
                print(f"{i + 1}. {df['question'][idx]}")
                print(f"   Score: {round(similarity_scores[0][idx], 2)}\n")

        # 3. TF-IDF Keywords
        elif choice == '3':
            vocabulary = vectorizer.get_feature_names_out()
            print("\nTF-IDF Keywords:\n")
            print(vocabulary)

        # 4. Show Categories
        elif choice == '4':
            print("\nQuestions with Categories:\n")
            print(df[['question', 'category']])

        # 5. Word2Vec Similar Words
        elif choice == '5':
            word = input("\nEnter word: ")
            if word in word2vec_model.wv:
                print("\nSimilar Words:\n")
                print(word2vec_model.wv.most_similar(word))
            else:
                print("Word not found in vocabulary")

        # 6. View History
        elif choice == '6':
            print("\nSearch History:\n")
            for t, q in search_history:
                print(t.strftime("%H:%M:%S"), "->", q)

        # 7. Exit
        elif choice == '7':
            print("Exiting... Goodbye buddy")
            break

        else:
            print("Invalid choice! Try again.")


# Run system
menu()
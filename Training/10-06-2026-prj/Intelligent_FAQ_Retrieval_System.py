import pandas as pd
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec

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


# MAIN MENU SYSTEM
def menu():
    while True:
        print("\n==============================")
        print("INTELLIGENT FAQ SYSTEM")
        print("==============================")
        print("1. Search FAQ (Best Answer)")
        print("2. Show Top 3 Similar Questions")
        print("3. View TF-IDF Keywords")
        print("4. Show Categories")
        print("5. Word2Vec Similar Words")
        print("6. Exit")

        choice = input("Enter your choice: ")

        # 1. RAG (Best Answer)
        if choice == '1':
            user_query = input("\nEnter Question: ")
            clean_query, _ = preprocess_text(user_query)

            query_vec = vectorizer.transform([clean_query])
            similarity_scores = cosine_similarity(query_vec, tfidf_matrix)

            best_index = similarity_scores.argmax()

            print("\nBest Match:")
            print(df['question'][best_index])

            print("\nSimilarity Score:")
            print(round(similarity_scores[0][best_index], 2))

            print("\nAnswer:")
            print(df['answer'][best_index])

            print("\nCategory:")
            print(df['category'][best_index])

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

        # 6. Exit
        elif choice == '6':
            print("Exiting... Goodbye buddy")
            break

        else:
            print("Invalid choice! Try again.")


# Run system
menu()
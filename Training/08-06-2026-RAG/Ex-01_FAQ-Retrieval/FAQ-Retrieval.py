from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Step-01 Reading the file
faq_questions = []
faq_answers = []
with open("faq.txt", "r") as file :
    for line in file :
        question, answer = line.strip().split("|")
        faq_questions.append(question)
        faq_answers.append(answer)

#Step-02 converting TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(faq_questions)

## step-03 loop for unlimited questions
while True:
    user_question = input("\n Ask your question(Type 'exit to stop): ")
    #Stop condition
    if user_question == "exit" :
        print("Exiting chat bot...")
        break

    # step-04 transforming input
    user_vector = vectorizer.transform([user_question])

    #Step-05 similarity
    similarity = cosine_similarity(user_vector, tfidf_matrix)

    #step-06 best match
    best_index = similarity.argmax()

    #step-07 output
    print("\n Matched Question :", faq_questions[best_index])
    print("\n Answer: ", faq_answers[best_index])

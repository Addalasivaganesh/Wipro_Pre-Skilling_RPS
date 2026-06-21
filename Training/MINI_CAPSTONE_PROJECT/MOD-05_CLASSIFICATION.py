import pandas as pd

# Load dataset
df = pd.read_csv("faq_data.csv")


# Classification Function (Rule-Based NLP)
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

#  Display result
print(df[['question', 'category']])
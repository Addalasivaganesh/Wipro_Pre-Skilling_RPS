# MODULE 05 - CLASSIFICATION

import pandas as pd

# Load data
df = pd.read_csv("resumes.csv")


# Classification function
def classify_resume(text):
    text = text.lower()

    if "python" in text and "nlp" in text:
        return "AI Engineer"
    elif "java" in text:
        return "Backend Developer"
    elif "react" in text or "angular" in text:
        return "Frontend Developer"
    elif "sql" in text or "power bi" in text:
        return "Data Analyst"
    else:
        return "Unknown"


# Apply
df['category'] = df['resume'].apply(classify_resume)

print(df[['candidate_id', 'category']])

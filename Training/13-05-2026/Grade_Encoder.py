import pandas as pd

data = {
    "Grade":["A", "B", "C", "D"]
}
df = pd.DataFrame(data)

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
df["GradeEncoder"] = encoder.fit_transform(df["Grade"])
print(df)
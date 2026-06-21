import pandas as pd

data = {
    "StudyHours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 60, 70, 80],
    "Attendance": [60, 70, 75, 85, 95]
}

df = pd.DataFrame(data)
print(df)

from sklearn.preprocessing import StandardScaler

scalar = StandardScaler()

#1. Learn dataset stats
#2. Apply scaling formula
scaled_data = scalar.fit_transform(df)
print(scaled_data)

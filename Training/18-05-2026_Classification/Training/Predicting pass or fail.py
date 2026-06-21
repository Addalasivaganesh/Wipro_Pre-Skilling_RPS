import pandas as pd

data = {
    "StudyHours": [1,2,3,4,5,6,7,8],

    "Attendance": [55,60,65,70,75,85,90,95],

    "Result": [
        "Fail",
        "Fail",
        "Fail",
        "Pass",
        "Pass",
        "Pass",
        "Pass",
        "Pass"
    ]
}

df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data)
print(df)

X = df[["StudyHours", "Attendance"]]

y= df[["Result"]]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train)
print(y_train)
print(X_test)
print(y_test)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Testing data prediction", y_pred)

prediction = model.predict([[5, 80]])
print(prediction)
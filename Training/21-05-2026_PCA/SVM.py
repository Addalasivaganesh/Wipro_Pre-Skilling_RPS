import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.svm import SVC

from sklearn.metrics import accuracy_score


# Create Dataset
data = {
    "StudyHours": [
        1,2,3,4,5,
        6,7,8,9,10
    ],

    "Attendance": [
        50,55,60,65,70,
        75,80,85,90,95
    ],

    "Result": [
        "Fail",
        "Fail",
        "Fail",
        "Fail",
        "Pass",
        "Pass",
        "Pass",
        "Pass",
        "Pass",
        "Pass"
    ]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

#Features
X = df[["StudyHours",
        "Attendance"]]

#Target
y = df["Result"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state = 42
)

#Model SVM
model = SVC(
    kernel = "linear"
)

#Training the model
model.fit(X_train, y_train)
print("\n model training completed")

#Predicting the values
y_pred = model.predict(X_test)
print("\n Predictions")
print(y_pred)

#Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\n Accuracy:", accuracy)

#predicting for new student
prediction = model.predict([[6, 80]])

print("\n Predicting for new student")
print(prediction)


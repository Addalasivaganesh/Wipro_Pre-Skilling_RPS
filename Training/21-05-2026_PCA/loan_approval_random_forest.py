import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt
# Create Dataset
data = {
    "Income": [
        25000,
        30000,
        35000,
        40000,
        50000,
        60000,
        70000,
        80000,
        90000,
        100000
    ],

    "CreditScore": [
        500,
        550,
        580,
        620,
        680,
        700,
        720,
        760,
        800,
        850
    ],

    "ExistingLoans": [
        3,
        3,
        2,
        2,
        2,
        1,
        1,
        1,
        0,
        0
    ],

    "LoanApproved": [
        "No",
        "No",
        "No",
        "No",
        "Yes",
        "Yes",
        "Yes",
        "Yes",
        "Yes",
        "Yes"
    ]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

#features
X = df[["Income","CreditScore", "ExistingLoans"]]

#Target
y = df["LoanApproved"]

#Train_Test_Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state = 42
)

#Create Random_forest model
model = RandomForestClassifier(
    n_estimators = 20,
    random_state = 42
)

#train the model
model.fit(X_train, y_train)
print("\n Model training completed")

from sklearn.tree import DecisionTreeClassifier
#Predictions
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("\n Predictions")
print(y_pred)

#Accuracy

accuracy = accuracy_score(y_test, y_pred)
print("\n Accuracy:")
print(accuracy)

#Feature importance
importance = pd.DataFrame({
    "Features": X.columns,
    "Importance": model.feature_importances_
})

print("\n Feature Importance")
print(importance)

#Tree

from sklearn.tree import plot_tree

plt.figure(figsize = (10,6))
plot_tree(
    model,
    feature_names=X.columns,

    class_names=model.classes_,

    filled = True
)
plt.show()


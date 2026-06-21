import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Create Dataset
data = {
    "Experience": [
        1,2,3,4,5,
        6,7,8,9,10
    ],

    "TrainingHours": [
        10,15,20,25,30,
        35,40,45,50,55
    ],

    "PerformanceRating": [
        45,50,55,60,68,
        72,78,82,88,95
    ]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)







# Features (Input)
X = df[["Experience", "TrainingHours"]]

# Target (Output)
y = df["PerformanceRating"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nX Train")
print(X_train)

print("\nX Test")
print(X_test)

# Create Model
model = LinearRegression()

# Train Model
model.fit(X_train, y_train)

print("\nModel Training Completed")

# Training Score
train_score = model.score(
    X_train,
    y_train
)

print("\nTraining Score")
print(train_score)

# Testing Score
test_score = model.score(
    X_test,
    y_test
)

print("\nTesting Score")
print(test_score)
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Create Dataset
data = {
    "HouseSize": [
        500,
        700,
        900,
        1100,
        1300,
        1500,
        1900,
        2100,
        2300
    ],

    "Price": [
        20,
        28,
        35,
        42,
        50,
        58,
        65,
        72,
        90
    ]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

# Features (Input)
X = df[["HouseSize"]]

# Target (Output)
y = df["Price"]

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

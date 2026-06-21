import pandas as pd

from sklearn.linear_model import LinearRegression


# Create Dataset
data = {
    "StudyHours": [
        1,2,3,4,5,
        6,7,8,9,10
    ],

    "Attendance": [
        55,60,65,70,75,
        80,85,90,95,98
    ],

    "SleepHours": [
        4,5,5,6,6,
        7,7,8,8,8
    ],

    # Intentionally Useless Feature
    "FavoriteJerseyNumber": [
        7,10,18,9,45,
        99,3,8,11,77
    ],

    "Marks": [
        35,40,48,55,62,
        70,78,85,92,96
    ]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)


# Features (Input)
X = df[
    [
        "StudyHours",
        "Attendance",
        "SleepHours",
        "FavoriteJerseyNumber"
    ]
]


# Target (Output)
y = df["Marks"]


# Create Model
model = LinearRegression()


# Train Model
model.fit(X, y)

print("\nModel Training Completed")


# Feature Coefficients
coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

print("\nFeature Coefficients")
print(coefficients)
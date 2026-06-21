import pandas as pd

from sklearn.linear_model import LinearRegression


# Create Dataset
data = {
    "Experience": [
        1,2,3,4,5,
        6,7,8,9,10
    ],

    "ProjectsCompleted": [
        2,3,4,5,6,
        7,8,9,10,12
    ],

    "PerformanceScore": [
        60,65,70,72,75,
        80,85,88,90,95
    ],

    # Intentionally Useless Feature
    "ShoeSize": [
        6,7,8,9,10,
        6,7,8,9,10
    ],

    "Salary": [
        25000,
        30000,
        35000,
        42000,
        50000,
        58000,
        65000,
        72000,
        82000,
        95000
    ]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)


# Features (Input)
X = df[
    [
        "Experience",
        "ProjectsCompleted",
        "PerformanceScore",
        "ShoeSize"
    ]
]


# Target (Output)
y = df["Salary"]


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
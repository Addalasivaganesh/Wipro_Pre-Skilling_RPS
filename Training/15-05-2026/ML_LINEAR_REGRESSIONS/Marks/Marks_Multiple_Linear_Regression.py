import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Create Dataset
data = {
    "StudyHours": [1,2,3,4,5,6,7,8],
    "SleepHours": [6,7,6,5,8,7,6,7],
    "Marks": [30,40,50,60,70,75,85,90]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

# Features (Input)
X = df[["StudyHours", "SleepHours"]]

# Target (Output)
y = df["Marks"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nX Train")
print(X_train)

print("\nX Test")
print(X_test)

print("\ny Train")
print(y_train)

print("\ny Test")
print(y_test)

# Model
model = LinearRegression()

model.fit(X_train, y_train)
print("\nModel Training Completed")

y_pred = model.predict(X_test)

print("\nPredicted Marks")
print(y_pred)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nActual Marks")
print(y_test.values)

print("\nPredicted Marks")
print(y_pred)

print("\nMAE")
print(mae)

print("\nMSE")
print(mse)

print("\nRMSE")
print(rmse)

print("\nR2 Score")
print(r2)
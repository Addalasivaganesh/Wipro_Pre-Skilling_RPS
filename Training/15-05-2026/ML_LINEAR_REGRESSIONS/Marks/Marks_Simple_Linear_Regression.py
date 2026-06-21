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
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 40, 50, 60, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

# Features (Input)
X = df[["StudyHours"]]

# Target (Output)
y = df["Marks"]

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

print("\ny Train")
print(y_train)

print("\ny Test")
print(y_test)

# Create Model
model = LinearRegression()

# Train Model
model.fit(X_train, y_train)
print("\nModel Training Completed")

# Make Predictions
y_pred = model.predict(X_test)

print("\nPredicted Marks")
print(y_pred)

# Model Evaluation

# Mean Absolute Error
mae = mean_absolute_error(y_test, y_pred)

# Mean Squared Error
mse = mean_squared_error(y_test, y_pred)

# Root Mean Squared Error
rmse = np.sqrt(mse)

# R2 Score
r2 = r2_score(y_test, y_pred)

# Print Results
print("\nActual Marks")
print(y_test.values)

print("\nPredicted Marks")
print(y_pred)

print("\nMean Absolute Error (MAE)")
print(mae)

print("\nMean Squared Error (MSE)")
print(mse)

print("\nRoot Mean Squared Error (RMSE)")
print(rmse)

print("\nR2 Score")
print(r2)

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
    "AdvertisingSpend": [10, 15, 20, 25, 30, 35, 40, 45],
    "Sales": [100, 140, 180, 220, 260, 300, 340, 380]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

# Features (Input)
X = df[["AdvertisingSpend"]]

# Target (Output)
y = df["Sales"]

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

print("\nPredicted Sales")
print(y_pred)

# Model Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Print Results
print("\nActual Sales")
print(y_test.values)

print("\nPredicted Sales")
print(y_pred)

print("\nMean Absolute Error (MAE)")
print(mae)

print("\nMean Squared Error (MSE)")
print(mse)

print("\nRoot Mean Squared Error (RMSE)")
print(rmse)

print("\nR2 Score")
print(r2)
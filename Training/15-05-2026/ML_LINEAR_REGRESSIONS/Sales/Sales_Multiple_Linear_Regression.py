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
    "ProductPrice": [100, 95, 90, 85, 80, 75, 70, 65],
    "StoreSize": [200, 220, 250, 270, 300, 320, 350, 370],
    "Sales": [100, 140, 180, 220, 260, 300, 340, 380]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

# Features (Input)
X = df[["AdvertisingSpend", "ProductPrice", "StoreSize"]]

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

# Mean Absolute Error
mae = mean_absolute_error(y_test, y_pred)

# Mean Squared Error
mse = mean_squared_error(y_test, y_pred)

# Root Mean Squared Error
rmse = np.sqrt(mse)

# R2 Score
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
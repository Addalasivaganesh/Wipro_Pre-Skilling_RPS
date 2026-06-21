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
    "Area": [800, 1000, 1200, 1400, 1600, 1800, 2000, 2200],
    "Price": [2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

# Features (Input)
X = df[["Area"]]

# Target (Output)
y = df["Price"]

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

# Create Model
model = LinearRegression()

# Train Model
model.fit(X_train, y_train)
print("\nModel Training Completed")

# Make Predictions
y_pred = model.predict(X_test)

print("\nPredicted Price")
print(y_pred)

# Model Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nActual Price")
print(y_test.values)

print("\nPredicted Price")
print(y_pred)

print("\nMean Absolute Error (MAE)")
print(mae)

print("\nMean Squared Error (MSE)")
print(mse)

print("\nRoot Mean Squared Error (RMSE)")
print(rmse)

print("\nR2 Score")
print(r2)
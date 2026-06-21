import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Dataset
data = {
    "Experience": [1,2,3,4,5,6,7,8],
    "Salary": [25000,30000,35000,40000,45000,50000,60000,70000]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

X = df[["Experience"]]
y = df["Salary"]

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

model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel Training Completed")

y_pred = model.predict(X_test)

print("\nPredicted Salary")
print(y_pred)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nActual Salary")
print(y_test.values)

print("\nPredicted Salary")
print(y_pred)

print("\nMAE")
print(mae)

print("\nMSE")
print(mse)

print("\nRMSE")
print(rmse)

print("\nR2 Score")
print(r2)
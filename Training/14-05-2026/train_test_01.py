import pandas as pd

data = {
    "Experience": [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Age": [22, 24, 26, 28, 30, 32, 34, 36, 38 ,40],
    "PerformanceScore": [60, 65, 70, 72, 75, 80, 85, 88, 90, 95],
    "Salary": [25000, 30000, 35000, 40000, 45000,
               52000, 60000, 68000, 75000, 85000],
}

df = pd.DataFrame(data)
# print(df)

x = df[["Experience", "Age", "PerformanceScore"]]

y = df["Salary"]

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size = 0.2, random_state=42)
print(x_train)
print(x_test)
print(y_train)
print(y_test)
print(x_train.shape)
print(x_test.shape)

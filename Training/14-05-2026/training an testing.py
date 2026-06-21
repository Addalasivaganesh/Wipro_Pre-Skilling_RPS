from ast import compare

import pandas as pd

data = {
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 95],
    "Marks": [35, 40, 50, 60, 65, 70, 80, 90]
}
df = pd.DataFrame(data)
print(df)

#FEATURES(x)
x = df[["StudyHours", "Attendance"]]

#Features are like sq yards, Location, 3bhk, Registered, ----.
#Target is price

#TARGET(y)
y = df["Marks"]

#performing train_test_split

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size = 0.2, random_state = 42)

print(x_train)
print(x_test)
# print(y_train)
# print(y_test)
from sklearn.linear_model import LinearRegression
# print(x_train.shape)
# print(x_test.shape)

new_data = pd.DataFrame([[6, 85]], columns = ["StudyHours", "Attendance"]) #6hrs and 85 attendance
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(x_train, y_train)

prediction = model.predict(new_data)

print("Predicted Marks:", prediction)

from sklearn.metrics import mean_absolute_error
y_pred = model.predict(x_test)

error = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", error)
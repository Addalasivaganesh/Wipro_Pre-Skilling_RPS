import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Create Dataset
data = {
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 40, 50, 60, 65, 70, 80, 90]
}
df = pd.DataFrame(data)

# print(df)

#features input
X = df[["StudyHours"]]

#Target marks
y = df["Marks"]

#Creating the  model
model = LinearRegression()
print("\n Model Created")
print(model)

#Training Model
model.fit(X, y)
print("\n Model training completed")

#predicting the Salary for 7 years Experience
# Predicted_Marks = model.predict(pd.DataFrame({"StudyHours": [x]}))

predicted_marks = model.predict(X)

#Scatter plot (Actual date)
plt.scatter(X, y)

#Regression line
plt.plot(X, predicted_marks)

#Labels
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("StudyHours vs Marks")

#Show Graph
plt.show()
plt.show()
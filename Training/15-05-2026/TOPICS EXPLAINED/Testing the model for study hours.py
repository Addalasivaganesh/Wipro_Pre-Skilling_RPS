import pandas as pd
from sklearn.linear_model import LinearRegression

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
Predicted_Marks = model.predict(pd.DataFrame({"StudyHours": [9]}))

print("\n Predicted Marks for 9hrs StudyHours is")
print(Predicted_Marks)

print(Predicted_Marks)
import pandas as pd

from sklearn.linear_model import LinearRegression

# Create Dataset
data = {
    "Experience": [1, 2, 3, 4, 5, 6],
    "Salary": [25000, 30000, 40000, 50000, 60000, 70000]
}

df = pd.DataFrame(data)

print("Dataset")
# print(df)

#Features(Input)
X = df[["Experience"]]

#Target (Output)
y = df["Salary"]

#Create model
model = LinearRegression()

print("\n Model Created")
print(model)

#Train Model using Fit()
model.fit(X, y)
print("\n Model training completed")

#predicting the Salary for 7 years Experience
Predicted_Salary = model.predict(pd.DataFrame({"Experience": [7]}))

print("\n Predicted Salary for 7 yrs Experience")
print(Predicted_Salary)
print(Predicted_Salary)
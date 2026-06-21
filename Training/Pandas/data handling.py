import pandas as pd
import numpy as np

data = {
    "EmployeeID" : [101, 102, 103, 104, 105, 106],
    "Name" : ["Rahul", "Siva", "John", "Fatima", "Arjun", "Raja"],
    "Departments" : ["IT", "HR", "IT", "FINANCE", "HR", "IT"],
    "Age" : [25, 30, 28, 35, 32, 26],
    "Salary" : [50000, 45000, 60000, 75000, np.nan, 58000],
    "Experience" : [2, 5, 4, 10, 7, 3]

}

df = pd.DataFrame(data)

#handling null values in the  dataset
# print(df.isnull())

# print(df.isnull().sum())

# #Filling the null data
# df["Salary"] = df['Salary'].fillna(df["Salary"].mean())
# print(df)

# #Adding a column
# df["Bonus"] = df["Salary"] * 0.10
# print(df)

#filling the null data
# df["Salary"] = df['Salary'].fillna(df["Salary"].mean())
# print(df)
# df["Bonus"] = df["Bonus"].fillna(df["Bonus"].mean())
# print(df)

#Updating the existing column
# df["Salary"] = df["Salary"] + 10000
# print(df)
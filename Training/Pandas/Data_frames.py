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

# print(df)
#
# print(df.head())
#
# print(df.tail())
#
# print(df.shape)
#
# print(df.columns)
#
# print(df.dtypes)

#print(df.info())
#
# print(df.describe())

# print(df["Salary"])

# print(df[["Name", "Departments", "Salary", "Experience"]])
#
# print(df.iloc[0])

# print(df.iloc[0:3])

# print(df[df["Salary"] > 50000])

# print(df[df["Departments"] == "HR"])

# print(df[(df["Departments"] == "IT") & (df["Salary"] > 50000)])
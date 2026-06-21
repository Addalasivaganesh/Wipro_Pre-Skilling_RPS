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
#
# print(df.sort_values(by = "Salary")) #low to high
#
# print(df.sort_values(by = "Salary", ascending = False))

# #Group by
# print(df.groupby("Departments")["Salary"].mean())

# print(df.groupby("Departments")["Experience"].sum())
#
# print(df.groupby("Departments")["Salary"].agg(["mean", "max", "min"]))

# print(df["Departments"].unique())
# print(df["Name"].unique())

# print(df["Departments"].value_counts())

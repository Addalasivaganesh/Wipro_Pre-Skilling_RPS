import pandas as pd
import numpy as np

data = {
    "EmployeeID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],

    "Name": ["Sivaganesh","Ayyappa", "Raja", "Lokesh", "Sunil", "Vinay", "Sai","Aravind", "Bhanu", "Pradeep"],

    "Department": ["IT", "HR", "FINANCE", "IT", "MARKETING", "FINANCE", "HR", "IT", "MARKETING", "FINANCE"],

    "AGE": [25, 22, 28, 35, 32, 29, 31, 26, 40, 27],

    "Salary": [50000, 45000, 70000, 65000, np.nan, 72000, 48000, 55000, 80000, 62000],

    "Experience": [2, 5, 6, 10, 7, 8, 4, 3, 15, 5],

    "City": ["Hyderabad", "Bangalore", "Chennai", "Hyderabad", "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Mumbai", "Chennai"],

    "PerformanceScore": [88, 76, 90, 95, 70, 92, 68, 85, 98, 80]
}

df = pd.DataFrame(data)
# print(df)

#01.
#Sorting Employees by Salary ascending
print(df.sort_values(by = "Salary", ascending = True))

#02.
#Sorting Employees by Salary decending
print(df.sort_values(by = "Salary", ascending = False))

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df["Salary"])

#01.
#now we again print the salary in the ascending order after placing the null value with mean value
print(df.sort_values(by = "Salary", ascending = True))

#02.
#now we are printing again the decending order after placing the null value with the mean value
print(df.sort_values(by = "Salary", ascending = False))

print(df[["Name", "Salary"]])

#03. Sort employees by experience decending
print(df.sort_values (by = "Experience", ascending = False))

#04. sorting employess by performance decending
print(df.sort_values(by = "PerformanceScore", ascending = False))

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

# print(df["Name"]) #Select Name Column

# print(df[["Salary", "Department"]]) #Selecting Salary and Department columns

# print(df[["AGE", "Salary", "City"]]) #Selecting AGE , Salary, City Columns

#print(df.PerformanceScore) #printing only PerformanceScore Column
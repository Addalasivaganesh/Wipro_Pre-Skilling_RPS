#Creating a barchart Experience vs salary

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Employee": [
        "Addala", "Rahul", "Alisha", "John", "Fatima",
        "Arjun", "Sara", "David", "Priya", "Karan",
        "Ali", "Zara", "Vikram", "Neha", "Omar"
    ],
    "Department":[
        "IT","HR","Finance","IT","Marketing",
        "Finance","HR","IT", "Marketing","Finance",
        "HR", "IT","Marketing","Finance","IT"
    ],
    "Age":[
        25, 30, 28, 35, 32,
        29, 31, 26, 40, 27,
        33, 24, 38, 29, 36
    ],
    "Salary":[
        50000, 45000, 70000, 65000, 55000,
        72000, 48000, 58000, 80000, 62000,
        53000, 49000, 76000, 61000, 85000
    ],
    "Experience":[
        2, 5, 6, 10, 7,
        8, 4, 3, 15, 5,
        6, 2, 12, 7, 14
    ],
    "Performance":[
        88, 76, 90, 95, 70,
        92, 68, 85, 98, 80,
        75, 82, 96 ,84, 99
    ]
}

df = pd.DataFrame(data)
# print(df)


# plt.bar(df["Experience"],df["Salary"])
# plt.title("Experience vs Salary")
# plt.xlabel("Experience (Years)")
# plt.ylabel("Salary")
# plt.show()

#01. The person who was receiving ("HIGHEST SALARY") was OMAR
#-------
#02. the person who was receiving ("LOWEST SALARY") was Rahul but here the graph showing that who has 4 years of experience has the lowest salary that is SARA
#but according to the data the person Rahul has the lowest salary
#by using the employee vs salary we get the correct graph who has the lowest

plt.bar(df["Employee"],df["Salary"])
plt.title("Employee vs Salary")
plt.xticks(rotation=90)#I helps to change the rotation of the names in the X-axis
plt.xlabel("Employee")
plt.ylabel("Salary")
plt.tight_layout()# It helps to view the graph without cutting the edges
plt.show()
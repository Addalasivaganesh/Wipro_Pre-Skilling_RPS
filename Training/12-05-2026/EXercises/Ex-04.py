#Creating a histogram

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Employee": [
        "Addala Siva Ganesh", "Rahul", "Alisha", "John", "Fatima",
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

#Creating histogram for age bins = 05, bins = 10

plt.hist(df["Age"], bins = 10)
plt.title("Histogram for Age")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

## using bins-05
#01. The 24-30 range appears most
#02. no the data was not evenly distributed

## using bins-10
#01. The 29 appears most
#02. No the data was not evenly distributed

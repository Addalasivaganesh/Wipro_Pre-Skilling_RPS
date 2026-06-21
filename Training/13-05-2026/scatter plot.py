import pandas as pd
from matplotlib import pyplot as plt

data = {
    "Student":[
        "Rahul","Alisha", "John",
        "Fatima", "Arjun"
    ],
    "StudyHours":[2, 5, 7, 4, 8],
    "Attendance":[60, 85, 95, 75, 98],
    "Marks":[40, 70, 90, 65, 96]
}

df = pd.DataFrame(data)
# print(df)

plt.scatter(df["StudyHours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()
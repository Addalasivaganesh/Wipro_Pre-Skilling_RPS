import pandas as pd

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

#Adding effort score that means adding a new feature to the machine learning
df["EffortScore"] = (df["StudyHours"] * 10 + df["Attendance"])
print(df)


df["HighAttendance"] = (df["Attendance"] > 80)
print(df)

df["Grade"] = pd.cut(df["Marks"], bins = [0, 50, 75, 100], labels = ["C", "B", "A"])

print(df)

df["StudyEfficiency"] = (df["Marks"] / df["StudyHours"])
print(df)

df["PerformanceIndex"] = (
    df["Marks"] + df["Attendance"] +df["StudyHours"] * 5
)
print(df)
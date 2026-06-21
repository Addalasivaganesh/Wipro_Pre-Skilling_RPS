import pandas as pd

data = {
    "Student":[
        "Rahul", "Alisha", "John", "Ramu",
        "Fatima", "Arjun", "Ravi", "Vijay"
    ],
    "StudyHours": [3, 4, 5, 6, 7, 8, 8, 9],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 98],
    "Marks": [80, 70, 60, 60, 70, 50, 40, 30]
}
dp = pd.DataFrame(data)
print(dp)

import pandas as pd
from scipy.stats import ttest_ind

data = {
    "Department": [
        "IT", "IT","IT",
        "HR", "HR","HR"
    ],
    "Salary":[
        65000, 70000,72000,
        45000, 48000,50000
    ]
}
df = pd.DataFrame(data)
print(df)

it_salary = df[df["Department"] == "IT"]["Salary"]
hr_salary = df[df["Department"] == "HR"]["Salary"]

t_stat, p_value = ttest_ind(it_salary, hr_salary)

print("t-statistics:", t_stat)
print("p-value:", p_value)
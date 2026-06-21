import pandas as pd

data = {
    "Class": [
        "A","A","A","A",
        "B","B","B","B",
        "C","C","C","C"
    ],
    "Marks": [
        85, 88, 90, 92,
        70, 72, 68, 75,
        95, 96, 94, 98
    ]
}
df = pd.DataFrame(data)
print(df)

class_a = df[df["Class"] == "A"]["Marks"]
class_b = df[df["Class"] == "B"]["Marks"]
class_c = df[df["Class"] == "C"]["Marks"]

from scipy.stats import f_oneway

f_stat, p_value = f_oneway(class_a, class_b, class_c)

print("F-statistics:", f_stat)
print("p-value:", p_value)
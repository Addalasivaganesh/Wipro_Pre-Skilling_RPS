import pandas as pd
from matplotlib import pyplot as plt

# data = {
#     "StudyHours": [1, 2, 3, 4, 5],
#     "Marks": [40, 50, 60, 70, 80]
# }

# df = pd.DataFrame(data)
# print(df)

# covariance = df["StudyHours"].cov(df["Marks"])
# print(covariance)

#Negative covariance
data = {
    "StudyHours": [1, 2, 3, 4, 5],
    "Marks":[90, 80, 70, 60, 50]
}
df = pd.DataFrame(data)
# print(df.cov())

plt.scatter(df["StudyHours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

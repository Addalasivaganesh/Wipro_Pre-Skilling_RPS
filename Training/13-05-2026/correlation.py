import pandas as pd
import matplotlib.pyplot as plt
#
# data = {
#     "StudyHours": [1, 2, 3, 4, 5 ,6, 7, 8],
#
#     "Marks": [35, 40, 50, 60, 65, 70, 80, 90]
# }
# df = pd.DataFrame(data)
# print(df)

# correlation = df["StudyHours"].corr(df["Marks"])
# print(correlation)

#Scatter plots

# plt.scatter(df["StudyHours"], df["Marks"])
# plt.title("SCATTER PLOT")
# plt.xlabel("StudyHours")
# plt.ylabel("Marks")
# plt.show()

# data = {
#     "MobileUsage":[1, 2, 3, 4, 5, 6, 7, 8],
#     "Marks":[90, 85, 80, 70, 65, 55, 50, 40]
# }
# df = pd.DataFrame(data)
# # print(df)
#
# plt.scatter(df["MobileUsage"], df["Marks"])
# plt.title("MobileUsage vs Marks")
# plt.xlabel("MobileUsage")
# plt.ylabel("Marks")
# plt.show()

data = {
    "StudyHours": [1, 2, 3, 4, 5],
    "Marks":[35, 45, 55, 65, 75],
    "Attendence":[60, 65, 70, 80, 90],
    "SleepHours":[8, 7, 6, 5, 4]
}

df = pd.DataFrame(data)

print(df.corr())

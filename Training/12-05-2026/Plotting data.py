import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    "Employee": [
        "Rahul","Aisha","John","Fatima","Arjun",
        "Sara","David","Priya","Karan","Meera"
    ],

    "Department": [
        "IT","HR","Finance","IT","Marketing",
        "Finance","HR","IT","Marketing","Finance"
    ],

    "Age": [25,30,28,35,32,29,31,26,40,27],

    "Salary": [
        50000,45000,70000,65000,55000,
        72000,48000,58000,80000,62000
    ],

    "Experience": [2,5,6,10,7,8,4,3,15,5],

    "PerformanceScore": [88,76,90,95,70,92,68,85,98,80]
}

df = pd.DataFrame(data)
#
# print(df)
#
# plt.plot(df["Experience"] , df["Salary"])
#
# plt.title("Experience vs Salary")
# plt.xlabel("Experience")
# plt.ylabel("Salary")
# plt.show()
# print("------------------------------------------------------")
#
# plt.bar(df["Experience"] , df["Salary"])
#
# plt.title("Experience Salary Comparision")
# plt.xlabel("Experience")
# plt.ylabel("Salary")
# plt.show()
# print("------------------------------------------------------")
# plt.barh(df["Experience"] , df["Salary"])
#
# plt.title("Horizontal Salary chart")
# plt.show()
# print("------------------------------------------------------")

#HISTOGRAM
# plt.hist(df["Age"], bins = 5)
# plt.xlabel("Age")
# plt.ylabel("Count")
#
# plt.show()
# print("------------------------------------------------------")

#SCATTER PLOT
# plt.scatter(df["Experience"] , df["Salary"])
#
# plt.title("Experience vs Salary")
# plt.xlabel("Experience")
# plt.ylabel("Salary")
# plt.show()
# print("------------------------------------------------------")

# department_counts = df["Department"].value_counts()
#
# plt.pie(
#     department_counts,
#     labels = department_counts.index,
#     autopct = "%1.1f%%" #33.3333 = 33.3
# )
#
# plt.title = ("Department_Distribution")
# plt.show()

# print("------------------------------------------------------")

# OUTLIERS

# plt.boxplot(df["Salary"])
#
# plt.title("Salary Boxplot")
#
# plt.show()

# print("------------------------------------------------------")

# df["Salary"].plot(kind = "area")
#
# plt.title = ("Salary Area Plot")
# plt.show()

# print("------------------------------------------------------")
# sns.countplot(x = "Department", data = df)
# plt.title = ("Department Count")
# plt.show()

# print("------------------------------------------------------")

# #pair plot
# sns.pairplot(df)
# plt.show()
# print("------------------------------------------------------")

#violin plot
# sns.violinplot(x = df["Salary"])
# plt.title("Salary Violin plot ")
# plt.show()
# print("------------------------------------------------------")

# #KDE plot
# sns.kdeplot(df["Salary"], fill = True)
# plt.title("Salary density plot")
# plt.show()
# print("------------------------------------------------------")



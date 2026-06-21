import pandas as pd

import matplotlib.pyplot as plt

from sklearn.cluster import KMeans


# Create Dataset
data = {
    "CreditLimit": [
        20000,
        25000,
        30000,
        45000,
        50000,
        70000,
        85000,
        100000,
        120000,
        150000
    ],

    "MonthlySpend": [
        5000,
        7000,
        8000,
        12000,
        15000,
        22000,
        28000,
        35000,
        42000,
        55000
    ]
}

df = pd.DataFrame(data)

print(df)

# Features
X = df[
    [
        "CreditLimit",
        "MonthlySpend"
    ]
]

# Store WCSS Values
wcss = []

# Try Different K Values
from sklearn.cluster import KMeans

for k in range(1, 11):
    model = KMeans(
        n_clusters=k,
        random_state=42
    )

    model.fit(X)
    wcss.append(model.inertia_)

print("\nWCSS Values")
print(wcss)

#Inertia Values
inertia_values = []
#try diffrerent K values
for k in range(1, 11):
    model = KMeans(
        n_clusters=k,
        random_state=42
    )
    model.fit(X)
    inertia_values.append(model.inertia_)
    print(f"K = {k} | Inertia = {model.inertia_}")


#plot Elbow graph
plt.plot(
    range(1,11),
    wcss,
    marker = "o")

plt.xlabel("Number of clusters(K)")
plt.ylabel("WCSS Value")
plt.title("ELBOW_METHOD")
plt.show()

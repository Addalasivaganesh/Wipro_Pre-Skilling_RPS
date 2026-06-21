import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Create Dataset
data = {
    "CustomerID": [
        101,102,103,104,105,
        106,107,108,109,110
    ],

    "AnnualIncome": [
        15000,
        18000,
        20000,
        35000,
        40000,
        60000,
        65000,
        85000,
        95000,
        120000
    ],

    "SpendingScore": [
        20,
        25,
        30,
        45,
        50,
        65,
        70,
        85,
        90,
        98
    ]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

# Features
X = df[
    [
        "AnnualIncome",
        "SpendingScore"
    ]
]

# Store WCSS Values
wcss = []

# Try Different K Values
for k in range(1, 11):
    model = KMeans(
        n_clusters=k,
        random_state=42
    )

    model.fit(X)
    wcss.append(model.inertia_)

print("\nWCSS Values")
print(wcss)

# Inertia Values
inertia_values = []

for k in range(1, 11):
    model = KMeans(
        n_clusters=k,
        random_state=42
    )
    model.fit(X)
    inertia_values.append(model.inertia_)
    print(f"K = {k} | Inertia = {model.inertia_}")

# Plot Elbow Graph
plt.plot(
    range(1, 11),
    wcss,
    marker="o"
)

plt.xlabel("Number of clusters (K)")
plt.ylabel("WCSS Value")
plt.title("ELBOW METHOD")
plt.grid(True)

plt.show()
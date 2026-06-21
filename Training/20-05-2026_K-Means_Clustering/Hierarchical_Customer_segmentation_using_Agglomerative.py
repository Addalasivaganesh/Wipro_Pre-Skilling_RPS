import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

# Create Dataset
data = {
    "CustomerID": [
        101,102,103,104,105,
        106,107,108,109,110
    ],

    "AccountBalance": [
        5000,
        7000,
        9000,
        15000,
        18000,
        25000,
        30000,
        45000,
        50000,
        65000
    ],

    "MonthlyTransactions": [
        5,
        8,
        10,
        15,
        18,
        25,
        30,
        40,
        45,
        55
    ]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

# Features
X = df[
    [
        "AccountBalance",
        "MonthlyTransactions"
    ]
]

# Create Model
model = AgglomerativeClustering(n_clusters=3)

# Fit and predict
clusters = model.fit_predict(X)

print("\nCluster Labels")
print(clusters)

# Add cluster labels to dataset
df["Cluster"] = clusters

print("\nDataset with Clusters")
print(df)

#Visualizing the Clusters
plt.scatter(df["AccountBalance"],
            df["MonthlyTransactions"],

            c = df["Cluster"]
)
plt.xlabel("AccountBalance")
plt.ylabel("Monthly Transactions")
plt.title("HIERARCHICAL CLUSTERING")
plt.show()


from scipy.cluster.hierarchy import dendrogram, linkage
linked = linkage(
    X,
    method = "ward"
)

plt.figure(figsize = (8,3))
dendrogram(linked)

plt.title("Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Distance")
plt.show()
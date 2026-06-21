import pandas as pd

import matplotlib.pyplot as plt

from sklearn.cluster import KMeans


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

#Features for clustering
X = df[["AccountBalance", "MonthlyTransactions"]]

#Create K-Means Model

model = KMeans(
    n_clusters = 3,
    random_state = 42)

#train the model
model.fit(X)
print("\nModel Training Completed")

#Get cluster labels
clusters = model.labels_
print("\nCluster Labels")
print(clusters)

#Add cluster Labels to Dataset
df["cluster"] = clusters
print("\nDataset with Cluster Labels")
print(df)

#Clusters Centers(Centroids)
print("\nCluster centers")
print(model.cluster_centers_)
print("\n Cluster Centers")

#printing cluster centers to human-readable
for index, center in enumerate(model.cluster_centers_):
    print(f"\nClusters {index}")

    print(f"Average Account Balance: {center[0]:.2f}")

    print(f"Average Monthly Transactions: {center[1]:.2f}")

#Visualizing the Clusters
plt.scatter(df["AccountBalance"],
            df["MonthlyTransactions"],

            c = df["cluster"]
)
plt.xlabel("AccountBalance")
plt.ylabel("Monthly Transactions")
plt.title("Bank customer segmentation using K-Means")
plt.show()
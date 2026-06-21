import pandas as pd

import matplotlib.pyplot as plt

from sklearn.cluster import KMeans


# Create Dataset
data = {
    "PatientID": [
        101,102,103,104,105,
        106,107,108,109,110
    ],

    "MonthlyHospitalVisits": [
        1,
        2,
        1,
        3,
        4,
        5,
        6,
        7,
        8,
        10
    ],

    "MedicalExpenses": [
        2000,
        3000,
        2500,
        5000,
        7000,
        12000,
        18000,
        25000,
        32000,
        50000
    ]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

#Features for clustering
X = df[["MonthlyHospitalVisits","MedicalExpenses"]]

#Creating k-means Model
model = KMeans(n_clusters=3,random_state=42)


#train the model
model.fit(X)
print("\n Model training completed")

#Get the cluster labels
clusters = model.labels_
print("\n Cluster Labels")
print(clusters)

#Adding the labels to dataset

df["cluster"] = clusters
print("\n Cluster Labels")
print(df["cluster"])


#Clusters Centers(Centroids)
print("\nCluster centers")
print(model.cluster_centers_)
print("\n Cluster Centers")

#printing cluster centers to human-readable
for index, center in enumerate(model.cluster_centers_):
    print(f"\nClusters {index}")

    print(f"MonthlyHospitalVisits: {center[0]:.2f}")

    print(f"MedicalExpenses: {center[1]:.2f}")

#Visualizing the Clusters
plt.scatter(df["MonthlyHospitalVisits"],
            df["MedicalExpenses"],

            c = df["cluster"]
)
plt.xlabel("MonthlyHospitalVisits")
plt.ylabel("MedicalExpenses")
plt.title("Patients customer segmentation using K-Means")
plt.show()





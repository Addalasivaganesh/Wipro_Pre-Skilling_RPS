

import pandas as pd

from sklearn.decomposition import PCA

from sklearn.preprocessing import StandardScaler


# Create Dataset
data = {
    "StudyHours": [
        1,2,3,4,5,
        6,7,8,9,10
    ],

    "Attendance": [
        55,60,65,70,75,
        80,85,90,95,98
    ],

    "SleepHours": [
        4,5,5,6,6,
        7,7,8,8,8
    ],

    "PracticeTests": [
        1,1,2,2,3,
        4,4,5,5,6
    ]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

#StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
print(scaled_data)


#PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(scaled_data)
print("\n PrincipalComponents")
print(principalComponents)

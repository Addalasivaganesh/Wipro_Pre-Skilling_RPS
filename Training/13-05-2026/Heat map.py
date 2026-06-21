import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "StudyHours": [1, 2, 3, 4, 5],
    "Marks":[35, 45, 55, 65, 75],
    "Attendence":[60, 65, 70, 80, 90],
    "SleepHours":[8, 7, 6, 5, 4]
}

df = pd.DataFrame(data)

sns.heatmap(df.corr(),annot = True)
plt.show()
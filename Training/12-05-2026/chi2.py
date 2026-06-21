import pandas as pd
from scipy.stats import ttest_ind

data = {
    "Department": [
        "IT", "IT","IT",
        "HR", "HR","HR",
        "Finance", "Finance", "Finance"
    ],
    "Promotion":[
        "Yes", "Yes", "No",
        "No", "No", "Yes",
        "Yes", "Yes", "Yes",
    ]
}
df = pd.DataFrame(data)
print(df)

table = pd.crosstab(
    df["Department"],
    df["Promotion"]
)
print(table)

from scipy.stats import chi2_contingency

chi2, p, dof, expected = chi2_contingency(table)

print("chi-square:",chi2)
print("p-value:",p)
print("dof:",dof)
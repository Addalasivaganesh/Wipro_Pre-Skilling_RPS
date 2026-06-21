import pandas as pd

data = {
    "Date": [
        "2025-01-10",
        "2025-02-13",
        "2025-03-14",
    ]
}
df = pd.DataFrame(data)


df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
print(df)

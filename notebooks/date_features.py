import pandas as pd
df = pd.read_csv("data/results.csv")
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
print(
    df[
        ["date","year","month"]
    ].head(10)
)
print(df["year"].min())
print(df["year"].max())
print(df["year"].value_counts().head())
import pandas as pd
df = pd.read_csv("data/results.csv")
print(df["home_team"].value_counts().head(20))
print(df["away_team"].value_counts().head(20))
print(df["country"].value_counts().head(20))
home_stats = df.groupby("home_team")["home_score"].agg(
    ["mean", "count"]
)

print(
    home_stats[home_stats["count"] >= 100]
    .sort_values("mean", ascending=False)
    .head(20)
)


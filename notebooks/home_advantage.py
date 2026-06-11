import pandas as pd
df = pd.read_csv("data/results.csv")
def get_result(row):

    if row["home_score"] > row["away_score"]:
        return "Home Win"

    elif row["home_score"] < row["away_score"]:
        return "Away Win"

    else:
        return "Draw"

df["result"] = df.apply(get_result, axis=1)
print(df["result"].value_counts(normalize=True) * 100)
print(df.groupby("neutral")["result"].value_counts(normalize=True) * 100)
print(df["neutral"].value_counts())
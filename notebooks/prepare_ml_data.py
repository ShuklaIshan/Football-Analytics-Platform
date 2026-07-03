import pandas as pd

df = pd.read_csv("data/model_data2.csv")

def get_result(row):

    if row["home_score"] > row["away_score"]:
        return "Home Win"

    elif row["home_score"] < row["away_score"]:
        return "Away Win"

    else:
        return "Draw"

df["result"] = df.apply(get_result, axis=1)

print(df["result"].value_counts())

features = df[
    [
        "home_win_rate",
        "home_draw_rate",
        "home_loss_rate",
        "away_win_rate",
        "away_draw_rate",
        "away_loss_rate",
        "home_goal_difference",
        "away_goal_difference",
    ]
]

target = df["result"]

print(features.shape)
print(target.shape)

features.to_csv(
    "data/features.csv",
    index=False
)

target.to_csv(
    "data/target.csv",
    index=False
)
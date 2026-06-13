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

away_matches = df["away_team"].value_counts()

away_wins = (
    df[df["result"] == "Away Win"]
    ["away_team"]
    .value_counts()
)

away_win_rate = (
    away_wins / away_matches
) * 100

away_win_rate = away_win_rate.fillna(0)

draws = (
    df[df["result"] == "Draw"]
    ["away_team"]
    .value_counts()
)

draw_rate = (
    draws / away_matches
) * 100

draw_rate = draw_rate.fillna(0)


losses = (
    df[df["result"] == "Home Win"]
    ["away_team"]
    .value_counts()
)

loss_rate = (
    losses / away_matches
) * 100

loss_rate = loss_rate.fillna(0)

team_stats = pd.DataFrame({
    "away_win_rate": away_win_rate,
    "away_draw_rate": draw_rate,
    "away_loss_rate": loss_rate
})

team_stats = team_stats.reset_index()

team_stats.columns = [
    "team",
    "away_win_rate",
    "away_draw_rate",
    "away_loss_rate"
]

print(team_stats.head())
team_stats.to_csv(
    "data/away_team_stats.csv",
    index=False
)

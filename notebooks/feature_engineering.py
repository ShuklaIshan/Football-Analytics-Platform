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

home_matches = df["home_team"].value_counts()

home_wins = (
    df[df["result"] == "Home Win"]
    ["home_team"]
    .value_counts()
)

home_win_rate = (
    home_wins / home_matches
) * 100

home_win_rate = home_win_rate.fillna(0)

draws = (
    df[df["result"] == "Draw"]
    ["home_team"]
    .value_counts()
)

draw_rate = (
    draws / home_matches
) * 100

draw_rate = draw_rate.fillna(0)


losses = (
    df[df["result"] == "Away Win"]
    ["home_team"]
    .value_counts()
)

loss_rate = (
    losses / home_matches
) * 100

loss_rate = loss_rate.fillna(0)

team_stats = pd.DataFrame({
    "home_win_rate": home_win_rate,
    "home_draw_rate": draw_rate,
    "home_loss_rate": loss_rate
})

team_stats = team_stats.reset_index()

team_stats.columns = [
    "team",
    "home_win_rate",
    "home_draw_rate",
    "home_loss_rate"
]

print(team_stats.head())
team_stats.to_csv(
    "data/team_stats.csv",
    index=False
)

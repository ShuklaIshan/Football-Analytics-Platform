import pandas as pd
matches = pd.read_csv("data/results.csv")
home_stats = pd.read_csv("data/home_team_stats.csv")
away_stats = pd.read_csv("data/away_team_stats.csv")

matches = matches.merge(
    home_stats,
    left_on="home_team",
    right_on="team",
    how="left"
)
matches = matches.drop(columns=["team"])

matches = matches.merge(
    away_stats,
    left_on="away_team",
    right_on="team",
    how="left"
)
matches = matches.drop(columns=["team"])

print(matches.head())
print(
    matches[
        [
        "home_win_rate",
        "away_win_rate"
        ]
    ].isnull().sum()
)
matches.to_csv(
    "data/model_data.csv",
    index=False
)
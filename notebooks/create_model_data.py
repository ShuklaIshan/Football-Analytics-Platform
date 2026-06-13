import pandas as pd
matches = pd.read_csv("data/results.csv")
team_stats = pd.read_csv("data/home_team_stats.csv")
matches = matches.merge(
    team_stats,
    left_on="home_team",
    right_on="team",
    how="left"
)
matches = matches.drop(columns=["team"])
print(matches.head())
print(
    matches[
        ["home_win_rate"]
    ].isnull().sum()
)
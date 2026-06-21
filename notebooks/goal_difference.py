import pandas as pd
df = pd.read_csv("data/results.csv")
home_scored = df.groupby("home_team")["home_score"].mean()
home_conceded = df.groupby("home_team")["away_score"].mean()
home_goal_difference = home_scored - home_conceded
away_scored = df.groupby("away_team")["away_score"].mean()
away_conceded = df.groupby("away_team")["home_score"].mean()
away_goal_difference = away_scored - away_conceded
print(home_goal_difference.head())
print(away_goal_difference.head())
goal_difference_df = pd.DataFrame({
    "home_goal_difference": home_goal_difference,
    "away_goal_difference": away_goal_difference
})

goal_difference_df = goal_difference_df.reset_index()

goal_difference_df.columns = [
    "team",
    "home_goal_difference",
    "away_goal_difference"
]

print(goal_difference_df.head())
goal_difference_df.to_csv(
    "data/goal_difference_stats.csv",
    index=False
)
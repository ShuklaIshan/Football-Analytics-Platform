import pandas as pd
matches = pd.read_csv("data/model_data.csv")
score = pd.read_csv("data/goal_difference_stats.csv")
matches = matches.merge(
    score[["team", "home_goal_difference"]],
    left_on = "home_team",
    right_on = "team",
    how = "left"
)
matches = matches.drop(columns = ["team"])
matches = matches.merge(
    score[["team", "away_goal_difference"]],
    left_on = "away_team",
    right_on = "team",
    how = "left"
)
matches = matches.drop(columns = ["team"])
print(matches.head())
matches.to_csv(
    "data/model_data2.csv",
    index=False
)
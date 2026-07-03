import pandas as pd

matches = pd.read_csv("data/model_data2.csv")
final = pd.read_csv("data/results_recent_form.csv")

matches = matches.merge(
    final[
        [
            "date",
            "home_team",
            "away_team",
            "home_recent_form",
            "away_recent_form"
        ]
    ],
    on=[
        "date",
        "home_team",
        "away_team"
    ],
    how="left"
)

print(
    matches[
        [
            "home_recent_form",
            "away_recent_form"
        ]
    ].isnull().sum()
)

matches.to_csv(
    "data/model_data3.csv",
    index=False
)
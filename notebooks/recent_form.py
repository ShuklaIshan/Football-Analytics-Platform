import pandas as pd

df = pd.read_csv("data/results.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date").reset_index(drop=True)

df["home_recent_form"] = 0.0
df["away_recent_form"] = 0.0

team_history = {}

for i, row in df.iterrows():

    home_team = row["home_team"]
    away_team = row["away_team"]

    # Create history if team is seen for the first time
    if home_team not in team_history:
        team_history[home_team] = []

    if away_team not in team_history:
        team_history[away_team] = []

    # ---------- Calculate HOME recent form ----------
    home_history = team_history[home_team][-5:]

    if len(home_history) == 0:
        home_form = 0
    else:
        home_form = sum(home_history) / (len(home_history) * 3)

    df.at[i, "home_recent_form"] = home_form

    # ---------- Calculate AWAY recent form ----------
    away_history = team_history[away_team][-5:]

    if len(away_history) == 0:
        away_form = 0
    else:
        away_form = sum(away_history) / (len(away_history) * 3)

    df.at[i, "away_recent_form"] = away_form

    # ---------- NOW update history using CURRENT match ----------
    if row["home_score"] > row["away_score"]:

        team_history[home_team].append(3)
        team_history[away_team].append(0)

    elif row["home_score"] < row["away_score"]:

        team_history[home_team].append(0)
        team_history[away_team].append(3)

    else:

        team_history[home_team].append(1)
        team_history[away_team].append(1)

print(df[[
    "date",
    "home_team",
    "away_team",
    "home_recent_form",
    "away_recent_form"
]].head(15))

df.to_csv("data/results_recent_form.csv", index=False)
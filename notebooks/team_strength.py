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

home_wins = df[df["result"] == "Home Win"]["home_team"].value_counts()

home_win_rate = (home_wins / home_matches) * 100

valid_teams = home_matches[home_matches >= 300]

filtered_rates1 = home_win_rate[valid_teams.index]

print(filtered_rates1.sort_values(ascending=False).head(20))

draws = df[df["result"] == "Draw"]["home_team"].value_counts()

draw_rate = (draws / home_matches) * 100

filtered_rates2 = draw_rate[valid_teams.index]

print(filtered_rates2.sort_values(ascending=False).head(20))

away_wins = df[df["result"] == "Away Win"]["home_team"].value_counts()

away_win_rate = (away_wins / home_matches) * 100

filtered_rates3 = away_win_rate[valid_teams.index]

print(filtered_rates3.sort_values(ascending=False).head(20))
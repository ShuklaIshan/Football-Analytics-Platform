import pandas as pd

appearances = pd.read_csv("../data/appearances.csv")

player_metrics = appearances.groupby("player_id").agg({
    "goals": "sum",
    "assists": "sum",
    "minutes_played": "sum",
    "yellow_cards": "sum",
    "red_cards": "sum"
}).reset_index()

print(player_metrics.head())

print("\nShape:")
print(player_metrics.shape)
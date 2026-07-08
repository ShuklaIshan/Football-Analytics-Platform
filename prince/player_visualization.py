import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
players = pd.read_csv("../data/players.csv")
appearances = pd.read_csv("../data/appearances.csv")

# Create player metrics
player_metrics = appearances.groupby("player_id").agg({
    "goals": "sum",
    "assists": "sum",
    "minutes_played": "sum"
}).reset_index()

# Merge with player names
player_stats = pd.merge(
    player_metrics,
    players[["player_id", "name"]],
    on="player_id",
    how="left"
)

# Top 10 Goal Scorers
top_scorers = player_stats.sort_values(
    by="goals",
    ascending=False
).head(10)

print(top_scorers[["name", "goals"]])

# Plot
plt.figure(figsize=(12,6))

plt.bar(top_scorers["name"], top_scorers["goals"])

plt.title("Top 10 Goal Scorers")

plt.xlabel("Player")

plt.ylabel("Goals")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
import pandas as pd
import plotly.express as px

# Load datasets
players = pd.read_csv("../data/players.csv")
appearances = pd.read_csv("../data/appearances.csv")

# Create player metrics
player_metrics = appearances.groupby("player_id").agg({
    "goals":"sum",
    "assists":"sum",
    "minutes_played":"sum"
}).reset_index()

# Merge datasets
player_stats = pd.merge(
    player_metrics,
    players[["player_id","name","position"]],
    on="player_id"
)

# Top 15 Goal Scorers
top_players = player_stats.sort_values(
    by="goals",
    ascending=False
).head(15)

fig = px.bar(
    top_players,
    x="name",
    y="goals",
    color="position",
    title="Top 15 Goal Scorers"
)

fig.show()
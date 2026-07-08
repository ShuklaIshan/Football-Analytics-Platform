import pandas as pd

# Load datasets
players = pd.read_csv("../data/players.csv")
appearances = pd.read_csv("../data/appearances.csv")

# Aggregate player performance
player_metrics = appearances.groupby("player_id").agg({
    "goals": "sum",
    "assists": "sum",
    "minutes_played": "sum",
    "yellow_cards": "sum",
    "red_cards": "sum"
}).reset_index()

# Select useful player information
player_info = players[[
    "player_id",
    "name",
    "position",
    "height_in_cm",
    "market_value_in_eur"
]]

# Merge datasets
clustering_data = pd.merge(
    player_info,
    player_metrics,
    on="player_id",
    how="inner"
)

print("Shape:")
print(clustering_data.shape)

print("\nColumns:")
print(clustering_data.columns)

print("\nFirst 5 Rows:")
print(clustering_data.head())
import pandas as pd

# Load datasets
players = pd.read_csv("../data/players.csv")
appearances = pd.read_csv("../data/appearances.csv")

# Aggregate player performance
player_metrics = appearances.groupby("player_id").agg({
    "goals": "sum",
    "assists": "sum",
    "minutes_played": "sum",
    "yellow_cards": "sum",
    "red_cards": "sum"
}).reset_index()

# Select useful player information
player_info = players[[
    "player_id",
    "name",
    "position",
    "height_in_cm",
    "market_value_in_eur"
]]

# Merge datasets
clustering_data = pd.merge(
    player_info,
    player_metrics,
    on="player_id",
    how="inner"
)

print("Shape:")
print(clustering_data.shape)

print("\nColumns:")
print(clustering_data.columns)

print("\nFirst 5 Rows:")
print(clustering_data.head())
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load datasets
players = pd.read_csv("../data/players.csv")
appearances = pd.read_csv("../data/appearances.csv")

# Create player metrics
player_metrics = appearances.groupby("player_id").agg({
    "goals": "sum",
    "assists": "sum",
    "minutes_played": "sum",
    "yellow_cards": "sum",
    "red_cards": "sum"
}).reset_index()

# Merge datasets
player_info = players[
    [
        "player_id",
        "name",
        "position",
        "height_in_cm",
        "market_value_in_eur"
    ]
]

clustering_data = pd.merge(
    player_info,
    player_metrics,
    on="player_id",
    how="inner"
)

# Feature matrix
features = clustering_data[
    [
        "height_in_cm",
        "market_value_in_eur",
        "goals",
        "assists",
        "minutes_played",
        "yellow_cards",
        "red_cards"
    ]
]

# Handle missing values
features["height_in_cm"] = features["height_in_cm"].fillna(features["height_in_cm"].median())
features["market_value_in_eur"] = features["market_value_in_eur"].fillna(features["market_value_in_eur"].median())

# Scale
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Train model
kmeans = KMeans(
    n_clusters=4,
    random_state=42
)

kmeans.fit(scaled_features)

# Save model
joblib.dump(kmeans, "../models/kmeans_model.pkl")

# Save scaler
joblib.dump(scaler, "../models/scaler.pkl")

print("✅ Model saved successfully!")
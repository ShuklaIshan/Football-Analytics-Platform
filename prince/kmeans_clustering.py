from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd

players = pd.read_csv("../data/players.csv")
appearances = pd.read_csv("../data/appearances.csv")

player_metrics = appearances.groupby("player_id").agg({
    "goals": "sum",
    "assists": "sum",
    "minutes_played": "sum",
    "yellow_cards": "sum",
    "red_cards": "sum"
}).reset_index()

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

# print(features.isnull().sum()) 

# Create a copy of the feature matrix
clean_features = features.copy()

clean_features["height_in_cm"] = clean_features["height_in_cm"].fillna(
    clean_features["height_in_cm"].median()
)

clean_features["market_value_in_eur"] = clean_features["market_value_in_eur"].fillna(
    clean_features["market_value_in_eur"].median()
)

print(clean_features.isnull().sum())

kmeans = KMeans(
    n_clusters=4,
    random_state=42
)

scaler = StandardScaler()

scaled_features = scaler.fit_transform(clean_features)

kmeans.fit(scaled_features)

clusters = kmeans.labels_

clustering_data["cluster"] = clusters

print(clustering_data[["name","cluster"]].head(20))

print("\n========== CLUSTER DISTRIBUTION ==========\n")

print(clustering_data["cluster"].value_counts())

cluster_summary = clustering_data.groupby("cluster").agg({
    "goals": "mean",
    "assists": "mean",
    "minutes_played": "mean",
    "yellow_cards": "mean",
    "red_cards": "mean",
    "market_value_in_eur": "mean",
    "height_in_cm": "mean"
})

print(cluster_summary)
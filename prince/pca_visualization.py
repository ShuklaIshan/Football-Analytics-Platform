import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt

players = pd.read_csv("../data/players.csv")
appearances = pd.read_csv("../data/appearances.csv")

player_metrics = appearances.groupby("player_id").agg({
    "goals":"sum",
    "assists":"sum",
    "minutes_played":"sum",
    "yellow_cards":"sum",
    "red_cards":"sum"
}).reset_index()

# Select useful player information
player_info = players[
    [
        "player_id",
        "name",
        "position",
        "height_in_cm",
        "market_value_in_eur"
    ]
]

# Merge datasets
clustering_data = pd.merge(
    player_info,
    player_metrics,
    on="player_id",
    how="inner"
)

# Select numerical features
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

# Clean missing values
clean_features = features.copy()

clean_features["height_in_cm"] = clean_features["height_in_cm"].fillna(
    clean_features["height_in_cm"].median()
)

clean_features["market_value_in_eur"] = clean_features["market_value_in_eur"].fillna(
    clean_features["market_value_in_eur"].median()
)

# Scale features
scaler = StandardScaler()

scaled_features = scaler.fit_transform(clean_features)

# Train KMeans again
kmeans = KMeans(
    n_clusters=4,
    random_state=42
)

kmeans.fit(scaled_features)

clustering_data["cluster"] = kmeans.labels_

pca = PCA(n_components=2)

pca_features = pca.fit_transform(scaled_features)

clustering_data["PC1"] = pca_features[:,0]
clustering_data["PC2"] = pca_features[:,1]

print(clustering_data[
    [
        "name",
        "cluster",
        "PC1",
        "PC2"
    ]
].head())

plt.figure(figsize=(10, 6))

plt.scatter(
    clustering_data["PC1"],
    clustering_data["PC2"],
    c=clustering_data["cluster"]
)

plt.title("Player Clusters using PCA")

plt.xlabel("Principal Component 1")

plt.ylabel("Principal Component 2")

plt.show()
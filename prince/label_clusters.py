import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# ==========================================================
# LOAD DATASETS
# ==========================================================

players = pd.read_csv("../data/players.csv")
appearances = pd.read_csv("../data/appearances.csv")

# ==========================================================
# CREATE PLAYER PERFORMANCE METRICS
# ==========================================================

player_metrics = appearances.groupby("player_id").agg({
    "goals": "sum",
    "assists": "sum",
    "minutes_played": "sum",
    "yellow_cards": "sum",
    "red_cards": "sum"
}).reset_index()

# ==========================================================
# SELECT PLAYER INFORMATION
# ==========================================================

player_info = players[
    [
        "player_id",
        "name",
        "position",
        "height_in_cm",
        "market_value_in_eur"
    ]
]

# ==========================================================
# MERGE PLAYER INFO WITH PERFORMANCE METRICS
# ==========================================================

clustering_data = pd.merge(
    player_info,
    player_metrics,
    on="player_id",
    how="inner"
)

# ==========================================================
# CREATE FEATURE MATRIX
# ==========================================================

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

# ==========================================================
# HANDLE MISSING VALUES
# ==========================================================

clean_features = features.copy()

clean_features["height_in_cm"] = clean_features["height_in_cm"].fillna(
    clean_features["height_in_cm"].median()
)

clean_features["market_value_in_eur"] = clean_features["market_value_in_eur"].fillna(
    clean_features["market_value_in_eur"].median()
)

# ==========================================================
# STANDARDIZE FEATURES
# ==========================================================

scaler = StandardScaler()
scaled_features = scaler.fit_transform(clean_features)

# ==========================================================
# TRAIN K-MEANS MODEL
# ==========================================================

kmeans = KMeans(
    n_clusters=4,
    random_state=42
)

kmeans.fit(scaled_features)

# Assign cluster labels
clustering_data["cluster"] = kmeans.labels_

# ==========================================================
# ASSIGN MEANINGFUL CLUSTER NAMES
# ==========================================================

cluster_labels = {
    0: "Regular First-Team Players",
    1: "Squad / Developing Players",
    2: "Elite Players",
    3: "Defensive Specialists"
}

clustering_data["cluster_name"] = clustering_data["cluster"].map(cluster_labels)

# ==========================================================
# POSITION DISTRIBUTION
# ==========================================================

position_summary = pd.crosstab(
    clustering_data["cluster"],
    clustering_data["position"]
)

print("\n========== POSITION DISTRIBUTION ==========\n")
print(position_summary)

# ==========================================================
# CLUSTER SUMMARY
# ==========================================================

cluster_summary = clustering_data.groupby("cluster").agg({
    "goals": "mean",
    "assists": "mean",
    "minutes_played": "mean",
    "yellow_cards": "mean",
    "red_cards": "mean",
    "market_value_in_eur": "mean",
    "height_in_cm": "mean"
})

print("\n========== CLUSTER SUMMARY ==========\n")
print(cluster_summary)

# ==========================================================
# SAMPLE PLAYERS FROM EACH CLUSTER
# ==========================================================

for cluster in sorted(clustering_data["cluster"].unique()):

    print(f"\n========== {cluster_labels[cluster]} (Cluster {cluster}) ==========\n")

    sample = clustering_data[
        clustering_data["cluster"] == cluster
    ][
        ["name", "position", "goals", "assists"]
    ].head(10)

    print(sample)

# ==========================================================
# SAVE FINAL DATASET
# ==========================================================

clustering_data.to_csv(
    "../data/player_clusters.csv",
    index=False
)

print("\n✅ player_clusters.csv saved successfully!")
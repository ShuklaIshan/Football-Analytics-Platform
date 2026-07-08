import pandas as pd

# Load clustered dataset
clustered_data = pd.read_csv("../data/player_clusters.csv")

print("========== DATASET INFORMATION ==========\n")

print(f"Total Players : {clustered_data.shape[0]}")
print(f"Total Features : {clustered_data.shape[1]}")

print("\n========== CLUSTER COUNT ==========\n")

print(clustered_data["cluster_name"].value_counts())

print("\n========== POSITION DISTRIBUTION ==========\n")

print(pd.crosstab(
    clustered_data["cluster_name"],
    clustered_data["position"]
))
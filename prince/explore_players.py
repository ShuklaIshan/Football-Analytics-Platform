import pandas as pd

# Load the players dataset
players = pd.read_csv("../data/players.csv")

print("✅ Players dataset loaded successfully!\n")

print("Shape:")
print(players.shape)

print("\nColumns:")
print(players.columns)

print("\nFirst 5 rows:")
print(players.head())
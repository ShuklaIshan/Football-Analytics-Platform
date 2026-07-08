import pandas as pd

# Load dataset
players = pd.read_csv("../data/players.csv")

print("========== DATASET INFO ==========\n")
print(players.info())

print("\n========== MISSING VALUES ==========\n")
print(players.isnull().sum())

print("\n========== MISSING VALUE PERCENTAGE ==========\n")

missing_percentage = (players.isnull().sum() / len(players)) * 100

print(missing_percentage.sort_values(ascending=False))

# Create a copy of the dataset
clean_players = players.copy()

# Fill missing categorical values
clean_players["sub_position"] = clean_players["sub_position"].fillna("Unknown")

clean_players["country_of_citizenship"] = clean_players["country_of_citizenship"].fillna("Unknown")

# Fill missing height with median
clean_players["height_in_cm"] = clean_players["height_in_cm"].fillna(
    clean_players["height_in_cm"].median()
)

print("\n========== MISSING VALUES AFTER CLEANING ==========\n")
print(clean_players[[
    "sub_position",
    "country_of_citizenship",
    "height_in_cm"
]].isnull().sum())
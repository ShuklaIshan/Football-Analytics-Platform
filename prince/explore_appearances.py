import pandas as pd

appearances = pd.read_csv("../data/appearances.csv")

print("========== SHAPE ==========")
print(appearances.shape)

print("\n========== COLUMNS ==========")
print(appearances.columns)

print("\n========== FIRST 5 ROWS ==========")
print(appearances.head())
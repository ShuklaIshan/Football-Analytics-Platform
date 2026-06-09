import pandas as pd

df = pd.read_csv("data/results.csv")

print(df.head())
print(df.columns.tolist())
print(df.shape)
print(df.isnull().sum())

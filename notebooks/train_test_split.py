import pandas as pd
from sklearn.model_selection import train_test_split
x = pd.read_csv("data/features.csv")
y = pd.read_csv("data/target.csv")
print(x.shape)
print(y.shape)
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
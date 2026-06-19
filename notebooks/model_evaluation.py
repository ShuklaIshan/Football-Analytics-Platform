import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

X = pd.read_csv("data/features.csv")

y = pd.read_csv("data/target.csv")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = KNeighborsClassifier()

model.fit(
    X_train,
    y_train.values.ravel()
)

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(accuracy)

print(
    classification_report(
        y_test,
        predictions
    )
)
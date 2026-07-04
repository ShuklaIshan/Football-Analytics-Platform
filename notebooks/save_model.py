import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
x = pd.read_csv("data/features.csv")
y = pd.read_csv("data/target.csv")
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)
knn = KNeighborsClassifier()
knn.fit(
    x_train,
    y_train.values.ravel()
)
knn_predictions = knn.predict(x_test)
knn_accuracy = accuracy_score(
    y_test,
    knn_predictions
)
rf = RandomForestClassifier(
    random_state=42
)
rf.fit(
    x_train,
    y_train.values.ravel()
)
joblib.dump(
    rf,
    "models/random_forest_model.pkl"
)

loaded_model = joblib.load(
    "models/random_forest_model.pkl"
)
print(type(loaded_model))

for feature, importance in zip(
    x.columns,
    rf.feature_importances_
):
    print(feature, importance)
import pandas as pd
df = pd.read_csv("data/results.csv")
df = pd.read_csv("data/model_data2.csv")

def tournament_importance(tournament):

    if tournament == "FIFA World Cup":
        return 5

    elif "qualification" in tournament.lower():
        return 3

    elif tournament in [
        "UEFA Euro",
        "Copa América",
        "African Cup of Nations",
        "AFC Asian Cup",
        "Gold Cup"
    ]:
        return 4

    elif "nations league" in tournament.lower():
        return 2

    elif tournament == "Friendly":
        return 1

    else:
        return 2

df["importance"] = df["tournament"].apply(
    tournament_importance
)
df.to_csv(
    "data/results_with_importance.csv",
    index=False
)

features = df[
    [
        "home_win_rate",
        "home_draw_rate",
        "home_loss_rate",
        "away_win_rate",
        "away_draw_rate",
        "away_loss_rate",
        "home_goal_difference",
        "away_goal_difference"
    ]
]

features.to_csv(
    "data/features.csv",
    index=False
)
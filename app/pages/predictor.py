import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Football Analytics Platform",
    page_icon="⚽",
    layout="wide"
)
st.title("⚽ Football Analytics Platform")
st.write("Predict the result of an international football match using Machine Learning.")

model = joblib.load("models/random_forest_model.pkl")

df = pd.read_csv("data/model_data2.csv")

teams = sorted(df["home_team"].unique())

home_team = st.selectbox(
    "🏠 Select Home Team",
    teams
)

away_team = st.selectbox(
    "✈️ Select Away Team",
    teams
)

if home_team != away_team:
    if st.button("🔮 Predict"):

        home_stats = df[df["home_team"] == home_team].iloc[0]

        away_stats = df[df["away_team"] == away_team].iloc[0]

        features = [[
            home_stats["home_win_rate"],
            home_stats["home_draw_rate"],
            home_stats["home_loss_rate"],

            away_stats["away_win_rate"],
            away_stats["away_draw_rate"],
            away_stats["away_loss_rate"],

            home_stats["home_goal_difference"],
            away_stats["away_goal_difference"]
        ]]

        with st.spinner("Analyzing match..."):
            prediction = model.predict(features)[0]
            if prediction == "Home Win":
                result = f"{home_team} vs {away_team}\n\nPrediction:🏆 {home_team} Wins"
            elif prediction == "Away Win":
                result = f"{home_team} vs {away_team}\n\nPrediction:🏆 {away_team} Wins"
            else:
                result = "{home_team} vs {away_team}\n\nPrediction:🤝 Match Draw"
            probabilities = model.predict_proba(features)
            away_prob = probabilities[0][0] * 100
            draw_prob = probabilities[0][1] * 100
            home_prob = probabilities[0][2] * 100

        st.success(result)

        st.subheader("📊 Prediction Confidence")

        st.write(f"🏠 Home Win: **{home_prob:.2f}%**")
        st.progress(home_prob / 100)

        st.write(f"🤝 Draw: **{draw_prob:.2f}%**")
        st.progress(draw_prob / 100)

        st.write(f"✈️ Away Win: **{away_prob:.2f}%**")
        st.progress(away_prob / 100)

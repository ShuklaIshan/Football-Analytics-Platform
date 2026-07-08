import streamlit as st
import joblib
import pandas as pd

def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.set_page_config(
    page_title="Football Analytics Platform",
    page_icon="⚽",
    layout="wide"
)
st.title("⚽ Match Predictor")
st.write("Predict the result of an international football match using Machine Learning.")

st.divider()

model = joblib.load("models/random_forest_model.pkl")

df = pd.read_csv("data/model_data2.csv")

teams = sorted(df["home_team"].unique())

st.subheader("⚽ Select Teams")

col1, col2 = st.columns(2)

with col1:
    home_team = st.selectbox(
    "🏠 Select Home Team",
    teams
    )

with col2:
    away_team = st.selectbox(
    "✈️ Select Away Team",
    teams
    )

left, center, right = st.columns([2,1,2])

with center:
    predict = st.button("🔮 Predict Match")

if home_team != away_team:
    if predict:

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

        st.divider()

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
        
        st.subheader("🏆 Match Prediction")
        st.success(f"### {result}")

        st.subheader("📊 Prediction Confidence")

        col1,col2,col3 = st.columns(3)

        with col1:
            st.metric("🏠 Home Win",f"{home_prob:.1f}%")

        with col2:
            st.metric("🤝 Draw",f"{draw_prob:.1f}%")

        with col3:
            st.metric("✈️ Away Win",f"{away_prob:.1f}%")

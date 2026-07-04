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

if home_team == away_team:
    st.error("Please select two different teams.")



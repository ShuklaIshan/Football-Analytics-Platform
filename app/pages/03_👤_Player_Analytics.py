import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Player Analytics",
    page_icon="👤",
    layout="wide"
)

# ==========================================================
# LOAD CSS
# ==========================================================

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():
    return pd.read_csv("data/player_clusters.csv")

df = load_data()

# ==========================================================
# FORMAT MARKET VALUE
# ==========================================================

def format_market_value(value):

    if pd.isna(value):
        return "N/A"

    if value >= 1_000_000:
        return f"€{value/1_000_000:.2f}M"

    if value >= 1000:
        return f"€{value/1000:.2f}K"

    return f"€{value}"

# ==========================================================
# HERO
# ==========================================================

st.markdown("""

<div class="hero">

<h1>👤 Player Analytics</h1>

<h3>Detailed Performance Analysis</h3>

<p>

Search any football player and explore
their career statistics, market value,
performance and cluster information.

</p>

</div>

""",unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.header("🔍 Search")

player = st.sidebar.selectbox(

    "Choose Player",

    sorted(df["name"].dropna().unique())

)

player_data = df[df["name"] == player].iloc[0]

# ==========================================================
# PLAYER PROFILE
# ==========================================================

st.markdown(
    f"""
<div class="feature-card">

<h2>👤 {player_data['name']}</h2>

<p>

<b>⚽ Position :</b> {player_data['position']}<br><br>

<b>📏 Height :</b> {player_data['height_in_cm']} cm<br><br>

<b>💰 Market Value :</b> {format_market_value(player_data['market_value_in_eur'])}<br><br>

<b>🏆 Cluster :</b> {player_data['cluster_name']}

</p>

</div>

""",
unsafe_allow_html=True
)

# ==========================================================
# CAREER OVERVIEW
# ==========================================================

st.subheader("📊 Career Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "⚽ Goals",
        int(player_data["goals"])
    )

with col2:
    st.metric(
        "🎯 Assists",
        int(player_data["assists"])
    )

with col3:
    st.metric(
        "⏱ Minutes",
        int(player_data["minutes_played"])
    )

with col4:
    st.metric(
        "📏 Height",
        f"{int(player_data['height_in_cm'])} cm"
    )

st.divider()

# ==========================================================
# PERFORMANCE BAR CHART
# ==========================================================

st.subheader("📈 Performance Overview")

performance = pd.DataFrame({

    "Statistic":[
        "Goals",
        "Assists",
        "Minutes /100"
    ],

    "Value":[

        player_data["goals"],

        player_data["assists"],

        player_data["minutes_played"]/100

    ]

})

import plotly.express as px

fig = px.bar(

    performance,

    x="Statistic",

    y="Value",

    color="Statistic",

    text="Value"

)

fig.update_layout(

    template="plotly_dark",

    showlegend=False,

    height=450

)

fig.update_traces(

    textposition="outside"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# ==========================================================
# PERFORMANCE RATING
# ==========================================================

st.subheader("⭐ Player Performance")

goals = player_data["goals"]
assists = player_data["assists"]
minutes = player_data["minutes_played"]

score = (
    goals * 4 +
    assists * 3 +
    (minutes / 90) * 0.1
)

if score >= 600:
    rating = "🌟 World Class"
elif score >= 350:
    rating = "🏆 Elite"
elif score >= 200:
    rating = "🔥 Excellent"
elif score >= 100:
    rating = "⚽ Regular"
else:
    rating = "📈 Developing"

col1, col2 = st.columns(2)

with col1:
    st.metric("Performance Score", round(score, 1))

with col2:
    st.metric("Player Rating", rating)

st.divider()

# ==========================================================
# PLAYER SUMMARY
# ==========================================================

st.subheader("📝 Career Summary")

summary = f"""
### {player_data['name']}

- **Position:** {player_data['position']}
- **Goals:** {int(player_data['goals'])}
- **Assists:** {int(player_data['assists'])}
- **Minutes Played:** {int(player_data['minutes_played'])}
- **Market Value:** {format_market_value(player_data['market_value_in_eur'])}
- **Cluster:** {player_data['cluster_name']}

This player belongs to the **{player_data['cluster_name']}** group
based on K-Means clustering using goals, assists,
minutes played, height and market value.
"""

st.markdown(summary)

st.divider()

# ==========================================================
# PLAYER ATTRIBUTES
# ==========================================================

st.subheader("📊 Player Attributes")

attributes = pd.DataFrame({

    "Attribute":[
        "Goals",
        "Assists",
        "Minutes",
        "Market Value"
    ],

    "Value":[

        player_data["goals"],

        player_data["assists"],

        player_data["minutes_played"]/100,

        player_data["market_value_in_eur"]/1000000

    ]

})

radar = go.Figure()

radar.add_trace(

    go.Scatterpolar(

        r=attributes["Value"],

        theta=attributes["Attribute"],

        fill="toself",

        name=player_data["name"]

    )

)

radar.update_layout(

    template="plotly_dark",

    polar=dict(
        radialaxis=dict(
            visible=True
        )
    ),

    height=500

)

st.plotly_chart(
    radar,
    use_container_width=True
)

st.divider()
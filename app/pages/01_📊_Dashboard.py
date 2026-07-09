import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==================================================
# LOAD CSS
# ==================================================

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ==================================================
# LOAD DATA
# ==================================================

@st.cache_data
def load_data():
    return pd.read_csv("data/player_clusters.csv")

df = load_data()

# ==================================================
# HERO
# ==================================================

st.markdown("""
<div class="hero">

<h1>📊 Football Analytics Dashboard</h1>

<h3>Dataset Overview & Insights</h3>

<p>

Explore player statistics,
market values,
positions,
and clustering insights.

</p>

</div>
""",unsafe_allow_html=True)

st.subheader("Dataset Overview")

col1,col2,col3,col4=st.columns(4)

col1.metric(
    "👥 Players",
    len(df)
)

col2.metric(
    "🏆 Elite Players",
    len(df[df["cluster_name"]=="Elite Players"])
)

col3.metric(
    "⚽ Positions",
    df["position"].nunique()
)

col4.metric(
    "💰 Avg Market Value",
    f"€{df['market_value_in_eur'].mean()/1000000:.2f}M"
)

st.divider()

# ==================================================
# CHARTS
# ==================================================

left, right = st.columns(2)

# ---------------------------------------------
# Cluster Distribution
# ---------------------------------------------

with left:

    st.subheader("📊 Player Clusters")

    cluster_counts = (
        df["cluster_name"]
        .value_counts()
        .reset_index()
    )

    cluster_counts.columns = [
        "Cluster",
        "Players"
    ]

    fig = px.bar(
        cluster_counts,
        x="Cluster",
        y="Players",
        color="Cluster",
        text="Players"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_dark",
        height=420,
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------------------
# Position Distribution
# ---------------------------------------------

with right:

    st.subheader("🥧 Player Positions")

    position_counts = (
        df["position"]
        .value_counts()
        .reset_index()
    )

    position_counts.columns = [
        "Position",
        "Players"
    ]

    pie = px.pie(
        position_counts,
        names="Position",
        values="Players",
        hole=0.45
    )

    pie.update_layout(
        template="plotly_dark",
        height=420
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

st.divider()

# ==================================================
# MARKET VALUE DISTRIBUTION
# ==================================================

st.subheader("💰 Market Value Distribution")

hist = px.histogram(
    df,
    x="market_value_in_eur",
    color="position",
    nbins=40
)

hist.update_layout(
    template="plotly_dark",
    height=450
)

st.plotly_chart(
    hist,
    use_container_width=True
)

st.divider()

# ==================================================
# TOP 10 PLAYERS
# ==================================================

st.subheader("🏆 Top 10 Valuable Players")

top10 = (
    df
    .sort_values(
        "market_value_in_eur",
        ascending=False
    )
    .head(10)
    .copy()
)

top10["Market Value"] = (
    top10["market_value_in_eur"] / 1_000_000
).round(2).astype(str) + " M €"

st.dataframe(
    top10[
        [
            "name",
            "position",
            "goals",
            "assists",
            "Market Value"
        ]
    ],
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==================================================
# DATASET INSIGHTS
# ==================================================

st.subheader("📈 Key Insights")

elite = len(df[df["cluster_name"] == "Elite Players"])
elite_percent = (elite / len(df)) * 100

most_common_position = df["position"].mode()[0]

avg_value = df["market_value_in_eur"].mean() / 1_000_000

st.markdown(f"""
<div class="feature-card">

<h2>📊 Dataset Insights</h2>

<ul>
<li><b>Elite Players:</b> {elite} ({elite_percent:.2f}% of the dataset)</li>

<li><b>Most Common Position:</b> {most_common_position}</li>

<li><b>Average Market Value:</b> €{avg_value:.2f} Million</li>

<li><b>Total Players Analysed:</b> {len(df)}</li>

</ul>

</div>
""", unsafe_allow_html=True)
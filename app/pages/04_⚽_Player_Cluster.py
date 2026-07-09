import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Player Clustering",
    page_icon="⚽",
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
# HELPER FUNCTIONS
# ==========================================================

@st.cache_data
def load_data():
    return pd.read_csv("data/player_clusters.csv")


def format_market_value(value):
    if pd.isna(value):
        return "N/A"

    if value >= 1_000_000:
        return f"€{value/1_000_000:.2f}M"

    if value >= 1_000:
        return f"€{value/1000:.1f}K"

    return f"€{value:,.0f}"


# ==========================================================
# HERO SECTION
# ==========================================================

st.markdown("""
<div class="hero">

<h1>⚽ Player Clustering Dashboard</h1>

<h3>K-Means Based Football Player Analysis</h3>

<p>
Explore football players grouped according to their
performance statistics using Machine Learning.
Use the filters to analyse player clusters,
performance and market value.
</p>

</div>
""", unsafe_allow_html=True)



# ==========================================================
# LOAD DATA
# ==========================================================

df = load_data()

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.header("🎯 Filters")

selected_cluster = st.sidebar.selectbox(
    "Cluster",
    sorted(df["cluster_name"].unique())
)

search_player = st.sidebar.text_input(
    "🔍 Search Player"
)

positions = ["All"] + sorted(
    df["position"].dropna().unique().tolist()
)

selected_position = st.sidebar.selectbox(
    "Position",
    positions
)

min_value = int(df["market_value_in_eur"].min())
max_value = int(df["market_value_in_eur"].max())

market_range = st.sidebar.slider(
    "💰 Market Value (€)",
    min_value,
    max_value,
    (min_value, max_value)
)

# ==========================================================
# APPLY FILTERS
# ==========================================================

filtered_df = df.copy()

filtered_df = filtered_df[
    filtered_df["cluster_name"] == selected_cluster
]

if search_player:
    filtered_df = filtered_df[
        filtered_df["name"].str.contains(
            search_player,
            case=False,
            na=False
        )
    ]

if selected_position != "All":
    filtered_df = filtered_df[
        filtered_df["position"] == selected_position
    ]

filtered_df = filtered_df[
    (filtered_df["market_value_in_eur"] >= market_range[0]) &
    (filtered_df["market_value_in_eur"] <= market_range[1])
]

# ==========================================================
# EMPTY RESULT
# ==========================================================

if filtered_df.empty:
    st.warning("No players found for the selected filters.")
    st.stop()

st.markdown(
    f"""
<div class="feature-card">

<h2>📊 Current Analysis</h2>

<p>

<b>Selected Cluster:</b> {selected_cluster}<br>

<b>Players Found:</b> {len(filtered_df)}<br>

<b>Position Filter:</b> {selected_position}

</p>

</div>
""",
unsafe_allow_html=True
)

# ==========================================================
# DASHBOARD METRICS
# ==========================================================

st.subheader("📊 Cluster Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Players",
        len(filtered_df)
    )

with col2:
    st.metric(
        "⚽ Avg Goals",
        round(filtered_df["goals"].mean(), 2)
    )

with col3:
    st.metric(
        "🎯 Avg Assists",
        round(filtered_df["assists"].mean(), 2)
    )

with col4:
    st.metric(
        "💰 Avg Market Value",
        format_market_value(
            filtered_df["market_value_in_eur"].mean()
        )
    )

st.divider()

# ==========================================================
# ROW 1
# CLUSTER + POSITION
# ==========================================================

left, right = st.columns(2)

# -------------------------
# Cluster Distribution
# -------------------------

with left:

    st.subheader("📊 Cluster Distribution")

    cluster_counts = (
        df["cluster_name"]
        .value_counts()
        .reset_index()
    )

    cluster_counts.columns = [
        "Cluster",
        "Players"
    ]

    cluster_chart = px.bar(
        cluster_counts,
        x="Cluster",
        y="Players",
        color="Cluster",
        text="Players"
    )

    cluster_chart.update_traces(
        textposition="outside"
    )

    cluster_chart.update_layout(
        template="plotly_dark",
        showlegend=False,
        height=430,
        margin=dict(l=20,r=20,t=40,b=20)
    )

    st.plotly_chart(
        cluster_chart,
        use_container_width=True
    )

# -------------------------
# Position Distribution
# -------------------------

with right:

    st.subheader("🥧 Position Distribution")

    position_counts = (
        filtered_df["position"]
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
        hole=0.5
    )

    pie.update_layout(
        template="plotly_dark",
        height=430,
        margin=dict(l=20,r=20,t=40,b=20)
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

st.divider()

# ==========================================================
# GOALS VS ASSISTS
# ==========================================================

st.subheader("🎯 Goals vs Assists")

scatter = px.scatter(

    filtered_df,

    x="goals",

    y="assists",

    color="position",

    size="market_value_in_eur",

    size_max=25,

    opacity=0.75,

    hover_name="name",

    hover_data={
        "goals": True,
        "assists": True,
        "minutes_played": True,
        "market_value_in_eur":":,.0f",
        "position":True
    }

)

scatter.update_layout(

    template="plotly_dark",

    height=600,

    legend_title="Position"

)

st.plotly_chart(

    scatter,

    use_container_width=True

)

st.divider()

# ==========================================================
# MARKET VALUE DISTRIBUTION
# ==========================================================

st.subheader("💰 Market Value Distribution")

hist = px.histogram(

    filtered_df,

    x="market_value_in_eur",

    color="position",

    nbins=30

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

# ==========================================================
# TOP 10 PLAYERS
# ==========================================================

st.subheader("🏆 Top 10 Players")

top_players = (
    filtered_df
    .sort_values(
        by="market_value_in_eur",
        ascending=False
    )
    .head(10)
    .copy()
)

top_players["market_value"] = top_players["market_value_in_eur"].apply(
    format_market_value
)

st.dataframe(
    top_players[
        [
            "name",
            "position",
            "goals",
            "assists",
            "market_value"
        ]
    ],
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# COMPLETE PLAYER TABLE
# ==========================================================

st.subheader("📋 Complete Player List")

table = filtered_df.copy()

table["market_value"] = table["market_value_in_eur"].apply(
    format_market_value
)

table = table.sort_values(
    by="market_value_in_eur",
    ascending=False
)

st.dataframe(
    table[
        [
            "name",
            "position",
            "goals",
            "assists",
            "minutes_played",
            "market_value"
        ]
    ],
    use_container_width=True,
    hide_index=True
)
import streamlit as st

st.set_page_config(
    page_title="Football Analytics Platform",
    page_icon="⚽",
    layout="wide"
)

# --------------------
# Load CSS
# --------------------

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# --------------------
# HERO
# --------------------

st.markdown("""
<div class="hero">

<div class="hero-left">

<h1>Football Analytics Platform</h1>

<h3>
Machine Learning Meets Football
</h3>

<p>
Predict international football matches,
analyze team performance,
explore player statistics,
and discover hidden insights using
Machine Learning.
</p>

</div>

</div>
""",unsafe_allow_html=True)

# --------------------

st.markdown("<br>",unsafe_allow_html=True)

# --------------------
# STATS
# --------------------

c1,c2,c3,c4=st.columns(4)

with c1:
    st.metric("Historical Matches","49,000+")

with c2:
    st.metric("ML Model","Ran. Forest")

with c3:
    st.metric("Prediction Classes","3")

with c4:
    st.metric("Interactive Pages","5")

st.markdown("<br>",unsafe_allow_html=True)

# --------------------
# FEATURES
# --------------------

st.markdown(
"<h2 class='section-title'>Platform Features</h2>",
unsafe_allow_html=True
)

left,right=st.columns(2)

with left:

    st.markdown("""
<div class="feature-card">

<div class="icon">⚽</div>

<h2>Match Predictor</h2>

<p>
Predict international football matches
using Machine Learning.
The model has been trained on thousands
of historical FIFA matches.
</p>

</div>
""",unsafe_allow_html=True)

    st.markdown("""
<div class="feature-card">

<div class="icon">📊</div>

<h2>Team Dashboard</h2>

<p>
Explore team performance,
goal trends,
historical statistics
and interactive visualizations.
</p>

</div>
""",unsafe_allow_html=True)

with right:

    st.markdown("""
<div class="feature-card">

<div class="icon">👤</div>

<h2>Player Analytics</h2>

<p>
Analyze player performance,
career statistics
and compare football legends.
</p>

</div>
""",unsafe_allow_html=True)

    st.markdown("""
<div class="feature-card">

<div class="icon">🎯</div>

<h2>Player Clustering</h2>

<p>
Use Machine Learning to discover
players with similar playing styles
through clustering.
</p>

</div>
""",unsafe_allow_html=True)

# --------------------

st.markdown("<br>",unsafe_allow_html=True)

# --------------------
# HOW IT WORKS
# --------------------

st.markdown(
"<h2 class='section-title'>How It Works</h2>",
unsafe_allow_html=True
)

step1,step2,step3,step4=st.columns(4)

with step1:
    st.markdown("""
<div class="step">

<h1>①</h1>

Choose Teams

</div>
""",unsafe_allow_html=True)

with step2:
    st.markdown("""
<div class="step">

<h1>②</h1>

Feature Engineering

</div>
""",unsafe_allow_html=True)

with step3:
    st.markdown("""
<div class="step">

<h1>③</h1>

Random Forest

</div>
""",unsafe_allow_html=True)

with step4:
    st.markdown("""
<div class="step">

<h1>④</h1>

Prediction

</div>
""",unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)

# --------------------
# ABOUT
# --------------------

st.markdown(
"<h2 class='section-title'>About Project</h2>",
unsafe_allow_html=True
)

st.markdown("""

<div class="about">

Football Analytics Platform combines
Machine Learning,
Data Analytics
and Interactive Visualization
to help users predict football matches,
analyze players
and explore historical football data.

</div>

""",unsafe_allow_html=True)

# --------------------

st.divider()

st.caption(
"Built with ❤️ using Python, Streamlit, Pandas and Scikit-Learn"
)
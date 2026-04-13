import streamlit as st

# ====================== INFINITE DRIVE STYLING ======================
st.set_page_config(page_title="Derivative Power Simulator", page_icon="🛡️", layout="centered")

st.markdown("""
<style>
    .stApp { background: linear-gradient(180deg, #0c0c0c 0%, #1f0f00 50%, #2a0a00 100%); color: #ffd700; }
    .title { font-family: 'Courier New', monospace; color: #ffd700; text-shadow: 0 0 20px #ffaa00, 0 0 35px #ff5500; font-weight: bold; letter-spacing: 4px; font-size: 3.0em; text-transform: uppercase; }
    .subtitle { color: #00ff9d; font-size: 1.3em; text-shadow: 0 0 12px #00ff9d; margin-bottom: 25px; }
    .explanation { background: rgba(0, 255, 157, 0.08); border-left: 5px solid #00ff9d; padding: 18px; border-radius: 10px; color: #b0ffdd; margin-bottom: 30px; }
    .stMetric label { color: #ffd700 !important; font-weight: bold; text-shadow: 0 0 8px #ffaa00; }
    .stMetric div[data-testid="stMetricValue"] { color: #ffffff !important; font-size: 1.95em; text-shadow: 0 0 15px #00ff9d; }
    .result-box { background: rgba(255, 215, 0, 0.15); border: 2px solid #ffd700; border-radius: 12px; padding: 25px; color: #ffffff; font-weight: bold; text-align: center; text-shadow: 0 0 10px #00ff9d; margin: 15px 0; }
    .header-logo { text-align: center; margin: 15px 0 10px 0; }
</style>
""", unsafe_allow_html=True)

# FundDog Logo
st.markdown('<div class="header-logo">', unsafe_allow_html=True)
st.image("funddog_logo.jpg", width=240)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<h1 class="title">DERIVATIVE POWER SIMULATOR</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">When $QOM moves → the Pack feels it. No extra buys required.</p>', unsafe_allow_html=True)

# Short Explanation
st.markdown("""
<div class="explanation">
<strong>Why $FUNDOG pumps when $QOM moves (even with no buys):</strong><br><br>
$FUNDOG is paired

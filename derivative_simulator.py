import streamlit as st

# ====================== INFINITE DRIVE STYLING ======================
st.set_page_config(page_title="Derivative Power Simulator", page_icon="🛡️", layout="centered")

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #0c0c0c 0%, #1f0f00 50%, #2a0a00 100%);
        color: #ffd700;
    }
    .title {
        font-family: 'Courier New', monospace;
        color: #ffd700;
        text-shadow: 0 0 15px #ffaa00, 0 0 30px #ff5500;
        font-weight: bold;
        letter-spacing: 4px;
        font-size: 3.0em;
        text-transform: uppercase;
    }
    .subtitle {
        color: #00ff9d;
        font-size: 1.25em;
        text-shadow: 0 0 10px #00ff9d;
        margin-bottom: 25px;
    }
    .stMetric label {
        color: #ffd700 !important;
        font-weight: bold;
        text-shadow: 0 0 8px #ffaa00;
    }
    .stMetric div[data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-size: 1.9em;
        text-shadow: 0 0 12px #00ff9d;
    }
    .result-box {
        background: rgba(255, 215, 0, 0.12);
        border: 2px solid #ffd700;
        border-radius: 12px;
        padding: 20px;
        color: #00ff9d;
        font-weight: bold;
        text-align: center;
        text-shadow: 0 0 10px #ffaa00;
    }
    .header-logo {
        text-align: center;
        margin: 15px 0 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# FundDog Logo Header - Half Size
st.markdown('<div class="header-logo">', unsafe_allow_html=True)
st.image("funddog_logo.jpg", width=240)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<h1 class="title">DERIVATIVE POWER SIMULATOR</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">When $QOM moves → the Pack feels it. No extra buys required.</p>', unsafe_allow_html=True)

# ====================== SIMULATOR ======================
st.subheader("Your Current Position")
current_fundog = st.number_input("Your $FUNDOG holdings", min_value=0.0, value=1000000.0, step=10000.0, format="%.0f")
current_qom_price = st.number_input("Current $QOM price (in USD)", min_value=0.000001, value=0.0008, format="%.8f", step=0.00001)

st.markdown("---")
st.subheader("Scenario: $QOM Price Pump")

qom_multiplier = st.slider("How much does $QOM pump?", min_value=1.0, max_value=50.0, value=5.0, step=0.5)

new_qom_price = current_qom_price * qom_multiplier

# Simple derivative model: FUNDOG gains ~60-80% of QOM's % move (tuned to feel reflexive but realistic)
fundog_multiplier = 1 + (qom_multiplier - 1) * 0.72   # 72% beta to QOM movement

new_fundog_value = current_fundog * fundog_multiplier

st.markdown('<div class="result-box">', unsafe_allow_html=True)
st.write(f"**If $QOM pumps {qom_multiplier:.1f}x**")
st.metric("New $QOM Price", f"${new_qom_price:.6f}")
st.metric("Your $FUNDOG Value", f"{new_fundog_value:,.0f} $FUNDOG")
st.metric("Gain from Derivative Power", f"+{ (fundog_multiplier-1)*100 :.1f}%", delta=f"{new_fundog_value - current_fundog:,.0f}")
st.markdown('</div>', unsafe_allow_html=True)

st.caption("This is a simulation based on historical derivative meme behavior on Layer 1 chains.\n"
           "The Guardian watches the base chain so the Pack can benefit reflexively.")

st.caption("For teh people. By teh people. Protected by teh Dog. 🦮")

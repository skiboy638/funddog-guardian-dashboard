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
        text-shadow: 0 0 20px #ffaa00, 0 0 35px #ff5500;
        font-weight: bold;
        letter-spacing: 4px;
        font-size: 3.0em;
        text-transform: uppercase;
    }
    .subtitle {
        color: #00ff9d;
        font-size: 1.3em;
        text-shadow: 0 0 12px #00ff9d;
        margin-bottom: 20px;
    }
    .explanation {
        background: rgba(0, 255, 157, 0.08);
        border-left: 5px solid #00ff9d;
        padding: 20px;
        border-radius: 10px;
        color: #b0ffdd;
        margin-bottom: 30px;
    }
    .stMetric label {
        color: #ffd700 !important;
        font-weight: bold;
        text-shadow: 0 0 8px #ffaa00;
    }
    .stMetric div[data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-size: 1.95em;
        text-shadow: 0 0 15px #00ff9d;
    }
    .result-box {
        background: rgba(255, 215, 0, 0.15);
        border: 2px solid #ffd700;
        border-radius: 12px;
        padding: 25px;
        color: #ffffff;
        font-weight: bold;
        text-align: center;
        text-shadow: 0 0 10px #00ff9d;
        margin: 15px 0;
    }
    .header-logo {
        text-align: center;
        margin: 15px 0 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# FundDog Logo Header
st.markdown('<div class="header-logo">', unsafe_allow_html=True)
st.image("funddog_logo.jpg", width=240)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<h1 class="title">DERIVATIVE POWER SIMULATOR</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">When $QOM moves → the Pack feels it. No extra buys required.</p>', unsafe_allow_html=True)

# ====================== EXPLANATION OF LP PAIRING ======================
st.markdown("""
<div class="explanation">
<strong>How the FUNDOG-QOM LP Pairing Creates Derivative Power</strong><br><br>

When you add liquidity to the <strong>$FUNDOG-QOM pool</strong>, you're pairing the two tokens together. 

As more $QOM flows into QL1 (bridge inflows, farming rewards, etc.), the value of the pool increases. 
Because $FUNDOG is the smaller, leveraged side of the pair, its price tends to move harder than $QOM — often 60-80% of $QOM’s percentage move.

This means:
- When $QOM pumps → $FUNDOG pumps **on no extra buys**
- The more $QOM that enters the ecosystem, the stronger the reflexive effect for $FUNDOG holders
- Your LP position benefits from both tokens, but $FUNDOG gives the amplified upside

The Guardian protects the base chain. The Pack rides the derivative wave.
</div>
""", unsafe_allow_html=True)

# ====================== SIMULATOR ======================
st.subheader("Your Current Position")
current_fundog = st.number_input("Your $FUNDOG holdings", min_value=0.0, value=1000000.0, step=10000.0, format="%.0f")
current_qom_price = st.number_input("Current $QOM price (in USD)", 
                                   min_value=0.0000000001, 
                                   value=0.0008000000, 
                                   format="%.10f", 
                                   step=0.0000000001)

st.markdown("---")
st.subheader("Scenario: $QOM Price Pump")

qom_multiplier = st.slider("How much does $QOM pump?", min_value=1.0, max_value=50.0, value=5.0, step=0.5)

new_qom_price = current_qom_price * qom_multiplier
fundog_multiplier = 1 + (qom_multiplier - 1) * 0.72   # 72% beta to QOM movement

new_fundog_value = current_fundog * fundog_multiplier
gain_percent = (fundog_multiplier - 1) * 100

st.markdown('<div class="result-box">', unsafe_allow_html=True)
st.write(f"**If $QOM pumps {qom_multiplier:.1f}x**")
st.metric("New $QOM Price", f"${new_qom_price:.10f}")
st.metric("Your $FUNDOG Value", f"{new_fundog_value:,.0f} $FUNDOG")
st.metric("Gain from Derivative Power", f"+{gain_percent:.1f}%", delta=f"{new_fundog_value - current_fundog:,.0f}")
st.markdown('</div>', unsafe_allow_html=True)

st.caption("This is a simulation based on typical derivative meme behavior on Layer 1 chains.\n"
           "The Guardian watches the base chain so the Pack can benefit reflexively.")

st.caption("For teh people. By teh people. Protected by teh Dog. 🦮")

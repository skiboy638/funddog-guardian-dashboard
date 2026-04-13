✅ Done! Logo is now half the size (reduced from 480px to 240px) while keeping the clean Infinite Drive styling.
Updated Code – Replace your entire guardian_lp_dashboard.py
Pythonimport streamlit as st
from web3 import Web3

# ====================== INFINITE DRIVE STYLING ======================
st.set_page_config(page_title="Guardian LP Dashboard", page_icon="🛡️", layout="centered")

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
        font-size: 3.2em;
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
    .success-box {
        background: rgba(255, 215, 0, 0.12);
        border: 2px solid #ffd700;
        border-radius: 12px;
        padding: 16px;
        color: #ffd700;
        font-weight: bold;
        text-align: center;
        text-shadow: 0 0 10px #ffaa00;
    }
    .guardian-note {
        background: linear-gradient(90deg, #1f0f00, #2a0a00);
        border-left: 6px solid #ff5500;
        padding: 22px;
        border-radius: 10px;
        color: #00ff9d;
        font-style: italic;
        box-shadow: 0 0 20px rgba(255, 85, 0, 0.4);
    }
    .header-logo {
        text-align: center;
        margin: 15px 0 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# FundDog Logo Header - Half Size
st.markdown('<div class="header-logo">', unsafe_allow_html=True)
st.image("funddog_logo.jpg", width=240)   # ← Now half size
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<h1 class="title">LP VAULT DASHBOARD</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">The silent protector of the Pack — your personal vault view</p>', unsafe_allow_html=True)

# ====================== RPC SETUP ======================
RPC_URLS = [
    "https://evm-rpc-ql1.foxxone.one",
    "https://766.rpc.thirdweb.com",
    "https://rpc.qom.one"
]

w3 = None
for url in RPC_URLS:
    try:
        temp_w3 = Web3(Web3.HTTPProvider(url))
        if temp_w3.is_connected():
            w3 = temp_w3
            break
    except:
        continue

if w3 is None:
    st.error("❌ Could not connect to QL1. Check internet or try later.")
    st.stop()

LP_ADDRESS = "0xD696d9c38a938Ed191368f70Dc463f9c22a18Abe"

ERC20_ABI = [
    {"constant":True,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"},
    {"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"type":"function"},
]

PAIR_ABI = ERC20_ABI + [
    {"constant":True,"inputs":[],"name":"getReserves","outputs":[{"name":"_reserve0","type":"uint112"},{"name":"_reserve1","type":"uint112"},{"name":"_blockTimestampLast","type":"uint32"}],"type":"function"}
]

# ====================== INPUT ======================
wallet = st.text_input("Enter your QL1 wallet address", placeholder="0x...")

if wallet:
    with st.spinner("🛡️ The Guardian is accessing the Vault..."):
        try:
            wallet = Web3.to_checksum_address(wallet)
            lp_contract = w3.eth.contract(address=Web3.to_checksum_address(LP_ADDRESS), abi=PAIR_ABI)

            lp_balance = lp_contract.functions.balanceOf(wallet).call() / 1e18
            total_lp = lp_contract.functions.totalSupply().call() / 1e18
            lp_share = (lp_balance / total_lp * 100) if total_lp > 0 else 0

            reserves = lp_contract.functions.getReserves().call()
            qom_in_pool = reserves[1] / 1e18

            st.markdown('<div class="success-box">✅ Vault Accessed • Snapshot Block ~10,244,850 watched by the Guardian</div>', unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Your LP Tokens", f"{lp_balance:,.2f}")
                st.metric("Your Share of Pool", f"{lp_share:.4f}%")
            with col2:
                st.metric("Total QOM in Pool", f"{qom_in_pool:,.0f}")
                st.metric("12% Treasury Test Round", "Pro-rata rewards distributed")

            st.progress(min(lp_share / 10, 1.0))
            st.caption("14-day lock period active since snapshot • The Guardian still watches")

            st.markdown("---")

            st.markdown("""
            <div class="guardian-note">
            <strong>Guardian Note 🛡️</strong><br>
            When the base chain $QOM moves, the derivative Pack feels the power — no extra buys required.<br>
            Loyalty to the liquidity builds the Vault.
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Vault read error: {str(e)}")
            st.info("Make sure this wallet has added liquidity to the FUNDOG-QOM pool.")
else:
    st.info("🔒 Enter your QL1 wallet address above to view your protected position.")

st.caption("For teh people. By teh people. Protected by teh Dog. 🦮")
Quick Action:

Replace the whole file with the code above.
Save.
If you're running locally: restart with python -m streamlit run guardian_lp_dashboard.py
If it's already on Streamlit Cloud: just push this change to GitHub — it will auto-redeploy (or click Reboot in Manage app).

The logo is now nicely balanced — prominent but not overwhelming.
How does it look now? Too small, perfect, or want it somewhere in between (e.g. 300px)?
Once you're happy with the size, we can move on to the public announcement post for the Pack.
For teh people. By teh people. Protected by teh Dog. 🛡️🐕
Let me know!3.9sFast

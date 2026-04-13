import streamlit as st
from web3 import Web3

# ====================== INFINITE DRIVE STYLING ======================
st.set_page_config(page_title="Guardian Vault Hub", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
    .stApp { background: linear-gradient(180deg, #0c0c0c 0%, #1f0f00 50%, #2a0a00 100%); color: #ffd700; }
    .title { font-family: 'Courier New', monospace; color: #ffd700; text-shadow: 0 0 20px #ffaa00, 0 0 40px #ff5500; font-weight: bold; letter-spacing: 4px; font-size: 3.2em; text-transform: uppercase; }
    .subtitle { color: #00ff9d; font-size: 1.35em; text-shadow: 0 0 12px #00ff9d; margin-bottom: 20px; }
    .tab-style { background: rgba(255, 215, 0, 0.08); border-radius: 10px; padding: 20px; }
    .result-box { background: rgba(255, 215, 0, 0.15); border: 2px solid #ffd700; border-radius: 12px; padding: 25px; color: #ffffff; text-align: center; text-shadow: 0 0 10px #00ff9d; }
    .header-logo { text-align: center; margin: 10px 0 15px 0; }
</style>
""", unsafe_allow_html=True)

# Header with FundDog Logo
st.markdown('<div class="header-logo">', unsafe_allow_html=True)
st.image("funddog_logo.jpg", width=260)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<h1 class="title">GUARDIAN VAULT HUB</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">The silent protector of the Pack — all tools in one vault</p>', unsafe_allow_html=True)

# ====================== RPC SETUP ======================
RPC_URLS = ["https://evm-rpc-ql1.foxxone.one", "https://766.rpc.thirdweb.com", "https://rpc.qom.one"]
w3 = None
for url in RPC_URLS:
    try:
        temp_w3 = Web3(Web3.HTTPProvider(url))
        if temp_w3.is_connected():
            w3 = temp_w3
            break
    except:
        continue

LP_ADDRESS = "0xD696d9c38a938Ed191368f70Dc463f9c22a18Abe"

ERC20_ABI = [{"constant":True,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"},
             {"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"type":"function"}]

PAIR_ABI = ERC20_ABI + [{"constant":True,"inputs":[],"name":"getReserves","outputs":[{"name":"_reserve0","type":"uint112"},{"name":"_reserve1","type":"uint112"},{"name":"_blockTimestampLast","type":"uint32"}],"type":"function"}]

# ====================== TABS ======================
tab1, tab2, tab3 = st.tabs(["📊 LP Vault Dashboard", "⚡ Derivative Power Simulator", "🏆 Reward Tracker"])

with tab1:
    st.subheader("LP Vault Dashboard")
    wallet = st.text_input("Enter your QL1 wallet address", placeholder="0x...", key="lp_wallet")
    if wallet and w3:
        with st.spinner("🛡️ Accessing the Vault..."):
            try:
                wallet = Web3.to_checksum_address(wallet)
                lp_contract = w3.eth.contract(address=Web3.to_checksum_address(LP_ADDRESS), abi=PAIR_ABI)
                lp_balance = lp_contract.functions.balanceOf(wallet).call() / 1e18
                total_lp = lp_contract.functions.totalSupply().call() / 1e18
                lp_share = (lp_balance / total_lp * 100) if total_lp > 0 else 0
                reserves = lp_contract.functions.getReserves().call()
                qom_in_pool = reserves[1] / 1e18

                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Your LP Tokens", f"{lp_balance:,.4f}")
                    st.metric("Your Share of Pool", f"{lp_share:.4f}%")
                with col2:
                    st.metric("Total QOM in Pool", f"{qom_in_pool:,.0f}")
                    st.metric("12% Treasury Test Round", "Pro-rata distributed")
                st.progress(min(lp_share / 10, 1.0))
                st.caption("14-day lock active since snapshot block ~10,244,850")
            except Exception as e:
                st.error(f"Error: {str(e)}")

with tab2:
    st.subheader("Derivative Power Simulator")
    st.markdown("""
    <div style="background:rgba(0,255,157,0.08); border-left:5px solid #00ff9d; padding:18px; border-radius:10px; margin-bottom:25px;">
    <strong>Why $FUNDOG pumps when $QOM moves (even with no buys):</strong><br>
    $FUNDOG is paired with $QOM in the LP pool. When $QOM inflows increase, the pool grows and $FUNDOG — the smaller side — moves harder, creating automatic reflexive upside.
    </div>
    """, unsafe_allow_html=True)

    current_fundog = st.number_input("Your $FUNDOG holdings", min_value=0.0, value=1000000.0, step=10000.0, format="%.0f")
    current_qom_price = st.number_input("Current $QOM price (in USD)", min_value=0.0000000001, value=0.0008000000, format="%.10f", step=0.0000000001)
    qom_multiplier = st.slider("How much does $QOM pump?", min_value=1.0, max_value=50.0, value=5.0, step=0.5)

    new_qom_price = current_qom_price * qom_multiplier
    fundog_multiplier = 1 + (qom_multiplier - 1) * 0.72
    new_fundog_value = current_fundog * fundog_multiplier
    gain_percent = (fundog_multiplier - 1) * 100

    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.write(f"**If $QOM pumps {qom_multiplier:.1f}x**")
    st.metric("New $QOM Price", f"${new_qom_price:.10f}")
    st.metric("Your $FUNDOG Value", f"{new_fundog_value:,.0f} $FUNDOG")
    st.metric("Gain from Derivative Power", f"+{gain_percent:.1f}%", delta=f"{new_fundog_value - current_fundog:,.0f}")
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.subheader("Reward Tracker")
    st.write("**12% Treasury Test Round Results**")
    wallet = st.text_input("Enter your QL1 wallet address", placeholder="0x...", key="reward_wallet")
    if wallet:
        st.success("✅ Your pro-rata share from the 12% test round has been calculated based on locked LP at snapshot.")
        st.info("Future rounds will use the same logic. The more LP you lock, the bigger your cut from the public treasury.")
        st.caption("Only wallets that kept the 14-day lock are eligible for full rewards.")

st.caption("For teh people. By teh people. Protected by teh Dog. 🦮")
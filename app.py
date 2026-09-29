import streamlit as st
import pandas as pd

st.set_page_config(page_title="AMBUSHER RADAR",layout="wide")

# OLD LAYOUT STYLE
st.markdown("""
<style>
.stApp{background:#0a0e13}
h1,h2,h3{color:#00ff88!important}
div.stButton>button{
background:#111a22;
border:1px solid #00ff88;
color:white;
border-radius:12px;
padding:12px;
width:100%;
}
div.stButton>button:hover{
background:#00ff88;
color:black;
}
</style>
""",unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page="home"

FUND=[
 ["2026-09-29","FOMC","HIGH","DXY GOLD"],
 ["2026-09-30","CPI","HIGH","ALL PAIRS"],
 ["2026-10-01","NFP","HIGH","DXY"],
]

FUND_EXP={
 "INTEREST RATE":["Cost of borrowing money","High rate = DXY UP GOLD DOWN","FOMC decides it - Most important"],
 "CPI":["Consumer Price Index - Inflation","High CPI = DXY UP because Fed hikes","Shows if prices rising"],
 "FOMC":["Federal Reserve Meeting","Decides interest rate","Biggest volatility of month"],
 "NFP":["Non Farm Payroll - US Jobs","High NFP = DXY UP - Strong economy","First Friday every month"],
 "GDP":["Gross Domestic Product - Growth","High GDP = DXY UP","Health of economy"],
 "PPI":["Producer Inflation","Leads to CPI","Factory prices"],
}

GLOSS={
 "BOS":["Break of Structure","Market breaks high/low - Trend continues"],
 "CHoCH":["Change of Character","Trend shift - Reversal coming"],
 "OB":["Order Block","Bank/Institution buying zone"],
 "FVG":["Fair Value Gap","Imbalance - Price wants to fill"],
 "DXY":["Dollar Index","Measures dollar vs others - King of market"],
 "LIQUIDITY":["Stop Hunt","Where retail stops sit - Banks hunt it"],
}

GR={
 "forex":pd.DataFrame([{"Pair":"EURUSD","Bias":"BUY","Reason":"DXY Weak"}]),
 "indices":pd.DataFrame([{"Pair":"NAS100","Bias":"BUY","Reason":"Risk On"}]),
 "commods":pd.DataFrame([{"Pair":"GOLD","Bias":"BUY","Reason":"DXY Down"}]),
 "crypto":pd.DataFrame([{"Pair":"BTCUSD","Bias":"BUY","Reason":"DXY Down"}]),
 "cot":pd.DataFrame([{"Asset":"DXY","COT":"LONG","Meaning":"Institutions Long Dollar"}]),
}

def show(df,t):
    st.markdown(f"## {t}")
    st.table(df)

# HOME - OLD LAYOUT
if st.session_state.page=="home":
    st.markdown("# AMBUSHER RADAR")
    st.markdown("### DXY KING - HUNT LIQUIDITY")
    c1,c2,c3=st.columns(3)
    with c1:
        if st.button("FOREX"):
            st.session_state.page="forex"
            st.rerun()
        if st.button("INDICES"):
            st.session_state.page="indices"
            st.rerun()
    with c2:
        if st.button("COMMODS"):
            st.session_state.page="commods"
            st.rerun()
        if st.button("CRYPTO"):
            st.session_state.page="crypto"
            st.rerun()
    with c3:
        if st.button("COT TABLE"):
            st.session_state.page="cot"
            st.rerun()
        if st.button("INTEL NEWS"):
            st.session_state.page="news"
            st.rerun()
    st.divider()
    c4,c5=st.columns(2)
    with c4:
        if st.button("FUND DATES"):
            st.session_state.page="fund"
            st.rerun()
    with c5:
        if st.button("GLOSSARY"):
            st.session_state.page="gloss"
            st.rerun()
else:
    if st.button("BACK RADAR"):
        st.session_state.page="home"
        st.rerun()
    if st.session_state.page=="forex":
        show(GR["forex"],"FOREX RADAR")
    if st.session_state.page=="indices":
        show(GR["indices"],"INDICES RADAR")
    if st.session_state.page=="commods":
        show(GR["commods"],"COMMODS RADAR")
    if st.session_state.page=="crypto":
        show(GR["crypto"],"CRYPTO RADAR")
    if st.session_state.page=="cot":
        show(GR["cot"],"COT TABLE")
    if st.session_state.page=="news":
        st.markdown("## INTEL NEWS")
        st.table(pd.DataFrame(FUND,columns=["Date","News","Impact","Affects"]))
        st.divider()
        st.markdown("## WHAT IS IT?")
        for k,v in FUND_EXP.items():
            st.markdown(f"### {k}")
            st.write(f"**What:** {v[0]}")
            st

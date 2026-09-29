import streamlit as st
import pandas as pd

st.set_page_config(page_title="AMBUSHER RADAR",layout="wide")

st.markdown("""
<style>
.stApp{background:#0a0e13}
h1,h2,h3{color:#00ff88!important}
div[data-testid="stHorizontalBlock"]{
display:flex;
flex-wrap:wrap;
gap:10px;
}
div[data-testid="column"]{
min-width:45%;
}
div.stButton>button{
background:#111a22;
border:1px solid #00ff88;
color:white;
border-radius:12px;
height:55px;
width:100%;
font-weight:bold;
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
 ["2026-09-30","CPI","HIGH","ALL"],
 ["2026-10-01","NFP","HIGH","DXY"],
]

FUND_EXP={
 "INTEREST RATE":["Cost of borrowing","High=DXY UP GOLD DOWN","FOMC decides"],
 "CPI":["Inflation data","High CPI=DXY UP","Price rise"],
 "FOMC":["Fed Meeting","Decides rate","Most volatile"],
 "NFP":["US Jobs","High NFP=DXY UP","First Friday"],
 "GDP":["Growth","High GDP=DXY UP","Economy health"],
}

GLOSS={
 "BOS":["Break of Structure","Break high/low"],
 "CHoCH":["Change of Character","Trend shift"],
 "OB":["Order Block","Bank zone"],
 "FVG":["Fair Value Gap","Gap fill"],
 "DXY":["Dollar Index","Dollar power"],
}

GR={
 "forex":pd.DataFrame([{"Pair":"EURUSD","Bias":"BUY"}]),
 "indices":pd.DataFrame([{"Pair":"NAS100","Bias":"BUY"}]),
 "commods":pd.DataFrame([{"Pair":"GOLD","Bias":"BUY"}]),
 "crypto":pd.DataFrame([{"Pair":"BTCUSD","Bias":"BUY"}]),
 "cot":pd.DataFrame([{"Pair":"DXY","COT":"LONG"}]),
}

def show(df,t):
    st.markdown(f"## {t}")
    st.table(df)

if st.session_state.page=="home":
    st.markdown("# AMBUSHER RADAR")
    st.markdown("### DXY KING - HUNT LIQUIDITY")
    c1,c2=st.columns(2)
    with c1:
        if st.button("FOREX"):
            st.session_state.page="forex"
            st.rerun()
        if st.button("COMMODS"):
            st.session_state.page="commods"
            st.rerun()
        if st.button("COT TABLE"):
            st.session_state.page="cot"
            st.rerun()
        if st.button("FUND DATES"):
            st.session_state.page="fund"
            st.rerun()
    with c2:
        if st.button("INDICES"):
            st.session_state.page="indices"
            st.rerun()
        if st.button("CRYPTO"):
            st.session_state.page="crypto"
            st.rerun()
        if st.button("INTEL NEWS"):
            st.session_state.page="news"
            st.rerun()
        if st.button("GLOSSARY"):
            st.session_state.page="gloss"
            st.rerun()
else:
    if st.button("BACK RADAR"):
        st.session_state.page="home"
        st.rerun()
    if st.session_state.page=="forex":
        show(GR["forex"],"FOREX")
    if st.session_state.page=="indices":
        show(GR["indices"],"INDICES")
    if st.session_state.page=="commods":
        show(GR["commods"],"COMMODS")
    if st.session_state.page=="crypto":
        show(GR["crypto"],"CRYPTO")
    if st.session_state.page=="cot":
        show(GR["cot"],"COT")
    if st.session_state.page=="news":
        st.markdown("## INTEL NEWS")
        st.table(pd.DataFrame(FUND,columns=["Date","News","Imp","Affects"]))
        st.divider()
        st.markdown("## WHAT IS IT?")
        for k,v in FUND_EXP.items():
            st.markdown(f"### {k}")
            st.write(f"**What:** {v[0]}")
            st.write(f"**Effect:** {v[1]}")
            st.write(f"**Note:** {v[2]}")
            st.divider()
        st.markdown("## LEARN WORDS")
        for k,v in GLOSS.items():
            st.markdown(f"**{k}**: {v[0]} -> {v[1]}")
    if st.session_state.page=="fund":
        st.markdown("## FUND DATES")
        st.table(pd.DataFrame(FUND))
        for k,v in FUND_EXP.items():
            st.markdown(f"**{k}**: {v[0]} - {v[1]}")
    if st.session_state.page=="gloss":
        st.markdown("## GLOSSARY")
        for k,v in GLOSS.items():
            st.markdown(f"**{k}**: {v[0]} -> {v[1]}")

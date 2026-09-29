import streamlit as st
import pandas as pd

st.set_page_config(page_title="AMBUSHER RADAR",layout="wide")

if "page" not in st.session_state:
    st.session_state.page="home"

# FUNDAMENTALS EXPLAINED
FUND=[
 ["2026-09-29","FOMC","HIGH","DXY GOLD"],
 ["2026-09-30","CPI","HIGH","ALL PAIRS"],
 ["2026-10-01","NFP","HIGH","DXY"],
]

FUND_EXP={
 "INTEREST RATE":["Cost of borrowing","High rate=DXY UP GOLD DOWN","FOMC decides it"],
 "CPI":["Inflation data","High CPI=DXY UP","Shows price rise"],
 "FOMC":["Fed Meeting","Decides rate","Most volatile"],
 "NFP":["US Jobs data","High NFP=DXY UP","1st Friday"],
 "GDP":["Growth data","High GDP=DXY UP","Economy health"],
}

GLOSS={
 "BOS":["Break of Structure","Break high/low"],
 "CHoCH":["Change Character","Trend shift"],
 "OB":["Order Block","Bank zone"],
 "FVG":["Fair Value Gap","Gap fill"],
 "DXY":["Dollar Index","Dollar power"],
 "LIQUIDITY":["Stop Hunt","Where stops sit"],
}

GR={
 "forex":pd.DataFrame([{"pair":"EURUSD","bias":"BUY"}]),
 "indices":pd.DataFrame([{"pair":"NAS100","bias":"BUY"}]),
 "commods":pd.DataFrame([{"pair":"GOLD","bias":"BUY"}]),
 "crypto":pd.DataFrame([{"pair":"BTCUSD","bias":"BUY"}]),
 "cot":pd.DataFrame([{"pair":"DXY","COT":"LONG"}]),
}

def show(df,t):
    st.markdown(f"### {t}")
    st.table(df)

if st.session_state.page=="home":
    st.markdown("## AMBUSHER RADAR")
    c1,c2=st.columns(2)
    with c1:
        if st.button("FOREX"):
            st.session_state.page="forex"
            st.rerun()
        if st.button("INDICES"):
            st.session_state.page="indices"
            st.rerun()
        if st.button("COMMODS"):
            st.session_state.page="commods"
            st.rerun()
        if st.button("CRYPTO"):
            st.session_state.page="crypto"
            st.rerun()
    with c2:
        if st.button("COT TABLE"):
            st.session_state.page="cot"
            st.rerun()
        if st.button("INTEL NEWS"):
            st.session_state.page="news"
            st.rerun()
        if st.button("FUND DATES"):
            st.session_state.page="fund"
            st.rerun()
        if st.button("GLOSSARY"):
            st.session_state.page="gloss"
            st.rerun()
else:
    if st.button("BACK RADAR"):
        st.session_state.page="home"
        st.rerun()
    if st.session_state.page=="forex":
        show(GR["forex"],"FOREX DXY KING")
    if st.session_state.page=="indices":
        show(GR["indices"],"INDICES")
    if st.session_state.page=="commods":
        show(GR["commods"],"GOLD OIL")
    if st.session_state.page=="crypto":
        show(GR["crypto"],"CRYPTO")
    if st.session_state.page=="cot":
        show(GR["cot"],"COT TABLE")
    if st.session_state.page=="news":
        st.markdown("### INTEL NEWS")
        st.table(pd.DataFrame(FUND))
        st.divider()
        st.markdown("### WHAT IS IT?")
        for k,v in FUND_EXP.items():
            st.markdown(f"**{k}**")
            st.write(f"- What: {v[0]}")
            st.write(f"- Effect: {v[1]}")
            st.write(f"- Note: {v[2]}")
            st.divider()
        st.markdown("### LEARN WORDS")
        for k,v in GLOSS.items():
            st.markdown(f"**{k}**: {v[0]} -> {v[1]}")
    if st.session_state.page=="fund":
        st.markdown("### FUND DATES")
        st.table(pd.DataFrame(FUND))
        for k,v in FUND_EXP.items():
            st.markdown(f"**{k}**: {v[0]} - {v[1]}")
    if st.session_state.page=="gloss":
        st.markdown("### GLOSSARY")
        for k,v in GLOSS.items():
            st.markdown(f"**{k}**: {v[0]} -> {v[1]}")

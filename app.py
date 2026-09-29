import streamlit as st
import pandas as pd

st.set_page_config(page_title="AMBUSHER RADAR", layout="wide")

if "page" not in st.session_state:
    st.session_state.page="home"

FUND=[
 ["2026-09-29","FOMC","HIGH","DXY GOLD"],
 ["2026-09-30","CPI","HIGH","ALL"],
 ["2026-10-01","NFP","HIGH","DXY"],
]

GLOSS={
 "BOS":["Break of Structure","Market breaks high/low"],
 "CHoCH":["Change of Character","Trend shift"],
 "OB":["Order Block","Institution zone"],
 "FVG":["Fair Value Gap","Gap to fill"],
 "DXY":["Dollar Index","Dollar strength"],
}

GR={
 "forex":pd.DataFrame([{"pair":"EURUSD","bias":"BUY"},{"pair":"DXY","bias":"SELL"}]),
 "indices":pd.DataFrame([{"pair":"NAS100","bias":"BUY"}]),
 "commods":pd.DataFrame([{"pair":"GOLD","bias":"BUY"}]),
 "crypto":pd.DataFrame([{"pair":"BTCUSD","bias":"BUY"}]),
 "cot":pd.DataFrame([{"pair":"DXY","COT":"LONG"}]),
}

def show(df,title):
    st.markdown(f"### {title}")
    st.table(df)

if st.session_state.page=="home":
    st.markdown("## AMBUSHER RADAR")
    c1,c2,c3=st.columns(3)
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
    with c2:
        if st.button("CRYPTO"):
            st.session_state.page="crypto"
            st.rerun()
        if st.button("COT TABLE"):
            st.session_state.page="cot"
            st.rerun()
        if st.button("INTEL NEWS"):
            st.session_state.page="news"
            st.rerun()
    with c3:
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
        st.markdown("### LEARN WORDS")
        for k,v in GLOSS.items():
            st.markdown(f"**{k}**: {v[0]} -> {v[1]}")
    if st.session_state.page=="fund":
        st.markdown("### FUND DATES")
        st.table(pd.DataFrame(FUND))
    if st.session_state.page=="gloss":
        st.markdown("### GLOSSARY")
        for k,v in GLOSS.items():
            st.markdown(f"**{k}**: {v[0]} -> {v[1]}")

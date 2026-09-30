import streamlit as st
import os

st.set_page_config(page_title="FX AMBUSHERS", layout="wide")

if os.path.exists("logo.jpg"):
    st.image("logo.jpg", width=110)

st.markdown("# FX AMBUSHERS")
st.caption("Patience is Profit")

if 'page' not in st.session_state:
    st.session_state.page = "radar"

with st.sidebar:
    st.button("🎯 RADAR", on_click=lambda: setattr(st.session_state, 'page', 'radar'))
    st.button("🔍 FINDER", on_click=lambda: setattr(st.session_state, 'page', 'finder'))
    st.button("📚 LEARN TECHNICAL", on_click=lambda: setattr(st.session_state, 'page', 'learn_tech'))

if st.session_state.page == "radar":
    st.subheader("AMBUSH RADAR - Live Bias")
    c1,c2,c3 = st.columns(3)
    with c1:
        st.metric("DXY", "108.5", "+7 BULL")
        st.progress(85)
        st.write("Powell Hawk No Cut + CPI 3.2% Hot")
        st.write("COT: +3% Long Change")
        st.write("Retail: 65% Long")
    with c2:
        st.metric("EURUSD", "1.0650", "-7 BEAR")
        st.progress(15)
        st.write("EUR Weak vs USD Strong")
        st.write("Retail 70% Long = SELL")
    with c3:
        st.metric("GOLD", "2650", "-8 BEAR")
        st.progress(10)
        st.write("DXY Strong + Yields Up")

if st.session_state.page == "finder":
    st.subheader("FINDER -10 to +10")
    st.info("Score 0 = NO TRADE. Only trade -7 or +7")
    st.metric("EURUSD", "-7 BEAR")

if st.session_state.page == "learn_tech":
    st.subheader("TECHNICAL ACADEMY")
    st.write("Your uploaded pictures:")
        for f in os.listdir("."):
        if f.lower().endswith((".png",".jpg")):
            if "logo" not in f.lower():
                st.image(f)

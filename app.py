import streamlit as st
import os

if "page" not in st.session_state:
    st.session_state.page = "radar"

st.write("AMBUSHER RADAR")
st.title("Patience is Profit")

c1,c2,c3 = st.columns(3)
if c1.button("RADAR"):
    st.session_state.page = "radar"
if c2.button("FINDER"):
    st.session_state.page = "finder"
if c3.button("LEARN"):
    st.session_state.page = "learn_tech"

if st.session_state.page == "radar":
    st.subheader("RADAR -10 to +10")
    st.metric("DXY", "+7 BULL")
    st.metric("GOLD", "-8 BEAR")
    st.write("DXY Strong + Yields Up")

if st.session_state.page == "finder":
    st.subheader("FINDER -10 to +10")
    st.info("Score 0 = NO TRADE. Only trade 7+")
    st.metric("EURUSD", "-7 BEAR")

if st.session_state.page == "learn_tech":
    st.subheader("TECHNICAL ACADEMY")
    st.write("Your pictures coming soon")

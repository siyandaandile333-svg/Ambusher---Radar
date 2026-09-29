import streamlit as st
import pandas as pd

st.set_page_config(page_title="FX AMBUSHERS",layout="wide")
st.markdown("<style>.stApp{background:#080a0a}</style>",unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page="home"

SCORE=71
BIAS="BULL"

def dxy_gauge():
    angle = -90 + (SCORE*1.8)
    st.markdown(f"""
    <div style='border:1px solid #222;border-radius:20px;padding:15px;background:#0f1414;border-left:4px solid #00ff66'>
     <div style='text-align:center;color:#888;letter-spacing:2px'>DXY AMBUSH</div>
     <div style='text-align:center;color:#00ff66;font-size:32px;font-weight:900;margin:5px 0'>{BIAS} {SCORE}</div>
     <div style='width:260px;height:130px;margin:0 auto;position:relative;background:conic-gradient(from 270deg at 50% 100%, #ff2b2b 0deg 60deg, #ffcc00 60deg 120deg, #00cc66 120deg 180deg);border-radius:130px 130px 0 0'>
      <div style='width:3px;height:110px;background:white;position:absolute;bottom:0;left:50%;transform-origin:bottom;transform:rotate({angle}deg)'></div>
      <div style='width:14px;height:14px;background:white;border-radius:50%;position:absolute;bottom:-7px;left:calc(50% - 7px)'></div>
     </div>
     <div style='font-size:12px;margin-top:10px;color:#00ff66'>Bull: Fed Hawk No Cut Dot High + Yield 4.2 Up = USD Buy</div>
     <div style='font-size:12px;color:#ff4444'>Bear: Fed Cut + Gold Risk On = USD Sell</div>
     <div style='font-size:12px;color:#888'>Neu: GPR Oil BoJ Rate</div>
    </div>
    """,unsafe_allow_html=True)

try:
    st.image("logo.png",use_container_width=True)
except:
    st.markdown("<h2 style='color:#d4af37;text-align:center'>FX AMBUSHERS</h2>",unsafe_allow_html=True)

dxy_gauge()
st.write("")

# BUTTONS - VERTICAL LIKE OLD
def go(p):
    st.session_state.page=p

if st.session_state.page=="home":
    if st.button("FOREX 6"): go("forex"); st.rerun()
    if st.button("INDICES"): go("indices"); st.rerun()
    if st.button("INTEL NEWS"): go("news"); st.rerun()
    if st.button("FUND DATES"): go("fund"); st.rerun()
    if st.button("LEARN WORDS"): go("words"); st.rerun()
    if st.button("GOLD OIL"): go("gold"); st.rerun()
    if st.button("CRYPTO"): go("crypto"); st.rerun()
    if st.button("COT TABLE"): go("cot"); st.rerun()
else:
    if st.button("⬅ BACK RADAR"):
        st.session_state.page="home"
        st.rerun()
    
    dxy_gauge()
    st.write("")

    if st.session_state.page=="forex":
        st.markdown("### FOREX 6 - WHY BULLISH / BEARISH")
        df=pd.DataFrame([
            ["EURUSD","SELL","DXY Bull 71 + Fed Hawk = USD Buy"],
            ["GBPUSD","SELL","DXY Bull + Yield 4.2 Up"],
            ["USDJPY","BUY","DXY Bull + BoJ Dovish"],
            ["AUDUSD","SELL","DXY Bull + Risk Off"],
            ["USDCHF","BUY","DXY Bull 71"],
            ["USDCAD","BUY","DXY Bull + Oil Down"],
        ],columns=["Pair","Bias","Why"])
        st.data
        

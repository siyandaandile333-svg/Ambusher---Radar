import streamlit as st, pandas as pd
from datetime import datetime

st.set_page_config(page_title="FX AMBUSHERS",layout="wide")
st.markdown("<style>.stApp{background:#080a0a} .card{border:1px solid #222;border-radius:20px;padding:15px;background:#0f1414;border-left:4px solid #00ff66}</style>",unsafe_allow_html=True)

if "page" not in st.session_state: st.session_state.page="home"

# DXY GAUGE DATA - OLD
BULL_TXT="Bull: Fed Hawk No Cut Dot High + Yield 4.2 Up = USD Buy"
BEAR_TXT="Bear: Fed Cut + Gold Risk On = USD Sell"
NEU_TXT="Neu: GPR Oil BoJ Rate"
SCORE=71
BIAS="BULL"

def dxy_gauge():
    # Angle: 71% => needle in green zone (about 35deg from center to right)
    angle = -90 + (SCORE*1.8)  # 0%= -90deg left, 100%= +90deg right
    st.markdown(f"""
    <div class="card">
     <div style='text-align:center;color:#888;letter-spacing:2px'>DXY AMBUSH</div>
     <div style='text-align:center;color:#00ff66;font-size:32px;font-weight:900;margin:5px 0'>{BIAS} {SCORE}</div>
     <div style='width:260px;height:130px;margin:0 auto;position:relative;background:conic-gradient(from 270deg at 50% 100%, #ff2b2b 0deg 60deg, #ffcc00 60deg 120deg, #00cc66 120deg 180deg);border-radius:130px 130px 0 0'>
      <div style='width:3px;height:110px;background:white;position:absolute;bottom:0;left:50%;transform-origin:bottom;transform:rotate({angle}deg);border-radius:2px'></div>
      <div style='width:14px;height:14px;background:white;border-radius:50%;position:absolute;bottom:-7px;left:calc(50% - 7px)'></div>
     </div>
     <div style='font-size:12px;margin-top:10px;color:#00ff66'>{BULL_TXT}</div>
     <div style='font-size:12px;color:#ff4444'>{BEAR_TXT}</div>
     <div style='font-size:12px;color:#888'>{NEU_TXT}</div>
    </div>
    """,unsafe_allow_html=True)

# OLD DATA - PAIRS WHY BULLISH/BEARISH
FOREX=pd.DataFrame([
 {"Pair":"EURUSD","Bias":"SELL","Why":"DXY Bull 71 + Fed Hawk = USD Buy, EUR Weak"},
 {"Pair":"GBPUSD","Bias":"SELL","Why":"DXY Bull + Yield 4.2 Up"},
 {"Pair":"USDJPY","Bias":"BUY","Why":"DXY Bull + BoJ Dovish"},
 {"Pair":"AUDUSD","Bias":"SELL","Why":"DXY Bull + Risk Off"},
 {"Pair":"USDCHF","Bias":"BUY","Why":"DXY Bull 71"},
 {"Pair":"USDCAD","Bias":"BUY","Why":"DXY Bull + Oil Down"},
])

try: st.image("logo.png",use_container_width=True)
except: st.markdown("<h2 style='color:#d4af37;text-align:center'>FX AMBUSHERS</h2>",unsafe_allow_html=True)

dxy_gauge()

st.markdown("## ")

if st.session_state.page=="home":
    if st.button("FOREX 6"): st.session_state.page="forex"; st.rerun

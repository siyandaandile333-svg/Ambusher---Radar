import streamlit as st
import pandas as pd
import os, glob

st.set_page_config(page_title="FX AMBUSHERS", layout="wide")
st.markdown("<style>.stApp{background:#080a0a}</style>", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page="home"

DXY=71

def gauge_card(title, score, bull, bear, neu, size=260):
    angle=-90 + (score*1.8)
    if score>=60:
        col="#00ff66"
        bcol="#00ff66"
        bias="BULL"
    elif score<=40:
        col="#ff4444"
        bcol="#ff4444"
        bias="BEAR"
    else:
        col="#ffcc00"
        bcol="#ffcc00"
        bias="NEU"
    h=size//2
    return f"""
<div style='border:1px solid #222;border-radius:18px;padding:12px;background:#0f1414;border-left:4px solid {bcol};margin-bottom:12px'>
<div style='text-align:center;color:#888;font-size:11px;letter-spacing:2px'>{title}</div>
<div style='text-align:center;color:{col};font-weight:900;font-size:{22 if size>200 else 16}px'>{bias} {score}</div>
<div style='width:{size}px;height:{h}px;margin:8px auto;position:relative;background:conic-gradient(from 270deg at 50% 100%, #ff2b2b 0deg 60deg, #ffcc00 60deg 120deg, #00cc66 120deg 180deg);border-radius:{size}px {size}px 0 0'>
<div style='width:3px;height:{h-10}px;background:white;position:absolute;bottom:0;left:50%;transform-origin:bottom;transform:rotate({angle}deg)'></div>
<div style='width:12px;height:12px;background:white;border-radius:50%;position:absolute;bottom:-6px;left:calc(50% - 6px)'></div>
</div>
<div style='font-size:11px;color:#00ff66;margin-top:6px'>Bull: {bull}</div>
<div style='font-size:11px;color:#ff5555'>Bear: {bear}</div>
<div style='font-size:11px;color:#888'>Neu: {neu}</div>
</div>
"""

def main_dxy():
    img=None
    for f in ["logo.png","logo.jpg","IMG-20260929-WA1810.jpg"]:
        if os.path.exists(f):
            img=f
            break
    if not img:
        files=glob.glob("*.jpg")+glob.glob("*.png")
        if files:
            img=files[0]
    if img:
        st.image(img, use_container_width=True)
    st.markdown(gauge_card("DXY AMBUSH", DXY, "Fed Hawk No Cut Dot High + Yield 4.2 Up = USD Buy", "Fed Cut + Gold Risk On = USD Sell", "GPR Oil BoJ Rate", 260), unsafe_allow_html=True)

main_dxy()

# PAIRS WITH FULL BULL/BEAR/NEU LIKE DXY
forex=[
    ("EURUSD",29,"ECB Hawk + Fed Dovish Cut + CPI Low = EUR Buy","Fed Hawk No Cut + Yield 4.2 Up + DXY Bull 71 = EUR Sell","ECB Rate + GPR + Oil"),
    ("GBPUSD",30,"BoE Hawk + Fed Cut + UK CPI High = GBP Buy","Fed Hawk + Yield Up + DXY Bull 71 = GBP Sell","BoE Rate + Brexit + GPR"),
    ("USDJPY",71,"DXY Bull 71 + BoJ Dovish No Hike + Yield Up = USDJPY Buy","BoJ Hawk Hike + Fed Cut + Risk On Yen Buy = USDJPY Sell","BoJ Rate + Ueda + GPR"),
    ("AUDUSD",28,"RBA Hawk + Gold Up + China Stimulus + Fed Cut = AUD Buy","DXY Bull 71 + Fed Hawk + Risk Off + Oil Down = AUD Sell","RBA Rate + China Data + Gold"),
    ("USDCHF",71,"DXY Bull 71 + SNB Dovish + Yield Up = USDCHF Buy","SNB Hawk + Fed Cut + Risk Off CHF Buy = USDCHF Sell","SNB Rate + Gold + GPR"),
    ("USDCAD",70,"DXY Bull 71 + Oil Down + BoC Dovish = USDCAD Buy","Oil Up + BoC Hawk + Fed Cut + DXY Bear = USDCAD Sell","BoC Rate + Oil + GPR"),
]
commod=[
    ("GOLD",25,"Fed Dovish Cut + Yield Down + GPR High War = Gold Buy","DXY Bull 71 + Fed Hawk + Yield 4.2 Up + Risk On = Gold Sell","GPR + Fed + CPI + Oil"),
    ("SILVER",27,"Fed Cut + Gold Up + Industrial Demand = Silver Buy","DXY Bull 71 + Yield Up + Risk Off = Silver Sell","Gold + Copper + GPR"),
    ("OIL",35,"GPR War + OPEC Cut + Demand Up = Oil Buy","DXY Bull 71 + Recession Fear + Supply Up = Oil Sell","OPEC + GPR + USD + Inventory"),
]
indices=[
    ("US30",30,"Fed Dovish Cut + Earnings Up + Yield Down = US30 Buy","DXY Bull 71 + Fed Hawk + Yield 4.2 Up + GPR = US30 Sell","FOMC + CPI + Earnings"),
    ("NAS100",28,"Fed Cut + Tech Earnings

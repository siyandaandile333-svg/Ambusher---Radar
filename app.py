import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="FX AMBUSHERS", layout="wide")
st.markdown('<style>.stApp{background:#080a0a}</style>', unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page="home"

DXY=71
SA_TIME = datetime.now().strftime("%H:%M SAST")

# HEALTH + LOGO - SAFE
st.markdown(f"<div style='background:#0a1a0a;border:1px solid #00ff66;border-radius:12px;padding:10px;text-align:center;color:#00ff66'>✅ RADAR LIVE v1.1 - {SA_TIME} | DXY {DXY} BULL | Why's RESTORED</div>", unsafe_allow_html=True)

for logo_file in ["logo.png","logo.jpg","IMG-20260929-WA1810.jpg"]:
    if os.path.exists(logo_file):
        st.image(logo_file, use_container_width=True)
        break

def gauge_card(title, score, bull, bear, neu, size=260):
    angle = -90 + (score*1.8)
    if score>=60:
        col="#00ff66"; bcol="#00ff66"; bias="BULL"
    elif score<=40:
        col="#ff4444"; bcol="#ff4444"; bias="BEAR"
    else:
        col="#ffcc00"; bcol="#ffcc00"; bias="NEU"
    h = size//2
    a = "<div style='border:1px solid #222;border-radius:18px;padding:12px;background:#0f1414;"
    a += "border-left:4px solid " + bcol + ";margin-bottom:12px'>"
    b = "<div style='text-align:center;color:#888;font-size:11px'>" + title + "</div>"
    c = "<div style='text-align:center;color:" + col + ";font-weight:900;font-size:20px'>"
    c += bias + " " + str(score) + "</div>"
    d = "<div style='width:" + str(size) + "px;height:" + str(h) + "px;margin:8px auto;position:relative;"
    d += "background:conic-gradient(from 270deg at 50% 100%, #ff2b2b 0 60deg, #ffcc00 60deg 120deg, #00cc66 120deg 180deg);"
    d += "border-radius:" + str(size) + "px " + str(size) + "px 0 0'>"
    e = "<div style='width:3px;height:" + str(h-10) + "px;background:white;position:absolute;bottom:0;left:50%;"
    e += "transform-origin:bottom;transform:rotate(" + str(angle) + "deg)'></div></div>"
    # Why's - broken into 3 short lines to avoid phone break
    f = "<div style='font-size:11px;color:#00ff66'>Bull: " + bull + "</div>"
    f += "<div style='font-size:11px;color:#ff6666'>Bear: " + bear + "</div>"
    f += "<div style='font-size:11px;color:#888'>Neu: " + neu + "</div></div>"
    return a+b+c+d+e+f

# FULL WHY'S RESTORED - SHORT LINES
st.markdown(gauge_card("DXY AMBUSH", DXY, "Fed Hawk No Cut + Yield 4.2 Up = USD Buy", "Fed Cut + Gold Risk On = USD Sell", "GPR Oil BoJ Rate", 280), unsafe_allow_html=True)

forex=[
    ("EURUSD",29,"ECB Hawk + Fed Cut = EUR Buy","Fed Hawk + Yield Up + DXY 71 = Sell","ECB Rate + GPR"),
    ("GBPUSD",30,"BoE Hawk + Fed Cut = GBP Buy","Fed Hawk + Yield Up + DXY 71 = Sell","BoE Rate + GPR"),
    ("USDJPY",71,"DXY 71 + BoJ Dovish + Yield Up = Buy","BoJ Hawk + Fed Cut = Sell","BoJ Rate + GPR"),
    ("AUDUSD",28,"RBA Hawk + Gold Up = Buy","DXY 71 + Risk Off = Sell","RBA Rate + China"),
    ("USDCHF",71,"DXY 71 + SNB Dovish = Buy","SNB Hawk + Fed Cut = Sell","SNB Rate + Gold"),
    ("USDCAD",70,"DXY 71 + Oil Down = Buy","Oil Up + BoC Hawk = Sell","BoC Rate + Oil"),
]
commod=[
    ("GOLD",25,"Fed Cut + Yield Down + GPR = Buy","DXY 71 + Hawk + Yield Up = Sell","GPR + Fed"),
    ("SILVER",27,"Fed Cut + Gold Up = Buy","DXY 71 + Yield Up = Sell","Gold + Copper"),
    ("OIL",35,"GPR War + OPEC Cut = Buy","DXY 71 + Recession = Sell","OPEC + GPR"),
]
indices=[
    ("US30",30,"Fed Cut + Earnings Up = Buy","DXY 71 + Hawk + Yield Up = Sell","FOMC + CPI"),
    ("NAS100",28,"Fed Cut + Tech Up = Buy","DXY 71 + Yield Up = Sell","Earnings + Yield"),
    ("SPX500",29,"Fed Cut + Strong = Buy","DXY 71 + Hawk = Sell","FOMC + NFP"),
]
crypto=[
    ("BTCUSD",30,"Fed

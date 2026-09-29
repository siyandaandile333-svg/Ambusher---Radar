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
<div style='text-align:center;color:#888;font-size:11px'>{title}</div>
<div style='text-align:center;color:{col};font-weight:900;font-size:20px'>{bias} {score}</div>
<div style='width:{size}px;height:{h}px;margin:8px auto;position:relative;background:conic-gradient(from 270deg at 50% 100%, #ff2b2b 0deg 60deg, #ffcc00 60deg 120deg, #00cc66 120deg 180deg);border-radius:{size}px {size}px 0 0'>
<div style='width:3px;height:{h-10}px;background:white;position:absolute;bottom:0;left:50%;transform-origin:bottom;transform:rotate({angle}deg)'></div>
<div style='width:12px;height:12px;background:white;border-radius:50%;position:absolute;bottom:-6px;left:calc(50% - 6px)'></div>
</div>
<div style='font-size:11px;color:#00ff66'>Bull: {bull}</div>
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
    st.markdown(gauge_card("DXY AMBUSH", DXY, "Fed Hawk No Cut + Yield 4.2 Up = USD Buy", "Fed Cut + Gold Risk On = USD Sell", "GPR Oil BoJ Rate", 260), unsafe_allow_html=True)

main_dxy()

forex=[
    ("EURUSD",29,"ECB Hawk + Fed Cut = EUR Buy","Fed Hawk + Yield Up + DXY 71 = EUR Sell","ECB Rate + GPR"),
    ("GBPUSD",30,"BoE Hawk + Fed Cut = GBP Buy","Fed Hawk + Yield Up + DXY 71 = GBP Sell","BoE Rate + GPR"),
    ("USDJPY",71,"DXY 71 + BoJ Dovish + Yield Up = Buy","BoJ Hawk Hike + Fed Cut = Sell","BoJ Rate + GPR"),
    ("AUDUSD",28,"RBA Hawk + Gold Up + China = AUD Buy","DXY 71 + Risk Off + Oil Down = AUD Sell","RBA Rate + China + Gold"),
    ("USDCHF",71,"DXY 71 + SNB Dovish + Yield Up = Buy","SNB Hawk + Fed Cut + Risk Off = Sell","SNB Rate + Gold"),
    ("USDCAD",70,"DXY 71 + Oil Down + BoC Dovish = Buy","Oil Up + BoC Hawk + Fed Cut = Sell","BoC Rate + Oil"),
]
commod=[
    ("GOLD",25,"Fed Cut + Yield Down + GPR High = Gold Buy","DXY 71 + Hawk + Yield Up = Gold Sell","GPR + Fed + CPI"),
    ("SILVER",27,"Fed Cut + Gold Up = Silver Buy","DXY 71 + Yield Up = Silver Sell","Gold + Copper"),
    ("OIL",35,"GPR War + OPEC Cut = Oil Buy","DXY 71 + Recession = Oil Sell","OPEC + GPR"),
]
indices=[
    ("US30",30,"Fed Cut + Earnings Up = Buy","DXY 71 + Hawk + Yield Up = Sell","FOMC + CPI"),
    ("NAS100",28,"Fed Cut + Tech Earnings Up = Buy","DXY 71 + Yield Up + Hawk = Sell","Earnings + Yield"),
    ("SPX500",29,"Fed Cut + Strong Econ = Buy","DXY 71 + Hawk + Yield Up = Sell","FOMC + NFP"),
]

if st.session_state.page=="home":
    if st.button("FOREX 6"): st.session_state.page="forex"
    if st.button("GOLD OIL"): st.session_state.page="gold"
    if st.button("INDICES"): st.session_state.page="indices"
else:
    if st.button("BACK RADAR"): st.session_state.page="home"
    main_dxy()
    if st.session_state.page=="forex":
        st.markdown("### FOREX 6 - FULL WHY LIKE DXY")
        c=st.columns(2)
        for i,(p,s,bu,be,ne) in enumerate(forex):
            with c[i%2]:
                st.markdown(gauge_card(p,s,bu,be,ne,170), unsafe_allow_html=True)
    if st.session_state.page=="gold":
        st.markdown("### COMMODITIES - FULL WHY")
        c=st.columns(2)
        for i,(p,s,bu,be,ne) in enumerate(commod):
            with c[i%2]:
                st.markdown(gauge_card(p,s,bu,be,ne,170), unsafe_allow_html=True)
    if st.session_state.page=="indices":
        st.markdown("### INDICES - FULL WHY")
        c=st.columns(2)
        for i,(p,s,bu,be,ne) in enumerate(indices):
            with c[i%2]:
                st.markdown(gauge_card(p,s,bu,be,ne,170), unsafe_allow_html=True)

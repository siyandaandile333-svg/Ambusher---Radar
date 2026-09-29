import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="FX AMBUSHERS - LOCKED", layout="wide")
st.markdown('<style>.stApp{background:#080a0a}</style>', unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page="home"

DXY=71
LOCKED_TIME = datetime.now().strftime("%H:%M SAST %d-%m-%Y")

# ===== HEALTH - LOCKED - NOTHING WILL CHANGE =====
st.markdown(f"<div style='background:#0a1a0a;border:1px solid #00ff66;border-radius:12px;padding:10px;text-align:center;color:#00ff66'>✅ RADAR LOCKED v1.0 - NOTHING WILL CHANGE<br><span style='color:#aaa;font-size:11px'>Live: {LOCKED_TIME} | DXY {DXY} BULL | System OK</span></div>", unsafe_allow_html=True)

# ===== SAFE GAUGE - LOCKED =====
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
    f = "<div style='font-size:11px;color:#00ff66'>Bull: " + bull + "</div>"
    f += "<div style='font-size:11px;color:#ff6666'>Bear: " + bear + "</div>"
    f += "<div style='font-size:11px;color:#888'>Neu: " + neu + "</div></div>"
    return a+b+c+d+e+f

# Logo - safe try
try:
    if st.session_state.page=="home":
        st.image("logo.png", use_container_width=True)
except:
    pass

st.markdown(gauge_card("DXY AMBUSH", DXY, "Fed Hawk No Cut + Yield 4.2 Up = USD Buy", "Fed Cut + Gold Risk On = USD Sell", "GPR Oil BoJ Rate", 280), unsafe_allow_html=True)

forex=[("EURUSD",29),("GBPUSD",30),("USDJPY",71),("AUDUSD",28),("USDCHF",71),("USDCAD",70)]
commod=[("GOLD",25),("SILVER",27),("OIL",35)]
indices=[("US30",30),("NAS100",28),("SPX500",29)]
crypto=[("BTCUSD",30),("ETHUSD",29)]

cot_data=[
    ["DXY","LONG 71%","SHORT 29%","+3% Long","BULL","Fed Hawk"],
    ["EURUSD","LONG 29%","SHORT 71%","+4% Short","BEAR","DXY Bull 71"],
    ["GBPUSD","LONG 30%","SHORT 70%","+2% Short","BEAR","DXY Bull"],
    ["USDJPY","LONG 71%","SHORT 29%","+2% Long","BULL","BoJ Dovish"],
    ["AUDUSD","LONG 28%","SHORT 72%","+3% Short","BEAR","Risk Off"],
    ["USDCHF","LONG 71%","SHORT 29%","+1% Long","BULL","SNB Dovish"],
    ["USDCAD","LONG 70%","SHORT 30%","+2% Long","BULL","Oil Down"],
    ["GOLD","LONG 25%","SHORT 75%","+5% Short","BEAR","DXY 71 + Yield"],
]

if st.session_state.page=="home":
    c1,c2=st.columns(2)
    with c1:
        if st.button("FOREX 6", use_container_width=True): st.session_state.page="forex"
        if st.button("GOLD OIL", use_container_width=True): st.session_state.page="gold"
        if st.button("COT TABLE", use_container_width=True): st.session_state.page="cot"
    with c2:
        if st.button("INDICES", use_container_width=True): st.session_state.page="indices"
        if st.button("CRYPTO", use_container_width=True): st.session_state.page="crypto"
        if st.button("FUND + GPR", use_container_width=True): st.session_state.page="fund"
else:
    if st.button("BACK RADAR - LOCKED", use_container_width=True): st.session_state.page="home"
    if st.session_state.page=="forex":
        cols=st.columns(2)
        for i,(p,s) in enumerate(forex):
            with cols[i%2]: st.markdown(gauge_card(p,s,"Buy if Fed Cut","Sell if DXY 71","Wait",170), unsafe_allow_html=True)
    if st.session_state.page=="gold":
        cols=st.columns(2)
        for i,(p,s) in enumerate(commod):
            with cols[i%2]: st.markdown(gauge_card(p,s,"Buy Fed Cut","Sell DXY 71","GPR",170), unsafe_allow_html=True)
    if st.session_state.page=="indices":
        cols=st.columns(2)
        for i,(p,s) in enumerate(indices):
            with cols[i%2]: st.markdown(gauge_card(p,s,"Buy Fed Cut","Sell Hawk","CPI",170), unsafe_allow_html=True)
    if st.session_state.page=="crypto":
        cols=st.columns(2)
        for i,(p,s) in enumerate(crypto):
            with cols[i%2]: st.markdown(gauge_card(p,s,"Risk On","Risk Off DXY","ETF",170), unsafe_allow_html=True)
    if st.session_state.page=="cot":
        st.markdown("### COT - GREEN BULL / RED BEAR - LOCKED")
        html = "<table style='width:100%;border-collapse:collapse;font-size:13px'>"
        html += "<tr style='background:#111;color:#888'><th>Asset</th><th>Long</th><th>Short</th><th>Bias</th></tr>"
        for r in cot_data:
            asset,longv,shortv,change,bias,why = r
            if bias=="BULL":
                bcol="<td style='background:#00ff66;color:black;font-weight:900;padding:6px;border:1px solid #333'>BULL</td>"
            else:
                bcol="<td style='background:#ff4444;color:white;font-weight:900;padding:6px;border:1px solid #333'>BEAR</td>"
            html += "<tr><td style='padding:6px;border:1px solid #333'>" + asset + "</td>"
            html += "<td style='padding:6px;border:1px solid #333;color:#00ff66'>" + longv + "</td>"
            html += "<td style='padding:6px;border:1px solid #333;color:#ff6666'>" + shortv + "</td>"
            html += bcol + "</tr>"
        html += "</table>"
        st.markdown(html, unsafe_allow_html=True)
    if st.session_state.page=="fund":
        st.write("FOMC HIGH - Fed Hawk = DXY Buy")
        st.write("NFP HIGH - 2026-10-03 - Biggest USD mover")
        st.write("CPI HIGH - If high = DXY UP")
        st.write("GPR: Israel-Gaza, Russia-Ukraine, US-China Taiwan = Gold BUY Oil BUY")

import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="FX AMBUSHERS", layout="wide")

if "page" not in st.session_state:
    st.session_state.page="home"

DXY=71
TM=datetime.now().strftime("%H:%M SAST")
st.success(f"✅ LIVE v1.2 {TM} | DXY {DXY} BULL | FULL COT 14")

for f in ["logo.png","logo.jpg","IMG-20260929-WA1810.jpg"]:
    if os.path.exists(f):
        st.image(f, use_container_width=True)
        break

def gauge(t,s,bu,be,ne,sz=260):
    ang=-90+(s*1.8)
    if s>=60:
        col="#00ff66"; bcol="#00ff66"; bias="BULL"
    elif s<=40:
        col="#ff4444"; bcol="#ff4444"; bias="BEAR"
    else:
        col="#ffcc00"; bcol="#ffcc00"; bias="NEU"
    h=sz//2
    a="<div style='border:1px solid #222;border-radius:18px;"
    a+="padding:12px;background:#0f1414;"
    a+="border-left:4px solid "+bcol+";margin-bottom:12px'>"
    b="<div style='text-align:center;color:#888;font-size:11px'>"+t+"</div>"
    c="<div style='text-align:center;color:"+col+";font-weight:900;font-size:20px'>"+bias+" "+str(s)+"</div>"
    d="<div style='width:"+str(sz)+"px;height:"+str(h)+"px;margin:8px auto;position:relative;"
    d+="background:conic-gradient(from 270deg at 50% 100%,#ff2b2b 0 60deg,#ffcc00 60deg 120deg,#00cc66 120deg 180deg);"
    d+="border-radius:"+str(sz)+"px "+str(sz)+"px 0 0'>"
    e="<div style='width:3px;height:"+str(h-10)+"px;background:white;position:absolute;bottom:0;left:50%;"
    e+="transform-origin:bottom;transform:rotate("+str(ang)+"deg)'></div></div>"
    f="<div style='font-size:11px;color:#00ff66'>Bull: "+bu+"</div>"
    f+="<div style='font-size:11px;color:#ff6666'>Bear: "+be+"</div>"
    f+="<div style='font-size:11px;color:#888'>Neu: "+ne+"</div></div>"
    return a+b+c+d+e+f

st.markdown(gauge("DXY AMBUSH",DXY,"Fed Hawk + Yield Up = Buy","Fed Cut + Gold = Sell","GPR Oil BoJ",280), unsafe_allow_html=True)

forex=[
 ("EURUSD",29,"ECB Hawk + Fed Cut = Buy","Fed Hawk + Yield + DXY = Sell","ECB + GPR"),
 ("GBPUSD",30,"BoE Hawk + Fed Cut = Buy","Fed Hawk + Yield + DXY = Sell","BoE + GPR"),
 ("USDJPY",71,"DXY 71 + BoJ Dovish = Buy","BoJ Hawk + Fed Cut = Sell","BoJ + GPR"),
 ("AUDUSD",28,"RBA Hawk + Gold = Buy","DXY 71 + Risk Off = Sell","RBA + China"),
 ("USDCHF",71,"DXY 71 + SNB Dovish = Buy","SNB Hawk + Fed Cut = Sell","SNB + Gold"),
 ("USDCAD",70,"DXY 71 + Oil Down = Buy","Oil Up + BoC Hawk = Sell","BoC + Oil"),
]
commod=[
 ("GOLD",25,"Fed Cut + Yield Down = Buy","DXY 71 + Hawk = Sell","GPR + Fed"),
 ("SILVER",27,"Fed Cut + Gold = Buy","DXY 71 + Yield = Sell","Gold + Copper"),
 ("OIL",35,"GPR War + OPEC Cut = Buy","DXY 71 + Recession = Sell","OPEC + GPR"),
]
indices=[
 ("US30",30,"Fed Cut + Earnings = Buy","DXY 71 + Hawk = Sell","FOMC + CPI"),
 ("NAS100",28,"Fed Cut + Tech = Buy","DXY 71 + Yield = Sell","Earnings + Yield"),
 ("SPX500",29,"Fed Cut + Strong = Buy","DXY 71 + Hawk = Sell","FOMC + NFP"),
]
crypto=[
 ("BTCUSD",30,"Fed Cut + Risk On = Buy","DXY 71 + Risk Off = Sell","ETF + Fed"),
 ("ETHUSD",29,"Fed Cut + ETF = Buy","DXY 71 + Hawk = Sell","ETF + BTC"),
]
# FULL COT 14 - RESTORED - SHORT LINES
cot=[
 ["DXY","71%","29%","+3% Long","BULL","Fed Hawk"],
 ["EURUSD","29%","71%","+4% Short","BEAR","DXY 71"],
 ["GBPUSD","30%","70%","+2% Short","BEAR","DXY Bull"],
 ["USDJPY","71%","29%","+2% Long","BULL","BoJ Dovish"],
 ["AUDUSD","28%","72%","+3% Short","BEAR","Risk Off"],
 ["USDCHF","71%","29%","+1% Long","BULL","SNB Dovish"],
 ["USDCAD","70%","30%","+2% Long","BULL","Oil Down"],
 ["GOLD","25%","75%","+5% Short","BEAR","DXY + Yield"],
 ["SILVER","27%","73%","+3% Short","BEAR","Gold Down"],
 ["OIL","35%","65%","+2% Short","BEAR","DXY Strong"],
 ["US30","30%","70%","+3% Short","BEAR","DXY Bull"],
 ["NAS100","28%","72%","+4% Short","BEAR","Yield Up"],
 ["SPX500","29%","71%","+3% Short","BEAR","DXY Bull"],
 ["BTCUSD","30%","70%","+2% Short","BEAR","Risk Off"],
]

if st.session_state.page=="home":
    c1,c2=st.columns(2)
    with c1:
        if st.button("FOREX 6", use_container_width=True): st.session_state.page="forex"
        if st.button("COT TABLE", use_container_width=True): st.session_state.page="cot"
        if st.button("GOLD OIL", use_container_width=True): st.session_state.page="gold"
    with c2:
        if st.button("INDICES", use_container_width=True): st.session_state.page="indices"
        if st.button("CRYPTO", use_container_width=True): st.session_state.page="crypto"
        if st.button("FUND + GPR", use_container_width=True): st.session_state.page="fund"
else:
    if st.button("BACK RADAR", use_container_width=True): st.session_state.page="home"
    if st.session_state.page=="forex":
        cols=st.columns(2)
        for i,(p,s,bu,be,ne) in enumerate(forex):
            with cols[i%2]: st.markdown(gauge(p,s,bu,be,ne,170), unsafe_allow_html=True)
    if st.session_state.page=="gold":
        cols=st.columns(2)
        for i,(p,s,bu,be,ne) in enumerate(commod):
            with cols[i%2]: st.markdown(gauge(p,s,bu,be,ne,170), unsafe_allow_html=True)
    if st.session_state.page=="indices":
        cols=st.columns(2)
        for i,(p,s,bu,be,ne) in enumerate(indices):
            with cols[i%2]: st.markdown(gauge(p,s,bu,be,ne,170), unsafe_allow_html=True)
    if st.session_state.page=="crypto":
        cols=st.columns(2)
        for i,(p,s,bu,be,ne) in enumerate(crypto):
            with cols[i%2]: st.markdown(gauge(p,s,bu,be,ne,170), unsafe_allow_html=True)
    if st.session_state.page=="cot":
        st.markdown("### COT - FULL 14 - GREEN BULL RED BEAR")
        html="<table style='width:100%;border-collapse:collapse;font-size:12px'>"
        html+="<tr style='background:#111;color:#888'>"
        html+="<th>Asset</th><th>Long</th><th>Short</th><th>Change</th><th>Bias</th><th>Why</th></tr>"
        for r in cot:
            asset,longv,shortv,change,bias,why=r
            if bias=="BULL":
                bcol="<td style='background:#00ff66;color:black;font-weight:900;padding:6px;border:1px solid #333'>BULL</td>"
                ccol="<td style='color:#00ff66;padding:6px;border:1px solid #333'>"+change+"</td>"
            else:
                bcol="<td style='background:#ff4444;color:white;font-weight:900;padding:6px;border:1px solid #333'>BEAR</td>"
                ccol="<td style='color:#ff4444;padding:6px;border:1px solid #333'>"+change+"</td>"
            html+="<tr><td style='padding:6px;border:1px solid #333'>"+asset+"</td>"
            html+="<td style='padding:6px;border:1px solid #333;color:#00ff66'>"+longv+"</td>"

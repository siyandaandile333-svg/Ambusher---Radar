import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="FX AMBUSHERS", layout="wide")
if "page" not in st.session_state:
    st.session_state.page="home"

DXY=71
TM=datetime.now().strftime("%H:%M SAST")
st.success(f"✅ LIVE v1.3 {TM} | SPECIFIC WHY'S | DXY {DXY} BULL")

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

st.markdown(gauge("DXY AMBUSH",DXY,"Powell Hawk No Cut + CPI 3.2% + Yield 4.2%","Powell Cut + Gold 2600 + Risk On","FOMC Sep 29 + NFP Oct 3",280), unsafe_allow_html=True)

# SUPER SPECIFIC WHY'S - NOT GENERIC
forex=[
 ("EURUSD",29,"ECB Lagarde Hawk + EU CPI 2.4% + Fed Cut","Powell Hawk No Cut + DXY 71 + US10Y 4.2%","ECB Oct5 + US CPI Oct4"),
 ("GBPUSD",30,"BoE Bailey Hawk + UK CPI 3.8% + Fed Cut","Fed Hawk + DXY 71 + Risk Off + Yield Up","BoE Oct5 + FOMC Sep29"),
 ("USDJPY",71,"DXY 71 + BoJ Ueda Dovish + US-JP Yield Gap","BoJ Hawk Rate Hike + Fed Cut + Risk Off","BoJ Rate Oct4 + FOMC"),
 ("AUDUSD",28,"RBA Bullock Hawk + Gold 2600 + China Stimulus","DXY 71 + Risk Off + China Weak + Iron Down","RBA + China PMI + Gold"),
 ("USDCHF",71,"DXY 71 + SNB Jordan Dovish + Safe Haven Off","SNB Hawk + Fed Cut + Gold Up + Risk Off","SNB + Gold + Fed"),
 ("USDCAD",70,"DXY 71 + Oil WTI 70 Down + BoC Dovish","Oil 85 Up + BoC Macklem Hawk + Risk On","BoC + Oil OPEC + NFP"),
]
commod=[
 ("GOLD",25,"Fed Cut 25bps + Yield 4.2 Down + GPR War","DXY 71 + Powell Hawk + US10Y Up + Risk On","GPR Israel + FOMC + CPI"),
 ("SILVER",27,"Gold 2600 Up + Fed Cut + Industrial Demand","DXY 71 + Yield Up + Gold Sell + Risk Off","Gold + Copper + Fed"),
 ("OIL",35,"GPR Iran Tanker + OPEC Cut 1M + War Risk","DXY 71 + US Recession + Demand Down + Stock Up","OPEC Meeting + GPR + EIA"),
]
indices=[
 ("US30",30,"Fed Cut + Dow Earnings Beat + CPI 3.2 Down","DXY 71 + Powell Hawk No Cut + Yield 4.2 Up","FOMC Sep29 + CPI Oct4 + NFP"),
 ("NAS100",28,"Fed Cut + Tech AAPL NVDA Beat + Yield Down","DXY 71 + US10Y 4.2 Up + Fed Hawk + CPI Up","Earnings + Yield + FOMC"),
 ("SPX500",29,"Fed Cut + SPX Earnings Up + Risk On + CPI Down","DXY 71 + Hawk + Yield Up + Recession Fear","FOMC + NFP Oct3 + CPI"),
]
crypto=[
 ("BTCUSD",30,"Fed Cut + ETF Inflow 500M + Risk On","DXY 71 + Risk Off + SEC FUD + Yield Up","ETF + FOMC + NFP"),
 ("ETHUSD",29,"Fed Cut + ETH ETF Inflow + BTC Up","DXY 71 + Hawk + BTC Sell + Risk Off","ETF + BTC + Fed"),
]
cot=[
 ["DXY","71%","29%","+3% Long","BULL","Powell Hawk No Cut"],
 ["EURUSD","29%","71%","+4% Short","BEAR","DXY 71 + Fed Hawk"],
 ["GBPUSD","30%","70%","+2% Short","BEAR","DXY Bull 71"],
 ["USDJPY","71%","29%","+2% Long","BULL","BoJ Ueda Dovish"],
 ["AUDUSD","28%","72%","+3% Short","BEAR","Risk Off + DXY"],
 ["USDCHF","71%","29%","+1% Long","BULL","SNB Dovish"],
 ["USDCAD","70%","30%","+2% Long","BULL","Oil Down WTI 70"],
 ["GOLD","25%","75%","+5% Short","BEAR","DXY 71 + Yield 4.2"],
 ["SILVER","27%","73%","+3% Short","BEAR","Gold Down"],
 ["OIL","35%","65%","+2% Short","BEAR","DXY Strong"],
 ["US30","30%","70%","+3% Short","BEAR","Fed Hawk No Cut"],
 ["NAS100","28%","72%","+4% Short","BEAR","Yield 4.2 Up"],
 ["SPX500","29%","71%","+3% Short","BEAR","DXY 71 Bull"],
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
        st.markdown("### COT - FULL 14")
        html="<table style='width:100%;border-collapse:collapse;font-size:12px'>"
        html+="<tr style='background:#111;color:#888'><th>Asset</th><th>Long</th><th>Short</th><th>Bias</th><th>Why</th></tr>"
        for r in cot:
            a,lo,sh,ch,bi,wh=r
            if bi=="BULL":
                bc="<td style='background:#00ff66;color:black;font-weight:900;padding:6px;border:1px solid #333'>BULL</td>"
            else:
                bc="<td style='background:#ff4444;color:white;font-weight:900;padding:6px;border:1px solid #333'>BEAR</td>"
            html+="<tr><td style='padding:6px;border:1px solid #333'>"+a+"</td>"
            html+="<td style='padding:6px;border:1px solid #333;color:#00ff66'>"+lo+"</td>"
            html+="<td style='padding:6px;border:1px solid #333;color:#ff6666'>"+sh+"</td>"+bc
            html+="<td style='padding:6px;border:1px solid #333;color:#aaa'>"+wh+"</td></tr>"
        html+="</table>"
        st.markdown(html, unsafe_allow_html=True)
    if st.session_state.page=="fund":
        st.markdown("### FUND DATES + GPR")
        st.write("FOMC Sep29 HIGH - Powell Hawk No Cut = DXY Buy")
        st.write("NFP Oct3 HIGH - Exp 180K - Biggest USD mover")
        st.write("CPI Oct4 HIGH - Exp 3.2% - If high = DXY UP")
        st.write("BoJ Oct4 HIGH - Ueda Hawk? = JPY Up")
        st.write("GPR: Israel-Gaza Talks = Gold SELL")
        st.write("GPR: Russia-Ukraine Attacks = Gold BUY Oil BUY")

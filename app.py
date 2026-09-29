import streamlit as st
import pandas as pd
import os, glob

st.set_page_config(page_title="FX AMBUSHERS", layout="wide")
st.markdown('<style>.stApp{background:#080a0a}</style>', unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page="home"

DXY=71

def gauge_card(title, score, bull, bear, neu, size=260):
    angle = -90 + (score*1.8)
    if score>=60:
        col="#00ff66"; bcol="#00ff66"; bias="BULL"
    elif score<=40:
        col="#ff4444"; bcol="#ff4444"; bias="BEAR"
    else:
        col="#ffcc00"; bcol="#ffcc00"; bias="NEU"
    h = size//2
    html = '<div style="border:1px solid #222;border-radius:18px;padding:12px;background:#0f1414;border-left:4px solid '+bcol+';margin-bottom:12px">'
    html += '<div style="text-align:center;color:#888;font-size:11px">'+title+'</div>'
    html += '<div style="text-align:center;color:'+col+';font-weight:900;font-size:20px">'+bias+' '+str(score)+'</div>'
    html += '<div style="width:'+str(size)+'px;height:'+str(h)+'px;margin:8px auto;position:relative;background:conic-gradient(from 270deg at 50% 100%, #ff2b2b 0deg 60deg, #ffcc00 60deg 120deg, #00cc66 120deg 180deg);border-radius:'+str(size)+'px '+str(size)+'px 0 0">'
    html += '<div style="width:3px;height:'+str(h-10)+'px;background:white;position:absolute;bottom:0;left:50%;transform-origin:bottom;transform:rotate('+str(angle)+'deg)"></div>'
    html += '<div style="width:12px;height:12px;background:white;border-radius:50%;position:absolute;bottom:-6px;left:calc(50% - 6px)"></div></div>'
    html += '<div style="font-size:11px;color:#00ff66">Bull: '+bull+'</div>'
    html += '<div style="font-size:11px;color:#ff6666">Bear: '+bear+'</div>'
    html += '<div style="font-size:11px;color:#888">Neu: '+neu+'</div></div>'
    return html

def show_logo():
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

show_logo()
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
    ("BTCUSD",30,"Fed Cut + Risk On = Buy","DXY 71 + Risk Off = Sell","ETF + Fed"),
    ("ETHUSD",29,"Fed Cut + ETF = Buy","DXY 71 + Hawk = Sell","ETF + BTC"),
]
cot_data=[
    ["DXY","LONG 71%","SHORT 29%","+3% Long","BULL","Fed Hawk"],
    ["EURUSD","LONG 29%","SHORT 71%","+4% Short","BEAR","DXY Bull 71"],
    ["GBPUSD","LONG 30%","SHORT 70%","+2% Short","BEAR","DXY Bull"],
    ["USDJPY","LONG 71%","SHORT 29%","+2% Long","BULL","BoJ Dovish"],
    ["AUDUSD","LONG 28%","SHORT 72%","+3% Short","BEAR","Risk Off"],
    ["USDCHF","LONG 71%","SHORT 29%","+1% Long","BULL","SNB Dovish"],
    ["USDCAD","LONG 70%","SHORT 30%","+2% Long","BULL","Oil Down"],
    ["GOLD","LONG 25%","SHORT 75%","+5% Short","BEAR","DXY 71 + Yield"],
    ["SILVER","LONG 27%","SHORT 73%","+3% Short","BEAR","Gold Down"],
    ["OIL","LONG 35%","SHORT 65%","+2% Short","BEAR","DXY Strong"],
    ["US30","LONG 30%","SHORT 70%","+3% Short","BEAR","DXY Bull"],
    ["NAS100","LONG 28%","SHORT 72%","+4% Short","BEAR","Yield Up"],
    ["SPX500","LONG 29%","SHORT 71%","+3% Short","BEAR","DXY Bull"],
    ["BTCUSD","LONG 30%","SHORT 70%","+2% Short","BEAR","Risk Off"],
]

if st.session_state.page=="home":
    c1,c2=st.columns(2)
    with c1:
        if st.button("FOREX 6", use_container_width=True): st.session_state.page="forex"
        if st.button("GOLD OIL", use_container_width=True): st.session_state.page="gold"
        if st.button("INDICES", use_container_width=True): st.session_state.page="indices"
        if st.button("CRYPTO", use_container_width=True): st.session_state.page="crypto"
    with c2:
        if st.button("COT TABLE", use_container_width=True): st.session_state.page="cot"
        if st.button("INTEL NEWS", use_container_width=True): st.session_state.page="news"
        if st.button("FUND DATES", use_container_width=True): st.session_state.page="fund"
        if st.button("LEARN WORDS", use_container_width=True): st.session_state.page="words"
else:
    if st.button("BACK RADAR", use_container_width=True): st.session_state.page="home"
    if st.session_state.page=="forex":
        cols=st.columns(2)
        for i,(p,s,bu,be,ne) in enumerate(forex):
            with cols[i%2]:
                st.markdown(gauge_card(p,s,bu,be,ne,170), unsafe_allow_html=True)
    if st.session_state.page=="gold":
        cols=st.columns(2)
        for i,(p,s,bu,be,ne) in enumerate(commod):
            with cols[i%2]:
                st.markdown(gauge_card(p,s,bu,be,ne,170), unsafe_allow_html=True)
    if st.session_state.page=="indices":
        cols=st.columns(2)
        for i,(p,s,bu,be,ne) in enumerate(indices):
            with cols[i%2]:
                st.markdown(gauge_card(p,s,bu,be,ne,170), unsafe_allow_html=True)
    if st.session_state.page=="crypto":
        cols=st.columns(2)
        for i,(p,s,bu,be,ne) in enumerate(crypto):
            with cols[i%2]:
                st.markdown(gauge_card(p,s,bu,be,ne,170), unsafe_allow_html=True)
    if st.session_state.page=="cot":
        st.markdown("### COT - LONG / SHORT / CHANGE")
        st.table(pd.DataFrame(cot_data, columns=["Asset","Long","Short","Change","Bias","Why"]))
    if st.session_state.page=="news":
        st.write("RATE High = DXY UP. CPI High = DXY UP. FOMC Hawk = USD Buy")
    if st.session_state.page=="fund":
        st.table(pd.DataFrame([["2026-09-29","FOMC","HIGH"]], columns=["Date","News","Impact"]))
    if st.session_state.page=="words":
        st.write("BOS=Break, CHoCH=Change, OB=Order Block")

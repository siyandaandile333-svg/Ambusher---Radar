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
    part1 = "<div style='border:1px solid #222;border-radius:18px;padding:12px;background:#0f1414;"
    part1 += "border-left:4px solid " + bcol + ";margin-bottom:12px'>"
    part2 = "<div style='text-align:center;color:#888;font-size:11px'>" + title + "</div>"
    part3 = "<div style='text-align:center;color:" + col + ";font-weight:900;font-size:20px'>"
    part3 += bias + " " + str(score) + "</div>"
    part4 = "<div style='width:" + str(size) + "px;height:" + str(h) + "px;margin:8px auto;position:relative;"
    part4 += "background:conic-gradient(from 270deg at 50% 100%, #ff2b2b 0deg 60deg, #ffcc00 60deg 120deg, #00cc66 120deg 180deg);"
    part4 += "border-radius:" + str(size) + "px " + str(size) + "px 0 0'>"
    part5 = "<div style='width:3px;height:" + str(h-10) + "px;background:white;position:absolute;bottom:0;left:50%;"
    part5 += "transform-origin:bottom;transform:rotate(" + str(angle) + "deg)'></div>"
    part5 += "<div style='width:12px;height:12px;background:white;border-radius:50%;position:absolute;bottom:-6px;left:calc(50% - 6px)'></div></div>"
    part6 = "<div style='font-size:11px;color:#00ff66'>Bull: " + bull + "</div>"
    part6 += "<div style='font-size:11px;color:#ff6666'>Bear: " + bear + "</div>"
    part6 += "<div style='font-size:11px;color:#888'>Neu: " + neu + "</div></div>"
    return part1 + part2 + part3 + part4 + part5 + part6

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
fund_full=[
    ["2026-09-29","FOMC","HIGH","Fed Hawk No Cut = DXY Buy"],
    ["2026-09-30","CB Confidence","MEDIUM","USD sentiment"],
    ["2026-10-01","ISM Manufacturing","HIGH","USD up if high"],
    ["2026-10-02","ADP + Jobless","HIGH","NFP preview"],
    ["2026-10-03","NFP + Unemployment","HIGH","Biggest USD mover"],
    ["2026-10-03","ISM Services","HIGH","USD + Stocks"],
    ["2026-10-04","CPI Inflation","HIGH","If high = DXY UP"],
    ["2026-10-04","BoJ Rate","HIGH","JPY mover"],
    ["2026-10-05","ECB Rate","HIGH","EUR mover"],
    ["2026-10-05","BoE Rate","HIGH","GBP mover"],
]
gpr_news=[
    ["Israel-Gaza Talks","MEDIUM","Gold SELL + Oil SELL if peace"],
    ["Russia-Ukraine Attacks","HIGH","Gold BUY + Oil BUY"],
    ["US-China Taiwan","HIGH","USD BUY + Gold BUY"],
    ["Iran Oil Tanker","HIGH","Oil BUY + Gold BUY"],
    ["OPEC+ Meeting","HIGH","Oil BUY if cut"],
    ["North Korea Missile","MEDIUM","Gold BUY + JPY BUY"],
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
        # Build colored HTML table - GREEN BULL, RED BEAR
        html_cot = "<table style='width:100%;border-collapse:collapse;font-size:13px'>"
        html_cot += "<tr style='background:#111;color:#888'><th>Asset</th><th>Long</th><th>Short</th><th>Change</th><th>Bias</th><th>Why</th></tr>"
        for row in cot_data:
            asset, longv, shortv, change, bias, why = row
            if bias=="BULL":
                bias_col = "<td style='background:#00ff66;color:black;font-weight:900;padding:6px;border:1px solid #333'>BULL</td>"
                change_col = "<td style='color:#00ff66;padding:6px;border:1px solid #333'>" + change + "</td>"
            else:
                bias_col = "<td style='background:#ff4444;color:white;font-weight:900;padding:6px;border:1px solid #333'>BEAR</td>"
                change_col = "<td style='color:#ff4444;padding:6px;border:1px solid #333'>" + change + "</td>"
            html_cot += "<tr style='border:1px solid #333'>"
            html_cot += "<td style='padding:6px;border:1px solid #333;font-weight:bold'>" + asset + "</td>"
            html_cot += "<td style='padding:6px;border:1px solid #333;color:#00ff66'>" + longv + "</td>"
            html_cot += "<td style='padding:6px;border:1px solid #333;color:#ff6666'>" + shortv + "</td>"
            html_cot += change_col
            html_cot += bias_col
            html_cot += "<td style='padding:6px;border:1px solid #333;color:#aaa'>" + why + "</td>"
            html_cot += "</tr>"
        html_cot += "</table>"
        st.markdown(html_cot, unsafe_allow_html=True)
    if st.session_state.page=="news":
        st.markdown("### INTEL NEWS + GEOPOLITICAL")
        st.table(pd.DataFrame(gpr_news, columns=["Event","Impact","What Happens"]))
    if st.session_state.page=="fund":
        st.markdown("### FUND DATES - FULL CALENDAR")
        st.table(pd.DataFrame(fund_full, columns=["Date","News","Impact","Why"]))
    if st.session_state.page=="words":
        st.write("BOS=Break, CHoCH=Change, OB=Order Block")

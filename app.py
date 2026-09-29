import streamlit as st
from datetime import datetime
import os

st.set_page_config(page_title="FX AMBUSHERS", layout="wide")
if "page" not in st.session_state:
    st.session_state.page="home"

DXY=71
TM=datetime.now().strftime("%H:%M SAST")
st.success(f"✅ LIVE v1.4 DETAILED WHY'S | {TM} | DXY {DXY}")

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
    f="<div style='font-size:11px;color:#00ff66;line-height:1.3'>Bull: "+bu+"</div>"
    f+="<div style='font-size:11px;color:#ff6666;line-height:1.3'>Bear: "+be+"</div>"
    f+="<div style='font-size:11px;color:#888;line-height:1.3'>Neu: "+ne+"</div></div>"
    return a+b+c+d+e+f

# DETAILED WHY - split in 2 lines so phone safe but shows LONG
st.markdown(gauge("DXY AMBUSH",DXY,
 "Powell Hawk No Cut Sep29 + US CPI 3.2% Hot + "
 "US10Y 4.2% Up + BoJ Ueda Dovish = USD Buy",
 "Powell Dovish Cut 25bps + Gold 2600 Risk On + "
 "BoJ Hawk Hike + Yield Down = USD Sell",
 "FOMC Sep29 HIGH + NFP Oct3 180K + CPI Oct4",
 280), unsafe_allow_html=True)

forex=[
 ("EURUSD",29,
  "ECB Lagarde Hawk + EU CPI 2.4% Hot + "
  "EU GDP Strong + Fed Dovish Cut = EUR Buy",
  "Fed Powell Hawk No Cut + DXY 71 Bull + "
  "US10Y 4.2% Up + US CPI 3.2% = EUR Sell",
  "ECB Oct5 Rate + US CPI Oct4 + GPR + Fed"),
 ("GBPUSD",30,
  "BoE Bailey Hawk + UK CPI 3.8% Hot + "
  "UK Wage Up + Fed Cut = GBP Buy",
  "Fed Hawk No Cut + DXY 71 + US Yield Up + "
  "UK Recession Fear + Risk Off = GBP Sell",
  "BoE Oct5 + FOMC Sep29 + UK CPI"),
 ("USDJPY",71,
  "DXY 71 Bull + BoJ Ueda Dovish No Hike + "
  "US-JP Yield Gap 4.2% vs 0.5% = USDJPY Buy",
  "BoJ Hawk Rate Hike + Ueda Hawk + "
  "Fed Dovish Cut + Risk Off Yen Safe = Sell",
  "BoJ Rate Oct4 HIGH + FOMC Sep29 + GPR"),
 ("AUDUSD",28,
  "RBA Bullock Hawk + Gold 2600 Up + "
  "China Stimulus + Iron Ore Up = AUD Buy",
  "DXY 71 Bull + Risk Off + China PMI Weak + "
  "Iron Ore Down + RBA Dovish = AUD Sell",
  "RBA Meeting + China PMI + Gold + DXY"),
 ("USDCHF",71,
  "DXY 71 Bull + SNB Jordan Dovish + "
  "Safe Haven Off + Gold Down = USDCHF Buy",
  "SNB Hawk + Jordan Hawk + Fed Cut + "
  "Gold 2600 Up + Risk Off CHF Safe = Sell",
  "SNB Rate + Gold 2600 + Fed + Risk"),
 ("USDCAD",70,
  "DXY 71 Bull + Oil WTI 70 Down + "
  "BoC Macklem Dovish + US Strong = Buy",
  "Oil WTI 85 Up + OPEC Cut + BoC Hawk + "
  "Canada CPI Up + Risk On CAD = Sell",
  "BoC Rate + Oil EIA + OPEC + NFP"),
]
commod=[
 ("GOLD",25,
  "Fed Dovish Cut 25bps + US10Y 4.2 Down + "
  "USD Weak + GPR War Risk = Gold Buy",
  "DXY 71 Bull + Powell Hawk No Cut + "
  "US10Y 4.2 Up + Risk On Stocks Up = Sell",
  "GPR Israel-Gaza + FOMC Sep29 + US CPI"),
 ("SILVER",27,
  "Gold 2600 Up + Fed Cut + Industrial + "
  "Solar Demand + Copper Up = Silver Buy",
  "DXY 71 + US Yield Up + Gold Sell + "
  "Industrial Weak + Risk Off = Sell",
  "Gold + Copper + Fed + Industrial"),
 ("OIL",35,
  "GPR Iran-Israel Tanker War + OPEC Cut 1M + "
  "Supply Tight + War Risk = Oil Buy",
  "DXY 71 Strong + US Recession + Demand Down + "
  "US Stock Up + OPEC No Cut = Oil Sell",
  "OPEC Meeting + GPR + EIA Stock + DXY"),
]
indices=[
 ("US30",30,
  "Fed Dovish Cut + Dow Earnings Beat + "
  "US CPI 3.2 Down + Risk On = US30 Buy",
  "DXY 71 + Powell Hawk No Cut + "
  "US10Y 4.2 Up + Earnings Miss = US30 Sell",
  "FOMC Sep29 HIGH + CPI Oct4 + NFP Oct3"),
 ("NAS100",28,
  "Fed Cut + Tech AAPL NVDA MSFT Beat + "
  "Yield Down + AI Demand = NAS100 Buy",
  "DXY 71 + US10Y 4.2 Up + Fed Hawk + "
  "US CPI 3.2 Hot + Tech Sell = Sell",
  "Earnings Week + US10Y Yield + FOMC"),
 ("SPX500",29,
  "Fed Dovish Cut + SPX Earnings Strong + "
  "Risk On + US CPI Down + GDP Up = Buy",
  "DXY 71 Bull + Powell Hawk + US10Y Up + "
  "Recession Fear + CPI Hot = SPX Sell",
  "FOMC Sep29 + NFP Oct3 HIGH + CPI"),
]
crypto=[
 ("BTCUSD",30,
  "Fed Cut + ETF Inflow 500M + "
  "Risk On + Halving + BTC Dominance = Buy",
  "DXY 71 Bull + Risk Off + SEC FUD + "
  "ETF Outflow + Yield Up = BTC Sell",
  "ETF Flow + FOMC Sep29 + NFP + Risk"),
 ("ETHUSD",29,
  "Fed Cut + ETH ETF Inflow + "
  "BTC Up + ETH Burn + Staking Up = Buy",
  "DXY 71 + Powell Hawk + BTC Sell + "
  "ETH ETF Outflow + Risk Off = Sell",
  "ETF + BTC + FOMC + Staking"),
]
cot=[
 ["DXY","71%","29%","+3% Long","BULL","Powell Hawk"],
 ["EURUSD","29%","71%","+4% Short","BEAR","DXY 71"],
 ["GBPUSD","30%","70%","+2% Short","BEAR","DXY Bull"],
 ["USDJPY","71%","29%","+2% Long","BULL","BoJ Dovish"],
 ["AUDUSD","28%","72%","+3% Short","BEAR","Risk Off"],
 ["USDCHF","71%","29%","+1% Long","BULL","SNB Dovish"],
 ["USDCAD","70%","30%","+2% Long","BULL","Oil Down"],
 ["GOLD","25%","75%","+5% Short","BEAR","DXY + Yield"],
 ["SILVER","27%","73%","+3% Short","BEAR","Gold Down"],
 ["OIL","35%","65%","+2% Short","BEAR","DXY Strong"],
 ["US30","30%","70%","+3% Short","BEAR","Hawk No Cut"],
 ["NAS100","28%","72%","+4% Short","BEAR","Yield 4.2"],
 ["SPX500","29%","71%","+3% Short","BEAR","DXY 71"],
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
        st.write("GPR: Israel-Gaza Talks = Gold SELL Oil SELL")
        st.write("GPR: Russia-Ukraine Attacks = Gold BUY Oil BUY")

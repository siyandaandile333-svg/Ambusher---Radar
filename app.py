import streamlit as st
from datetime import datetime
import os

st.set_page_config(page_title="FX AMBUSHERS", layout="wide")
if "page" not in st.session_state:
    st.session_state.page="home"

DXY=7
TM=datetime.now().strftime("%H:%M SAST")
st.success(f"LIVE v1.9 SCORE -10 to +10 | {TM}")

for f in ["logo.png","logo.jpg","IMG-20260929-WA1810.jpg"]:
    if os.path.exists(f):
        st.image(f, use_container_width=True)
        break

def j(parts, end):
    return " + ".join(parts) + " = " + end

def gauge(t,s,bu,be,ne,sz=260):
    # s is -10 to +10
    ang=s*9
    if s>=1:
        col="#00ff66"; bcol="#00ff66"; bias="BULL"
    elif s<=-1:
        col="#ff4444"; bcol="#ff4444"; bias="BEAR"
    else:
        col="#ffcc00"; bcol="#ffcc00"; bias="NEU"
    h=sz//2
    a="<div style='border:1px solid #222;"
    a+="border-radius:18px;padding:12px;"
    a+="background:#0f1414;border-left:4px solid "
    a+=bcol+";margin-bottom:12px'>"
    b="<div style='text-align:center;"
    b+="color:#888;font-size:11px'>"+t+"</div>"
    c="<div style='text-align:center;color:"
    c+=col+";font-weight:900;font-size:20px'>"
    if s>0: c+=bias+" +"+str(s)
    else: c+=bias+" "+str(s)
    c+="</div>"
    d="<div style='width:"+str(sz)+"px;height:"
    d+=str(sz//2)+"px;margin:8px auto;"
    d+="position:relative;background:conic-gradient"
    d+="(from 270deg at 50% 100%,#ff2b2b 0 60deg,"
    d+="#ffcc00 60deg 120deg,#00cc66 120deg 180deg);"
    d+="border-radius:"+str(sz)+"px "+str(sz)+"px 0 0'>"
    e="<div style='width:3px;height:"
    e+=str(h-10)+"px;background:white;"
    e+="position:absolute;bottom:0;left:50%;"
    e+="transform-origin:bottom;transform:rotate("
    e+=str(ang)+"deg)'></div></div>"
    f="<div style='font-size:11px;color:#00ff66'>"
    f+="Bull: "+bu+"</div>"
    f+="<div style='font-size:11px;color:#ff6666'>"
    f+="Bear: "+be+"</div>"
    f+="<div style='font-size:11px;color:#888'>"
    f+="Neu: "+ne+"</div></div>"
    return a+b+c+d+e+f

dxy_bu=j(["Powell Hawk No Cut","US CPI 3.2% Hot","US10Y 4.2% Up","BoJ Dovish"],"USD Buy")
dxy_be=j(["Powell Cut 25bps","Gold 2600 Risk On","BoJ Hawk Hike","Yield Down"],"USD Sell")
dxy_ne="FOMC Sep29 HIGH + NFP Oct3 + CPI Oct4"
st.markdown(gauge("DXY AMBUSH",DXY,dxy_bu,dxy_be,dxy_ne,280), unsafe_allow_html=True)

forex=[
 ("EURUSD",-7,j(["ECB Lagarde Hawk","EU CPI 2.4% Hot","EU GDP Strong","Fed Cut"],"EUR Buy"),j(["Powell Hawk No Cut","DXY +7 Bull","US10Y 4.2% Up","CPI 3.2%"],"EUR Sell"),"ECB Oct5 + US CPI Oct4 + GPR"),
 ("GBPUSD",-7,j(["BoE Bailey Hawk","UK CPI 3.8% Hot","UK Wage Up","Fed Cut"],"GBP Buy"),j(["Fed Hawk No Cut","DXY +7","Yield Up","UK Recession"],"GBP Sell"),"BoE Oct5 + FOMC Sep29"),
 ("USDJPY",7,j(["DXY +7 Bull","BoJ Ueda Dovish","US-JP Gap 4.2%"],"USDJPY Buy"),j(["BoJ Hawk Hike","Ueda Hawk","Fed Cut","Risk Off"],"Sell"),"BoJ Oct4 HIGH + FOMC"),
 ("AUDUSD",-7,j(["RBA Hawk","Gold 2600 Up","China Stimulus","Iron Up"],"AUD Buy"),j(["DXY +7","Risk Off","China PMI Weak","Iron Down"],"AUD Sell"),"RBA + China PMI + Gold"),
 ("USDCHF",7,j(["DXY +7 Bull","SNB Dovish","Safe Off","Gold Down"],"Buy"),j(["SNB Hawk","Fed Cut","Gold 2600 Up","Risk Off"],"Sell"),"SNB + Gold + Fed"),
 ("USDCAD",6,j(["DXY +7 Bull","Oil WTI 70 Down","BoC Dovish"],"Buy"),j(["Oil 85 Up","OPEC Cut","BoC Hawk","CPI Up"],"Sell"),"BoC + Oil + OPEC"),
]
commod=[
 ("GOLD",-8,j(["Fed Cut 25bps","US10Y Down","USD Weak","GPR War"],"Gold Buy"),j(["DXY +7 Bull","Powell Hawk","US10Y Up","Risk On"],"Sell"),"GPR Israel + FOMC + CPI"),
 ("SILVER",-7,j(["Gold 2600 Up","Fed Cut","Solar Demand","Copper Up"],"Buy"),j(["DXY +7","Yield Up","Gold Sell","Risk Off"],"Sell"),"Gold + Copper + Fed"),
 ("OIL",-3,j(["GPR Iran War","OPEC Cut 1M","Supply Tight"],"Oil Buy"),j(["DXY Strong","Recession","Demand Down","Stock Up"],"Sell"),"OPEC + GPR + EIA"),
]
indices=[
 ("US30",-7,j(["Fed Cut","Dow Earnings Beat","CPI 3.2 Down","Risk On"],"Buy"),j(["DXY +7","Powell Hawk","Yield 4.2 Up","Miss"],"Sell"),"FOMC Sep29 + CPI Oct4"),
 ("NAS100",-7,j(["Fed Cut","AAPL NVDA Beat","Yield Down","AI Demand"],"Buy"),j(["DXY +7","US10Y Up","Hawk","CPI Hot"],"Sell"),"Earnings + Yield + FOMC"),
 ("SPX500",-7,j(["Fed Cut","SPX Earnings Up","CPI Down","GDP Up"],"Buy"),j(["DXY +7","Hawk","Yield Up","Recession"],"Sell"),"FOMC + NFP Oct3 + CPI"),
]
crypto=[
 ("BTCUSD",-7,j(["Fed Cut","ETF Inflow 500M","Risk On","Halving"],"BTC Buy"),j(["DXY +7","Risk Off","SEC FUD","Outflow"],"BTC Sell"),"ETF + FOMC + NFP"),
 ("ETHUSD",-7,j(["Fed Cut","ETH ETF In","BTC Up","Burn Up"],"ETH Buy"),j(["DXY +7","Hawk","BTC Sell","Outflow"],"ETH Sell"),"ETF + BTC + FOMC"),
]
cot=[
 ["DXY","71%","29%","+3% Long","BULL","Powell Hawk"],
 ["EURUSD","29%","71%","+4% Short","BEAR","DXY +7"],
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
 ["SPX500","29%","71%","+3% Short","BEAR","DXY +7"],
 ["BTCUSD","30%","70%","+2% Short","BEAR","Risk Off"],
]
retail=[
 ["EURUSD","70%","30%","72% Long Retail","CONTRARIAN SELL","Retail Long Crowded"],
 ["GBPUSD","68%","32%","70% Long Retail","CONTRARIAN SELL","Retail Long"],
 ["USDJPY","35%","65%","66% Short Retail","CONTRARIAN BUY","Retail Short Crowded"],
 ["AUDUSD","65%","35%","68% Long Retail","CONTRARIAN SELL","Retail Wrong"],
 ["USDCHF","38%","62%","64% Short Retail","CONTRARIAN BUY","Retail Short"],
 ["USDCAD","40%","60%","62% Short Retail","CONTRARIAN BUY","Retail Short"],
 ["GOLD","75%","25%","80% Long Retail","CONTRARIAN SELL","Top Signal"],
 ["SILVER","72%","28%","75% Long Retail","CONTRARIAN SELL","Retail Long"],
 ["OIL","60%","40%","65% Long Retail","CONTRARIAN SELL","Retail Long Oil"],
 ["US30","68%","32%","70% Long Retail","CONTRARIAN SELL","Retail Bull Trap"],
 ["NAS100","70%","30%","73% Long Retail","CONTRARIAN SELL","Retail Bull"],
 ["SPX500","69%","31%","71% Long Retail","CONTRARIAN SELL","Retail Bull"],
 ["BTCUSD","78%","22%","85% Long Retail","CONTRARIAN SELL","Retail FOMO"],
 ["DXY","30%","70%","68% Short Retail","CONTRARIAN BUY","Retail Short USD"],
]

all_assets={}
for p,s,bu,be,ne in forex: all_assets[p]=(s,bu,be,ne,"FOREX")
for p,s,bu,be,ne in commod: all_assets[p]=(s,bu,be,ne,"METAL")
for p,s,bu,be,ne in indices: all_assets[p]=(s,bu,be,ne,"INDICES")
for p,s,bu,be,ne in crypto: all_assets[p]=(s,bu,be,ne,"CRYPTO")
all_assets["DXY"]=(DXY,dxy_bu,dxy_be,dxy_ne,"DXY")

if st.session_state.page=="home":
    c1,c2=st.columns(2)
    with c1:
        if st.button("FOREX 6", use_container_width=True): st.session_state.page="forex"
        if st.button("GOLD OIL", use_container_width=True): st.session_state.page="gold"
        if st.button("COT TABLE", use_container_width=True): st.session_state.page="cot"
        if st.button("RETAIL SENTIMENT", use_container_width=True): st.session_state.page="retail"
    with c2:
        if st.button("INDICES", use_container_width=True): st.session_state.page="indices"
        if st.button("CRYPTO", use_container_width=True): st.session_state.page="crypto"
        if st.button("SCORE FINDER", use_container_width=True): st.session_state.page="finder"
        if st.button("FUND + GPR", use_container_width=True): st.session_state.page="fund"
else:
    if st.button("BACK RADAR", use_container_width=True): st.session_state.page="home"
    if st.session_state.page=="finder":
        st.markdown("### SCORE FINDER -10 to +10")
        ch=st.selectbox("Choose Asset", list(all_assets.keys()))
        s,bu,be,ne,typ=all_assets[ch]
        st.write(f"Type: {typ}")
        st.markdown(gauge(ch,s,bu,be,ne,280), unsafe_allow_html=True)
        if s>=1: st.success(f"Score +{s} = BULL")
        elif s<=-1: st.error(f"Score {s} = BEAR")
        else: st.warning(f"Score 0 = WAIT NEUTRAL")
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
        st.markdown("### COT - WITH CHANGE")
        html="<table style='width:100%;border-collapse:collapse;font-size:11px'>"
        html+="<tr style='background:#111;color:#888'>"
        html+="<th>Asset</th><th>Long</th><th>Short</th><th>Change</th><th>Bias</th><th>Why</th></tr>"
        for r in cot:
            a,lo,sh,ch,bi,wh=r
            if bi=="BULL":
                bc="<td style='background:#00ff66;color:black;font-weight:900;padding:5px;border:1px solid #333'>BULL</td>"
                cc="<td style='color:#00ff66;padding:5px;border:1px solid #333'>"+ch+"</td>"
            else:
                bc="<td style='background:#ff4444;color:white;font-weight:900;padding:5px;border:1px solid #333'>BEAR</td>"
                cc="<td style='color:#ff6666;padding:5px;border:1px solid #333'>"+ch+"</td>"
            html+="<tr><td style='padding:5px;border:1px solid #333'>"+a+"</td>"
            html+="<td style='padding:5px;border:1px solid #333;color:#00ff66'>"+lo+"</td>"
            html+="<td style='padding:5px;border:1px solid #333;color:#ff6666'>"+sh+"</td>"
            html+=cc+bc
            html+="<td style='padding:5px;border:1px solid #333;color:#aaa'>"+wh+"</td></tr>"
        html+="</table>"
        st.markdown(html, unsafe_allow_html=True)
    if st.session_state.page=="retail":
        st.markdown("### RETAIL SENTIMENT - CONTRARIAN")
        st.write("Retail = Crowd | We fade them")
        html="<table style='width:100%;border-collapse:collapse;font-size:11px'>"
        html+="<tr style='background:#111;color:#888'>"
        html+="<th>Asset</th><th>RLong</th><th>RShort</th><th>Crowd</th><th>Signal</th><th>Why</th></tr>"
        for r in retail:
            a,lo,sh,cr,sg,wh=r
            if "SELL" in sg:
                bc="<td style='background:#ff4444;color:white;font-weight:900;padding:5px;border:1px solid #333'>SELL</td>"
            else:
                bc="<td style='background:#00ff66;color:black;font-weight:900;padding:5px;border:1px solid #333'>BUY</td>"
            html+="<tr><td style='padding:5px;border:1px solid #333'>"+a+"</td>"
            html+="<td style='padding:5px;border:1px solid #333;color:#00ff66'>"+lo+"</td>"
            html+="<td style='padding:5px;border:1px solid #333;color:#ff6666'>"+sh+"</td>"
            html+="<td style='padding:5px;border:1px solid #333;color:#ffcc00'>"+cr+"</td>"
            html+=bc
            html+="<td style='padding:5px;border:1px solid #333;color:#aaa'>"+wh+"</td></tr>"
        html+="</table>"
        st.markdown(html, unsafe_allow_html=True)
    if st.session_state.page=="fund":
        st.markdown("### FUND DATES + GPR")
        st.write("FOMC Sep29 HIGH - Powell Hawk = DXY Buy")
        st.write("NFP Oct3 HIGH - Exp 180K")
        st.write("CPI Oct4 HIGH - Exp 3.2%")
        st.write("GPR: Israel-Gaza = Gold SELL")
        st.write("GPR: Russia-Ukraine = Gold BUY Oil BUY")

import streamlit as st
from datetime import datetime, timedelta
import os
st.set_page_config(page_title="FX AMBUSHERS", layout="wide")
if "page" not in st.session_state:
    st.session_state.page="home"
DXY=7
TM=(datetime.utcnow()+timedelta(hours=2)).strftime("%H:%M SAST")
st.success(f"LIVE v2.2 TECH ACADEMY | {TM}")
for f in ["logo.png","logo.jpg","IMG-20260929-WA1810.jpg"]:
    if os.path.exists(f):
        st.image(f, use_container_width=True)
        break
def j(parts, end):
    return " + ".join(parts) + " = " + end
def gauge(t,s,bu,be,ne,sz=260):
    ang=s*9
    if s>=1:
        col="#00ff66"; bcol="#00ff66"; bias="BULL"
    elif s<=-1:
        col="#ff4444"; bcol="#ff4444"; bias="BEAR"
    else:
        col="#ffcc00"; bcol="#ffcc00"; bias="NEU"
    h=sz//2
    a="<div style='border:1px solid #222;border-radius:18px;padding:12px;background:#0f1414;border-left:4px solid "+bcol+";margin-bottom:12px'>"
    b="<div style='text-align:center;color:#888;font-size:11px'>"+t+"</div>"
    c="<div style='text-align:center;color:"+col+";font-weight:900;font-size:20px'>"
    if s>0: c+=bias+" +"+str(s)
    else: c+=bias+" "+str(s)
    c+="</div>"
    d="<div style='width:"+str(sz)+"px;height:"+str(sz//2)+"px;margin:8px auto;position:relative;background:conic-gradient(from 270deg at 50% 100%,#ff2b2b 0 60deg,#ffcc00 60deg 120deg,#00cc66 120deg 180deg);border-radius:"+str(sz)+"px "+str(sz)+"px 0 0'>"
    e="<div style='width:3px;height:"+str(h-10)+"px;background:white;position:absolute;bottom:0;left:50%;transform-origin:bottom;transform:rotate("+str(ang)+"deg)'></div></div>"
    f="<div style='font-size:11px;color:#00ff66'>Bull: "+bu+"</div><div style='font-size:11px;color:#ff6666'>Bear: "+be+"</div><div style='font-size:11px;color:#888'>Neu: "+ne+"</div></div>"
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
 "USDCHF":{"cot":"Long 68 Short 32 Bullish","cotLS":"Bullish","techL":"Bullish","4h":"Bullish","seas":"Bullish","gdp":"1.2 vs 0.8 Bullish","pmiM":"52.0 vs 51.0 Bullish","pmiS":"54.0 vs 53.0 Bullish","retail":"0.3 vs 0.1 Bullish","conf":"99 vs 97 Bullish","cpi":"2.0 vs 1.8 Bullish","ppi":"2.2 vs 2.0 Bullish","pce":"Bullish 2.8","yld":"Bullish","nfp":"160k Bullish","unemp":"Bullish","jobless":"Bullish","adp":"Bullish","jolts":"Bullish","why":"USDCHF AMBUSH: DXY Bull + CHF safe sell = BUY"},
 "USDCAD":{"cot":"Long 72 Short 28 Bullish","cotLS":"Very Bullish","techL":"Bullish","4h":"Bullish","seas":"Very Bullish","gdp":"1.5 vs 1.0 Bullish","pmiM":"50.2 vs 50.5 Neutral","pmiS":"53.5 vs 52.8 Bullish","retail":"0.5 vs 0.2 Bullish","conf":"100 vs 98 Bullish","cpi":"3.0 vs 2.8 Bullish","ppi":"2.5 vs 2.2 Bullish","pce":"Bullish","yld":"Bullish","nfp":"Bullish","unemp":"Neutral","jobless":"Bullish","adp":"Bullish","jolts":"Bullish","why":"USDCAD AMBUSH: DXY Bull + Oil weak = BUY"},
 "GOLD":{"cot":"Long 25 Short 75 Bearish","cotLS":"Bearish","techL":"Very Bearish","4h":"Bearish","seas":"Bearish","gdp":"1.5 vs 1.5 Neutral","pmiM":"54.6 vs 55.2 Bullish","pmiS":"55.4 vs 54.1 Bearish","retail":"-0.6 vs 0.1 Bullish","conf":"89.4 vs 90.3 Bullish","cpi":"3.4 vs 3.4 Neutral","ppi":"4.7 vs 4.9 Bullish","pce":"3.3 vs 3.3 Neutral","yld":"Bearish yield rising","nfp":"162k vs 55k Bearish","unemp":"4.1 vs 4.1 Neutral","jobless":"206k vs 205k Bullish","adp":"38k vs 47k Bullish","jolts":"7.27M vs 7.33M Bullish","why":"GOLD AMBUSH: Tech Very Bearish + Retail 75 Long trapped = SELL"},
 "SILVER":{"cot":"Long 40 Short 60 Bearish","cotLS":"Neutral","techL":"Bearish","4h":"Bearish","seas":"Neutral","gdp":"Neutral 1.5","pmiM":"54.6 vs 55.2 Bullish","pmiS":"55.4 vs 54.1 Bearish","retail":"0.2 Bullish","conf":"90 Bullish","cpi":"3.4 Neutral","ppi":"4.7 Bullish","pce":"3.3 Neutral","yld":"Bearish","nfp":"162k Bearish","unemp":"4.1 Neutral","jobless":"206k Bullish","adp":"38k Bullish","jolts":"7.27M Bullish","why":"SILVER AMBUSH: Gold trap + Tech Bear = SELL"},
 "OIL":{"cot":"Long 45 Short 55 Bearish","cotLS":"Bearish","techL":"Bearish","4h":"Bearish","seas":"Bearish","gdp":"1.0 vs 1.5 Bearish","pmiM":"49.0 vs 50.0 Bearish","pmiS":"52.0 vs 52.5 Neutral","retail":"-0.1 vs 0.3 Bearish","conf":"95 vs 100 Bearish","cpi":"3.4 Neutral","ppi":"1.5 Bearish","pce":"2.5 Neutral","yld":"Neutral","nfp":"140k Neutral","unemp":"4.3 Neutral","jobless":"205k Neutral","adp":"40k Neutral","jolts":"7.3M Neutral","why":"OIL AMBUSH: DXY strong + Demand weak = SELL"},
 "US30":{"cot":"Long 38 Short 62 Bearish","cotLS":"Bearish","techL":"Very Bearish","4h":"Very Bearish","seas":"Bearish","gdp":"1.2 vs 2.0 Bearish","pmiM":"48.5 vs 50.0 Bearish","pmiS":"51.0 vs 53.0 Bearish","retail":"-0.3 vs 0.2 Bearish","conf":"92 vs 98 Bearish","cpi":"2.8 Bearish","ppi":"1.8 Bearish","pce":"2.5 Bearish","yld":"Very Bearish yield up","nfp":"100k Bearish","unemp":"4.3 Neutral","jobless":"220k Bearish","adp":"20k Bearish","jolts":"7.0M Bearish","why":"US30 AMBUSH: Risk off + Yield up = SELL"},
 "NAS100":{"cot":"Long 35 Short 65 Bearish","cotLS":"Very Bearish","techL":"Very Bearish","4h":"Very Bearish","seas":"Very Bearish","gdp":"1.0 Bearish","pmiM":"48.5 Bearish","pmiS":"51.0 Bearish","retail":"-0.3 Bearish","conf":"92 Bearish","cpi":"2.8 Bearish","ppi":"1.8 Bearish","pce":"2.5 Bearish","yld":"Very Bearish tech sell","nfp":"100k Bearish","unemp":"4.3 Neutral","jobless":"220k Bearish","adp":"20k Bearish","jolts":"7.0M Bearish","why":"NAS100 AMBUSH: Tech sell off = SELL"},
 "SPX500":{"cot":"Long 40 Short 60 Bearish","cotLS":"Bearish","techL":"Very Bearish","4h":"Bearish","seas":"Bearish","gdp":"1.2 Bearish","pmiM":"48.5 Bearish","pmiS":"51.0 Bearish","retail":"-0.3 Bearish","conf":"92 Bearish","cpi":"2.8 Bearish","ppi":"1.8 Bearish","pce":"2.5 Bearish","yld":"Very Bearish","nfp":"100k Bearish","unemp":"4.3 Neutral","jobless":"220k Bearish","adp":"20k Bearish","jolts":"7.0M Bearish","why":"SPX500 AMBUSH: Risk off = SELL"},
 "BTCUSD":{"cot":"Long 30 Short 70 Bearish","cotLS":"Very Bearish","techL":"Very Bearish","4h":"Very Bearish","seas":"Bearish","gdp":"Neutral","pmiM":"Bearish risk off","pmiS":"Bearish risk off","retail":"78 Long trapped","conf":"Bearish fear 22","cpi":"Bearish risk off","ppi":"Bearish risk off","pce":"Bearish risk off","yld":"Bearish risk off","nfp":"Bearish risk off","unemp":"Neutral","jobless":"Bearish risk off","adp":"Bearish risk off","jolts":"Bearish risk off","why":"BTC AMBUSH: Retail 78 Long trapped = SELL"},
 "ETHUSD":{"cot":"Long 32 Short 68 Bearish","cotLS":"Very Bearish","techL":"Very Bearish","4h":"Very Bearish","seas":"Bearish","gdp":"Neutral","pmiM":"Bearish risk off","pmiS":"Bearish risk off","retail":"76 Long trapped","conf":"Bearish fear 25","cpi":"Bearish risk off","ppi":"Bearish risk off","pce":"Bearish risk off","yld":"Bearish risk off","nfp":"Bearish risk off","unemp":"Neutral","jobless":"Bearish risk off","adp":"Bearish risk off","jolts":"Bearish risk off","why":"ETH AMBUSH: Retail 76 Long trapped = SELL"},
}
def badge(t):
    c='#ff3355' if 'Bear' in t else '#00ff88' if 'Bull' in t else '#ffcc00'
    return f"<span style='background:{c}22;color:{c};border:1px solid {c};padding:3px 7px;border-radius:7px;font-size:11px'>{t}</span>"
if st.session_state.page=="home":
    c1,c2=st.columns(2)
    with c1:
        if st.button("FOREX 6", use_container_width=True): st.session_state.page="forex"
        if st.button("GOLD OIL", use_container_width=True): st.session_state.page="gold"
        if st.button("COT TABLE", use_container_width=True): st.session_state.page="cot"
        if st.button("RETAIL SENTIMENT", use_container_width=True): st.session_state.page="retail"
        if st.button("FUNDAMENTALS SCHOOL", use_container_width=True): st.session_state.page="learn_fund"
        if st.button("TECHNICAL SCHOOL", use_container_width=True): st.session_state.page="learn_tech"
    with c2:
        if st.button("INDICES", use_container_width=True): st.session_state.page="indices"
        if st.button("CRYPTO", use_container_width=True): st.session_state.page="crypto"
        if st.button("SCORE FINDER - AMBUSH FINDER", use_container_width=True): st.session_state.page="finder"
        if st.button("FUND + GPR", use_container_width=True): st.session_state.page="fund"
else:
    if st.button("BACK RADAR", use_container_width=True): st.session_state.page="home"
    if st.session_state.page=="finder":
        st.markdown("### AMBUSH-FINDER Scorecard - FULL DATA -10 to +10")
        ch=st.selectbox("Choose Asset - 15 Pairs", list(all_assets.keys()))
        s,bu,be,ne,typ=all_assets[ch]
        st.write(f"Type: {typ}")
        st.markdown(gauge(ch,s,bu,be,ne,280), unsafe_allow_html=True)
        if s>=

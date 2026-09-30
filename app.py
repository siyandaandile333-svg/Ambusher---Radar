import streamlit as st
from datetime import datetime, timedelta
import os

st.set_page_config(page_title="FX AMBUSHERS", layout="wide")
if "page" not in st.session_state:
    st.session_state.page="home"

DXY=7
TM=(datetime.utcnow()+timedelta(hours=2)).strftime("%H:%M SAST")

# BRAND HEADER - FX AMBUSHERS
st.markdown("""
<div style='text-align:center;background:#0a0a0a;border:2px solid #00ff66;border-radius:15px;padding:12px;margin-bottom:10px'>
<div style='font-size:32px;font-weight:900;color:#00ff66;letter-spacing:3px'>FX AMBUSHERS</div>
<div style='font-size:12px;color:#888;letter-spacing:2px'>PATIENCE IS PROFIT • EST 2025</div>
</div>
""", unsafe_allow_html=True)

st.success(f"LIVE v2.4 BRANDED | {TM} | DXY +7 BULL")

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
        if st.button("FUNDAMENTALS SCHOOL", use_container_width=True): st.session_state.page="learn_fund"
        if st.button("TECHNICAL SCHOOL", use_container_width=True): st.session_state.page="learn_tech"
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
    if st.session_state.page in ["forex","gold","indices","crypto"]:
        data={"forex":forex,"gold":commod,"indices":indices,"crypto":crypto}[st.session_state.page]
        cols=st.columns(2)
        for i,(p,s,bu,be,ne) in enumerate(data):
            with cols[i%2]: st.markdown(gauge(p,s,bu,be,ne,170), unsafe_allow_html=True)
    if st.session_state.page=="cot":
        st.markdown("### COT - WITH CHANGE")
        html="<table style='width:100%;border-collapse:collapse;font-size:11px'><tr style='background:#111;color:#888'><th>Asset</th><th>Long</th><th>Short</th><th>Change</th><th>Bias</th><th>Why</th></tr>"
        for r in cot:
            a,lo,sh,ch,bi,wh=r
            if bi=="BULL": bc="<td style='background:#00ff66;color:black;font-weight:900;padding:5px;border:1px solid #333'>BULL</td>"; cc="<td style='color:#00ff66;padding:5px;border:1px solid #333'>"+ch+"</td>"
            else: bc="<td style='background:#ff4444;color:white;font-weight:900;padding:5px;border:1px solid #333'>BEAR</td>"; cc="<td style='color:#ff6666;padding:5px;border:1px solid #333'>"+ch+"</td>"
            html+="<tr><td style='padding:5px;border:1px solid #333'>"+a+"</td><td style='padding:5px;border:1px solid #333;color:#00ff66'>"+lo+"</td><td style='padding:5px;border:1px solid #333;color:#ff6666'>"+sh+"</td>"+cc+bc+"<td style='padding:5px;border:1px solid #333;color:#aaa'>"+wh+"</td></tr>"
        html+="</table>"; st.markdown(html, unsafe_allow_html=True)
    if st.session_state.page=="retail":
        st.markdown("### RETAIL SENTIMENT - CONTRARIAN")
        html="<table style='width:100%;border-collapse:collapse;font-size:11px'><tr style='background:#111;color:#888'><th>Asset</th><th>RLong</th><th>RShort</th><th>Crowd</th><th>Signal</th><th>Why</th></tr>"
        for r in retail:
            a,lo,sh,cr,sg,wh=r
            if "SELL" in sg: bc="<td style='background:#ff4444;color:white;font-weight:900;padding:5px;border:1px solid #333'>SELL</td>"
            else: bc="<td style='background:#00ff66;color:black;font-weight:900;padding:5px;border:1px solid #333'>BUY</td>"
            html+="<tr><td style='padding:5px;border:1px solid #333'>"+a+"</td><td style='padding:5px;border:1px solid #333;color:#00ff66'>"+lo+"</td><td style='padding:5px;border:1px solid #333;color:#ff6666'>"+sh+"</td><td style='padding:5px;border:1px solid #333;color:#ffcc00'>"+cr+"</td>"+bc+"<td style='padding:5px;border:1px solid #333;color:#aaa'>"+wh+"</td></tr>"
        html+="</table>"; st.markdown(html, unsafe_allow_html=True)
    if st.session_state.page=="fund":
        st.markdown("### FUND DATES + GPR")
        st.write("FOMC Sep29 HIGH - Powell Hawk = DXY Buy")
        st.write("NFP Oct3 HIGH - Exp 180K")
        st.write("CPI Oct4 HIGH - Exp 3.2%")
    if st.session_state.page=="learn_fund":
        st.markdown("## FX AMBUSHERS FUNDAMENTAL ACADEMY")
        with st.expander("1. DXY - King of Forex"):
            st.write("DXY = USD vs 6 majors. DXY UP = EURUSD DOWN. Check DXY first.")
        with st.expander("2. Economic Indicators"):
            st.write("CPI Hot = Hawk = DXY Buy. NFP High = DXY Buy. FOMC Hawk = DXY Buy. Yield UP = DXY UP NAS100 DOWN.")
        with st.expander("3. Central Banks"):
            st.write("FED DXY, ECB EUR, BoE GBP, BoJ JPY, RBA AUD Gold China, SNB CHF safe, BoC CAD Oil.")
        with st.expander("4. GPR Geopolitical"):
            st.write("War = Gold Buy Oil Buy. Ceasefire = Gold Sell. OPEC Cut = Oil Buy. China Stimulus = AUD Gold Buy.")
        with st.expander("5. COT Smart Money"):
            st.write("71% Long DXY = Banks buying USD = Bull. Change +3% Long = adding momentum.")
        with st.expander("6. Retail Contrarian"):
            st.write("Retail 70% long = crowd wrong = SELL. BTC 78% long FOMO = Top = SELL.")
        with st.expander("7. Score -10 to +10"):
            st.write("+1 to +10 BULL, -1 to -10 BEAR, 0 WAIT. DXY +7 Strong Bull.")
    if st.session_state.page=="learn_tech":
        st.markdown("## FX AMBUSHERS TECHNICAL ACADEMY")
        st.caption("Patience is Profit - Unique Ambush Method")
        if os.path.exists("tech_structure.png"):
            st.image("tech_structure.png", use_container_width=True)
        with st.expander("1. MARKET STRUCTURE - Bull Road / Bear Road"):
            st.write("HH HL = Bull Road stairs UP. LL LH = Bear Road stairs DOWN. BOS = Road Continues. CHoCH = Road Flips = Ambush zone. Never enter BOS, wait CHoCH + pullback.")
            if os.path.exists("tech_structure.png"):
                st.image("tech_structure.png", use_container_width=True)
        with st.expander("2. SUPPORT & RESISTANCE - Battle Zones"):
            st.write("Support = Floor zone 10-20 pips where price bounced 2-3x. Resistance = Roof. 3rd touch = Ambush. Broken support becomes resistance FLIP retest SELL. Only trade S/R with DXY +7 alignment.")
            if os.path.exists("tech_sr.png"):
                st.image("tech_sr.png", use_container_width=True)
        with st.expander("3. SUPPLY & DEMAND - Bank Vaults"):
            st.write("Demand = Wholesale - big green move from tight base. Banks bought cheap. Supply = Expensive - big red drop from tight base. First return strongest.")
        with st.expander("4. SMC - Ambush Translation"):
            st.write("Order Block = Ambush Block last opposite candle before big move. FVG = Gap Trap 3 candles gap fill 50%. Liquidity = Crowd Trap equal highs stop hunt then reverse. Stop Hunt = Fake Push. Premium above 50% only SELL, Discount below 50% only BUY.")
            if os.path.exists("tech_smc.png"):
                st.image("tech_smc.png", use_container_width=True)
        with st.expander("5. ENTRY MODELS - 3 AMBUSH SETUPS"):
            st.write("SETUP A: CHoCH + Ambush Block - CHoCH break HL, mark last green Block, wait return + DXY +7 + Score -7 = SELL. SETUP B: Liquidity Grab + Flip - equal highs spike take stops then rejection SELL. SETUP C: Gap Trap 50% - pullback to 50% of FVG + DXY bias.")
        with st.expander("6. RISK - Patience is Profit"):
            st.write("Stop behind Block or liquidity. Target next vault or 2R. 1% max per ambush. Score 0 = NO TRADE. Kill Zones 08:00-11:00 SAST London, 15:30-18:00 NY.")

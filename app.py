import streamlit as st
from datetime import datetime, timedelta
import os

st.set_page_config(page_title="FX AMBUSHERS", layout="wide")
if "page" not in st.session_state:
    st.session_state.page="home"

DXY=7
TM=(datetime.utcnow()+timedelta(hours=2)).strftime("%H:%M SAST")
st.success(f"LIVE v2.2 TECH ACADEMY FULL EDGEFINDER | {TM}")

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
    a="<div style='border:1px solid #222;border-radius:18px;padding:12px;background:#0f1414;border-left:4px solid "+bcol+";margin-bottom:12px'>"
    b="<div style='text-align:center;color:#888;font-size:11px'>"+t+"</div>"
    c="<div style='text-align:center;color:"+col+";font-weight:900;font-size:20px'>"
    if s>0:
        c+=bias+" +"+str(s)
    else:
        c+=bias+" "+str(s)
    c+="</div>"
    d="<div style='width:"+str(sz)+"px;height:"+str(sz//2)+"px;margin:8px auto;position:relative;background:conic-gradient(from 270deg at 50% 100%,#ff2b2b 0 60deg,#ffcc00 60deg 120deg,#00cc66 120deg 180deg);border-radius:"+str(sz)+"px "+str(sz)+"px 0 0'>"
    e="<div style='width:3px;height:120px;background:white;position:absolute;bottom:0;left:50%;transform-origin:bottom;transform:rotate("+str(ang)+"deg)'></div></div>"
    f="<div style='font-size:11px;color:#00ff66'>Bull: "+bu+"</div><div style='font-size:11px;color:#ff6666'>Bear: "+be+"</div><div style='font-size:11px;color:#888'>Neu: "+ne+"</div></div>"
    return a+b+c+d+e+f

def edge_badge(label):
    label=str(label)
    if "Very Bearish" in label:
        return "<span style='background:#7f1d1d;color:#fecaca;padding:3px 9px;border-radius:6px;font-weight:800;font-size:11px;border:1px solid #991b1b'>"+label+"</span>"
    if "Bearish" in label or "BEAR" in label or "SELL" in label:
        return "<span style='background:#450a0a;color:#fca5a5;padding:3px 9px;border-radius:6px;font-weight:700;font-size:11px;border:1px solid #7f1d1d'>"+label+"</span>"
    if "Very Bullish" in label:
        return "<span style='background:#1e3a8a;color:#bfdbfe;padding:3px 9px;border-radius:6px;font-weight:800;font-size:11px;border:1px solid #1e40af'>"+label+"</span>"
    if "Bullish" in label or "BULL" in label or "BUY" in label:
        return "<span style='background:#172554;color:#93c5fd;padding:3px 9px;border-radius:6px;font-weight:700;font-size:11px;border:1px solid #1e3a8a'>"+label+"</span>"
    return "<span style='background:#1f2937;color:#9ca3af;padding:3px 9px;border-radius:6px;font-weight:700;font-size:11px'>"+label+"</span>"

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
        if s>=1:
            st.success(f"Score +{s} = BULL")
        elif s<=-1:
            st.error(f"Score {s} = BEAR")
        else:
            st.warning(f"Score 0 = WAIT")

        # === EDGEFINDER WHY - EXACT LIKE YOUR SCREENSHOT ===
        cot_row = next((x for x in cot if x[0]==ch), ["-","-","-","-","-","-"])
        ret_row = next((x for x in retail if x[0]==ch), ["-","-","-","-","-","-"])
        try:
            r_long = int(ret_row[1].replace("%",""))
        except:
            r_long = 70
        r_short = 100 - r_long

        # Header like EdgeFinder
        st.markdown("<div style='background:#0b0f19;border:1px solid #1f2937;border-radius:12px;padding:12px;margin-top:12px'><div style='display:flex;justify-content:space-between'><div><b style='font-size:13px'>Asset Scorecard | </b><span style='color:#f87171;font-size:13px'>Bearish</span> <span style='background:#1f2937;padding:2px 6px;border-radius:4px;font-size:11px;margin-left:6px'>"+ch+"</span></div><div style='font-size:11px;color:#9ca3af'>EdgeFinder score: <b style='color:white'>"+str(s)+"</b> Technical: <span style='color:#f87171'>"+str(s)+"</span> Sentiment: <span style='color:#60a5fa'>"+cot_row[4]+"</span> Macro: <span style='color:#60a5fa'>"+str(DXY)+"</span></div></div></div>", unsafe_allow_html=True)

        st.markdown("<div style='margin-top:10px;border:1px solid #1f2937;border-radius:10px;padding:10px;background:#0e1212'><div style='display:flex;justify-content:space-between'><b style='font-size:12px'>Crowd sentiment signal</b><b style='color:#60a5fa;font-size:12px'>"+str(ret_row[4])+"</b></div><div style='display:flex;gap:2px;margin:8px 0'><div style='flex:"+str(r_long)+";height:10px;background:#dc2626'></div><div style='flex:"+str(r_short)+";height:10px;background:#2563eb'></div></div><div style='font-size:11px;color:#9ca3af'>Long % <span style='color:#f87171'>"+str(ret_row[1])+"</span> | Short % <span style='color:#60a5fa'>"+str(ret_row[2])+"</span> | <span style='color:#eab308'>"+str(ret_row[3])+"</span> Econ surprise index <b style='color:#60a5fa'>0.00%</b> | "+str(ret_row[5])+"</div></div>", unsafe_allow_html=True)

        # Full table like screenshot
        t_html = "<div style='margin-top:10px;overflow-x:auto'><table style='width:100%;border-collapse:collapse;font-size:11px'>"
        t_html += "<tr style='background:#111827'><td style='padding:7px;color:#9ca3af;font-weight:700'>Technicals</td><td style='padding:7px'>"+edge_badge("Very Bearish" if s <= -6 else "Bearish" if s < 0 else "Neutral")+"</td><td style='padding:7px;color:#6b7280'></td><td style='padding:7px;color:#6b7280'></td></tr>"
        t_html += "<tr><td style='padding:6px;border-bottom:1px solid #1f2937'>4H Chart Trend / Daily Chart Trend</td><td style='padding:6px;border-bottom:1px solid #1f2937'>"+edge_badge("Bearish")+"</td><td style='padding:6px;border-bottom:1px solid #1f2937'></td><td style='padding:6px;border-bottom:1px solid #1f2937'></td></tr>"
        t_html += "<tr><td style='padding:6px;border-bottom:1px solid #1f2937'>Seasonality Trend</td><td style='padding:6px;border-bottom:1px solid #1f2937'>"+edge_badge("Bearish")+"</td><td style='padding:6px;border-bottom:1px solid #1f2937'></td><td style='padding:6px;border-bottom:1px solid #1f2937'></td></tr>"
        t_html += "<tr style='background:#111827'><td style='padding:7px;color:#9ca3af;font-weight:700'>Institutional activity</td><td style='padding:7px'>"+edge_badge("Neutral")+"</td><td style='padding:7px;color:#6b7280'>Long %</td><td style='padding:7px;color:#6b7280'>Short %</td></tr>"
        t_html += "<tr><td style='padding:6px;border-bottom:1px solid #1f2937'>COT - Net Positioning</td><td style='padding:6px;border-bottom:1px solid #1f2937'>"+edge_badge(cot_row[4])+"</td><td style='padding:6px;border-bottom:1px solid #1f2937'>"+cot_row[1]+" Long</td><td style='padding:6px;border-bottom:1px solid #1f2937'>"+cot_row[2]+" Short</td></tr>"
        t_html += "<tr><td style='padding:6px;border-bottom:1px solid #1f2937'>COT - Latest Buys/Sells</td><td style='padding:6px;border-bottom:1px solid #1f2937'>"+edge_badge(cot_row[3])+"</td><td style='padding:6px;border-bottom:1px solid #1f2937' colspan=2>"+cot_row[5]+"</td></tr>"
        t_html += "<tr style='background:#111827'><td style='padding:7px;color:#9ca3af;font-weight:700'>Economic growth</td><td style='padding:7px'>"+edge_badge("Very Bullish" if DXY>=5 else "Bullish")+"</td><td style='padding:7px;color:#6b7280'>Actual</td><td style='padding:7px;color:#6b7280'>Forecast</td></tr>"
        t_html += "<tr><td style='padding:6px;border-bottom:1px solid #1f2937'>GDP Growth QoQ / DXY King +"+str(DXY)+"</td><td style='padding:6px;border-bottom:1px solid #1f2937'>"+edge_badge("Bullish")+"</td><td style='padding:6px;border-bottom:1px solid #1f2937'>1.50%</td><td style='padding:6px;border-bottom:1px solid #1f2937'>1.50%</td></tr>"
        t_html += "<tr><td style='padding:6px;border-bottom:1px solid #1f2937'>Manufacturing / Services PMI</td><td style='padding:6px;border-bottom:1px solid #1f2937'>"+edge_badge("Bearish" if s<0 else "Bullish")+"</td><td style='padding:6px;border-bottom:1px solid #1f2937'>54.6</td><td style='padding:6px;border-bottom:1px solid #1f2937'>55.2</td></tr>"
        t_html += "<tr><td style='padding:6px;border-bottom:1px solid #1f2937'>Retail Sales MoM (Fade Retail "+ret_row[1]+")</td><td style='padding:6px;border-bottom:1px solid #1f2937'>"+edge_badge(ret_row[4])+"</td><td style='padding:6px;border-bottom:1px solid #1f2937'>"+ret_row[1]+" Long</td><td style='padding:

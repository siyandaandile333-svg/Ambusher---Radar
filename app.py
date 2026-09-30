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
        if s>=1: st.success(f"Score +{s} = BULL")
        elif s<=-1: st.error(f"Score {s} = BEAR")
        else: st.warning(f"Score 0 = WAIT")

                # ===== NEW WHY ADDON - FIXED NO ERROR - ONLY ADD =====
        cot_row = next((x for x in cot if x[0]==ch), ["-","-","-","-","-","-"])
        ret_row = next((x for x in retail if x[0]==ch), ["-","-","-","-","-","-"])

        try:
            r_long = int(ret_row[1].replace("%",""))
        except:
            r_long = 70
        r_short = 100 - r_long

        st.markdown("<div style='margin-top:12px;border:1px solid #222;border-radius:12px;padding:10px;background:#0e1212'>Crowd sentiment signal: <b style='color:#6aa8ff;float:right'>"+str(ret_row[4])+"</b><div style='display:flex;gap:2px;margin:6px 0'><div style='flex:"+str(r_long)+";height:8px;background:#ff4444'></div><div style='flex:"+str(r_short)+";height:8px;background:#3b82f6'></div></div><div style='font-size:11px;color:#888'>Long % "+str(ret_row[1])+" | Short % "+str(ret_row[2])+" | "+str(ret_row[3])+" | "+str(ret_row[5])+"</div></div>", unsafe_allow_html=True)

        html2 = "<table style='width:100%;border-collapse:collapse;font-size:11px;margin-top:10px'>"
        html2 += "<tr style='background:#111'><th style='text-align:left;padding:6px;color:#888'>Technicals</th><th style='text-align:left;padding:6px;color:#ff7777'>"+("Very Bearish" if s<=-6 else "Bearish" if s<0 else "Bullish")+"</th></tr>"
        html2 += "<tr><td style='padding:5px;border-bottom:1px solid #1a1a1a'>4H / Daily Trend Score "+str(s)+"</td><td style='padding:5px;border-bottom:1px solid #1a1a1a'>Score "+str(s)+"</td></tr>"
        html2 += "<tr style='background:#111'><th style='text-align:left;padding:6px;color:#888'>Institutional</th><th style='padding:6px;color:#888'>Long Short Change</th></tr>"
        html2 += "<tr><td style='padding:5px;border-bottom:1px solid #1a1a1a'>COT Net Positioning</td><td style='padding:5px;border-bottom:1px solid #1a1a1a;color:#6aa8ff'>"+str(cot_row[1])+" Long "+str(cot_row[2])+" Short "+str(cot_row[4])+"</td></tr>"
        html2 += "<tr><td style='padding:5px;border-bottom:1px solid #1a1a1a'>COT Latest</td><td style='padding:5px;border-bottom:1px solid #1a1a1a'>"+str(cot_row[3])+" | "+str(cot_row[5])+"</td></tr>"
        html2 += "<tr style='background:#111'><th style='text-align:left;padding:6px;color:#888'>Economic Growth</th><th></th></tr>"
        html2 += "<tr><td style='padding:5px;border-bottom:1px solid #1a1a1a'>DXY +"+str(DXY)+" Bull King</td><td style='padding:5px;border-bottom:1px solid #1a1a1a;color:#aaa'>"+str(bu)[:60]+"</td></tr>"
        html2 += "<tr><td style='padding:5px;border-bottom:1px solid #1a1a1a'>Retail Contrarian "+str(ret_row[1])+"</td><td style='padding:5px;border-bottom:1px solid #1a1a1a;color:#ffcc00'>"+str(ret_row[4])+" | "+str(ret_row[3])+"</td></tr>"
        html2 += "<tr style='background:#111'><th style='text-align:left;padding:6px;color:#888'>Inflation / Jobs / GPR</th><th></th></tr>"
        html2 += "<tr><td style='padding:5px;border-bottom:1px solid #1a1a1a'>CPI 3.2% + US10Y 4.2% + NFP</td><td style='padding:5px;border-bottom:1px solid #1a1a1a;color:#aaa'>"+str(ne)+"</td></tr>"
        html2 += "</table>"
        st.markdown(html2, unsafe_allow_html=True)

        st.caption("WHY: DXY +"+str(DXY)+" + COT "+str(cot_row[1])+" "+str(cot_row[4])+" "+str(cot_row[3])+" + Retail "+str(ret_row[1])+" vs "+str(ret_row[2])+" = "+str(ret_row[4]))
        st.write("Bull WHY: "+str(bu))
        st.write("Bear WHY: "+str(be))
        # ===== END FIXED ADDON =====
        # Find COT and Retail for chosen asset
        cot_row = next((x for x in cot if x[0]==ch), ["-","-","-","-","-","-"])
        ret_row = next((x for x in retail if x[0]==ch), ["-","-","-","-","-","-"])

        def bb(t):
            t=str(t)
            if "BEAR" in t or "Bearish" in t or "SELL" in t:
                return f"<span style='background:#ff444433;color:#ff7777;padding:2px 7px;border-radius:5px;font-weight:700;font-size:11px'>{t}</span>"
            elif "BULL" in t or "Bullish" in t or "BUY" in t:
                return f"<span style='background:#2a5bd744;color:#6aa8ff;padding:2px 7px;border-radius:5px;font-weight:700;font-size:11px'>{t}</span>"
            else:
                return f"<span style='background:#333;color:#aaa;padding:2px 7px;border-radius:5px;font-weight:700;font-size:11px'>{t}</span>"

        # crowd bar
        try:
            r_long = int(ret_row[1].replace("%",""))
        except:
            r_long = 70
        r_short = 100 - r_long

        st.markdown(f"""
        <div style="margin-top:10px;border:1px solid #222;border-radius:12px;padding:10px;background:#0e1212">
        <div style="display:flex;justify-content:space-between"><b style="font-size:12px">Crowd sentiment signal</b><b style="color:#6aa8ff;font-size:12px">{ret_row[4]}</b></div>
        <div style="display:flex;gap:2px;margin:6px 0"><div style="flex:{r_long};height:8px;background:#ff4444"></div><div style="flex:{r_short};height:8px;background:#3b82f6"></div></div>
        <div style="font-size:11px;color:#888">Long % {ret_row[1]} | Short % {ret_row[2]} | Change {ret_row[3]} | <span style="color:#aaa">{ret_row[5]}</span></div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="margin-top:10px">
        <table style="width:100%;border-collapse:collapse;font-size:11px">
        <tr style="background:#111"><th style="text-align:left;padding:6px;color:#888">Technicals</th><th style="text-align:left;padding:6px">{bb('Very Bearish' if s<=-6 else 'Bearish' if s<0 else 'Very Bullish' if s>=6 else 'Neutral')}</th><th></th></tr>
        <tr><td style="padding:5px;border-bottom:1px solid #1a1a1a">4H / Daily Chart Trend</td><td style="padding:5px;border-bottom:1px solid #1a1a1a">{bb('Bearish' if s<0 else 'Bullish')}</td><td style="padding:5px;border-bottom:1px solid #1a1a1a;color:#666">Score {s}</td></tr>
        <tr><td style="padding:5px;border-bottom:1px solid #1a1a1a">Seasonality Trend</td><td style="padding:5px;border-bottom:1px solid #1a1a1a">{bb('Bearish' if 'DXY' in bu else 'Bullish')}</td><td></td></tr>

        <tr style="background:#111"><th style="text-align:left;padding:6px;color:#888">Institutional activity</th><th style="padding:6px">Neutral</th><th style="padding:6px;color:#888">Long% Short% Change</th></tr>
        <tr><td style="padding:5px;border-bottom:1px solid #1a1a1a">COT - Net Positioning</td><td style="padding:5px;border-bottom:1px solid #1a1a1a">{bb(cot_row[4])}</td><td style="padding:5px;border-bottom:1px solid #1a1a1a;color:#6aa8ff">{cot_row[1]} Long {cot_row[2]} Short</td></tr>
        <tr><td style="padding:5px;border-bottom:1px solid #1a1a1a">COT - Latest Buys/Sells</td><td style="padding:5px;border-bottom:1px solid #1a1a1a">{bb(cot_row[3])}</td><td style="padding:5px;border-bottom:1px solid #1a1a1a;color:#aaa">{cot_row[5]}</td></tr>

        <tr style="background:#111"><th style="text-align:left;padding:6px;color:#888">Economic growth</th><th style="padding:6px">{bb('Very Bullish' if DXY>=5 else 'Bearish')}</th><th></th></tr>
        <tr><td style="padding:5px

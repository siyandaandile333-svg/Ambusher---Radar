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

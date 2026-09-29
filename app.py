import streamlit as st
from datetime import datetime
import os

st.set_page_config(page_title="FX AMBUSHERS", layout="wide")
if "page" not in st.session_state:
    st.session_state.page="home"

DXY=71
TM=datetime.now().strftime("%H:%M SAST")
st.success(f"✅ LIVE v1.5 SCORE FINDER | {TM} | DXY {DXY}")

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

# DXY MAIN
dxy_bull="Powell Hawk No Cut Sep29 + US CPI 3.2% Hot + US10Y 4.2% Up + BoJ Ueda Dovish = USD Buy"
dxy_bear="Powell Dovish Cut 25bps + Gold 2600 Risk On + BoJ Hawk Hike + Yield Down = USD Sell"
dxy_neu="FOMC Sep29 HIGH + NFP Oct3 180K + CPI Oct4"
st.markdown(gauge("DXY AMBUSH",DXY,dxy_bull,dxy_bear,dxy_neu,280), unsafe_allow_html=True)

forex=[
 ("EURUSD",29,
  "ECB Lagarde Hawk + EU CPI 2.4% Hot + EU GDP Strong + Fed Dovish Cut = EUR Buy",
  "Fed Powell Hawk No Cut + DXY 71 Bull + US10Y 4.2% Up + US CPI 3.2% = EUR Sell",
  "ECB Oct5 Rate + US CPI Oct4 + GPR + Fed"),
 ("GBPUSD",30,
  "BoE Bailey Hawk + UK CPI 3.8% Hot + UK Wage Up + Fed Cut = GBP Buy",
  "Fed Hawk No Cut + DXY 71 + US Yield Up + UK Recession Fear + Risk Off = GBP Sell",
  "BoE Oct5 + FOMC Sep29 + UK CPI"),
 ("USDJPY",71,
  "DXY 71 Bull + BoJ Ueda Dovish No Hike + US-JP Yield Gap 4.2% vs 0.5% = USDJPY Buy",
  "BoJ Hawk Rate Hike + Ueda Hawk + Fed Dovish Cut + Risk Off Yen Safe = Sell",
  "BoJ Rate Oct4 HIGH + FOMC Sep29 + GPR"),
 ("AUDUSD",28,
  "RBA Bullock Hawk + Gold 2600 Up + China Stimulus + Iron Ore Up = AUD Buy",
  "DXY 71 Bull + Risk Off + China PMI Weak + Iron Ore Down + RBA Dovish = AUD Sell",
  "RBA Meeting + China PMI + Gold + DXY"),
 ("USDCHF",71,
  "DXY 71 Bull + SNB Jordan Dovish + Safe Haven Off + Gold Down = USDCHF Buy",
  "SNB Hawk + Jordan Hawk + Fed Cut + Gold 2600 Up + Risk Off CHF Safe = Sell",
  "SNB Rate + Gold 2600 + Fed + Risk"),
 ("USDCAD",70,
  "DXY 71 Bull + Oil WTI 70 Down + BoC Macklem Dovish + US Strong = Buy",
  "Oil WTI 85 Up + OPEC Cut + BoC Hawk + Canada CPI Up + Risk On CAD = Sell",
  "BoC Rate + Oil EIA + OPEC + NFP"),
]
commod=[
 ("GOLD",25,
  "Fed Dovish Cut 25bps + US10Y 4.2 Down + USD Weak + GPR War Risk = Gold Buy",
  "DXY 71 Bull + Powell Hawk No Cut + US10Y 4.2 Up + Risk On Stocks Up = Sell",
  "GPR Israel-Gaza + FOMC Sep29 + US CPI"),
 ("SILVER",27,
  "Gold 2600 Up + Fed Cut + Industrial + Solar Demand + Copper Up = Silver Buy",
  "DXY 71 + US Yield Up + Gold Sell + Industrial Weak +

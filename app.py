import streamlit as st
import yfinance as yf
import pandas as pd
import pytz
from datetime import datetime
st.set_page_config(layout="wide")
st.markdown("<style>.stApp{background:#070709;color:#E8E6D9}.macro-card{background:#101018;border:1px solid #2A2A3A;border-radius:14px;padding:14px;margin:8px 0}.why{font-size:11px;line-height:1.4}</style>", unsafe_allow_html=True)
try:
 st.image("IMG-20260929-WA1810.jpg",width=340)
except:
 st.markdown("<h2 style='color:#FFD60A;text-align:center'>FX AMBUSHERS</h2>", unsafe_allow_html=True)
sa=datetime.now(pytz.timezone('Africa/Johannesburg')).strftime("%d %b %H:%M SA")
st.markdown("<div style='background:#111;padding:6px;color:#FFD60A;font-size:11px'>"+sa+" PREDATOR MODE</div>", unsafe_allow_html=True)
# FULL WHY'S - BROKEN INTO TINY LINES SO PHONE CANT CUT
DB={}
DB["DXY"]=[
 "71",
 "BULL",
 "Fed Hawkish + Real Yield 4.2% + COT 98K Long Most Bull 6M",
 "Fed Cut + SP500 + Gold Risk On",
 "GPR + Oil + BoJ Intervention"
]
DB["EURUSD"]=[
 "39",
 "BEAR",
 "GPR + CB Buying + COT Longs Trap 68%",
 "DXY 71 + Yield 4.2 + Fed Hawk + COT -125K Short EUR",
 "VIX + SP500 + CPI"
]
DB["GBPUSD"]=[
 "42",
 "BEAR",
 "UK Wage + GPR + COT Longs 65% Trap",
 "DXY 71 + BoE Dovish + CPI Low + COT -89K Short GBP",
 "VIX + Oil + Fed"
]
DB["USDJPY"]=[
 "72",
 "BULL",
 "DXY 71 + Fed Hawk + BoJ Dovish + COT 148K Long",
 "Intervention Risk + VIX Safe Haven",
 "GPR + SP500 + CPI"
]
DB["XAUUSD"]=[
 "39",
 "BEAR",
 "GPR + CB Buying + COT 82% Long TOP Trap",
 "DXY 71 + Yield 4.2 + Fed Hawk + COT -28K Cut +19K Short",
 "VIX + SP500 + GDX"
]
DB["XAGUSD"]=[
 "44",
 "BEAR",
 "GPR + Industry + CB + COT 76% Trap",
 "DXY 71 + Yield 4.2 + Fed Hawk + COT -12K +22K Short",
 "VIX + CPI + Oil"
]
DB["USDCAD"]=[
 "52",
 "NEUT",
 "DXY 71 + Fed Hawk + CPI + Yield",
 "Oil 82 + OPEC Cut + CB Buy CAD",
 "VIX + SP500 + GPR"
]
DB["USDCHF"]=[
 "61",
 "BULL",
 "DXY 71 + SNB Dovish + Yield + COT 98K",
 "CHF Safe + GPR + Gold Fear",
 "SP500 + CPI + Oil"
]
DB["OILWTI"]=[
 "68",
 "BULL",
 "GPR + OPEC Cut + Inventory Draw",
 "DXY 71 + Fed Hawk + Yield 4.2",
 "VIX + CPI + Gold"
]
DB["BTCUSD"]=[
 "54",
 "NEUT",
 "ETF Inflow + GPR + CB + Halving",
 "DXY 71 + Bear BTC + Yield 4.2",
 "SP500 + CPI + Gold"
]
DB["US30"]=[
 "48",
 "NEUT",
 "Fed Pause + CB Earnings + COT 15K Long +32K Asset",
 "DXY 71 + Yield 4.2 + VIX + Oil",
 "CPI + Gold + SP500"
]
DB["NAS100"]=[
 "45",
 "BEAR",
 "AI Demand + CB + COT Longs Trap",
 "DXY 71 + Yield 4.2 + Fed + VIX + COT -18K",
 "SP500 + CPI + Oil"
]
DB["SP500"]=[
 "50",
 "NEUT",
 "Fed Pause + Buybacks + Earnings",
 "DXY 71 + Yield 4.2 + VIX",
 "CPI + Oil + Gold"
]
DB["GER30"]=[
 "44",
 "BEAR",
 "ECB Dovish + GPR + CB + PMI 44.2",
 "DXY 71 + Yield 4.2 + COT -18K Short DAX",
 "SP500 + CPI + Oil"
]
DB["UK100"]=[
 "53",
 "NEUT",
 "BoE Pause + Oil 82 + FTSE + COT +12K Long",
 "DXY 71 + Yield 4.2 + UK PMI",
 "VIX + SP500 + CPI"
]
MP={
 "EURUSD":"EURUSD=X",
 "GBPUSD":"GBPUSD=X",
 "USDJPY":"USDJPY=X",
 "XAUUSD":"GC=F",
 "XAGUSD":"SI=F",
 "USDCAD":"USDCAD=X",
 "USDCHF":"USDCHF=X",
 "OILWTI":"CL=F",
 "BTCUSD":"BTC-USD",
 "US30":"^DJI",
 "NAS100":"^IXIC",
 "SP500":"^GSPC",
 "GER30":"^GDAXI",
 "UK100":"^FTSE",
 "DXY":"DX-Y.NYB"
}
GR={
 "forex":["EURUSD","GBPUSD","USDJPY","USDCAD","USDCHF","DXY"],
 "commods":["XAUUSD","XAGUSD","OILWTI"],
 "crypto":["BTCUSD"],
 "indices":["US30","NAS100","SP500","GER30","UK100","DXY"]
}
def gauge(d,n):
 col="#22C55E" if d[1]=="BULL" else "#FF2A2A" if d[1]=="BEAR" else "#FFD60A"
 a="<div class='macro-card'>"
 b="<div style='color:#9AA0B3;font-size:11px'>"+n+" MACRO</div>"
 c="<div style='color:"+col+";font-weight:900;font-size:18px'>"+d[1]+" "+d[0]+"/100</div>"
 d1="<div class='why' style='color:#22C55E;margin-top:8px'><b>Bull:</b> "+d[2]+"</div>"
 d2="<div class='why' style='color:#FF2A2A'><b>Bear:</b> "+d[3]+"</div>"
 d3="<div class='why' style='color:#6B7280'><b>Neu:</b> "+d[4]+"</div></div>"
 return a+b+c+d1+d2+d3
if "page" not in st.session_state:
 st.session_state.page="home"
def show(lst,head):
 st.markdown("## "+head)
 for name in lst:
  d=DB[name]
  t=MP.get(name)
  try:
   df=yf.Ticker(t).history(period="1d",interval="5m")
   daily=yf.Ticker(t).history(period="5d")
   p=daily['Close'].iloc[-1]
   pc=(daily['Close'].iloc[-1]-daily['Close'].iloc[-2])/daily['Close'].iloc[-2]*100
  except:
   df=pd.DataFrame({"Close":[1]*40})
   p=0
   pc=0
  lab=d[1]+" "+name+" "+str(round(p,2))+" ("+str(round(pc,2))+"%) "+d[0]
  with st.expander(lab):
   st.line_chart(df['Close'],height=90)
   st.markdown(gauge(d,name),unsafe_allow_html=True)
if st.session_state.page=="home":
 st.markdown("### DXY KING 71 BULLISH - FULL WHY")
 st.markdown(gauge(DB["DXY"],"DXY"),unsafe_allow_html=True)
 st.markdown("### 6 PREDATOR SYSTEMS")
 c1,c2=st.columns(2)
 with c1:
  if st.button("FOREX 6 PAIRS"):
   st.session_state.page="forex"
   st.rerun()
  if st.button("INDICES HUNT"):
   st.session_state.page="indices"
   st.rerun()
  if st.button("INTEL NEWS"):
   st.session_state.page="news"
   st.rerun()
 with c2:
  if st.button("GOLD OIL TRAP"):
   st.session_state.page="commods"
   st.rerun()
  if st.button("CRYPTO AMBUSH"):
   st.session_state.page="crypto"
   st.rerun()
  if st.button("COT TABLE 12"):
   st.session_state.page="cot"
   st.rerun()
else:
 if st.button("BACK RADAR"):
  st.session_state.page="home"
  st.rerun()
 if st.session_state.page=="forex":
  show(GR["forex"],"FOREX AMBUSH DXY KING")
 if st.session_state.page=="commods":
  show(GR["commods"],"COMMODITIES TRAP")
 if st.session_state.page=="crypto":
  show(GR["crypto"],"CRYPTO AMBUSH")
 if st.session_state.page=="indices":
  show(GR["indices"],"INDICES HUNT")
 if st.session_state.page=="news":
  st.markdown("## INTEL NEWS")
  st.markdown("<div class='macro-card'>DXY 104.5 BULL 71 Fed hawk EUR BEAR 39 GOLD 82 TOP TRAP OIL 68 BULL</div>",unsafe_allow_html=True)
 if st.session_state.page=="cot":
  st.markdown("## COT FULL 12 PAIRS WITH DXY - TABLE")
  rows=[]
  rows.append(["DXY 71","62 SHORT SQZ","98K Long Most Bull 6M","BULL KING"])
  rows.append(["XAU 39","82 LONG TOP","-28K Cut +19K Short","BEAR"])
  rows.append(["XAG 44","76 LONG TRAP","-12K Cut +22K Short","BEAR"])
  rows.append(["US30 48","60 LONG","15K Long +32K Asset","NEUTRAL"])
  rows.append(["NAS100 45","64 LONG TRAP","-18K Selloff","BEAR"])
  rows.append(["SP500 50","60 LONG","Flat Hedged","NEUTRAL"])
  rows.append(["GER30 44","55 LONG","-18K Short DAX","BEAR"])
  rows.append(["UK100 53","52 LONG","12K Long FTSE","NEUTRAL"])
  rows.append(["EURUSD 39","68 LONG TRAP","-125K Short EUR","BEAR"])
  rows.append(["GBPUSD 42","65 LONG TRAP","-89K Short GBP","BEAR"])
  rows.append(["USDJPY 72","71 SHORT SQZ","148K Long DXY","BULL"])
  rows.append(["OIL 68","58 SHORT SQZ","112K Long OPEC","BULL"])
  df=pd.DataFrame(rows,columns=["PAIR","RETAIL","SMART MONEY","BIAS"])
  st.dataframe(df,use_container_width=True,hide_index=True)
if st.button("RE-SCAN"):
 st.rerun()

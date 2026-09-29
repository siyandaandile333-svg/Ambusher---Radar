import streamlit as st
import yfinance as yf
import pandas as pd, pytz
from datetime import datetime
st.set_page_config(layout="wide")
st.markdown("<style>.stApp{background:#070709;color:#E8E6D9}.macro-card{background:#101018;border:1px solid #2A2A3A;border-radius:18px;padding:16px;margin:10px 0}</style>", unsafe_allow_html=True)
try:
 st.image("IMG-20260929-WA1810.jpg",width=340)
except:
 st.markdown("<h1 style='color:#FFD60A;text-align:center'>FX AMBUSHERS</h1>", unsafe_allow_html=True)
sa=datetime.now(pytz.timezone('Africa/Johannesburg')).strftime("%H:%M SA")
st.markdown("<div style='background:#111;padding:6px;color:#FFD60A'>"+sa+" PREDATOR</div>", unsafe_allow_html=True)
DB={}
DB["DXY"]=["71","BULL","Fed Hawk Yield 4.2 COT 98K Long Bull 6M","Fed Cut Gold Risk On","GPR Oil BoJ"]
DB["EURUSD"]=["39","BEAR","GPR CB COT Longs Trap","DXY 71 Yield 4.2 Hawk","VIX SP500"]
DB["GBPUSD"]=["42","BEAR","UK Wage GPR Long Trap","DXY 71 BoE Dov","VIX Oil"]
DB["USDJPY"]=["72","BULL","DXY 71 Fed Hawk BoJ 148K Long","Intervention VIX","GPR SP500"]
DB["XAUUSD"]=["39","BEAR","GPR CB COT 82% Long TOP","DXY 71 Yield 4.2 Hawk","VIX GDX"]
DB["XAGUSD"]=["44","BEAR","GPR CB 76% Long Trap","DXY 71 Yield 4.2","VIX CPI"]
DB["USDCAD"]=["52","NEUT","DXY 71 Fed Hawk","Oil 82 OPEC Cut","VIX GPR"]
DB["USDCHF"]=["61","BULL","DXY 71 SNB Dovish","CHF Safe GPR","SP500 CPI"]
DB["OILWTI"]=["68","BULL","GPR OPEC Cut Draw","DXY 71 Hawk","VIX CPI"]
DB["BTCUSD"]=["54","NEUT","ETF GPR Halving","DXY 71 Bear","SP500 CPI"]
DB["US30"]=["48","NEUT","Fed Pause CB 15K","DXY 71 Yield VIX","CPI Gold"]
DB["NAS100"]=["45","BEAR","AI CB Long Trap","DXY 71 Yield VIX","SP500 CPI"]
DB["SP500"]=["50","NEUT","Fed Pause Buy","DXY 71 Yield VIX","CPI Oil"]
DB["GER30"]=["44","BEAR","ECB Dov GPR","DXY 71 PMI 44.2","SP500 CPI"]
DB["UK100"]=["53","NEUT","BoE Pause Oil 82","DXY 71 PMI","VIX CPI"]
MP={"EURUSD":"EURUSD=X","GBPUSD":"GBPUSD=X","USDJPY":"USDJPY=X","XAUUSD":"GC=F","XAGUSD":"SI=F","USDCAD":"USDCAD=X","USDCHF":"USDCHF=X","OILWTI":"CL=F","BTCUSD":"BTC-USD","US30":"^DJI","NAS100":"^IXIC","SP500":"^GSPC","GER30":"^GDAXI","UK100":"^FTSE","DXY":"DX-Y.NYB"}
GR={"forex":["EURUSD","GBPUSD","USDJPY","USDCAD","USDCHF","DXY"],"commods":["XAUUSD","XAGUSD","OILWTI"],"crypto":["BTCUSD"],"indices":["US30","NAS100","SP500","GER30","UK100","DXY"]}
def gauge(d,n):
 c="#22C55E" if d[1]=="BULL" else "#FF2A2A" if d[1]=="BEAR" else "#FFD60A"
 a="<div class='macro-card'><center style='color:#9AA0B3'>"+n+"</center>"
 b="<center><span style='color:"+c+";font-weight:900'>"+d[1]+" "+d[0]+"/100</span></center>"
 cc="<div style='font-size:11px'><div style='color:#22C55E'>Bull: "+d[2]+"</div>"
 dd="<div style='color:#FF2A2A'>Bear: "+d[3]+"</div>"
 ee="<div style='color:#6B7280'>Neu: "+d[4]+"</div></div></div>"
 return a+b+cc+dd+ee
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
   pct=(daily['Close'].iloc[-2]-daily['Close'].iloc[-1])/daily['Close'].iloc[-2]*100
  except:
   df=pd.DataFrame({"Close":[1]*50})
   p=0
   pct=0
  label=d[1]+" "+name+" "+str(round(p,2))+" "+str(d[0])
  with st.expander(label,expanded=(name==lst[0])):
   st.line_chart(df['Close'],height=90)
   st.markdown(gauge(d,name),unsafe_allow_html=True)
if st.session_state.page=="home":
 st.markdown("### DXY KING 71 BULLISH")
 st.markdown(gauge(DB["DXY"],"DXY"),unsafe_allow_html=True)
 st.markdown("### 6 PREDATOR SYSTEMS")
 c1,c2=st.columns(2)
 with c1:
  if st.button("Forex Ambush 6 PAIRS incl DXY",use_container_width=True):
   st.session_state.page="forex"
   st.rerun()
  if st.button("Indices Hunt",use_container_width=True):
   st.session_state.page="indices"
   st.rerun()
  if st.button("Intel News",use_container_width=True):
   st.session_state.page="news"
   st.rerun()
 with c2:
  if st.button("Commodities Trap",use_container_width=True):
   st.session_state.page="commods"
   st.rerun()
  if st.button("Crypto Ambush",use_container_width=True):
   st.session_state.page="crypto"
   st.rerun()
  if st.button("COT FULL 12 PAIRS TABLE",use_container_width=True):
   st.session_state.page="cot"
   st.rerun()
else:
 if st.button("RETURN TO

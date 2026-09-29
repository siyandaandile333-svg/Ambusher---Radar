import streamlit as st
import yfinance as yf
import pandas as pd
import pytz
from datetime import datetime
st.set_page_config(layout="wide")
st.markdown("<style>.stApp{background:#070709;color:#E8E6D9}.macro-card{background:#101018;border:1px solid #2A2A3A;border-radius:12px;padding:12px}</style>", unsafe_allow_html=True)
try:
 st.image("IMG-20260929-WA1810.jpg",width=320)
except:
 st.markdown("<h2 style='color:#FFD60A'>FX AMBUSHERS</h2>", unsafe_allow_html=True)
DB={}
DB["DXY"]=["71","BULL","Fed Hawk 4.2 COT 98K","Fed Cut Gold","GPR Oil"]
DB["EURUSD"]=["39","BEAR","GPR CB COT","DXY 71 4.2","VIX"]
DB["GBPUSD"]=["42","BEAR","UK Wage GPR","DXY BoE","VIX"]
DB["USDJPY"]=["72","BULL","DXY BoJ 148K","Interv","GPR"]
DB["XAUUSD"]=["39","BEAR","GPR CB 82% TOP","DXY 71","VIX"]
DB["XAGUSD"]=["44","BEAR","GPR 76% Trap","DXY 71","VIX"]
DB["USDCAD"]=["52","NEUT","DXY Fed","Oil 82","VIX"]
DB["USDCHF"]=["61","BULL","DXY SNB","Safe GPR","SP500"]
DB["OILWTI"]=["68","BULL","OPEC Cut","DXY Hawk","VIX"]
DB["BTCUSD"]=["54","NEUT","ETF Halv","DXY Bear","SP500"]
DB["US30"]=["48","NEUT","Fed Pause","DXY VIX","CPI"]
DB["NAS100"]=["45","BEAR","AI CB","DXY VIX","SP500"]
DB["SP500"]=["50","NEUT","Fed Buy","DXY VIX","CPI"]
DB["GER30"]=["44","BEAR","ECB Dov","DXY PMI","SP500"]
DB["UK100"]=["53","NEUT","BoE Oil","DXY PMI","VIX"]
MP={"EURUSD":"EURUSD=X","GBPUSD":"GBPUSD=X","USDJPY":"USDJPY=X","XAUUSD":"GC=F","XAGUSD":"SI=F","USDCAD":"USDCAD=X","USDCHF":"USDCHF=X","OILWTI":"CL=F","BTCUSD":"BTC-USD","US30":"^DJI","NAS100":"^IXIC","SP500":"^GSPC","GER30":"^GDAXI","UK100":"^FTSE","DXY":"DX-Y.NYB"}
GR={"forex":["EURUSD","GBPUSD","USDJPY","USDCAD","USDCHF","DXY"],"commods":["XAUUSD","XAGUSD","OILWTI"],"crypto":["BTCUSD"],"indices":["US30","NAS100","SP500","GER30","UK100","DXY"]}
def gauge(d,n):
 c="#22C55E" if d[1]=="BULL" else "#FF2A2A" if d[1]=="BEAR" else "#FFD60A"
 a="<div class='macro-card'>"+n+" "+d[1]+" "+d[0]+"/100<br>"
 b="Bull:"+d[2]+"<br>Bear:"+d[3]+"<br>Neu:"+d[4]+"</div>"
 return a+b
if "page" not in st.session_state:
 st.session_state.page="home"
def show(lst,head):
 st.markdown("## "+head)
 for name in lst:
  d=DB[name]
  t=MP.get(name)
  try:
   df=yf.Ticker(t).history(period="1d",interval="5m")
   p=yf.Ticker(t).history(period="5d")['Close'].iloc[-1]
  except:
   df=pd.DataFrame({"Close":[1]*30})
   p=0
  lab=d[1]+" "+name+" "+str(int(p))+" "+d[0]
  with st.expander(lab):
   st.line_chart(df['Close'],height=80)
   st.markdown(gauge(d,name),unsafe_allow_html=True)
if st.session_state.page=="home":
 st.markdown("### DXY 71 BULL")
 st.markdown(gauge(DB["DXY"],"DXY"),unsafe_allow_html=True)
 st.markdown("### 6 SYSTEMS")
 c1,c2=st.columns(2)
 with c1:
  if st.button("FOREX"):
   st.session_state.page="forex"
   st.rerun()
  if st.button("INDICES"):
   st.session_state.page="indices"
   st.rerun()
  if st.button("NEWS"):
   st.session_state.page="news"
   st.rerun()
 with c2:
  if st.button("GOLD OIL"):
   st.session_state.page="commods"
   st.rerun()
  if st.button("CRYPTO"):
   st.session_state.page="crypto"
   st.rerun()
  if st.button("COT TABLE"):
   st.session_state.page="cot"
   st.rerun()
else:
 if st.button("BACK"):
  st.session_state.page="home"
  st.rerun()
 if st.session_state.page=="forex":
  show(GR["forex"],"FOREX")
 if st.session_state.page=="commods":
  show(GR["commods"],"GOLD OIL")
 if st.session_state.page=="crypto":
  show(GR["crypto"],"CRYPTO")
 if st.session_state.page=="indices":
  show(GR["indices"],"INDICES")
 if st.session_state.page=="news":
  st.markdown("## NEWS")
  st.markdown("<div class='macro-card'>DXY 104.5 BULL 71 Fed hawk EUR BEAR 39 GOLD 82 TOP</div>",unsafe_allow_html=True)
 if st.session_state.page=="cot":
  st.markdown("## COT TABLE")
  d=[]
  d.append(["DXY 71","62 SHORT","98K Long","BULL"])
  d.append(["XAU 39","82 LONG TOP","-28K +19K S","BEAR"])
  d.append(["XAG 44","76 LONG","-12K +22K S","BEAR"])
  d.append(["US30 48","60 LONG","15K +32K","NEUT"])
  d.append(["NAS100 45","64 LONG","-18K Sell","BEAR"])
  d.append(["SP500 50","60 LONG","Flat","NEUT"])
  d.append(["GER30 44","55 LONG","-18K DAX","BEAR"])
  d.append(["UK100 53","52 LONG","12K FTSE","NEUT"])
  d.append(["EUR 39","68 LONG","-125K EUR","BEAR"])
  d.append(["GBP 42","65 LONG","-89K GBP","BEAR"])
  d.append(["JPY 72","71 SHORT","148K Long","BULL"])
  d.append(["OIL 68","58 SHORT","112K OPEC","BULL"])
  df=pd.DataFrame(d,columns=["PAIR","RETAIL","SMART","BIAS"])
  st.dataframe(df,hide_index=True,use_container_width=True)
if st.button("SCAN"):
 st.rerun()

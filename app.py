import streamlit as st, yfinance as yf, pandas as pd, pytz
from datetime import datetime
st.set_page_config(layout="wide")
st.markdown("<style>.stApp{background:#070709;color:#E8E6D9}.macro-card{background:#101018;border:1px solid #2A2A3A;border-radius:18px;padding:16px;margin:10px 0}</style>", unsafe_allow_html=True)
try: st.image("IMG-20260929-WA1810.jpg", width=340)
except: st.markdown("<h1 style='color:#FFD60A;text-align:center'>FX AMBUSHERS</h1>", unsafe_allow_html=True)
sa=datetime.now(pytz.timezone('Africa/Johannesburg')).strftime("%H:%M SA")
st.markdown("<div style='background:#111;padding:6px;color:#FFD60A'>"+sa+" PREDATOR MODE</div>", unsafe_allow_html=True)
# FULL WHY'S - LONG VERSION NOW SAFE
DB={}
DB["DXY"]=["71","BULL","Fed Hawkish + Real Yield 4.2% + COT 98K Long Most Bull 6M","Fed Cut + SP500 + Gold Risk On","GPR + Oil + BoJ Intervention"]
DB["EURUSD"]=["39","BEAR","GPR + CB Buying + COT Longs Trap","DXY 71 + Yield 4.2 + Fed Hawk + COT -125K Short EUR","VIX + SP500 + CPI"]
DB["GBPUSD"]=["42","BEAR","UK Wage + GPR + COT Longs Trap","DXY 71 + BoE Dovish + CPI Low + COT -89K Short GBP","VIX + Oil + Fed"]
DB["USDJPY"]=["72","BULL","DXY 71 + Fed Hawk + BoJ Dovish + COT 148K Long","Intervention Risk + VIX Safe Haven","GPR + SP500 + CPI"]
DB["XAUUSD"]=["39","BEAR","GPR + CB Buying + COT Longs 82% TOP Trap","DXY 71 + Yield 4.2 + Fed Hawk + COT -28K Cut +19K Short","VIX + SP500 + GDX"]
DB["XAGUSD"]=["44","BEAR","GPR + Industry + CB + COT 76% Long Trap","DXY 71 + Yield 4.2 + Fed Hawk + COT -12K +22K Short","VIX + CPI + Oil"]
DB["USDCAD"]=["52","NEUT","DXY 71 + Fed Hawk + CPI + Yield","Oil 82 + OPEC Cut + CB Buy CAD","VIX + SP500 + GPR"]
DB["USDCHF"]=["61","BULL","DXY 71 + SNB Dovish + Yield + COT 98K","CHF Safe + GPR + Gold Fear","SP500 + CPI + Oil"]
DB["OILWTI"]=["68","BULL","GPR + OPEC Cut + Inventory Draw","DXY 71 + Fed Hawk + Yield 4.2","VIX + CPI + Gold"]
DB["BTCUSD"]=["54","NEUT","ETF Inflow + GPR + CB + Halving","DXY 71 + Bear BTC + Yield 4.2","SP500 + CPI + Gold"]
DB["US30"]=["48","NEUT","Fed Pause + CB Earnings + COT 15K Long +32K Asset","DXY 71 + Yield 4.2 + VIX + Oil","CPI + Gold + SP500"]
DB["NAS100"]=["45","BEAR","AI Demand + CB + COT Longs Trap","DXY 71 + Yield 4.2 + Fed + VIX","SP500 + CPI + Oil"]
DB["SP500"]=["50","NEUT","Fed Pause + Buybacks + Earnings","DXY 71 + Yield 4.2 + VIX","CPI + Oil + Gold"]
DB["GER30"]=["44","BEAR","ECB Dovish + GPR + CB","DXY 71 + Yield 4.2 + PMI 44.2","SP500 + CPI + Oil"]
DB["UK100"]=["53","NEUT","BoE Pause + Oil 82 + FTSE + COT +12K Long","DXY 71 + Yield 4.2 + UK PMI","VIX + SP500 + CPI"]
MP={"EURUSD":"EURUSD=X","GBPUSD":"GBPUSD=X","USDJPY":"USDJPY=X","XAUUSD":"GC=F","XAGUSD":"SI=F","USDCAD":"USDCAD=X","USDCHF":"USDCHF=X","OILWTI":"CL=F","BTCUSD":"BTC-USD","US30":"^DJI","NAS100":"^IXIC","SP500":"^GSPC","GER30":"^GDAXI","UK100":"^FTSE","DXY":"DX-Y.NYB"}
GR={"forex":["EURUSD","GBPUSD","USDJPY","USDCAD","USDCHF","DXY"],"commods":["XAUUSD","XAGUSD","OILWTI"],"crypto":["BTCUSD"],"indices":["US30","NAS100","SP500","GER30","UK100","DXY"]}
def gauge(d,n):
 c="#22C55E" if d[1]=="BULL" else "#FF2A2A" if d[1]=="BEAR" else "#FFD60A"
 h="<div class='macro-card'><center style='color:#9AA0B3'>"+n+" MACRO</center>"
 h+="<center><span style='color:"+c+";font-weight:900;font-size:20px'>"+d[1]+" "+d[0]+"/100</span></center>"
 h+="<div style='font-size:11px;margin-top:10px'><div style='color:#22C55E'><b>Bull:</b> "+d[2]+"</div>"
 h+="<div style='color:#FF2A2A;margin-top:6px'><b>Bear:</b> "+d[3]+"</div>"
 h+="<div style='color:#6B7280;margin-top:6px'><b>Neu:</b> "+d[4]+"</div></div></div>"
 return h
if "page" not in st.session_state: st.session_state.page="home"
def show(lst,head):
 st.markdown("## "+head)
 for name in lst:
  d=DB[name]; t=MP.get(name)
  try: df=yf.Ticker(t).history(period="1d",interval="5m"); daily=yf.Ticker(t).history(period="5d"); p=daily['Close'].iloc[-1]; pct=(daily['Close'].iloc[-1]-daily['Close'].iloc[-2])/daily['Close'].iloc[-2]*100
  except: df=pd.DataFrame({"Close":[1]*50}); p=0; pct=0
  label=d[1]+" "+name+" "+str(round(p,2))+" ("+str(round(pct,2))+"%) "+d[0]
  with st.expander(label, expanded=(name==lst[0])): st.line_chart(df['Close'],height=90); st.markdown(gauge(d,name),unsafe_allow_html=True)
if st.session_state.page=="home":
 st.markdown("### DXY KING 71 BULLISH - FULL WHY BOX")
 st.markdown(gauge(DB["DXY"],"DXY"),unsafe_allow_html=True)
 st.markdown("### 6 PREDATOR SYSTEMS - 2 COLUMNS")
 c1,c2=st.columns(2)
 with c1:
  if st.button("Forex Ambush 6 PAIRS incl DXY",use_container_width=True): st.session_state.page="forex"; st.rerun()
  if st.button("Indices Hunt US30 NAS100 SP500 GER30 UK100 DXY",use_container_width=True): st.session_state.page="indices"; st.rerun()
  if st.button("Intel News",use_container_width=True): st.session_state.page="news"; st.rerun()
 with c2:
  if st.button("Commodities Trap GOLD SILVER OIL",use_container_width=True): st.session_state.page="commods"; st.rerun()
  if st.button("Crypto Ambush",use_container_width=True): st.session_state.page="crypto"; st.rerun()
  if st.button("COT FULL 12 PAIRS WITH DXY - TABLE",use_container_width=True): st.session_state.page="cot"; st.rerun()
else:
 if st.button("RETURN TO RADAR"): st.session_state.page="home"; st.rerun()
 if st.session_state.page=="forex": show(GR["forex"],"FOREX AMBUSH DXY KING")
 if st.session_state.page=="commods": show(GR["commods"],"COMMODITIES TRAP")
 if st.session_state.page=="crypto": show(GR["crypto"],"CRYPTO AMBUSH")
 if st.session_state.page=="indices": show(GR["indices"],"INDICES HUNT")
 if st.session_state.page=="news": st.markdown("## INTEL NEWS"); st.markdown("<div class='macro-card

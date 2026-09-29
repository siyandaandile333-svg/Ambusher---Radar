import streamlit as st, yfinance as yf, pandas as pd, pytz
from datetime import datetime
st.set_page_config(layout="wide")
st.markdown("<style>.stApp{background:#070709;color:#E8E6D9}.macro-card{background:#101018;border:1px solid #2A2A3A;border-radius:18px;padding:16px;margin:10px 0}</style>", unsafe_allow_html=True)
try: st.image("IMG-20260929-WA1810.jpg", width=340)
except: st.markdown("<h1 style='color:#FFD60A;text-align:center'>FX AMBUSHERS</h1>", unsafe_allow_html=True)
sa=datetime.now(pytz.timezone('Africa/Johannesburg')).strftime("%H:%M SA")
st.markdown("<div style='background:#111;padding:6px;color:#FFD60A'>"+sa+" PREDATOR MODE</div>", unsafe_allow_html=True)
DB={}
DB["DXY"]=[71,"BULL","Fed Hawk 4.2 COT 98K","Fed Cut Gold","GPR Oil"]
DB["EURUSD"]=[39,"BEAR","GPR CB COT","DXY 71 Yield 4.2","VIX SP500"]
DB["GBPUSD"]=[42,"BEAR","UK Wage GPR","DXY 71 BoE Dov","VIX Oil"]
DB["USDJPY"]=[72,"BULL","DXY 71 Fed BoJ 148K","Intervent VIX","GPR SP500"]
DB["XAUUSD"]=[39,"BEAR","GPR CB COT","DXY 71 Yield 4.2","VIX GDX"]
DB["XAGUSD"]=[44,"BEAR","GPR CB COT","DXY 71 Yield 4.2","VIX CPI"]
DB["USDCAD"]=[52,"NEUT","DXY 71 Fed Hawk","Oil 82 OPEC","VIX GPR"]
DB["USDCHF"]=[61,"BULL","DXY 71 SNB Dov","CHF Safe GPR","SP500 CPI"]
DB["OILWTI"]=[68,"BULL","GPR OPEC Cut Draw","DXY 71 Hawk","VIX CPI"]
DB["BTCUSD"]=[54,"NEUT","ETF GPR Halving","DXY 71 Bear","SP500 CPI"]
DB["US30"]=[48,"NEUT","Fed Pause CB 15K","DXY 71 Yield VIX","CPI Gold"]
DB["NAS100"]=[45,"BEAR","AI CB COT","DXY 71 Yield VIX","SP500 CPI"]
DB["SP500"]=[50,"NEUT","Fed Pause Buy","DXY 71 Yield VIX","CPI Oil"]
DB["GER30"]=[44,"BEAR","ECB Dov GPR","DXY 71 PMI 44.2","SP500 CPI"]
DB["UK100"]=[53,"NEUT","BoE Pause Oil 82","DXY 71 PMI","VIX CPI"]
MP={"EURUSD":"EURUSD=X","GBPUSD":"GBPUSD=X","USDJPY":"USDJPY=X","XAUUSD":"GC=F","XAGUSD":"SI=F","USDCAD":"USDCAD=X","USDCHF":"USDCHF=X","OILWTI":"CL=F","BTCUSD":"BTC-USD","US30":"^DJI","NAS100":"^IXIC","SP500":"^GSPC","GER30":"^GDAXI","UK100":"^FTSE","DXY":"DX-Y.NYB"}
GR={"forex":["EURUSD","GBPUSD","USDJPY","USDCAD","USDCHF","DXY"],"commods":["XAUUSD","XAGUSD","OILWTI"],"crypto":["BTCUSD"],"indices":["US30","NAS100","SP500","GER30","UK100","DXY"]}
def gauge(d,n):
 c="#22C55E" if d[1]=="BULL" else "#FF2A2A" if d[1]=="BEAR" else "#FFD60A"
 html="<div class='macro-card'><center style='color:#9AA0B3'>"+n+" MACRO</center><center><span style='color:"+c+";font-weight:900'>"+d[1]+" "+str(d[0])+"/100</span></center><div style='font-size:11px'><div style='color:#22C55E'>Bull: "+d[2]+"</div><div style='color:#FF2A2A'>Bear: "+d[3]+"</div><div style='color:#6B7280'>Neu: "+d[4]+"</div></div></div>"
 return html
if "page" not in st.session_state: st.session_state.page="home"
def show(lst,head):
 st.markdown("## "+head)
 for name in lst:
  d=DB[name]; t=MP.get(name)
  try: df=yf.Ticker(t).history(period="1d",interval="5m"); daily=yf.Ticker(t).history(period="5d"); p=daily['Close'].iloc[-1]; pct=(daily['Close'].iloc[-1]-daily['Close'].iloc[-2])/daily['Close'].iloc[-2]*100
  except: df=pd.DataFrame({"Close":[1]*50}); p=0; pct=0
  label=d[1]+" "+name+" "+str(round(p,2))+" ("+str(round(pct,2))+"%) "+str(d[0])
  with st.expander(label, expanded=(name==lst[0])): st.line_chart(df['Close'],height=90); st.markdown(gauge(d,name),unsafe_allow_html=True)
if st.session_state.page=="home":
 st.markdown("### DXY KING 71 BULLISH - WHY BOX")
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
  if st.button("COT FULL 12 PAIRS WITH DXY",use_container_width=True): st.session_state.page="cot"; st.rerun()
else:
 if st.button("RETURN TO RADAR"): st.session_state.page="home"; st.rerun()
 if st.session_state.page=="forex": show(GR["forex"],"FOREX AMBUSH DXY KING")
 if st.session_state.page=="commods": show(GR["commods"],"COMMODITIES TRAP")
 if st.session_state.page=="crypto": show(GR["crypto"],"CRYPTO AMBUSH")
 if st.session_state.page=="indices": show(GR["indices"],"INDICES HUNT")
 if st.session_state.page=="news": st.markdown("## INTEL NEWS"); st.markdown("<div class='macro-card'>DXY 104.5 BULL 71 Fed hawk EUR BEAR 39 GOLD TRAP 82 OIL BULL 68</div>",unsafe_allow_html=True)
 if st.session_state.page=="cot": st.markdown("## COT FULL WITH DXY"); st.markdown("<div class='macro-card' style='font-size:11px'>DXY 71 BULL KING +98K Long | XAU 39 BEAR 82 LONG TOP -28K | XAG 44 BEAR 76 TRAP -12K | US30 48 NEUT +15K | NAS100 45 BEAR -18K | SP500 50 NEUT Flat | GER30 44 BEAR -18K DAX | UK100 53 NEUT +12K | EURUSD 39 BEAR -125K Short | GBPUSD 42 BEAR -89K Short | USDJPY 72 BULL +148K | OIL 68 BULL +112K OPEC</div>",unsafe_allow_html=True)
if st.button("RE-SCAN"): st.rerun()

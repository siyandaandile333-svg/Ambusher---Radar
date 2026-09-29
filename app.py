import streamlit as st,yfinance as yf,pandas as pd,pytz
from datetime import datetime
st.set_page_config(layout="wide")
DB={}
DB["DXY"]=[71,"BULL","Fed Hawk 98K","Fed Cut","GPR"]
DB["EURUSD"]=[39,"BEAR","GPR CB","DXY 71","VIX"]
DB["GBPUSD"]=[42,"BEAR","UK Wage","DXY BoE","VIX"]
DB["USDJPY"]=[72,"BULL","DXY BoJ 148K","Intervent","GPR"]
DB["XAUUSD"]=[39,"BEAR","GPR CB","DXY 71","VIX"]
DB["XAGUSD"]=[44,"BEAR","GPR CB","DXY 71","VIX"]
DB["USDCAD"]=[52,"NEUT","DXY Fed","Oil 82","VIX"]
DB["USDCHF"]=[61,"BULL","DXY SNB","CHF Safe","SP500"]
DB["OILWTI"]=[68,"BULL","OPEC Cut","DXY Hawk","VIX"]
DB["BTCUSD"]=[54,"NEUT","ETF Halv","DXY Bear","SP500"]
DB["US30"]=[48,"NEUT","Fed Pause","DXY VIX","CPI"]
DB["NAS100"]=[45,"BEAR","AI CB","DXY VIX","SP500"]
DB["SP500"]=[50,"NEUT","Fed Buy","DXY VIX","CPI"]
DB["GER30"]=[44,"BEAR","ECB Dov","DXY PMI","SP500"]
DB["UK100"]=[53,"NEUT","BoE Oil","DXY PMI","VIX"]
MP={"EURUSD":"EURUSD=X","GBPUSD":"GBPUSD=X","USDJPY":"USDJPY=X","XAUUSD":"GC=F","XAGUSD":"SI=F","USDCAD":"USDCAD=X","USDCHF":"USDCHF=X","OILWTI":"CL=F","BTCUSD":"BTC-USD","US30":"^DJI","NAS100":"^IXIC","SP500":"^GSPC","GER30":"^GDAXI","UK100":"^FTSE","DXY":"DX-Y.NYB"}
GR={"forex":["EURUSD","GBPUSD","USDJPY","USDCAD","USDCHF","DXY"],"commods":["XAUUSD","XAGUSD","OILWTI"],"crypto":["BTCUSD"],"indices":["US30","NAS100","SP500","GER30","UK100","DXY"]}
def gauge(d,n):
 c="#22C55E" if d[1]=="BULL" else "#FF2A2A" if d[1]=="BEAR" else "#FFD60A"
 return f"<div style='background:#101018;border:1px solid #2A2A3A;border-radius:18px;padding:16px;margin:10px 0'><center style='color:#9AA0B3'>{n}</center><center><span style='color:{c};font-weight:900'>{d[1]} {d[0]}/100</span></center><div style='font-size:11px'><div style='color:#22C55E'>Bull:{d[2]}</div><div style='color:#FF2A2A'>Bear:{d[3]}</div><div style='color:#6B7280'>Neu:{d[4]}</div></div></div>"
if "page" not in st.session_state: st.session_state.page="home"
def show(lst,head):
 st.markdown(f"## {head}")
 for name in lst:
  d=DB[name];t=MP.get(name)
  try: df=yf.Ticker(t).history(period="1d",interval="5m");daily=yf.Ticker(t).history(period="5d");p=daily['Close'].iloc[-1];pct=(daily['Close'].iloc[-1]-daily['Close'].iloc[-2])/daily['Close'].iloc[-2]*100
  except: df=pd.DataFrame({"Close":[1]*50});p=0;pct=0
  label=f"{d[1]} {name} {p:.2f} ({pct:+.2f}%) {d[0]}"
  with st.expander(label,expanded=(name==lst[0])): st.line_chart(df['Close'],height=90);st.markdown(gauge(d,name),unsafe_allow_html=True)
if st.session_state.page=="home":
 st.markdown("### DXY KING 71 BULLISH");st.markdown(gauge(DB["DXY"],"DXY"),unsafe_allow_html=True)
 st.markdown("### 6 PREDATOR SYSTEMS")
 if st.button("Forex Ambush 6 PAIRS incl DXY",use_container_width=True): st.session_state.page="forex";st.rerun()
 if st.button("Commodities Trap GOLD SILVER OIL",use_container_width=True): st.session_state.page="commods";st.rerun()
 if st.button("Indices Hunt US30 NAS100 SP500 GER30 UK100 DXY",use_container_width=True): st.session_state.page="indices";st.rerun()
 if st.button("Crypto Ambush",use_container_width=True): st.session_state.page="crypto";st.rerun()
 if st.button("Intel News",use_container_width=True): st.session_state.page="news";st.rerun()
 if st.button("COT FULL 12 PAIRS WITH DXY",use_container_width=True): st.session_state.page="cot";st.rerun()
else:
 if st.button("RETURN TO RADAR"): st.session_state.page="home";st.rerun()
 if st.session_state.page=="forex": show(GR["forex"],"FOREX AMBUSH DXY KING")
 if st.session_state.page=="commods": show(GR["commods"],"COMMODITIES TRAP")
 if st.session_state.page=="crypto": show(GR["crypto"],"CRYPTO AMBUSH")
 if st.session_state.page=="indices": show(GR["indices"],"INDICES HUNT")
 if st.session_state.page=="news": st.markdown("## INTEL NEWS");st.markdown("<div style='background:#101018;padding:12px'>DXY 104.5 BULL 71 Fed hawk EUR BEAR 39 GOLD TRAP 82 OIL BULL 68</div>",unsafe_allow_html=True)
 if st.session_state.page=="cot":
  st.markdown("## COT FULL WITH DXY")
  st.markdown("<div style='background:#101018;padding:8px;font-size:11px'>DXY 71 BULL KING +98K Long | XAU 39 BEAR 82 LONG TOP | XAG 44 BEAR 76 TRAP | US30 48 NEUT +15K | NAS100 45 BEAR -18K | SP500 50 NEUT Flat | GER30 44 BEAR -18K DAX | UK100 53 NEUT +12K | EURUSD 39 BEAR -125K Short | GBPUSD 42 BEAR -89K Short | USDJPY 72 BULL +148K | OIL 68 BULL +112K OPEC</div>",unsafe_allow_html=True)
if st.button("RE-SCAN"): st.rerun()

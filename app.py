import streamlit as st
import yfinance as yf
import pandas as pd
import pytz
from datetime import datetime
st.set_page_config(layout="wide")
st.markdown("<style>.stApp{background:#070709;color:#E8E6D9}.macro-card{background:#101018;border:1px solid #2A2A3A;border-radius:18px;padding:16px;margin:10px 0}.circle{width:80px;height:80px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-direction:column;font-weight:900}.why-box{background:#0F0F1A;border:1px solid #2A2A3A;border-radius:12px;padding:12px;font-size:11px}.cot-table{width:100%;border-collapse:collapse;font-size:11px}.cot-table th{background:#1A1A2E;padding:8px;color:#FFD60A;text-align:left}.cot-table td{padding:8px;border-bottom:1px solid #222}</style>", unsafe_allow_html=True)
try:
 st.image("IMG-20260929-WA1810.jpg",width=340)
except:
 st.markdown("<h2 style='color:#FFD60A;text-align:center'>FX AMBUSHERS</h2>",unsafe_allow_html=True)
st.markdown("<div style='text-align:center;color:#FFD60A;font-weight:900'>FX AMBUSHERS - MR SA DLAMINI</div>",unsafe_allow_html=True)
sa=datetime.now(pytz.timezone('Africa/Johannesburg')).strftime("%d %b %H:%M SA")
st.markdown(f"<div style='background:#111;border:1px solid #333;padding:6px 12px;font-size:11px'><span style='color:#FF2A2A'>PREDATOR MODE</span> <span style='color:#FFD60A'>{sa}</span></div><br>",unsafe_allow_html=True)
DB={}
DB["DXY"]={"s":71,"b":"BULLISH","bu":8,"be":3,"bf":"Fed Hawk Yield 4.2 CPI 3.7 COT 98K Long","rf":"Fed Cut SP500 Gold","n":"GPR Oil BoJ"}
DB["EURUSD"]={"s":39,"b":"BEARISH","bu":3,"be":6,"bf":"GPR CB COT Longs","rf":"DXY 71 Yield 4.2 Fed Hawk","n":"VIX SP500 CPI"}
DB["GBPUSD"]={"s":42,"b":"BEARISH","bu":4,"be":6,"bf":"UK Wage GPR COT Longs","rf":"DXY 71 BoE Dovish CPI Low","n":"VIX Oil Fed"}DB["USDJPY"]={"s":72,"b":"BULLISH","bu":8,"be":3,"bf":"DXY 71 Fed Hawk BoJ Dovish COT 148K","rf":"Intervention VIX Safe","n":"GPR SP500 CPI"}
DB["XAUUSD"]={"s":39,"b":"BEARISH","bu":3,"be":6,"bf":"GPR CB COT Longs","rf":"DXY 71 Yield 4.2 Fed Hawk","n":"VIX SP500 GDX"}
DB["XAGUSD"]={"s":44,"b":"BEARISH","bu":3,"be":6,"bf":"GPR Industry CB COT Longs","rf":"DXY 71 Yield 4.2 Fed Hawk","n":"VIX CPI Oil"}
DB["USDCAD"]={"s":52,"b":"NEUTRAL","bu":5,"be":5,"bf":"DXY 71 Fed Hawk CPI Yield","rf":"Oil 82 OPEC Cut CB Buy","n":"VIX SP500 GPR"}
DB["USDCHF"]={"s":61,"b":"BULLISH","bu":6,"be":3,"bf":"DXY 71 SNB Dovish Yield COT 98K","rf":"CHF Safe GPR Gold","n":"SP500 CPI Oil"}
DB["OILWTI"]={"s":68,"b":"BULLISH","bu":7,"be":3,"bf":"GPR OPEC Cut Inventory Draw","rf":"DXY 71 Fed Hawk Yield 4.2","n":"VIX CPI Gold"}
DB["BTCUSD"]={"s":54,"b":"NEUTRAL","bu":5,"be":4,"bf":"ETF Inflow GPR CB Halving","rf":"DXY 71 Bear BTC Yield 4.2","n":"SP500 CPI Gold"}
DB["US30"]={"s":48,"b":"NEUTRAL","bu":5,"be":5,"bf":"Fed Pause CB Earnings COT 15K","rf":"DXY 71 Yield 4.2 VIX Oil","n":"CPI Gold SP500"}
DB["NAS100"]={"s":45,"b":"BEARISH","bu":3,"be":6,"bf":"AI Demand CB COT Longs","rf":"DXY 71 Yield 4.2 Fed VIX","n":"SP500 CPI Oil"}
DB["SP500"]={"s":50,"b":"NEUTRAL","bu":5,"be":5,"bf":"Fed Pause Buybacks Earnings","rf":"DXY 71 Yield 4.2 VIX","n":"CPI Oil Gold"}
DB["GER30"]={"s":44,"b":"BEARISH","bu":3,"be":6,"bf":"ECB Dovish GPR CB","rf":"DXY 71 Yield 4.2 PMI 44.2","n":"SP500 CPI Oil"}
DB["UK100"]={"s":53,"b":"NEUTRAL","bu":5,"be":4,"bf":"BoE Pause Oil 82 FTSE","rf":"DXY 71 Yield 4.2 UK PMI","n":"VIX SP500 CPI"}
pairs_map={"EURUSD":"EURUSD=X","GBPUSD":"GBPUSD=X","USDJPY":"USDJPY=X","XAUUSD":"GC=F","XAGUSD":"SI=F","USDCAD":"USDCAD=X","USDCHF":"USDCHF=X","OILWTI":"CL=F","BTCUSD":"BTC-USD","US30":"^DJI","NAS100":"^IXIC","SP500":"^GSPC","GER30":"^GDAXI","UK100":"^FTSE","DXY":"DX-Y.NYB"}
GROUPS={"forex":["EURUSD","GBPUSD","USDJPY","USDCAD","USDCHF","DXY"],"commods":["XAUUSD","XAGUSD","OILWTI"],"crypto":["BTCUSD"],"indices":["US30","NAS100","SP500","GER30","UK100","DXY"]}
def gauge(d,name):
 c="#22C55E" if d["b"]=="BULLISH" else "#FF2A2A" if d["b"]=="BEARISH" else "#FFD60A"
 return f"<div class='macro-card'><div style='text-align:center;color:#9AA0B3;font-size:12px'>{name} MACRO</div><div style='text-align:center'><span style='color:{c};font-weight:900;font-size:18px'>{d['b']}</span></div><div style='display:flex;gap:12px;margin-top:10px'><div class='circle' style='border:4px solid #222;border-top:4px solid {c};border-right:4px solid {c}'><span style='color:{c};font-size:22px'>{d['s']}</span><span style='font-size:10px'>/100</span></div><div class='why-box'><div style='color:#22C55E'>Bull: {d['bf']}</div><div style='color:#FF2A2A;margin-top:4px'>Bear: {d['rf']}</div><div style='color:#6B7280;margin-top:4px'>Neutral: {d['n']}</div></div></div></div>"
if "page" not in st.session_state:
 st.session_state.page="home"def show_detail(lst, head):
 st.markdown(f"## {head}", unsafe_allow_html=True)
 for name in lst:
  d=DB[name]
  t=pairs_map.get(name)
  try:
   df=yf.Ticker(t).history(period="1d",interval="5m")
   daily=yf.Ticker(t).history(period="5d")
   p=daily['Close'].iloc[-1]
   pct=(daily['Close'].iloc[-1]-daily['Close'].iloc[-2])/daily['Close'].iloc[-2]*100
  except:
   df=pd.DataFrame({"Close":[1]*50});p=0;pct=0
  label=f"{d['b']} {name} | {p:.2f} ({pct:+.2f}%) SCORE {d['s']}"
  with st.expander(label, expanded=(name==lst[0])):
   st.line_chart(df['Close'], height=90)
   st.markdown(gauge(d,name), unsafe_allow_html=True)
if st.session_state.page=="home":
 st.markdown("### GEOPOLINTEL LIVE")
 st.markdown("<div style='background:#101A10;border-left:3px solid #22C55E;padding:8px;font-size:11px'>DXY 104.5 BULLISH 71 - Fed hawkish - Real Yield 4.2 = Gold Bearish</div>", unsafe_allow_html=True)
 st.markdown("### DXY KING 71 BULLISH - WHY BULLISH/BEARISH")
 st.markdown(gauge(DB["DXY"],"DXY"), unsafe_allow_html=True)
 st.markdown("### SELECT TARGET - 6 PREDATOR SYSTEMS")
 c1,c2=st.columns(2)
 with c1:
  if st.button("Forex Ambush - 6 PAIRS incl DXY - LOCK TARGET", use_container_width=True):
   st.session_state.page="forex";st.rerun()
  if st.button("Commodities Trap - GOLD SILVER OIL - LOCK TARGET", use_container_width=True):
   st.session_state.page="commods";st.rerun()
  if st.button("Intel News - LOCK TARGET", use_container_width=True):
   st.session_state.page="news";st.rerun()
 with c2:
  if st.button("Indices Hunt - US30 NAS100 SP500 GER30 UK100 DXY - LOCK TARGET", use_container_width=True):
   st.session_state.page="indices";st.rerun()
  if st.button("Crypto Ambush - LOCK TARGET", use_container_width=True):
   st.session_state.page="crypto";st.rerun()
  if st.button("Institutional COT - FULL WITH DXY - LOCK TARGET", use_container_width=True):
   st.session_state.page="cot";st.rerun()else:
 if st.button("RETURN TO RADAR"):
  st.session_state.page="home";st.rerun()
 if st.session_state.page=="forex":
  show_detail(GROUPS["forex"],"FOREX AMBUSH - DXY KING")
 elif st.session_state.page=="commods":
  show_detail(GROUPS["commods"],"COMMODITIES TRAP")
 elif st.session_state.page=="crypto":
  show_detail(GROUPS["crypto"],"CRYPTO AMBUSH")
 elif st.session_state.page=="indices":
  show_detail(GROUPS["indices"],"INDICES HUNT")
 elif st.session_state.page=="news":
  st.markdown("## INTEL NEWS", unsafe_allow_html=True)
  st.markdown("<div class='macro-card'>DXY 104.5 BULLISH 71 - Fed hawkish - EUR BEARISH 39 - GOLD TRAP 82 long - OIL BULLISH 68</div>", unsafe_allow_html=True)
 elif st.session_state.page=="cot":
  st.markdown("## COT INSTITUTIONAL REPORT - FULL - WITH DXY", unsafe_allow_html=True)
  st.markdown("<div class='macro-card'><table class='cot-table'><tr><th>PAIR</th><th>RETAIL</th><th>SMART MONEY</th><th>BIAS</th></tr><tr><td><b>DXY 71</b></td><td>62 SHORT SQUEEZE</td><td>+98K Long Most Bullish 6M</td><td style='color:#22C55E'>BULLISH KING</td></tr><tr><td><b>XAUUSD 39</b></td><td>82 LONG TOP</td><td>-28K Cut +19K Short</td><td style='color:#FF2A2A'>BEARISH</td></tr><tr><td><b>XAGUSD 44</b></td><td>76 LONG TRAP</td><td>-12K Cut +22K Short</td><td style='color:#FF2A2A'>BEARISH</td></tr><tr><td><b>US30 48</b></td><td>60 LONG</td><td>+15K Long +32K Asset</td><td style='color:#FFD60A'>NEUTRAL</td></tr><tr><td><b>NAS100 45</b></td><td>64 LONG TRAP</td><td>-18K Selloff</td><td style='color:#FF2A2A'>BEARISH</td></tr><tr><td><b>SP500 50</b></td><td>60 LONG</td><td>Flat Hedged</td><td style='color:#FFD60A'>NEUTRAL</td></tr><tr><td><b>GER30 44</b></td><td>55 LONG</td><td>-18K Short DAX</td><td style='color:#FF2A2A'>BEARISH</td></tr><tr><td><b>UK100 53</b></td><td>52 LONG</td><td>+12K Long FTSE</td><td style='color:#FFD60A'>NEUTRAL</td></tr><tr><td><b>EURUSD 39</b></td><td>68 LONG TRAP</td><td>-125K Short EUR</td><td style='color:#FF2A2A'>BEARISH</td></tr><tr><td><b>GBPUSD 42</b></td><td>65 LONG TRAP</td><td>-89K Short GBP</td><td style='color:#FF2A2A'>BEARISH</td></tr><tr><td><b>USDJPY 72</b></td><td>71 SHORT SQUEEZE</td><td>+148K Long DXY</td><td style='color:#22C55E'>BULLISH</td></tr><tr><td><b>OIL WTI 68</b></td><td>58 SHORT SQUEEZE</td><td>+112K Long OPEC</td><td style='color:#22C55E'>BULLISH</td></tr></table></div>", unsafe_allow_html=True)
if st.button("RE-SCAN ALL MARKETS"):
 st.rerun()

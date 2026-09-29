import streamlit as st
import yfinance as yf
import pandas as pd
import pytz
from datetime import datetime

st.set_page_config(page_title="FX AMBUSHERS - Mr SA Dlamini", layout="wide", page_icon="🦅")

st.markdown("<style>.stApp{background:#070709;color:#E8E6D9}.macro-card{background:#101018;border:1px solid #2A2A3A;border-radius:18px;padding:16px;margin:10px 0}.circle{width:80px;height:80px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-direction:column;font-weight:900}.why-box{background:#0F0F1A;border:1px solid #2A2A3A;border-radius:12px;padding:12px;font-size:11px;line-height:1.5}.cot-table{width:100%;border-collapse:collapse;font-size:11px}.cot-table th{background:#1A1A2E;padding:8px;color:#FFD60A;text-align:left}.cot-table td{padding:8px;border-bottom:1px solid #222}</style>", unsafe_allow_html=True)

try:
 st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
 st.image("IMG-20260929-WA1810.jpg", width=340)
 st.markdown("</div>", unsafe_allow_html=True)
except:
 st.markdown("<h1 style='color:#FFD60A;text-align:center'>FX AMBUSHERS</h1>", unsafe_allow_html=True)

st.markdown("<div style='text-align:center;color:#FFD60A;letter-spacing:3px;font-size:13px;font-weight:900'>FX AMBUSHERS - MR SA DLAMINI</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center;color:#E8E6D9;font-size:10px'>PATIENCE IS PROFIT - AMBUSH THE MARKET</div>", unsafe_allow_html=True)

sa = datetime.now(pytz.timezone('Africa/Johannesburg')).strftime("%d %b %H:%M SA")
st.markdown(f"<div style='background:#111;border:1px solid #333;padding:6px 12px;display:flex;justify-content:space-between;font-size:11px;margin-top:12px'><span style='color:#FF2A2A'>PREDATOR MODE</span><span style='color:#FFD60A'>{sa}</span></div><br>", unsafe_allow_html=True)

DB = {}
DB["EURUSD"] = {"s":39,"b":"BEARISH","bull":3,"bear":6,"tot":14,"bf":"GPR, CB Buying, COT Longs","rf":"DXY 71 Bullish, RealYield 4.2, Fed Hawk, Oil, MOVE","n":"VIX, SP500, CPI, Fed"}
DB["GBPUSD"] = {"s":42,"b":"BEARISH","bull":4,"bear":6,"tot":14,"bf":"UK Wage, GPR, COT Longs","rf":"DXY 71 Bullish, BoE Dovish, UK CPI Low, Yield 4.2","n":"VIX, Oil, Fed Rate"}
DB["USDJPY"] = {"s":72,"b":"BULLISH","bull":8,"bear":3,"tot":14,"bf":"DXY 71 KING, Fed Hawk, BoJ Dovish, Yield Gap, COT 148K Long","rf":"Intervention Risk, VIX, JPY Safe Haven","n":"GPR, SP500, CPI"}
DB["XAUUSD"] = {"s":39,"b":"BEARISH","bull":3,"bear":6,"tot":14,"bf":"GPR, CB Buying, COT Longs","rf":"DXY 71 KING, RealYield 4.2, Fed Hawk, Oil, MOVE, GLD","n":"VIX, SP500, CPI, GDX"}
DB["XAGUSD"] = {"s":44,"b":"BEARISH","bull":3,"bear":6,"tot":14,"bf":"GPR, Industry Demand, CB Buying, COT Longs","rf":"DXY 71 KING, RealYield 4.2, Fed Hawk, SP500 Weak","n":"VIX, CPI, Oil, Fed Rate"}
DB["USDCAD"] = {"s":52,"b":"NEUTRAL","bull":5,"bear":5,"tot":14,"bf":"DXY 71 Bullish, Fed Hawk, US CPI, Yield, COT","rf":"Brent Oil 82 Bullish CAD, OPEC Cut, CB Buying","n":"VIX, SP500, GPR, Gold"}
DB["USDCHF"] = {"s":61,"b":"BULLISH","bull":6,"bear":3,"tot":14,"bf":"DXY 71 KING, SNB Dovish, Yield Gap, COT 98K Long, VIX","rf":"CHF Safe Haven, GPR, Gold","n":"SP500, CPI, Oil, GLD"}
DB["OILWTI"] = {"s":68,"b":"BULLISH","bull":7,"bear":3,"tot":14,"bf":"GPR War Risk, OPEC Cut, Inventory Draw, DXY Pullback","rf":"DXY 71 Strong, Fed Hawk, RealYield 4.2, SP500","n":"VIX, CPI, Gold, GLD"}
DB["BTCUSD"] = {"s":54,"b":"NEUTRAL","bull":5,"bear":4,"tot":14,"bf":"ETF Inflow, GPR, CB Buying, Halving, COT Longs","rf":"DXY 71 KING Bearish BTC, RealYield 4.2, Fed Hawk","n":"SP500, CPI, Oil, Gold"}
DB["US30"] = {"s":48,"b":"NEUTRAL","bull":5,"bear":5,"tot":14,"bf":"Fed Pause, CB Buying, GPR, Earnings, COT 15K Long","rf":"DXY 71 Bullish, RealYield 4.2, VIX, Oil","n":"CPI, Gold, SP500, GLD"}
DB["NAS100"] = {"s":45,"b":"BEARISH","bull":3,"bear":6,"tot":14,"bf":"AI Demand, CB Buying, COT Longs","rf":"DXY 71 KING, RealYield 4.2, Fed Hawk, VIX, MOVE","n":"SP500, CPI, Oil, Gold"}
DB["SP500"] = {"s":50,"b":"NEUTRAL","bull":5,"bear":5,"tot":14,"bf":"Fed Pause, Buybacks, GPR, Earnings Beat, COT Longs","rf":"DXY 71 Bullish, RealYield 4.2, Fed Hawk, VIX","n":"CPI, Oil, Gold, GLD"}
DB["GER30"] = {"s":44,"b":"BEARISH","bull":3,"bear":6,"tot":14,"bf":"ECB Dovish, GPR, CB Buying","rf":"DXY 71 KING, RealYield 4.2, PMI 44.2 Weak","n":"SP500, CPI, Oil, Gold"}
DB["UK100"] = {"s":53,"b":"NEUTRAL","bull":5,"bear":4,"tot":14,"bf":"BoE Pause, Oil 82 Bullish, GBP Weak helps FTSE","rf":"DXY 71 Bullish, RealYield 4.2, UK PMI, Brexit","n":"VIX, SP500, CPI, Gold"}
DB["DXY"] = {"s":71,"b":"BULLISH","bull":8,"bear":3,"tot":14,"bf":"Fed Hawkish Hold, RealYield 10Y 4.2 High, US CPI 3.7 Strong, Safe Haven, COT 98K Net Long Most Bullish 6M, VIX 18 Fear, EUR PMI 44.2 Weak","rf":"Fed Cut Bets 2024, SP500 Rally Risk-On, Gold Safe Haven Bid","n":"GPR Middle East, Oil 82, BoJ Intervention, CB Gold Buying"}

pairs_map = {"EURUSD":"EURUSD=X","GBPUSD":"GBPUSD=X","USDJPY":"USDJPY=X","XAUUSD":"GC=F","XAGUSD":"SI=F","USDCAD":"USDCAD=X","USDCHF":"USDCHF=X","OILWTI":"CL=F","BTCUSD":"BTC-USD","US30":"^DJI","NAS100":"^IXIC","SP500":"^GSPC","GER30":"^GDAXI","UK100":"^FTSE","DXY":"DX-Y.NYB"}
GROUPS = {"forex":["EURUSD","GBPUSD","USDJPY","USDCAD","USDCHF","DXY"],"commods":["XAUUSD","XAGUSD","OILWTI"],"crypto":["BTCUSD"],"indices":["US30","NAS100","SP500","GER30","UK100","DXY"]}

def macro_html(d,name):
 col = "#22C55E" if d["b"]=="BULLISH" else "#FF2A2A" if d["b"]=="BEARISH" else "#FFD60A"
 return f"<div class='macro-card'><div style='text-align:center;color:#9AA0B3;font-size:12px;letter-spacing:2px'>{name} MACRO ENVIRONMENT</div><div style='text-align:center;margin:6px 0'><span style='color:{col};font-weight:900;font-size:18px'>{d['b']}</span> <span style='color:#FFD60A;font-size:12px'>Why? ^</span></div><div style='text-align:center;font-size:11px;color:#9AA0B3;margin-bottom:8px'>{d['bull']} bullish - {d['bear']} bearish of {d['tot']} indicators</div><div style='display:flex;gap:12px;align-items:center'><div class='circle' style='border:4px solid #1F2937;border-top:4px solid {col};border-right:4px solid {col};min-width:80px'><span style='font-size:22px;color:{col}'>{d['s']}</span><span style='font-size:10px;color:#9AA0B3'>/100</span></div><div class='why-box' style='flex:1'><div style='color:#22C55E;font-weight:700'>Bullish for {name}: <span style='color:#CBD5E1;font-weight:400'>{d['bf']}</span></div><div style='margin-top:6px;color:#FF2A2A;font-weight:700'>Bearish for {name}: <span style='color:#9AA0B3;font-weight:400'>{d['rf']}</span></div><div style='margin-top:6px;color:#6B7280;font-weight:700'>Neutral: <span style='font-weight:400'>{d['n']}</span></div></div></div></div>"

if "page" not in st.session_state:
 st.session_state.page = "home"

def show_detail(pair_list, header):
 st.markdown(f"## <span style='color:#FFD60A'>{header}</span>", unsafe_allow_html=True)
 for name in pair_list:
  d = DB[name]
  ticker = pairs_map.get(name)
  try:
   df = yf.Ticker(ticker).history(period="1d", interval="5m")
   daily = yf.Ticker(ticker).history(period="5d")
   p = daily['Close'].iloc[-1]
   pct = (daily['Close'].iloc[-1]-daily['Close'].iloc[-2])/daily['Close'].iloc[-2]*100
  except:
   df = pd.DataFrame({"Close":[1]*50})
   p = 0
   pct = 0
  label = f"{d['b']} {name} | {p:.2f} ({pct:+.2f} pct) - SCORE {d['s']}"
  with st.expander(label, expanded=(name==pair_list[0])):
   st.line_chart(df['Close'], height=90)
   st.markdown(macro_html(d,name), unsafe_allow_html=True)

if st.session_state.page=="home":
 st.markdown("### GEOPOLINTEL LIVE")
 st.markdown("<div style='background:#101A10;border-left:3px solid #22C55E;padding:8px;font-size:11px'>DXY 104.5 BULLISH 71/100 - Fed hawkish - Real Yield 4.2 = Gold Bearish NAS100 Bearish - EUR PMI 44.2 weak</div>", unsafe_allow_html=True)
 st.markdown("### DXY KING - DOLLAR INDEX GAUGE - WHY BULLISH OR BEARISH")
 st.markdown(macro_html(DB["DXY"],"DXY"), unsafe_allow_html=True)
 st.markdown("### SELECT TARGET - 6 PREDATOR SYSTEMS")
 c1,c2 = st.columns(2)
 with c1:
  if st.button("Forex Ambush - 6 PAIRS incl DXY - LOCK TARGET", use_container_width=True):
   st.session_state.page="forex"
   st.rerun()
  if st.button("Commodities Trap - GOLD SILVER OIL - LOCK TARGET", use_container_width=True):
   st.session_state.page="commods"
   st.rerun()
  if st.button("Intel News - LOCK TARGET", use_container_width=True):
   st.session_state.page="news"
   st.rerun()
 with c2:
  if st.button("Indices Hunt - US30 NAS100 SP500 GER30 UK100 DXY - LOCK TARGET", use_container_width=True):
   st.session_state.page="indices"
   st.rerun()
  if st.button("Crypto Ambush - LOCK TARGET", use_container_width=True):
   st.session_state.page="crypto"
   st.rerun()
  if st.button("Institutional COT - DXY XAU XAG US30 NAS100 - LOCK TARGET", use_container_width=True):
   st.session_state.page="cot"
   st.rerun()
else:
 if st.button("RETURN TO RADAR"):
  st.session_state.page="home"
  st.rerun()
 if st.session_state.page=="forex":
  show_detail(GROUPS["forex"],"FOREX AMBUSH - DXY KING")
 elif st.session_state.page=="commods":
  show_detail(GROUPS["commods"],"COMMODITIES TRAP")
 elif st.session_state.page=="crypto":
  show_detail(GROUPS["crypto"],"CRYPTO AMBUSH")
 elif st.session_state.page=="indices":
  show_detail(GROUPS["indices"],"INDICES HUNT")
 elif st.session_state.page=="news":
  st.markdown("## <span style='color:#FF2A2A'>INTEL NEWS</span>", unsafe_allow_html=True)
  st.markdown("<div class='macro-card'>DXY 104.5 BULLISH 71/100 - Fed hawkish - EUR BEARISH 39 - GOLD TRAP 82 long - OIL BULLISH 68</div>", unsafe_allow_html=True)
 elif st.session_state.page=="cot":
  st.markdown("## <span style='color:#FFD60A'>COT INSTITUTIONAL REPORT - WITH DXY</span>", unsafe_allow_html=True)
  st.markdown("<div class='macro-card'><table class='cot-table'><tr><th>PAIR</th><th>RETAIL</th><th>SMART MONEY</th><th>BIAS</th></tr><tr><td><b>DXY 71</b></td><td>62 SHORT SQUEEZE</td><td>+98K Long Most Bullish 6M</td><td style='color:#22C55E'>BULLISH KING</td></tr><tr><td><b>XAUUSD 39</b></td><td>82 LONG TOP</td><td>-28K Cut Long +19K Short</td><td style='color:#FF2A2A'>BEARISH</td></tr><tr><td><b>XAGUSD 44</b></td><td>76 LONG TRAP</td><td>-12K Cut +22K Short</td><td style='color:#FF2A2A'>BEARISH</td></tr><tr><td><b>US30 48</b></td><td>60 LONG</td><td>+15K Long +32K Asset</td><td style='color:#FFD60A'>NEUTRAL</td></tr><tr><td><b>NAS100 45</b></td><td>64 LONG TRAP</td><td>-18K Selloff DXY Bearish NAS</td><td style='color:#FF2A2A'>BEARISH</td></tr></table></div>", unsafe_allow_html=True)

if st.button("RE-SCAN ALL MARKETS"):
 st.rerun()

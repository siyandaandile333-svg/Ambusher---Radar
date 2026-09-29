import streamlit as st, yfinance as yf, pandas as pd, pytz
from datetime import datetime
st.set_page_config(page_title="FX AMBUSHERS - Mr SA Dlamini", layout="wide", page_icon="🦅")
st.markdown("<style>.stApp{background:#070709;color:#E8E6D9}.macro-card{background:#101018;border:1px solid #2A2A3A;border-radius:18px;padding:16px;margin:10px 0}.circle{width:80px;height:80px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-direction:column;font-weight:900}.why-box{background:#0F0F1A;border:1px solid #2A2A3A;border-radius:12px;padding:12px;font-size:11px;line-height:1.5}.cot-table{width:100%;border-collapse:collapse;font-size:11px}.cot-table th{background:#1A1A2E;padding:8px;color:#FFD60A;text-align:left}.cot-table td{padding:8px;border-bottom:1px solid #222}</style>", unsafe_allow_html=True)

# LOGO RESTORED
try:
 st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
 st.image("IMG-20260929-WA1810.jpg", width=340)
 st.markdown("</div>", unsafe_allow_html=True)
except:
 st.markdown("<h1 style='color:#FFD60A;text-align:center'>FX AMBUSHERS</h1>", unsafe_allow_html=True)

st.markdown("<div style='text-align:center;color:#FFD60A;letter-spacing:3px;font-size:13px;font-weight:900'>FX AMBUSHERS • MR SA DLAMINI</div><div style='text-align:center;color:#E8E6D9;font-size:10px'>PATIENCE IS PROFIT • AMBUSH THE MARKET</div>", unsafe_allow_html=True)
sa=datetime.now(pytz.timezone('Africa/Johannesburg')).strftime("%d %b • %H:%M SA • PREDATOR ACTIVE")
st.markdown(f"<div style='background:#111;border:1px solid #333;padding:6px 12px;display:flex;justify-content:space-between;font-size:11px;margin-top:12px'><span style='color:#FF2A2A'>● PREDATOR MODE</span><span style='color:#FFD60A'>{sa}</span></div><br>", unsafe_allow_html=True)

# DB - SAFE SHORT LINES - NO BREAK
DB={}
DB["EURUSD"]={"s":39,"b":"BEARISH","bull":3,"bear":6,"tot":14,"bf":"GPR CB Buying COT Longs","rf":"DXY 71 Bullish RealYield 4.2 Fed Hawk Oil MOVE GLD","n":"VIX SP500 CPI Fed"}
DB["GBPUSD"]={"s":42,"b":"BEARISH","bull":4,"bear":6,"tot":14,"bf":"UK Wage GPR COT Longs","rf":"DXY 71 Bullish BoE Dovish UK CPI Low Yield 4.2","n":"VIX Oil Fed Rate"}
DB["USDJPY"]={"s":72,"b":"BULLISH","bull":8,"bear":3,"tot":14,"bf":"DXY 71 KING Fed Hawk BoJ Dovish Yield Gap COT 148K Long","rf":"Intervention Risk VIX JPY Safe Haven","n":"GPR SP500 CPI Oil"}
DB["XAUUSD"]={"s":39,"b":"BEARISH","bull":3,"bear":6,"tot":14,"bf":"GPR CB Buying COT Longs","rf":"DXY 71 KING RealYield 4.2 Fed Hawk Oil MOVE GLD","n":"VIX SP500 CPI GDX"}
DB["XAGUSD"]={"s":44,"b":"BEARISH","bull":3,"bear":6,"tot":14,"bf":"GPR Industry Demand CB Buying COT Longs","rf":"DXY 71 KING RealYield 4.2 Fed Hawk SP500 Weak","n":"VIX CPI Oil Fed"}
DB["USDCAD"]={"s":52,"b":"NEUTRAL","bull":5,"bear":5,"tot":14,"bf":"DXY 71 Bullish Fed Hawk US CPI Yield COT","rf":"Brent Oil 82 Bullish CAD OPEC Cut CB Buying","n":"VIX SP500 GPR Gold"}
DB["USDCHF"]={"s":61,"b":"BULLISH","bull":6,"bear":3,"tot":14,"bf":"DXY 71 KING SNB Dovish Yield Gap COT 98K Long VIX","rf":"CHF Safe Haven GPR Gold","n":"SP500 CPI Oil GLD"}
DB["OILWTI"]={"s":68,"b":"BULLISH","bull":7,"bear":3,"tot":14,"bf":"GPR War Risk OPEC Cut Inventory Draw DXY Pullback","rf":"DXY 71 Strong Fed Hawk RealYield 4.2 SP500","n":"VIX CPI Gold GLD"}
DB["BTCUSD"]={"s":54,"b":"NEUTRAL","bull":5,"bear":4,"tot":14,"bf":"ETF Inflow GPR CB Buying Halving COT Longs","rf":"DXY 71 KING Bearish BTC RealYield 4.2 Fed Hawk","n":"SP500 CPI Oil Gold"}
DB["US30"]={"s":48,"b":"NEUTRAL","bull":5,"bear":5,"tot":14,"bf":"Fed Pause CB Buying GPR Earnings COT 15K Long","rf":"DXY 71

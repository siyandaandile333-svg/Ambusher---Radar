import streamlit as st, yfinance as yf, pandas as pd
import pytz
from datetime import datetime
st.set_page_config(page_title="FX AMBUSHERS - Mr SA Dlamini", layout="wide", page_icon="🦅")

st.markdown("""<style>
.stApp{background:#070709;color:#E8E6D9}
.macro-card{background:#101018;border:1px solid #2A2A3A;border-radius:18px;padding:16px;margin:10px 0}
.circle{width:80px;height:80px;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:900}
.why-box{background:#0F0F1A;border:1px solid #2A2A3A;border-radius:12px;padding:12px;font-size:11px;line-height:1.6}
.cot-table{width:100%;border-collapse:collapse;font-size:11px}
.cot-table th{background:#1A1A2E;padding:8px;text-align:left;color:#FFD60A}
.cot-table td{padding:8px;border-bottom:1px solid #222}
</style>""", unsafe_allow_html=True)

# LOGO - RESTORED
try:
 st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
 st.image("IMG-20260929-WA1810.jpg", width=340)
 st.markdown("</div>", unsafe_allow_html=True)
except:
 try:
  st.image("logo.png", width=340)
 except:
  st.markdown("<h1 style='color:#FFD60A;text-align:center'>FX AMBUSHERS</h1>", unsafe_allow_html=True)

st.markdown("<div style='text-align:center;color:#FFD60A;letter-spacing:3px;font-size:13px;font-weight:900'>FX AMBUSHERS • MR SA DLAMINI</div><div style='text-align:center;color:#E8E6D9;font-size:10px'>PATIENCE IS PROFIT • AMBUSH THE MARKET</div>", unsafe_allow_html=True)

sa=datetime.now(pytz.timezone('Africa/Johannesburg')).strftime("%d %b • %H:%M SA • PREDATOR ACTIVE")
st.markdown(f"<div style='background:#111;border:1px solid #333;padding:6px 12px;display:flex;justify-content:space-between;font-size:11px;margin-top:12px'><span style='color:#FF2A2A'>● PREDATOR MODE</span><span style='color:#FFD60A'>{sa}</span></div><br>", unsafe_allow_html=True)

# DB - SAFE NO SLASH KEYS
DB={
"EURUSD":{"score":39,"bias":"BEARISH","bull":3,"bear":6,"total":14,"b_for":"GPR CB Buying COT Longs","br_for":"DXY 71 Bullish RealYield 4.2 Fed Hawk Oil MOVE GLD","neu":"VIX SP500 CPI Fed Rate Miners"},
"GBPUSD":{"score":42,"bias":"BEARISH","bull":4,"bear":6,"total":14,"b_for":"UK Wage GPR COT Longs","br_for":"DXY 71 Bullish BoE Dovish UK CPI Low RealYield SP500 GLD","neu":"VIX Oil Fed Rate Miners"},
"USDJPY":{"score":72,"bias":"BULLISH","bull":8,"bear":3,"total":14,"b_for":"DXY 71 KING Fed Hawk BoJ Dovish Yield Gap MOVE COT 148K Long","br_for":"Intervention Risk VIX JPY Safe Haven","neu":"GPR SP500 CPI Oil"},
"XAUUSD":{"score":39,"bias":"BEARISH","bull":3,"bear":6,"total":14,"b_for":"GPR CB Buying COT Longs","br_for":"DXY 71 KING RealYield 4.2 Fed Hawk Oil MOVE GLD","neu":"VIX SP500 CPI Fed Rate GDX"},
"XAGUSD":{"score":44,"bias":"BEARISH","bull":3,"bear":6,"total":14,"b_for":"GPR Industry Demand CB Buying COT Longs","br_for":"DXY 71 KING RealYield 4.2 Fed Hawk SP500 Weak GLD Outflow","neu":"VIX CPI Oil Fed Rate Miners"},
"USDCAD":{"score":52,"bias":"NEUTRAL","bull":5,"bear":5,"total":14,"b_for":"DXY 71 Bullish Fed Hawk US CPI Yield COT","br_for":"Brent Oil 82 Bullish CAD OPEC Cut CB Buying CAD Jobs Inventory","neu":"VIX SP500 GPR Gold RealYield"},
"USDCHF":{"score":61,"bias":"BULLISH","bull":6,"bear":3,"total":14,"b_for":"DXY 71 KING SNB Dovish Yield Gap Fed Expect COT 98K Long VIX","br_for":"CHF Safe Haven GPR Gold","neu":"SP500 CPI Oil RealYield GLD"},
"OILWTI":{"score":68,"bias":"BULLISH","bull":7,"bear":3,"total":14,"b_for":"GPR War Risk OPEC Cut Inventory Draw DXY Pullback CB Demand Brent MOVE","br_for":"DXY 71 Strong vs Oil Fed Hawk RealYield 4.2 SP500","neu":"VIX CPI Gold GLD GDX"},
"BTCUSD":{"score":54,"bias":"NEUTRAL","bull":5,"bear":4,"total":14,"b_for":"ETF Inflow GPR CB Buying Halving COT Longs","br_for":"DXY 71 KING Bearish BTC RealYield 4.2 Fed Hawk VIX","neu":"SP500 CPI Oil Gold MOVE"},
"US30":{"score":48,"bias":"NEUTRAL","bull":5,"bear":5,"total":14,"b_for":"Fed Pause CB Buying GPR Earnings COT 15K Long DXY Pullback","br_for":"DXY 71 Bullish RealYield 4.2 VIX Oil Fed Expect","neu":"CPI Gold SP500 GLD GDX"},
"NAS100":{"score":45,"bias":"BEARISH","bull":3,"bear":6,"total":14,"b_for":"AI Demand CB Buying COT Longs","br_for":"DXY 71 KING RealYield 4.2 Fed Hawk VIX MOVE GLD","neu":"SP500 CPI Oil Gold GDX"},
"SP500":{"score":50,"bias":"NEUTRAL","bull":5,"bear":5,"total":14,"b_for":"Fed Pause Buybacks GPR Earnings Beat COT Longs","br_for":"DXY 71 Bullish RealYield 4.2 Fed Hawk VIX MOVE","neu":"CPI Oil Gold GLD GDX"},
"GER30":{"score":44,"bias":"BEARISH","bull":3,"bear":6,"total":14,"b_for":"ECB Dovish GPR CB Buying","br_for":"DXY 71 KING RealYield 4.2 German PMI 44.2 Weak Energy Risk VIX DAX","neu":"SP500 CPI Oil Gold Fed Rate"},
"UK100":{"score":53,"bias":"NEUTRAL","bull":5,"bear":4,"total":14,"b_for":"BoE Pause Oil 82 Bullish GBP Weak FTSE Commodity Bid COT","br_for":"DXY 71 Bullish RealYield 4.2 UK PMI Brexit Drag","neu":"VIX SP500 CPI Gold GDX"},
"DXY":{"score":71,"bias":"BULLISH","bull":8,"bear":3,"total":14,"b_for":"

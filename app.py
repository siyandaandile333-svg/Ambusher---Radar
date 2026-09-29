import streamlit as st, yfinance as yf, pandas as pd, pytz
from datetime import datetime
st.set_page_config(page_title="FX AMBUSHERS - Mr SA Dlamini", layout="wide", page_icon="🦅")
st.markdown("""<style>.stApp{background:#070709;color:#E8E6D9}.macro-card{background:#101018;border:1px solid #2A2A3A;border-radius:18px;padding:16px;margin:10px 0}.circle{width:80px;height:80px;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:900}.why-box{background:#0F0F1A;border:1px solid #2A2A3A;border-radius:12px;padding:12px;font-size:11px;line-height:1.6}.cot-table{width:100%;border-collapse:collapse;font-size:11px}.cot-table th{background:#1A1A2E;padding:8px;text-align:left;color:#FFD60A}.cot-table td{padding:8px;border-bottom:1px solid #222}</style>""", unsafe_allow_html=True)
try:
 st.markdown("<div style='text-align:center'>", unsafe_allow_html=True);st.image("IMG-20260929-WA1810.jpg", width=340);st.markdown("</div>", unsafe_allow_html=True)
except:
 try: st.image("logo.png", width=340)
 except: st.markdown("<h1 style='color:#FFD60A;text-align:center'>FX AMBUSHERS</h1>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center;color:#FFD60A;letter-spacing:3px;font-size:13px;font-weight:900'>FX AMBUSHERS - MR SA DLAMINI</div><div style='text-align:center;color:#E8E6D9;font-size:10px'>PATIENCE IS PROFIT - AMBUSH THE MARKET</div>", unsafe_allow_html=True)
sa=datetime.now(pytz.timezone('Africa/Johannesburg')).strftime("%d %b - %H:%M SA - PREDATOR ACTIVE")
st.markdown(f"<div style='background:#111;border:1px solid #333;padding:6px 12px;display:flex;justify-content:space-between;font-size:11px;margin-top:12px'><span style='color:#FF2A2A'>PREDATOR MODE</span><span style='color:#FFD60A'>{sa}</span></div><br>", unsafe_allow_html=True)

DB={
"EUR/USD":{"score":39,"bias":"BEARISH","bull":3,"bear":6,"total":14,"b_for":"GPR, CB Buying, COT Longs","br_for":"DXY 71 Bullish, Real Yield 4.2pct, Fed Hawkish, Oil, MOVE, GLD","neu":"VIX, SP500, CPI, Fed Rate, Miners"},
"GBP/USD":{"score":42,"bias":"BEARISH","bull":4,"bear":6,"total":14,"b_for":"UK Wage, GPR, COT Longs","br_for":"DXY 71 Bullish, BoE Dovish, UK CPI Low, Real Yield, SP500, GLD","neu":"VIX, Oil, Fed Rate, Miners"},
"USD/JPY":{"score":72,"bias":"BULLISH","bull":8,"bear":3,"total":14,"b_for":"DXY 71 KING, Fed Hawkish, BoJ Dovish, Yield Gap, MOVE, COT Long 148K","br_for":"Intervention Risk, VIX, JPY Safe Haven","neu":"GPR, SP500, CPI, Oil"},
"XAU/USD":{"score":39,"bias":"BEARISH","bull":3,"bear":6,"total":14,"b_for":"GPR, CB Buying, COT Longs","br_for":"DXY 71 KING, Real Yield 4.2pct, Fed Hawkish, Oil, MOVE, GLD","neu":"VIX, SP500, CPI, Fed Rate, GDX"},
"GOLD":{"score":39,"bias":"BEARISH","bull":3,"bear":6,"total":14,"b_for":"GPR, CB Buying, COT Longs","br_for":"DXY 71 KING, Real Yield 4.2pct, Fed Hawkish, Oil, MOVE, GLD","neu":"VIX, SP500, CPI, Fed Rate, GDX"},
"XAUUSD":{"score":39,"bias":"BEARISH","bull":3,"bear":6,"total":14,"b_for":"GPR, CB Buying, COT Longs","br_for":"DXY 71 KING, Real Yield 4.2pct, Fed Hawkish, Oil, MOVE, GLD","neu":"VIX, SP500, CPI, Fed Rate, GDX"},
"XAGUSD":{"score":44,"bias":"BEARISH","bull":3,"bear":6,"total":14,"b_for":"GPR, Industry Demand, CB Buying, COT Longs","br_for":"DXY 71 KING, Real Yield 4.2pct, Fed Hawkish, SP500 Weak, GLD Outflow","neu":"VIX, CPI, Oil, Fed Rate, Miners"},
"AUD/USD":{"score":31,"bias":"BEARISH","bull":2,"bear":7,"total":14,"b_for":"CB Buying, GPR","br_for":"DXY 71 KING, China PMI 49.2, Iron Ore, Real Yield, Oil, SP500, COT Short","neu":"VIX, CPI, Fed Rate, Gold"},
"NZD/USD":{"score":29,"bias":"BEARISH","bull":2,"bear":8,"total":14,"b_for":"GPR, Dairy","br_for":"DXY 71 KING, China Slow, RBNZ Dovish, Yield, Oil, VIX, SP500, COT Short","neu":"CPI, Fed Rate, Gold"},
"USD/CAD":{"score":52,"bias":"NEUTRAL","bull":5,"bear":5,"total":14,"b_for":"DXY 71 Bullish, Fed Hawkish, US CPI, Yield, COT","br_for":"Brent Oil 82 Bullish CAD, OPEC Cut, CB Buying, CAD Jobs, Inventory","

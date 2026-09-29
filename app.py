import streamlit as st, yfinance as yf, pandas as pd
import pytz
from datetime import datetime
st.set_page_config(page_title="FX AMBUSHERS - Mr SA Dlamini", layout="wide", page_icon="🦅")
st.markdown("""<style>.stApp{background:#070709;color:#E8E6D9}.macro-card{background:#101018;border:1px solid #2A2A3A;border-radius:18px;padding:16px;margin:10px 0}.circle{width:80px;height:80px;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:900}.why-box{background:#0F0F1A;border:1px solid #2A2A3A;border-radius:12px;padding:12px;font-size:11px;line-height:1.6}.cot-table{width:100%;border-collapse:collapse;font-size:11px}.cot-table th{background:#1A1A2E;padding:8px;text-align:left;color:#FFD60A}.cot-table td{padding:8px;border-bottom:1px solid #222}.dxy-king{background:linear-gradient(135deg,#0F101A 0%,#1A1A2E 100%);border:2px solid #FFD60A;border-radius:18px;padding:16px;margin:12px 0}</style>""", unsafe_allow_html=True)
try:
 st.markdown("<div style='text-align:center'>", unsafe_allow_html=True);st.image("IMG-20260929-WA1810.jpg", width=340);st.markdown("</div>", unsafe_allow_html=True)
except:
 try: st.image("logo.png", width=340)
 except: st.markdown("<h1 style='color:#FFD60A;text-align:center'>FX AMBUSHERS</h1>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center;color:#FFD60A;letter-spacing:3px;font-size:13px;font-weight:900'>FX AMBUSHERS • MR SA DLAMINI</div><div style='text-align:center;color:#E8E6D9;font-size:10px'>PATIENCE IS PROFIT • AMBUSH THE MARKET</div>", unsafe_allow_html=True)
sa=datetime.now(pytz.timezone('Africa/Johannesburg')).strftime("%d %b • %H:%M SA • PREDATOR ACTIVE")
st.markdown(f"<div style='background:#111;border:1px solid #333;padding:6px 12px;display:flex;justify-content:space-between;font-size:11px;margin-top:12px'><span style='color:#FF2A2A'>● PREDATOR MODE</span><span style='color:#FFD60A'>{sa}</span></div><br>", unsafe_allow_html=True)

DB={
"EUR/USD":{"score":39,"bias":"BEARISH","bull":3,"bear":6,"total":14,"b_for":"GPR, CB Purchases, COT Net Longs","br_for":"DXY Bullish 71, Real Yield 10Y 4.2%, Fed Expect., Brent Oil, MOVE (Bond Vol), GLD ETF","neu":"VIX, S&P 500, CPI, Fed Rate, Gold Miners"},
"GBP/USD":{"score":42,"bias":"BEARISH","bull":4,"bear":6,"total":14,"b_for":"UK Wage, GPR, COT Net Longs","br_for":"DXY 71 Bullish, BoE Dovish, UK CPI Low, Real Yield 4.2%, S&P 500, GLD","neu":"VIX, Oil, Fed Rate, Miners"},
"USD/JPY":{"score":72,"bias":"BULLISH","bull":8,"bear":3,"total":14,"b_for":"DXY 71 Bullish KING, Fed Hawkish, BoJ Dovish, Yield Gap 4.2% vs 0.5%, MOVE, COT Longs +148K","br_for":"Intervention Risk, VIX, JPY Safe Haven","neu":"GPR, S&P 500, CPI, Oil"},
"XAU/USD":{"score":39,"bias":"BEARISH","bull":3,"bear":6,"total":14,"b_for":"GPR, CB Purchases, COT Net Longs","br_for":"DXY 71 BULLISH KING, Real Yield 10Y 4.2%, Fed Expect., Brent Oil, MOVE, GLD ETF","neu":"VIX, S&P 500, CPI, Fed Rate, Gold Miners (GDX)"},
"GOLD":{"score":39,"bias":"BEARISH","bull":3,"bear":6,"total":14,"b_for":"GPR, CB Purchases, COT Net Longs","br_for":"DXY 71 BULLISH KING, Real Yield 10Y 4.2%, Fed Expect., Brent Oil, MOVE, GLD ETF","neu":"VIX, S&P 500, CPI, Fed Rate, Gold Miners (GDX)"},
"XAUUSD":{"score":39,"bias":"BEARISH","bull":3,"bear":6,"total":14,"b_for":"GPR, CB Purchases, COT Net Longs","br_for":"DXY 71 BULLISH KING, Real Yield 10Y 4.2%, Fed Expect., Brent Oil, MOVE, GLD ETF","neu":"VIX, S&P 500, CPI, Fed Rate, Gold Miners (GDX)"},
"XAGUSD":{"score":44,"bias":"BEARISH","bull":3,"bear":6,"total":14,"b_for":"GPR, Industrial Demand, CB Buying, COT Net Longs","br_for":"DXY 71 BULLISH KING, Real Yield 10Y 4.2

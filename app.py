import streamlit as st, yfinance as yf, pandas as pd
import pytz
from datetime import datetime
st.set_page_config(page_title="FX AMBUSHERS - Mr SA Dlamini", layout="wide", page_icon="🦅")
st.markdown("""<style>.stApp{background:#070709;color:#E8E6D9}.macro-card{background:#101018;border:1px solid #2A2A3A;border-radius:18px;padding:16px;margin:10px 0}.circle{width:80px;height:80px;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:900}.why-box{background:#0F0F1A;border:1px solid #2A2A3A;border-radius:12px;padding:12px;font-size:11px;line-height:1.6}</style>""", unsafe_allow_html=True)
try:
 st.markdown("<div style='text-align:center'>", unsafe_allow_html=True);st.image("IMG-20260929-WA1810.jpg", width=340);st.markdown("</div>", unsafe_allow_html=True)
except:
 try: st.image("logo.png", width=340)
 except: st.markdown("<h1 style='color:#FFD60A;text-align:center'>FX AMBUSHERS</h1>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center;color:#FFD60A;letter-spacing:3px;font-size:13px;font-weight:900'>FX AMBUSHERS • MR SA DLAMINI</div><div style='text-align:center;color:#E8E6D9;font-size:10px'>PATIENCE IS PROFIT • AMBUSH THE MARKET</div>", unsafe_allow_html=True)
sa=datetime.now(pytz.timezone('Africa/Johannesburg')).strftime("%d %b • %H:%M SA • PREDATOR ACTIVE")
st.markdown(f"<div style='background:#111;border:1px solid #333;padding:6px 12px;display:flex;justify-content:space-between;font-size:11px;margin-top:12px'><span style='color:#FF2A2A'>● PREDATOR MODE</span><span style='color:#FFD60A'>{sa}</span></div><br>", unsafe_allow_html=True)
DB={"EUR/USD":{"score":39,"bias":"BEARISH","bull":3,"bear":6,"total":14,"b_for":"GPR, CB Purchases, COT Net Longs","br_for":"DXY, Real Yield 10Y, Fed Expect., Brent Oil, MOVE (Bond Vol), GLD ETF","neu":"VIX, S&P 500, CPI, Fed Rate, Gold Miners (GDX)"},"GBP/USD":{"score":42,"bias":"BEARISH","bull":4,"bear":6,"total":14,"b_for":"UK Wage, GPR, COT Net Longs","br_for":"DXY, BoE Dovish, UK CPI Low, Real Yield, S&P 500, GLD","neu":"VIX, Oil, Fed Rate, Miners"},"USD/JPY":{"score":72,"bias":"BULLISH","bull":8,"bear":3,"total":14,"b_for":"DXY, Fed Hawkish, BoJ Dovish, Yield Gap, MOVE, COT Longs","br_for":"Intervention Risk, VIX, JPY Safe Haven","neu":"GPR, S&P 500, CPI, Oil"},"XAU/USD":{"score":39,"bias":"BEARISH","bull":3,"bear":6,"total":14,"b_for":"GPR, CB Purchases, COT Net Longs","br_for":"DXY, Real Yield 10Y, Fed Expect., Brent Oil, MOVE (Bond Vol), GLD ETF","neu":"VIX, S&P 500, CPI, Fed Rate, Gold Miners (GDX)"},"GOLD":{"score":39,"bias":"BEARISH","bull":3,"bear":6,"total":14,"b_for":"GPR, CB Purchases, COT Net Longs","br_for":"DXY, Real Yield 10Y, Fed Expect., Brent Oil, MOVE (Bond Vol), GLD ETF","neu":"VIX, S&P 500, CPI, Fed Rate, Gold Miners (GDX)"},"AUD/USD":{"score":31,"bias":"BEARISH","bull":2,"bear":7,"total":14,"b_for":"CB Purchases, GPR","br_for":"DXY, China PMI, Iron Ore, Real Yield, Oil, S&P 500, COT Shorts","neu":"VIX, CPI, Fed Rate, Gold"},"NZD/USD":{"score":29,"bias":"BEARISH","bull":2,"bear":8,"total":14,"b_for":"GPR, Dairy Rebound","br_for":"DXY, China Slow, RBNZ Dovish, Yield, Oil, VIX, S&P 500, COT Shorts","neu":"CPI, Fed Rate, Gold"},"USD/CAD":{"score":52,"bias":"NEUTRAL","bull":5,"bear":5,"total":14,"b_for":"DXY, Fed Hawkish, US CPI, Yield, COT","br_for":"Brent Oil, OPEC Cut, CB Purchases, CAD Jobs, Oil Inventory","neu":"VIX, S&P 500, GPR, Gold, Real Yield"},"USD/CHF":{"score":61,"bias":"BULLISH","bull":6,"bear":3,"total":14,"b_for":"DXY, SNB Dovish, Yield Gap, Fed Expect., COT Longs, VIX","br_for":"CHF Safe Haven, GPR, Gold","neu":"S&P 500, CPI, Oil, Real Yield, GLD"},"OIL WTI":{"score":68,"bias":"BULLISH","bull":7,"bear":3,"total":14,"b_for":"GPR, OPEC Cut, Inventory Draw, DXY Weak, CB Demand, Brent, MOVE","br_for":"Fed Hawkish, Real Yield, S&P 500","neu":"VIX, CPI, Gold, GLD, GDX"},"BTC/USD":{"score":54,"bias":"NEUTRAL","bull":5,"bear":4,"total":14,"b_for":"ETF Inflow, GPR, CB Purchases, Halving, COT Longs","br_for":"DXY, Real Yield, Fed Hawkish, VIX","neu":"S&P 500, CPI, Oil, Gold, MOVE"},"US30":{"score":48,"bias":"NEUTRAL","bull":5,"bear":5,"total":14,"b_for":"Fed Pause, CB Purchases, GPR, Earnings, COT","br_for":"DXY, Real Yield, VIX, Oil, Fed Expect.","neu":"CPI, Gold, S&P 500, GLD, GDX"},"NAS100":{"score":45,"bias":"BEARISH","bull":3,"bear":6,"total":14,"b_for":"AI Demand, CB Purchases, COT Longs","br_for":"Real Yield 10Y, DXY, Fed Hawkish, VIX, MOVE, GLD ETF","neu":"S&P 500, CPI, Oil, Gold, GDX"}}
pairs_map={"EUR/USD":"EURUSD=X","GBP/USD":"GBPUSD=X","USD/JPY":"USDJPY=X","AUD/USD":"AUDUSD=X","NZD/USD":"NZDUSD=X","USD/CAD":"USDCAD=X","USD/CHF":"USDCHF=X","XAU/USD":"GC=F","GOLD":"GC=F","OIL WTI":"CL=F","BTC/USD":"BTC-USD","US30":"^DJI","NAS100":"^IXIC"}
GROUPS={"forex":["EUR/USD","GBP/USD","USD/JPY","AUD/USD","NZD/USD","USD/CAD","USD/CHF"],"commods":["XAU/USD","GOLD","OIL WTI"],"crypto":["BTC/USD"],"indices":["US30","NAS100"]}
def macro_html(d,name):
 color="#22C55E" if d["bias"]=="BULLISH" else "#FF2A2A" if d["bias"]=="BEARISH" else "#FFD60A"
 return f"<div class='macro-card'><div style='text-align:center;letter-spacing:2px;font-size:12px;color:#9AA0B3'>{name} MACRO ENVIRONMENT</div><div style='text-align:center;margin:8px 0'><span style='color:{color};font-weight:900;font-size:18px'>{d['bias']}</span> <span style='color:#FFD60A;font-size:12px'>Why? ▲</span></div><div style='text-align:center;font-size:12px;color:#9AA0B3;margin-bottom:12px'>{d['bull']} bullish · {d['bear']} bearish of {d['total']} indicators</div><div style='display:flex;gap:14px;align-items:center'><div class='circle' style='border:4px solid #1F2937;border-top:4px solid {color};border-right:4px solid {color};min-width:80px'><span style='font-size:22px;color:{color}'>{d['score']}</span><span style='font-size:12px;color:#9AA0B3'>/100</span></div><div class='why-box' style='flex:1'><div style='color:#22C55E;font-weight:700'>Bullish for {name}: <span style='color:#CBD5E1;font-weight:400'>{d['b_for']}</span></div><div style='margin-top:8px;color:#FF2A2A;font-weight:700'>Bearish for {name}: <span style='color:#9AA0B3;font-weight:400'>{d['br_for']}</span></div><div style='margin-top:8px;color:#6B7280;font-weight:700'>Neutral: <span style='color:#6B7280;font-weight:400'>{d['neu']}</span></div></div></div></div>"
if 'page' not in st.session_state: st.session_state.page="home"
def show_detail(pair_list, header):
 st.markdown(f"## <span style='color:#FFD60A'>{header}</span>", unsafe_allow_html=True)
 for name in pair_list:
  d=DB[name];ticker=pairs_map.get(name)
  try: df=yf.Ticker(ticker).history(period="1d",interval="5m");daily=yf.Ticker(ticker).history(period="5d");p=daily['Close'].iloc[-1];pct=(daily['Close'].iloc[-1]-daily['Close'].iloc[-2])/daily['Close'].iloc[-2]*100
  except: df=pd.DataFrame({"Close":[1]*50});p=0;pct=0
  label=f"{d['bias']} {name} | {p:.4f} ({pct:+.2f}%) • SCORE {d['score']}"
  with st.expander(label, expanded=(name==pair_list[0])):
   st.line_chart(df['Close'], height=90);st.markdown(macro_html(d,name), unsafe_allow_html=True)
if st.session_state.page=="home":
 st.markdown("### 🎯 SELECT TARGET - 6 PREDATOR SYSTEMS")
 c1,c2=st.columns(2)
 with c1:
  if st.button("◎ Forex Ambush • 7 PAIRS • LOCK TARGET", use_container_width=True): st.session_state.page="forex";st.rerun()
  if st.button("◈ Commodities Trap • GOLD OIL • LOCK TARGET", use_container_width=True): st.session_state.page="commods";st.rerun()
  if st.button("◉ Intel News • LOCK TARGET", use_container_width=True): st.session_state.page="news";st.rerun()
 with c2:
  if st.button("▲ Indices Hunt • LOCK TARGET", use_container_width=True): st.session_state.page="indices";st.rerun()
  if st.button("₿ Crypto Ambush • LOCK TARGET", use_container_width=True): st.session_state.page="crypto";st.rerun()
  if st.button("⬡ Institutional COT • LOCK TARGET", use_container_width=True): st.session_state.page="cot";st.rerun()
else:
 if st.button("← RETURN TO RADAR"): st.session_state.page="home";st.rerun()
 if st.session_state.page=="forex": show_detail(GROUPS["forex"],"FOREX AMBUSH")
 elif st.session_state.page=="commods": show_detail(GROUPS["commods"],"COMMODITIES TRAP")
 elif st.session_state.page=="crypto": show_detail(GROUPS["crypto"],"CRYPTO AMBUSH")
 elif st.session_state.page=="indices": show_detail(GROUPS["indices"],"INDICES HUNT")
if st.button("🔄 RE-SCAN ALL MARKETS"): st.rerun()

import streamlit as st, yfinance as yf, pandas as pd, pytz
from datetime import datetime
st.set_page_config(layout="wide")
st.markdown("<style>.stApp{background:#070709;color:#E8E6D9}.macro-card{background:#101018;border:1px solid #2A2A3A;border-radius:18px;padding:16px;margin:10px 0}.circle{width:80px;height:80px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-direction:column;font-weight:900}.why-box{background:#0F0F1A;border:1px solid #2A2A3A;border-radius:12px;padding:12px;font-size:11px}.cot-table{width:100%;border-collapse:collapse;font-size:11px}.cot-table th{background:#1A1A2E;padding:8px;color:#FFD60A;text-align:left}.cot-table td{padding:8px;border-bottom:1px solid #222}</style>", unsafe_allow_html=True)
try: st.image("IMG-20260929-WA1810.jpg", width=340)
except: st.markdown("<h1 style='color:#FFD60A;text-align:center'>FX AMBUSHERS</h1>", unsafe_allow_html=True)
sa=datetime.now(pytz.timezone('Africa/Johannesburg')).strftime("%d %b %H:%M SA")
st.markdown(f"<div style='background:#111;border:1px solid #333;padding:6px 12px;font-size:11px'><span style='color:#FF2A2A'>PREDATOR MODE</span> <span style='color:#FFD60A'>{sa}</span></div><br>", unsafe_allow_html=True)
DB={}
DB["DXY"]={"s":71,"b":"BULL","bf":"Fed Hawk Yield 4.2 COT 98K Long","rf":"Fed Cut SP500 Gold","n":"GPR Oil BoJ"}
DB["EURUSD"]={"s":39,"b":"BEAR","bf":"GPR CB COT Longs","rf":"DXY 71 Yield 4.2 Fed Hawk","n":"VIX SP500 CPI"}
DB["GBPUSD"]={"s":42,"b":"BEAR","bf":"UK Wage GPR COT Longs","rf":"DXY 71 BoE Dovish CPI Low","n":"VIX Oil Fed"}
DB["USDJPY"]={"s":72,"b":"BULL","bf":"DXY 71 Fed Hawk BoJ Dovish 148K","rf":"Intervention VIX Safe","n":"GPR SP500 CPI"}
DB["XAUUSD"]={"s":39,"b":"BEAR","bf":"GPR CB COT Longs","rf":"DXY 71 Yield 4.2 Fed Hawk","n":"VIX SP500 GDX"}
DB["XAGUSD"]={"s":44,"b":"BEAR","bf":"GPR Industry CB COT Longs","rf":"DXY 71 Yield 4.2 Fed Hawk","n":"VIX CPI Oil"}
DB["USDCAD"]={"s":52,"b":"NEUT","bf":"DXY 71 Fed Hawk CPI Yield","rf":"Oil 82 OPEC Cut CB Buy","n":"VIX SP500 GPR"}
DB["USDCHF"]={"s":61,"b":"BULL","bf":"DXY 71 SNB Dovish Yield COT 98K","rf":"CHF Safe GPR Gold","n":"SP500 CPI Oil"}
DB["OILWTI"]={"s":68,"b":"BULL","bf":"GPR OPEC Cut Inventory Draw","rf":"DXY 71 Fed Hawk Yield 4.2","n":"VIX CPI Gold"}
DB["BTCUSD"]={"s":54,"b":"NEUT","bf":"ETF Inflow GPR CB Halving","rf":"DXY 71 Bear BTC Yield 4.2","n":"SP500 CPI Gold"}
DB["US30"]={"s":48,"b":"NEUT","bf":"Fed Pause CB Earnings COT 15K","rf":"DXY 71 Yield 4.2 VIX Oil","n":"CPI Gold SP500"}
DB["NAS100"]={"s":45,"b":"BEAR","bf":"AI Demand CB COT Longs","rf":"DXY 71 Yield 4.2 Fed VIX","n":"SP500 CPI Oil"}
DB["SP500"]={"s":50,"b":"NEUT","bf":"Fed Pause Buybacks Earnings","rf":"DXY 71 Yield 4.2 VIX","n":"CPI Oil Gold"}
DB["GER30"]={"s":44,"b":"BEAR","bf":"ECB Dovish GPR CB","rf":"DXY 71 Yield 4.2 PMI 44.2","n":"SP500 CPI Oil"}
DB["UK100"]={"s":53,"b":"NEUT","bf":"BoE Pause Oil 82 FTSE","rf":"DXY 71 Yield 4.2 UK PMI","n":"VIX SP500 CPI"}
MP={"EURUSD":"EURUSD=X","GBPUSD":"GBPUSD=X","USDJPY":"USDJPY=X","XAUUSD":"GC=F","XAGUSD":"SI=F","USDCAD":"USDCAD=X","USDCHF":"USDCHF=X","OILWTI":"CL=F","BTCUSD":"BTC-USD","US30":"^DJI","NAS100":"^IXIC","SP500":"^GSPC","GER30":"^GDAXI","UK100":"^FTSE","DXY":"DX-Y.NYB"}
GR={"forex":["EURUSD","GBPUSD","USDJPY","USDCAD","USDCHF","DXY"],"commods":["XAUUSD","XAGUSD","OILWTI"],"crypto":["BTCUSD"],"indices":["US30","NAS100","SP500","GER30","UK100","DXY"]}
def gauge(d,n):
 c="#22C55E" if d["b"]=="BULL" else "#FF2A2A" if d["b"]=="BEAR" else "#FFD60A"
 return f"<div class='macro-card'><div style='text

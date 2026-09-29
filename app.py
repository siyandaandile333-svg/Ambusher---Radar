import streamlit as st
import yfinance as yf
import pandas as pd
import pytz
from datetime import datetime

st.set_page_config(layout="wide")

try:
 st.image("IMG-20260929-WA1810.jpg",width=320)
except:
 st.markdown("<h2 style='color:#FFD60A;text-align:center'>FX AMBUSHERS</h2>",unsafe_allow_html=True)

DB={}
DB["DXY"]={"s":71,"b":"BULLISH","bu":8,"be":3,"bf":"Fed Hawk Yield 4.2 CPI 3.7 COT 98K Long","rf":"Fed Cut SP500 Gold","n":"GPR Oil BoJ"}
DB["EURUSD"]={"s":39,"b":"BEARISH","bu":3,"be":6,"bf":"GPR CB COT Longs","rf":"DXY 71 Yield 4.2 Fed Hawk","n":"VIX SP500 CPI"}
DB["GBPUSD"]={"s":42,"b":"BEARISH","bu":4,"be":6,"bf":"UK Wage GPR COT Longs","rf":"DXY 71 BoE Dovish CPI Low","n":"VIX Oil Fed"}
DB["USDJPY"]={"s":72,"b":"BULLISH","bu":8,"be":3,"bf":"DXY 71 Fed Hawk BoJ Dovish COT 148K","rf":"Intervention VIX Safe","n":"GPR SP500 CPI"}
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

def gauge(d,name):
 c="#22C55E" if d["b"]=="BULLISH" else "#FF2A2A" if d["b"]=="BEARISH" else "#FFD60A"
 html=f"""
 <div style='background:#101018;border:1px solid #2A2A3A;border-radius:18px;padding:16px;margin:10px 0'>
 <div style='text-align:center;color:#9AA0B3;font-size:12px'>{name} MACRO</div>
 <div style='text-align:center'><span style='color:{c};font-weight:900;font-size:18px'>{d["b"]}</span></div>
 <div style='display:flex;gap:12px;margin-top:10px'>
 <div style='width:80px;height:80px;border-radius:50%;border:4px solid #222;border-top:4px solid {c};display:flex;align-items:center;justify-content:center'>
 <span style='color:{c};font-size:22px;font-weight:900'>{d["s"]}</span></div>
 <div style='font-size:11px'>
 <div style='color:#22C55E'>Bull: {d["bf"]}</div>
 <div style='color:#FF2A2A;margin-top:4px'>Bear: {d["rf"]}</div>
 <div style='color:#6B7280;margin-top:4px'>Neutral: {d["n"]}</div>
 </div></div></div>
 """
 return html

st.markdown("### DXY KING 71 BULLISH - WHY BULLISH/BEARISH LIKE PAIRS")
st.markdown(gauge(DB["DXY"],"DXY"),unsafe_allow_html=True)

st.markdown("### COT INSTITUTIONAL - FULL - WITH DXY")
st.markdown("""
<div style='background:#101018;border:1px solid #2A2A3A;border-radius:18px;padding:12px'>
<table style='width:100%;font-size:11px;border-collapse:collapse'>
<tr><th style='color:#FFD60A;text-align:left'>PAIR</th><th style='color:#FFD60A;text-align:left'>RETAIL</th><th style='color:#FFD60A;text-align:left'>SMART MONEY</th><th style='color:#FFD60A;text-align:left'>BIAS</th></tr>
<tr><td><b>DXY 71</b></td><td>62 SHORT SQUEEZE</td><td>+98K Long Most Bullish</td><td style='color:#22C55E'>BULLISH KING</td></tr>
<tr><td><b>XAUUSD 39</b></td><td>82 LONG TOP</td><td>-28K Cut +19K Short</td><td style='color:#FF2A2A'>BEARISH</td></tr>
<tr><td><b>XAGUSD 44</b></td><td>76 LONG TRAP</td><td>-12K Cut +22K Short</td><td style='color:#FF2A2A'>BEARISH</td></tr>
<tr><td><b>US30 48</b></td><td>60 LONG</td><td>+15K Long +32K Asset</td><td style='color:#FFD60A'>NEUTRAL</td></tr>
<tr><td><b>NAS100 45</b></td><td>64 LONG TRAP</td><td>-18K Selloff</td><td style='color:#FF2A2A'>BEARISH</td></tr>
<tr><td><b>SP500 50</b></td><td>60 LONG</td><td>Flat Hedged</td><td style='color:#FFD60A'>NEUTRAL</td></tr>
<tr><td><b>GER30 44</b></td><td>55 LONG</td><td>-18K Short DAX</td><td style='color:#FF2A2A'>BEARISH</td></tr>
<tr><td><b>UK100 53</b></td><td>52 LONG</td><td>+12K Long FTSE</td><td style='color:#FFD60A'>NEUTRAL</td></tr>
<tr><td><b>EURUSD 39</b></td><td>68 LONG TRAP</td><td>-125K Short EUR</td><td style='color:#FF2A2A'>BEARISH</td></tr>
<tr><td><b>GBPUSD 42</b></td><td>65 LONG TRAP</td><td>-89K Short GBP</td><td style='color:#FF2A2A'>BEARISH</td></tr>
<tr><td><b>USDJPY 72</b></td><td>71 SHORT SQUEEZE</td><td>+148K Long DXY</td><td style='color:#22C55E'>BULLISH</td></tr>
<tr><td><b>OIL 68</b></td><td>58 SHORT SQUEEZE</td><td>+112K Long OPEC</td><td style='color:#22C55E'>BULLISH</td></tr>
</table></div>
""",unsafe_allow_html=True)

st.markdown("### ALL PAIRS - MACRO ENVIRONMENT - WHY BULLISH/BEARISH")
for k in ["EURUSD","GBPUSD","USDJPY","XAUUSD","XAGUSD","USDCAD","USDCHF","OILWTI","BTCUSD","US30","NAS100","SP500","GER30","UK100","DXY"]:
 st.markdown(gauge(DB[k],k),unsafe_allow_html=True)

if st.button("RE-SCAN"):
 st.rerun()

import streamlit as st, yfinance as yf, pandas as pd
import pytz
from datetime import datetime
st.set_page_config(page_title="FX AMBUSHERS", layout="wide")
st.markdown("<style>.stApp{background:#070709;color:#E8E6D9}.macro-card{background:#101018;border:1px solid #2A2A3A;border-radius:18px;padding:16px;margin:10px 0}.circle{width:80px;height:80px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-direction:column;font-weight:900}.why-box{background:#0F0F1A;border:1px solid #2A2A3A;border-radius:12px;padding:12px;font-size:11px}.cot-table{width:100%;border-collapse:collapse;font-size:11px}.cot-table th{background:#1A1A2E;padding:8px;color:#FFD60A;text-align:left}.cot-table td{padding:8px;border-bottom:1px solid #222}</style>", unsafe_allow_html=True)

DB = {
"EURUSD": {"s":39,"b":"BEARISH","bull":3,"bear":6,"tot":14,"bf":"GPR CB Buying","rf":"DXY 71 RealYield 4.2 Fed Hawk Oil MOVE","n":"VIX SP500 CPI Fed"},
"XAGUSD": {"s":44,"b":"BEARISH","bull":3,"bear":6,"tot":14,"bf":"GPR Industry CB Buying","rf":"DXY 71 KING RealYield 4.2 Fed Hawk SP500","n":"VIX CPI Oil Fed"},
"USDCAD": {"s":52,"b":"NEUTRAL","bull":5,"bear":5,"tot":14,"bf":"DXY 71 Fed Hawk CPI Yield","rf":"Brent 82 Bull CAD OPEC Cut CB Buying","n":"VIX SP500 GPR Gold"},
"DXY": {"s":71,"b":"BULLISH","bull":8,"bear":3,"tot":14,"bf":"Fed Hawk RealYield 4.2 CPI 3.7 SafeHaven COT 98K Long VIX 18 EUR PMI 44.2 Weak","rf":"Fed Cut Bets SP500 Rally Gold Bid","n":"GPR Oil BoJ Intervention"},
"XAUUSD": {"s":39,"b":"BEARISH","bull":3,"bear":6,"tot":14,"bf":"GPR CB Buying COT Longs","rf":"DXY 71 KING RealYield 4.2 Fed Hawk Oil MOVE","n":"VIX SP500 CPI GDX"},
"US30": {"s":48,"b":"NEUTRAL","bull":5,"bear":5,"tot":14,"bf":"Fed Pause CB Buying GPR Earnings COT 15K","rf":"DXY 71 RealYield 4.2 VIX Oil","n":"CPI Gold SP500 GLD"},
"NAS100": {"s":45,"b":"BEARISH","bull":3,"bear":6,"tot":14,"bf":"AI Demand CB Buying COT Longs","rf":"DXY 71 KING RealYield 4.2 Fed Hawk VIX MOVE","n":"SP500 CPI Oil Gold"},
"SP500": {"s":50,"b":"NEUTRAL","bull":5,"bear":5,"tot":14,"bf":"Fed Pause Buybacks GPR Earnings COT Longs","rf":"DXY 71 RealYield 4.2 Fed Hawk VIX","n":"CPI Oil Gold GLD"},
"GER30": {"s":44,"b":"BEARISH","bull":3,"bear":6,"tot":14,"bf":"ECB Dovish GPR CB Buying","rf":"DXY 71 KING RealYield PMI 44.2 Weak VIX","n":"SP500 CPI Oil Gold"},
"UK100": {"s":53,"b":"NEUTRAL","bull":5,"bear":4,"tot":14,"bf":"BoE Pause Oil 82 Bullish GBP Weak FTSE","rf":"DXY 71 RealYield UK PMI Brexit","n":"VIX SP500 CPI Gold"}
}

def macro_html(d,name):
 col="#22C55E" if d["b"]=="BULLISH" else "#FF2A2A" if d["b"]=="BEARISH" else "#FFD60A"
 return f"<div class='macro-card'><div style='text-align:center;color:#9AA0B3;font-size:12px'>{name} MACRO</div><div style='text-align:center'><span style='color:{col};font-weight:900;font-size:18px'>{d['b']}</span></div><div style='text-align:center;font-size:11px;color:#9AA0B3'>{d['bull']} bull - {d['bear']} bear of {d['tot']}</div><div style='display:flex;gap:12px;margin-top:10px'><div class='circle' style='border:4px solid #222;border-top:4px solid {col};border-right:4px solid {col}'><span style='font-size:22px;color:{col}'>{d['s']}</span><span style='font-size:10px'>/100</span></div><div class='why-box'><div style='color:#22C55E'>Bull: <span style='color:#CBD5E1'>{d['bf']}</span></div><div style='color:#FF2A2A;margin-top:6px'>Bear: <span style='color:#9AA0B3'>{d['rf']}</span></div><div style='color:#6B7280;margin-top:6px'>Neutral: {d['n']}</div></div></div></div>"

st.markdown("## DXY KING - DOLLAR INDEX GAUGE - 71 BULLISH")
st.markdown(macro_html(DB["DXY"],"DXY"), unsafe_allow_html=True)
st.markdown("## COT REPORT - XAUUSD XAGUSD US30 NAS100")
st.markdown("<div class='macro-card'><table class='cot-table'><tr><th>PAIR</th><th>RETAIL</th><th>SMART MONEY</th><th>BIAS</th></tr><tr><td><b>DXY 71</b></td><td>62pct SHORT SQUEEZE</td><td>+98K Long Most Bullish 6M</td><td style='color:#22C55E'>BULLISH KING</td></tr><tr><td><b>XAUUSD 39</b></td><td>82pct LONG TOP</td><td>-28K Cut Long +19K Short</td><td style='color:#FF2A2A'>BEARISH</td></tr><tr><td><b>XAGUSD 44</b></td><td>76pct LONG TRAP</td><td>-12K Cut +22K Short</td><td style='color:#FF2A2A'>BEARISH</td></tr><tr><td><b>US30 48</b></td><td>60pct LONG</td><td>+15K Long +32K Asset</td><td style='color:#FFD60A'>NEUTRAL</td></tr><tr><td><b>NAS100 45</b></td><td>64pct LONG TRAP</td><td>-18K Selloff DXY Bearish NAS</td><td style='color:#FF2A2A'>BEARISH</td></tr></table></div>", unsafe_allow_html=True)

for k in ["EURUSD","XAUUSD","XAGUSD","USDCAD","US30","NAS100","SP500","GER30","UK100","DXY"]:
 st.markdown(macro_html(DB[k],k), unsafe_allow_html=True)

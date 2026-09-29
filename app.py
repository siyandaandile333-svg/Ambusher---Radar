import streamlit as st, yfinance as yf, pandas as pd, pytz
from datetime import datetime
st.set_page_config(page_title="FX AMBUSHERS", layout="wide")
st.markdown("<style>.stApp{background:#070709;color:#E8E6D9}.macro-card{background:#101018;border:1px solid #2A2A3A;border-radius:18px;padding:16px;margin:10px 0}.circle{width:80px;height:80px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-direction:column;font-weight:900}.why-box{background:#0F0F1A;border:1px solid #2A2A3A;border-radius:12px;padding:12px;font-size:11px}.cot-table{width:100%;border-collapse:collapse;font-size:11px}.cot-table th{background:#1A1A2E;padding:8px;color:#FFD60A;text-align:left}.cot-table td{padding:8px;border-bottom:1px solid #222}</style>", unsafe_allow_html=True)
try:
 st.image("IMG-20260929-WA1810.jpg", width=340)
except:
 st.markdown("<h1 style='color:#FFD60A;text-align:center'>FX AMBUSHERS</h1>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center;color:#FFD60A;font-weight:900'>FX AMBUSHERS - MR SA DLAMINI</div>", unsafe_allow_html=True)
sa=datetime.now(pytz.timezone('Africa/Johannesburg')).strftime("%d %b %H:%M SA")
st.markdown(f"<div style='background:#111;border:1px solid #333;padding:6px 12px;font-size:11px'><span style='color:#FF2A2A'>PREDATOR MODE</span> <span style='color:#FFD60A'>{sa}</span></div><br>", unsafe_allow_html=True)
DB={}
DB["DXY"]={"s":71,"b":"BULLISH","bull":8,"bear":3,"tot":14,"bf":"Fed Hawk RealYield 4.2 CPI 3.7 SafeHaven COT 98K Long VIX 18 EUR PMI 44.2 Weak","rf":"Fed Cut Bets SP500 Rally Gold Bid","n":"GPR Oil BoJ Intervention"}
DB["XAUUSD"]={"s":39,"b":"BEARISH","bull":3,"bear":6,"tot":14,"bf":"GPR CB Buying COT Longs","rf":"DXY 71 KING RealYield 4.2 Fed Hawk","n":"VIX SP500 GDX"}
DB["XAGUSD"]={"s":44,"b":"BEARISH","bull":3,"bear":6,"tot":14,"bf":"GPR Industry CB Buying COT Longs","rf":"DXY 71 KING RealYield 4.2 Fed Hawk","n":"VIX CPI Oil"}
DB["US30"]={"s":48,"b":"NEUTRAL","bull":5,"bear":5,"tot":14,"bf":"Fed Pause CB Buying Earnings COT 15K Long","rf":"DXY 71 Bullish RealYield 4.2 VIX Oil","n":"CPI Gold SP500"}
DB["NAS100"]={"s":45,"b":"BEARISH","bull":3,"bear":6,"tot":14,"bf":"AI Demand CB Buying COT Longs","rf":"DXY 71 KING RealYield 4.2 Fed Hawk VIX","n":"SP500 CPI Oil"}
DB["SP500"]={"s":50,"b":"NEUTRAL","bull":5,"bear":5,"tot":14,"bf":"Fed Pause Buybacks Earnings COT Longs","rf":"DXY 71 Bullish RealYield 4.2 VIX","n":"CPI Oil Gold"}
DB["GER30"]={"s":44,"b":"BEARISH","bull":3,"bear":6,"tot":14,"bf":"ECB Dovish GPR CB Buying","rf":"DXY 71 KING RealYield 4.2 PMI 44.2 Weak","n":"SP500 CPI Oil"}
DB["UK100"]={"s":53,"b":"NEUTRAL","bull":5,"bear":4,"tot":14,"bf":"BoE Pause Oil 82 Bullish FTSE","rf":"DXY 71 Bullish RealYield 4.2 UK PMI","n":"VIX SP500 CPI"}
DB["EURUSD"]={"s":39,"b":"BEARISH","bull":3,"bear":6,"tot":14,"bf":"GPR CB Buying COT Longs","rf":"DXY 71 Bullish RealYield 4.2 Fed Hawk","n":"VIX SP500 CPI"}
DB["GBPUSD"]={"s":42,"b":"BEARISH","bull":4,"bear":6,"tot":14,"bf":"UK Wage GPR COT Longs","rf":"DXY 71 Bullish BoE Dovish UK CPI Low","n":"VIX Oil Fed"}
DB["USDJPY"]={"s":72,"b":"BULLISH","bull":8,"bear":3,"tot":14,"bf":"DXY 71 KING Fed Hawk BoJ Dovish COT 148K Long","rf":"Intervention Risk VIX JPY Safe Haven","n":"GPR SP500 CPI"}
DB["OILWTI"]={"s":68,"b":"BULLISH","bull":7,"bear":3,"tot":14,"bf":"GPR War Risk OPEC Cut Inventory Draw","rf":"DXY 71 Strong Fed Hawk RealYield 4.2","n":"VIX CPI Gold"}
def macro_html(d,name):
 col="#22C55E" if d["b"]=="BULLISH" else "#FF2A2A" if d["b"]=="BEARISH" else "#FFD60A"
 return f"<div class='macro-card'><div style='text-align:center;color:#9AA0B3;font-size:12px'>{name} MACRO</div><div style='text-align:center'><span style='color:{col};font-weight:900;font-size:18px'>{d['b']}</span></div><div style='text-align:center;font-size:11px;color:#9AA0B3'>{d['bull']} bull - {d['bear']} bear of {d['tot']}</div><div style='display:flex;gap:12px;margin-top:10px'><div class='circle' style='border:4px solid #222;border-top:4px solid {col};border-right:4px solid {col}'><span style='font-size:22px;color:{col}'>{d['s']}</span><span style='font-size:10px'>/100</span></div><div class='why-box'><div style='color:#22C55E'>Bull: <span style='color:#CBD5E1'>{d['bf']}</span></div><div style='color:#FF2A2A;margin-top:6px'>Bear: <span style='color:#9AA0B3'>{d['rf']}</span></div><div style='color:#6B7280;margin-top:6px'>Neutral: {d['n']}</div></div></div></div>"
if "page" not in st.session_state:
 st.session_state.page="home"
if st.session_state.page=="home":
 st.markdown("### DXY KING - 71 BULLISH - WHY BULLISH OR BEARISH LIKE PAIRS")
 st.markdown(macro_html(DB["DXY"],"DXY"), unsafe_allow_html=True)
 st.markdown("### COT INSTITUTIONAL REPORT - FULL - WITH DXY")
 st.markdown("<div class='macro-card'><table class='cot-table'><tr><th>PAIR</th><th>RETAIL</th><th>SMART MONEY</th><th>BIAS</th></tr><tr><td><b>DXY 71</b></td><td>62 SHORT SQUEEZE</td><td>+98K Long Most Bullish 6M</td><td style='color:#22C55E'>BULLISH KING</td></tr><tr><td><b>XAUUSD 39</b></td><td>82 LONG TOP TRAP</td><td>-28K Cut +19K Short</td><td style='color:#FF2A2A'>BEARISH</td></tr><tr><td><b>XAGUSD 44</b></td><td>76 LONG TRAP</td><td>-12K Cut +22K Short</td><td style='color:#FF2A2A'>BEARISH</td></tr><tr><td><b>US30 48</b></td><td>60 LONG</td><td>+15K Long +32K Asset</td><td style='color:#FFD60A'>NEUTRAL</td></tr><tr><td><b>NAS100 45</b></td><td>64 LONG TRAP</td><td>-18K Selloff DXY Bearish NAS</td><td style='color:#FF2A2A'>BEARISH</td></tr><tr><td><b>SP500 50</b></td><td>60 LONG</td><td>Flat Hedged</td><td style='color:#FFD60A'>NEUTRAL</td></tr><tr><td><b>GER30 44</b></td><td>55 LONG</td><td>-18K Short DAX Weak</td><td style='color:#FF2A2A'>BEARISH</td></tr><tr><td><b>UK100 53</b></td><td>52 LONG</td><td>+12K Long FTSE</td><td style='color:#FFD60A'>NEUTRAL</td></tr><tr><td><b>EURUSD 39</b></td><td>68 LONG TRAP</td><td>-125K Short EUR DXY Bull</td><td style='color:#FF2A2A'>BEARISH</td></tr><tr><td><b>GBPUSD 42</b></td><td>65 LONG TRAP</td><td>-89K Short GBP</td><td style='color:#FF2A2A'>BEARISH</td></tr><tr><td><b>USDJPY 72</b></td><td>71 SHORT SQUEEZE</td><td>+148K Long DXY Yield</td><td style='color:#22C55E'>BULLISH</td></tr><tr><td><b>OIL WTI 68</b></td><td>58 SHORT SQUEEZE</td><td>+112K Long OPEC Cut</td><td style='color:#22C55E'>BULLISH</td></tr></table></div>", unsafe_allow_html=True)
 for k in ["EURUSD","GBPUSD","USDJPY","XAUUSD","XAGUSD","OILWTI","US30","NAS100","SP500","GER30","UK100","DXY"]:
  st.markdown(macro_html(DB[k],k), unsafe_allow_html=True)
if st.button("RE-SCAN ALL MARKETS"):
 st.rerun()

import streamlit as st
import yfinance as yf
import pandas as pd
import pytz
from datetime import datetime
st.set_page_config(layout="wide")
st.markdown("<style>.stApp{background:#070709;color:#E8E6D9}.macro-card{background:#101018;border:1px solid #2A2A3A;border-radius:14px;padding:12px;margin:6px 0}.why{font-size:11px}</style>",unsafe_allow_html=True)
try:
 st.image("IMG-20260929-WA1810.jpg",width=340)
except:
 st.markdown("<h2 style='color:#FFD60A;text-align:center'>FX AMBUSHERS</h2>",unsafe_allow_html=True)
sa=datetime.now(pytz.timezone('Africa/Johannesburg')).strftime("%d %b %H:%M SA")
st.markdown("<div style='background:#111;padding:6px;color:#FFD60A;font-size:11px'>"+sa+"</div>",unsafe_allow_html=True)
DB={}
DB["DXY"]=["71","BULL","Fed Hawk No Cut Dot High + Yield 4.2 Up = USD Buy","Fed Cut + Gold Risk On = USD Sell","GPR Oil BoJ"]
DB["EURUSD"]=["39","BEAR","GPR CB Buy + Retail 68 Long Trap = Fake Up","DXY 71 Bull + Yield 4.2 US>EU + Hawk -125K Short = EUR Down","VIX SP500"]
DB["GBPUSD"]=["42","BEAR","UK Wage Strong + GPR 65 Long Trap = Fake Up","DXY 71 Bull + BoE Dov No Hike -89K Short = GBP Down","VIX Oil"]
DB["USDJPY"]=["72","BULL","DXY Bull + Fed Hawk High + BoJ Dov No Hike 148K Long = Up","BoJ Intervention + VIX Safe = Down","GPR"]
DB["XAUUSD"]=["39","BEAR","GPR War + CB Buy + 82 Long Top Trap = Fake Pump","DXY 71 Bull + Yield 4.2 Up Gold No Yield Sell + Hawk = Down","VIX GDX"]
DB["XAGUSD"]=["44","BEAR","GPR Industry + 76 Long Trap = Fake Up","DXY 71 Bull + Yield Up + Hawk -12K +22K Short = Down","VIX CPI"]
DB["USDCAD"]=["52","NEUT","DXY Bull + Fed Hawk + CPI High = USD Up","Oil 82 + OPEC Cut + CB Buy CAD = CAD Up","VIX GPR"]
DB["USDCHF"]=["61","BULL","DXY Bull + SNB Dov Cut + Yield 4.2 = CHF Down","CHF Safe + GPR Fear + Gold Up = CHF Up","SP500"]
DB["OILWTI"]=["68","BULL","GPR War + OPEC Cut + Draw = Oil Up","DXY Bull + Fed Hawk Demand Down = Oil Down","VIX"]
DB["BTCUSD"]=["54","NEUT","ETF Inflow + Halving Low Supply = Up","DXY Bull + Yield 4.2 Up Risk Off = Down","SP500"]
DB["US30"]=["48","NEUT","Fed Pause No Hike + Earn Up + 15K Long = Up","DXY Bull + Yield 4.2 + VIX + Oil = Down","CPI"]
DB["NAS100"]=["45","BEAR","AI Demand + CB + Long Trap = Fake Up","DXY Bull + Yield Up Tech Sell + Hawk -18K = Down","SP500"]
DB["SP500"]=["50","NEUT","Fed Pause + Buyback + Earn = Up","DXY Bull + Yield Up + VIX Fear = Down","CPI Oil"]
DB["GER30"]=["44","BEAR","ECB Dov Cut + GPR + PMI 44.2 Low = Fake Up","DXY Bull + Yield + COT -18K Short DAX = Down","SP500"]
DB["UK100"]=["53","NEUT","BoE Pause + Oil 82 + FTSE + 12K Long = Up","DXY Bull + Yield + PMI Low = Down","VIX"]
MP={"EURUSD":"EURUSD=X","GBPUSD":"GBPUSD=X","USDJPY":"USDJPY=X","XAUUSD":"GC=F","XAGUSD":"SI=F","USDCAD":"USDCAD=X","USDCHF":"USDCHF=X","OILWTI":"CL=F","BTCUSD":"BTC-USD","US30":"^DJI","NAS100":"^IXIC","SP500":"^GSPC","GER30":"^GDAXI","UK100":"^FTSE","DXY":"DX-Y.NYB"}
GR={"forex":["EURUSD","GBPUSD","USDJPY","USDCAD","USDCHF","DXY"],"commods":["XAUUSD","XAGUSD","OILWTI"],"crypto":["BTCUSD"],"indices":["US30","NAS100","SP500","GER30","UK100","DXY"]}
FUND=[["01 Oct","ISM PMI","HIGH","DXY"],["02 Oct","NFP Wage","HIGH","DXY GOLD"],["03 Oct","OPEC","HIGH","OIL"],["08 Oct","FOMC Min","HIGH","DXY"],["10 Oct","US CPI","CRIT","DXY GOLD"],["15 Oct","UK CPI","HIGH","GBP"],["17 Oct","EU CPI ECB","HIGH","EUR GER"],["24 Oct","US GDP","HIGH","DXY SP500"],["29 Oct","FOMC Powell","CRIT","ALL"],["30 Oct","BOJ Rate","HIGH","JPY"]]
def gauge(d,n):
 s=int(d[0])
 ang=-90 + s*1.8
 col="#22C55E" if d[1]=="BULL" else "#FF2A2A" if d[1]=="BEAR" else "#FFD60A"
 h="<div class='macro-card' style='text-align:center;border-left:4px solid "+col+"'>"
 h+="<div style='color:#9AA0B3;font-size:11px'>"+n+" AMBUSH METER</div>"
 h+="<div style='position:relative;width:200px;height:100px;margin:10px auto;background:conic-gradient(from 270deg at 50% 100%, #FF2A2A 0deg 70deg, #FFD60A 70deg 110deg, #22C55E 110deg 180deg);border-radius:200px 200px 0 0'></div>"
 h+="<div style='width:200px;height:0;margin:-50px auto 0;position:relative'>"
 h+="<div style='width:3px;height:85px;background:"+col+";transform:rotate("+str(ang)+"deg);transform-origin:bottom center;margin:0 auto;box-shadow:0 0 8px "+col+"'></div>"
 h+="<div style='width:12px;height:12px;background:"+col+";border-radius:50%;margin:-6px auto 0'></div></div>"
 h+="<div style='color:"+col+";font-weight:900;font-size:26px;margin-top:20px'>"+d[1]+" "+str(s)+"/100</div>"
 h+="<div style='display:flex;justify-content:space-between;font-size:10px;color:#666;width:200px;margin:0 auto'><span>0 BEAR</span><span>50</span><span>100 BULL</span></div>"
 h+="<div class='why' style='color:#22C55E;margin-top:8px;text-align:left'><b>Bull:</b> "+d[2]+"</div>"
 h+="<div class='why' style='color:#FF2A2A;text-align:left'><b>Bear:</b> "+d[3]+"</div>"
 h+="<div class='why' style='color:#6B7280;text-align:left'><b>Neu:</b> "+d[4]+"</div></div>"
 return h
if "page" not in st.session_state:
 st.session_state.page="home"
def show(lst,head):
 st.markdown("## "+head)
 for name in lst:
  d=DB[name]
  t=MP.get(name)
  try:
   df=yf.Ticker(t).history(period="1d",interval="5m")
   daily=yf.Ticker(t).history(period="5d")
   p=daily['Close'].iloc[-1]
  except:
   df=pd.DataFrame({"Close":[1]*40})
   p=0
  lab=d[1]+" "+name+" "+str(round(p,2))+" "+d[0]
  with st.expander(lab):
   try:
    c=df['Close'].dropna()
    c=c[c>0.5]
    st.line_chart(c.tail(100),height=120)
   except:
    st.line_chart(df['Close'],height=90)
   st.markdown(gauge(d,name),unsafe_allow_html=True)
if st.session_state.page=="home":
 st.markdown("### DXY 71 BULL - WHY EXPLAINED")
 st.markdown(gauge(DB["DXY"],"DXY"),unsafe_allow_html=True)
 c1,c2=st.columns(2)
 with c1:
  if st.button("FOREX 6"):
   st.session_state.page="forex"
   st.rerun()
  if st.button("INDICES"):
   st.session_state.page="indices"
   st.rerun()
  if st.button("INTEL NEWS"):
   st.session_state.page="news"
   st.rerun()
  if st.button("FUND DATES"):
   st.session_state.page="fund"
   st.rerun()
 with c2:
  if st.button("GOLD OIL"):
   st.session_state.page="commods"
   st.rerun()
  if st.button("CRYPTO"):
   st.session_state.page="crypto"
   st.rerun()
  if st.button("COT TABLE"):
   st.session_state.page="cot"
   st.rerun()
else:
 if st.button("BACK RADAR"):
  st.session_state.page="home"
  st.rerun()
 if st.session_state.page=="forex":
  show(GR["forex"],"FOREX DXY KING")
 if st.session_state.page=="commods":
  show(GR["commods"],"GOLD OIL TRAP")
 if st.session_state.page=="crypto":
  show(GR["crypto"],"CRYPTO AMBUSH")
 if st.session_state.page=="indices":
  show(GR["indices"],"INDICES HUNT")
 if st.session_state.page=="news":
  st.markdown("## INTEL NEWS")
  st.markdown("<div class='macro-card'>DXY 104.5 BULL 71 Fed hawk Yield 4.2 EUR BEAR 39 GOLD 82 TOP</div>",unsafe_allow_html=True)
 if st.session_state.page=="fund":
  st.markdown("## FUND DATES - FUTURE COMINGS")
  df=pd.DataFrame(FUND,columns=["DATE","EVENT","IMPACT","PAIR"])
  st.dataframe(df,hide_index=True,use_container_width=True)
 if st.session_state.page=="cot":
  st.markdown("## COT 12 PAIRS")
  rows=[["DXY 71","62 SHORT SQZ","98K Long Bull","BULL"],["XAU 39","82 LONG TOP","-28K +19K Short","BEAR"],["XAG 44","76 LONG TRAP","-12K +22K Short","BEAR"],["US30 48","60 LONG","15K +32K","NEUT"],["NAS 45","64 LONG TRAP","-18K Sell","BEAR"],["SP500 50","60 LONG","Flat","NEUT"],["GER 44","55 LONG","-18K DAX","BEAR"],["UK 53","52 LONG","12K FTSE","NEUT"],["EUR 39","68 LONG TRAP","-125K EUR","BEAR"],["GBP 42","65 LONG TRAP","-89K GBP","BEAR"],["JPY 72","71 SHORT SQZ","148K Long","BULL"],["OIL 68","58 SHORT SQZ","112K OPEC","BULL"]]
  df=pd.DataFrame(rows,columns=["PAIR","RETAIL","SMART","BIAS"])
  st.dataframe(df,hide_index=True,use_container_width=True)
if st.button("RE-SCAN"):
 st.rerun()

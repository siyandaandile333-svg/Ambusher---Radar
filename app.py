import streamlit as st,yfinance as yf,pandas as pd,pytz
from datetime import datetime
st.set_page_config(layout="wide")
st.markdown("<style>.stApp{background:#070709;color:#E8E6D9}.macro-card{background:#101018;border:1px solid #2A2A3A;border-radius:14px;padding:12px;margin:6px 0}</style>",unsafe_allow_html=True)
try:
 st.image("IMG-20260929-WA1810.jpg",width=340)
except:
 st.markdown("<h2 style='color:#FFD60A;text-align:center'>FX AMBUSHERS</h2>",unsafe_allow_html=True)
sa=datetime.now(pytz.timezone('Africa/Johannesburg')).strftime("%d %b %H:%M SA")
st.markdown("<div style='background:#111;padding:6px;color:#FFD60A'>"+sa+"</div>",unsafe_allow_html=True)
DB={}
DB["DXY"]=["71","BULL","Fed Hawk + Yield 4.2 Up","Fed Cut + Gold Risk On","GPR Oil"]
DB["EURUSD"]=["39","BEAR","GPR + 68 Long Trap Fake Up","DXY 71 + Yield + -125K Short","VIX"]
DB["GBPUSD"]=["42","BEAR","UK Wage + 65 Trap Fake Up","DXY + BoE Dov -89K Short","VIX Oil"]
DB["USDJPY"]=["72","BULL","DXY + Fed Hawk + BoJ Dov 148K","BoJ Intervention + VIX","GPR"]
DB["XAUUSD"]=["39","BEAR","GPR + CB Buy + 82 Top Trap Fake","DXY 71 + Yield Up + Hawk","VIX GDX"]
DB["XAGUSD"]=["44","BEAR","GPR + 76 Long Trap Fake","DXY 71 + Yield + -12K","VIX CPI"]
DB["USDCAD"]=["52","NEUT","DXY + Fed Hawk + CPI High","Oil 82 + OPEC + CB Buy CAD","VIX GPR"]
DB["USDCHF"]=["61","BULL","DXY + SNB Dov + Yield 4.2","CHF Safe + GPR + Gold Up","SP500"]
DB["OILWTI"]=["68","BULL","GPR War + OPEC Cut + Draw","DXY + Hawk Demand Down","VIX"]
DB["BTCUSD"]=["54","NEUT","ETF Inflow + Halving","DXY + Yield 4.2 Risk Off","SP500"]
DB["US30"]=["48","NEUT","Fed Pause + Earn + 15K Long","DXY + Yield 4.2 + VIX + Oil","CPI"]
DB["NAS100"]=["45","BEAR","AI Demand + Trap Fake Up","DXY + Yield Tech Sell + Hawk","SP500"]
DB["SP500"]=["50","NEUT","Fed Pause + Buyback + Earn","DXY + Yield + VIX Fear","CPI Oil"]
DB["GER30"]=["44","BEAR","ECB Dov + PMI 44.2 Low Fake Up","DXY + Yield + -18K Short","SP500"]
DB["UK100"]=["53","NEUT","BoE Pause + Oil 82 + 12K Long","DXY + Yield + PMI Low","VIX"]
MP={"EURUSD":"EURUSD=X","GBPUSD":"GBPUSD=X","USDJPY":"USDJPY=X","XAUUSD":"GC=F","XAGUSD":"SI=F","USDCAD":"USDCAD=X","USDCHF":"USDCHF=X","OILWTI":"CL=F","BTCUSD":"BTC-USD","US30":"^DJI","NAS100":"^IXIC","SP500":"^GSPC","GER30":"^GDAXI","UK100":"^FTSE","DXY":"DX-Y.NYB"}
GR={"forex":["EURUSD","GBPUSD","USDJPY","USDCAD","USDCHF","DXY"],"commods":["XAUUSD","XAGUSD","OILWTI"],"crypto":["BTCUSD"],"indices":["US30","NAS100","SP500","GER30","UK100","DXY"]}
FUND=[["01 Oct","ISM PMI","HIGH","DXY"],["02 Oct","NFP Wage","HIGH","DXY GOLD"],["03 Oct","OPEC","HIGH","OIL"],["08 Oct","FOMC Min","HIGH","DXY"],["10 Oct","US CPI","CRIT","DXY GOLD"],["15 Oct","UK CPI","HIGH","GBP"],["17 Oct","EU CPI ECB","HIGH","EUR GER"],["24 Oct","US GDP","HIGH","DXY SP500"],["29 Oct","FOMC Powell","CRIT","ALL"],["30 Oct","BOJ Rate","HIGH","JPY"]]
GLOSS={"Fed Hawk":["Fed NO CUT high rates","USD UP GOLD DOWN SP DOWN"],"Fed Cut":["Fed cutting low","USD DOWN GOLD UP SP UP"],"Yield 4.2 Up":["10yr yield rising","USD UP GOLD DOWN NAS DOWN"],"DXY 71 Bull":["Dollar bullish","EUR DOWN GBP DOWN GOLD DOWN"],"GPR War":["War fear","GOLD UP OIL UP USD UP"],"COT -125K":["Funds short EUR","EUR DOWN"],"Retail 68 Trap":["68% long at top","Fake Up then DOWN"],"82 Top":["82% long GOLD top","Pump then CRASH"],"BoJ Dov":["BoJ dovish","JPY DOWN USDJPY UP"],"Oil 82":["Oil high","OIL UP USDCAD DOWN"],"ETF Inflow":["BTC ETF buy","BTC UP"],"VIX Fear":["VIX high","SP DOWN GOLD UP"]}

def gauge(d,n):
 s=int(d[0])
 a=-90+s*1.8
 col="#22C55E" if d[1]=="BULL" else ("#FF2A2A" if d[1]=="BEAR" else "#FFD60A")
 t="<div class='macro-card' style='text-align:center;border-left:5px solid "+col+"'>"
 t+="<div style='color:#9AA0B3'>"+n+" AMBUSH</div>"
 t+="<div style='color:"+col+";font-size:28px;font-weight:900'>"+d[1]+" "+str(s)+"</div>"
 t+="<div style='position:relative;width:220px;height:110px;margin:0 auto'>"
 t+="<div style='width:220px;height:110px;background:conic-gradient(from 270deg at 50% 100%, #FF2A2A 0deg 72deg,#FFD60A 72deg 108deg,#22C55E 108deg 180deg);border-radius:220px 220px 0 0'></div>"
 t+="<div style='position:absolute;left:50%;bottom:0;width:3px;height:95px;background:white;transform:translateX(-50%) rotate("+str(a)+"deg);transform-origin:bottom'></div>"
 t+="<div style='position:absolute;left:50%;bottom:-6px;width:14px;height:14px;background:white;border-radius:50%;transform:translateX(-50%)'></div>"
 t+="</div>"
 t+="<div style='text-align:left;font-size:11px;color:#22C55E'>Bull: "+d[2]+"</div>"
 t+="<div style='text-align:left;font-size:11px;color:#FF2A2A'>Bear: "+d[3]+"</div>"
 t+="<div style='text-align:left;font-size:11px;color:#888'>Neu: "+d[4]+"</div></div>"
 return t

if "page" not in st.session_state:
 st.session_state.page="home"

def show(lst,head):
 st.markdown("## "+head)
 for name in lst:
  d=DB[name]
  t=MP.get(name)
  try:
   df=yf.Ticker(t).history(period="1d",interval="5m")
   p=yf.Ticker(t).history(period="5d")['Close'].iloc[-1]
   cl=df['Close'].dropna()
   cl=cl[cl>0]
  except:
   cl=pd.Series([1,2,3])
   p=0
  lab=d[1]+" "+name+" "+str(round(float(p),2))+" "+d[0]
  with st.expander(lab):
   st.line_chart(cl.tail(80),height=140)
   st.markdown(gauge(d,name),unsafe_allow_html=True)

if st.session_state.page=="home":
 st.markdown("### DXY 71 BULL")
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
  if st.button("LEARN WORDS"):
   st.session_state.page="gloss"
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
  show

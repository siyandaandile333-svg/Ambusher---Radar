import streamlit as st
import yfinance as yf
import pandas as pd
import pytz
from datetime import datetime
st.set_page_config(layout="wide")
st.markdown("<style>.stApp{background:#070709;color:#E8E6D9}.macro-card{background:#101018;border:1px solid #2A2A3A;border-radius:14px;padding:12px;margin:6px 0}.why{font-size:11px;line-height:1.3}</style>",unsafe_allow_html=True)
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
GLOSS={"Fed Hawk":["Fed says NO CUT, rates HIGH","USD UP, GOLD DOWN, SP500 DOWN - high rates = USD buys"],"Fed Cut":["Fed cutting rates LOW","USD DOWN, GOLD UP, SP500 UP - cheap money"],"Yield 4.2 Up":["US 10yr yield 4.2% rising","USD UP, GOLD DOWN, NAS DOWN - money goes to USD"],"DXY 71 Bull":["Dollar index 71 bullish","EUR DOWN, GBP DOWN, GOLD DOWN - strong dollar kills others"],"GPR War":["Geopolitical Risk war fear","GOLD UP, OIL UP, USD UP - safe haven buy"],"COT -125K Short":["Hedge funds -125K short EUR","EUR DOWN - smart money selling"],"Retail 68 Long Trap":["Retail 68% long at top","Fake Up then DOWN - crowd trapped"],"82 Long Top":["Retail 82% long GOLD at top","Fake Pump then CRASH - no buyers left"],"BoJ Dov":["Bank Japan dovish no hike","JPY DOWN, USDJPY UP - yen weak"],"Oil 82":["Oil $82 high","OIL UP, USDCAD DOWN - CAD follows oil"],"ETF Inflow":["BTC ETF inflow","BTC UP - more buyers"],"VIX Fear":["VIX fear high","SP500 DOWN, GOLD UP - fear = sell stocks"]}

def gauge(d,n):
 s=int(d[0])
 ang=-90 + s*1.8
 if d[1]=="BULL":
  col="#22C55E"
 else:
  if d[1]=="BEAR":
   col="#FF2A2A"
  else:
   col="#FFD60A"
 html = ""
 html += "<div class='macro-card' style='text-align:center;border-left:5px solid "+col+"'>"
 html += "<div style='color:#9AA0B3;font-size:11px'>"+n+" AMBUSH METER</div>"
 html += "<div style='color:"+col+";font-weight:900;font-size:28px;margin:6px 0'>"+d[1]+" "+str(s)+"/100</div>"
 html += "<div style='position:relative;width:220px;height:110px;margin:0 auto'>"
 html += "<div style='width:220px;height:110px;background:conic-gradient(from 270deg at 50% 100%, #FF2A2A 0deg 72deg, #FFD60A 72deg 108deg, #22C55E 108deg 180deg);border-radius:220px 220px 0 0'></div>"
 html += "<div style='position:absolute;left:50%;bottom:0;width:3px;height:95px;background:white;transform:translateX(-50%) rotate("+str(ang)+"deg);transform-origin:bottom center'></div>"
 html += "<div style='position:absolute;left:50%;bottom:-6px;width:14px;height:14px;background:white;border:3px solid "+col+";border-radius:50%;transform:translateX(-50%)'></div>"
 html += "</div>"
 html += "<div style='display:flex;justify-content:space-between;font-size:11px;color:#888;width:220px;margin:6px auto'><span>0 BEAR</span><span>50</span><span>100 BULL</span></div>"
 html += "<div style='margin-top:10px;text-align:left'>"
 html += "<div class='why'

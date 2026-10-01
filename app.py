import streamlit as st
from datetime import datetime, timedelta
import os
st.set_page_config(page_title="FX AMBUSHERS PRO", layout="wide")
if "page" not in st.session_state: st.session_state.page="home"
DXY=7
TM=(datetime.utcnow()+timedelta(hours=2)).strftime("%H:%M SAST")
st.success(f"LIVE v3 | {TM} | HOME = ALL PAIRS | PRO = SCORECARD")
def j(p,e): return " + ".join(p)+" = "+e
def gauge(t,s,bu,be,ne,sz=260):
 ang=s*9; col="#ffcc00";bcol="#ffcc00";bias="NEU"
 if s>=1: col="#00ff66";bcol="#00ff66";bias="BULL"
 elif s<=-1: col="#ff4444";bcol="#ff4444";bias="BEAR"
 h=sz//2
 a=f"<div style='border:1px solid #222;border-radius:18px;padding:12px;background:#0f1414;border-left:4px solid {bcol};margin-bottom:12px'>"
 b=f"<div style='text-align:center;color:#888;font-size:11px'>{t}</div>"
 c=f"<div style='text-align:center;color:{col};font-weight:900;font-size:20px'>{bias} {'+'+str(s) if s>0 else str(s)}</div>"
 d=f"<div style='width:{sz}px;height:{h}px;margin:8px auto;position:relative;background:conic-gradient(from 270deg at 50% 100%,#ff2b2b 0 60deg,#ffcc00 60deg 120deg,#00cc66 120deg 180deg);border-radius:{sz}px {sz}px 0 0'>"
 e=f"<div style='width:3px;height:{h-10}px;background:white;position:absolute;bottom:0;left:50%;transform-origin:bottom;transform:rotate({ang}deg)'></div></div>"
 f=f"<div style='font-size:11px;color:#00ff66'>Bull: {bu}</div><div style='font-size:11px;color:#ff6666'>Bear: {be}</div><div style='font-size:11px;color:#888'>Neu: {ne}</div></div>"
 return a+b+c+d+e+f

dxy_bu=j(["Powell Hawk No Cut","US CPI 3.2% Hot","US10Y 4.2% Up","BoJ Dovish"],"USD Buy")
dxy_be=j(["Powell Cut 25bps","Gold 2600 Risk On","BoJ Hawk Hike","Yield Down"],"USD Sell")
dxy_ne="FOMC Sep29 + NFP Oct3 + CPI Oct4"

forex=[("EURUSD",-7,j(["DXY +7","ECB Dovish","CPI Hot","Hawk"],"Sell"),j(["DXY -7","ECB Hawk"],"Buy"),"ECB+FOMC"),("GBPUSD",-7,j(["DXY +7","BoE Dovish","UK CPI Down"],"Sell"),j(["DXY -7","BoE Hawk"],"Buy"),"BoE+DXY"),("USDJPY",7,j(["DXY +7","BoJ Dovish","Yield Up"],"Buy"),j(["BoJ Hawk","Risk Off"],"Sell"),"BoJ"),("AUDUSD",-7,j(["DXY +7","China Down","Risk Off"],"Sell"),j(["DXY -7","Risk On"],"Buy"),"China"),("USDCHF",7,j(["DXY +7","SNB Dovish"],"Buy"),j(["SNB Hawk"],"Sell"),"SNB"),("USDCAD",7,j(["DXY +7","Oil Down"],"Buy"),j(["Oil Up","BoC Hawk"],"Sell"),"Oil")]
commod=[("GOLD",-7,j(["DXY +7","Yield Up","Risk Off"],"Sell"),j(["DXY -7","Fed Cut"],"Buy"),"DXY+CPI"),("SILVER",-7,j(["DXY +7","Gold Down"],"Sell"),j(["Gold Up"],"Buy"),"Gold"),("OIL",-2,j(["DXY +7","Supply Up"],"Sell"),j(["Demand Up","OPEC Cut"],"Buy"),"OPEC")]
indices=[("US30",-7,j(["Fed Cut","Earnings Beat"],"Buy"),j(["DXY +7","Hawk"],"Sell"),"FOMC"),("NAS100",-7,j(["Fed Cut","NVDA Beat"],"Buy"),j(["DXY +7","Yield Up"],"Sell"),"Earnings"),("SPX500",-7,j(["Fed Cut","Earnings Up"],"Buy"),j(["DXY +7","Hawk"],"Sell"),"FOMC")]
crypto=[("BTCUSD",-7,j(["Fed Cut","ETF Inflow"],"Buy"),j(["DXY +7","Risk Off"],"Sell"),"ETF"),("ETHUSD",-7,j(["Fed Cut","ETH ETF In"],"Buy"),j(["DXY +7","BTC Sell"],"Sell"),"BTC")]

all_assets={}
for p,s,bu,be,ne in forex: all_assets[p]=(s,bu,be,ne)
for p,s,bu,be,ne in commod: all_assets[p]=(s,bu,be,ne)
for p,s,bu,be,ne in indices: all_assets[p]=(s,bu,be,ne)
for p,s,bu,be,ne in crypto: all_assets[p]=(s,bu,be,ne)
all_assets["DXY"]=(DXY,dxy_bu,dxy_be,dxy_ne)

PRO_NEWS=[["GDP","5.6%","5.6%","0.0%","Jun 05","BULL"],["PMI","53.0","52.0","+1.0%","May 23","BULL"],["Retail Sales","0.8%","0.6%","+0.2%","May 29","BULL"],["Consumer Conf","103.0","101.0","+2.0%","May 28","BULL"],["JOLTS Job","8.06M","8.34M","-0.28M","Jun 04","BEAR"],["ADP Employ","152K","175K","-23K","Jun 05","BEAR"]]
PRO_CPI=[["CPI","3.4%","3.4%","0.0%","Aug 12","NEU"],["Core CPI","2.1%","2.0%","+0.1%","Aug 12","BULL"]]

# --- NAV ---
if st.session_state.page=="home":
 st.markdown("### HOME - ALL PAIRS + DXY")
 c1,c2=st.columns(2)
 if c1.button("SCORE FINDER - PRO", use_container_width=True): st.session_state.page="pro"; st.rerun()
 if c2.button("COT + RETAIL + SCHOOLS", use_container_width=True): st.session_state.page="tables"; st.rerun()
 st.markdown(gauge("DXY AMBUSH",DXY,dxy_bu,dxy_be,dxy_ne,280), unsafe_allow_html=True)
 cols=st.columns(2)
 i=0
 for p in all_assets:
  if p=="DXY": continue
  s,bu,be,ne=all_assets[p]
  with cols[i%2]: st.markdown(gauge(p,s,bu,be,ne,280), unsafe_allow_html=True)
  i+=1

elif st.session_state.page=="pro":
 if st.button("← BACK TO HOME - ALL PAIRS"): st.session_state.page="home"; st.rerun()
 st.markdown("<h2>SCORE FINDER - PRO</h2>", unsafe_allow_html=True)
 st.markdown("<div style='border:1px solid #333;border-radius:20px;padding:20px;background:#111616'><div style='color:#00ffd0;font-size:20px;font-weight:900'>EdgeFinder Score: 2</div><div style='margin-top:8px'>Technical: -3 (Very Bearish)</div><div>Sentiment: 1</div><div>Macro: 4</div><div style='height:1px;background:#222;margin:20px 0'></div><div style='color:#888'>Technicals</div><div>Very Bearish | 4H: Bearish | Seasonality: Bearish</div><div style='height:1px;background:#222;margin:20px 0'></div><div style='color:#888'>Levels</div><div>Support: $2450 | Resistance: $2550 | ATR: $18 | RSI: 68</div><div style='height:1px;background:#222;margin:20px 0'></div><div style='color:#888'>COT</div><div>Long 88.95% | Short 11.05% | Change -0.17% | Sep 04</div></div>", unsafe_allow_html=True)
 html="<div style='overflow-x:auto;margin-top:12px'><table style='width:100%;font-size:12px;border-collapse:collapse'><tr style='color:#888'><th>Indicator</th><th>Actual</th><th>Forecast</th><th>Surprise</th><th>Date</th><th>Bias</th></tr>"
 for r in PRO_NEWS:
  c="#00ff66" if r[5]=="BULL" else "#ff4444" if r[5]=="BEAR" else "#ffcc00"
  html+=f"<tr style='border-top:1px solid #222'><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td><td>{r[4]}</td><td style='color:{c}'>{r[5]}</td></tr>"
 for r in PRO_CPI:
  c="#00ff66" if r[5]=="BULL" else "#ffcc00"
  html+=f"<tr style='border-top:1px solid #222'><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td><td>{r[4]}</td><td style='color:{c}'>{r[5]}</td></tr>"
 html+="</table></div>"
 st.markdown(html, unsafe_allow_html=True)
 st.markdown("<div style='margin-top:12px;border:1px solid #222;border-radius:12px;padding:10px'><div>Crowd: Bullish vs Bearish | 65% Bull 35% Bear - Buy Dominant</div><div style='height:8px;background:#222;border-radius:4px;margin-top:6px'><div style='width:65%;height:8px;background:#00ff66;border-radius:4px'></div></div></div>", unsafe_allow_html=True)

elif st.session_state.page=="tables":
 if st.button("← BACK TO HOME - ALL PAIRS"): st.session_state.page="home"; st.rerun()
 st.subheader("COT + RETAIL + SCHOOLS")
 st.markdown("<div style='border-left:4px solid #00ff66;padding:10px;background:#0f1414;border-radius:10px;margin:6px 0'><b>DXY AMBUSH SCHOOL</b> DXY +7 = EURUSD SELL, USDJPY BUY, GOLD SELL</div><div style='border-left:4px solid #ff4444;padding:10px;background:#0f1414;border-radius:10px;margin:6px 0'><b>COT SCHOOL</b> 71% Long = Trap. Retail 70% Long = CONTRARIAN SELL</div><div style='border-left:4px solid #ffcc00;padding:10px;background:#0f1414;border-radius:10px;margin:6px 0'><b>NEWS SCHOOL</b> Actual vs Forecast = Surprise</div>", unsafe_allow_html=True)

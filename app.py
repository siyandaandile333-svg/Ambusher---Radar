import streamlit as st
from datetime import datetime, timedelta
st.set_page_config(page_title="FX AMBUSHERS PRO", layout="wide")
if "page" not in st.session_state: st.session_state.page="home"
DXY=7
TM=(datetime.utcnow()+timedelta(hours=2)).strftime("%H:%M SAST")
st.success(f"LIVE | {TM} | NFP Oct 2 CORRECTED")
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
dxy_ne="FOMC Sep17 + NFP Oct2 + CPI Oct3" # <-- FIXED

forex=[("EURUSD",-7,j(["DXY +7","ECB Dovish","CPI Hot"],"EUR Sell"),j(["DXY -7","ECB Hawk"],"EUR Buy"),"ECB+FOMC Sep17"),("GBPUSD",-7,j(["DXY +7","BoE Dovish"],"GBP Sell"),j(["DXY -7","BoE Hawk"],"GBP Buy"),"BoE"),("USDJPY",7,j(["DXY +7","BoJ Dovish","Yield Up"],"USDJPY Buy"),j(["BoJ Hawk"],"USDJPY Sell"),"BoJ"),("AUDUSD",-7,j(["DXY +7","China Down"],"AUD Sell"),j(["DXY -7","Risk On"],"AUD Buy"),"China"),("USDCHF",7,j(["DXY +7","SNB Dovish"],"USDCHF Buy"),j(["SNB Hawk"],"USDCHF Sell"),"SNB"),("USDCAD",7,j(["DXY +7","Oil Down"],"USDCAD Buy"),j(["Oil Up"],"USDCAD Sell"),"Oil")]
commod=[("GOLD",-7,j(["DXY +7","Yield Up"],"GOLD Sell"),j(["DXY -7","Fed Cut"],"GOLD Buy"),"NFP Oct2 + CPI Oct3"),("SILVER",-7,j(["DXY +7","Gold Down"],"SILVER Sell"),j(["Gold Up"],"SILVER Buy"),"Gold"),("OIL",-2,j(["DXY +7","Supply Up"],"OIL Sell"),j(["Demand Up"],"OIL Buy"),"OPEC")]
indices=[("US30",-7,j(["Fed Cut","Earnings Beat"],"US30 Buy"),j(["DXY +7","Hawk"],"US30 Sell"),"FOMC Sep17 + NFP Oct2"),("NAS100",-7,j(["Fed Cut","NVDA Beat"],"NAS100 Buy"),j(["DXY +7","Yield Up"],"NAS100 Sell"),"Yield"),("SPX500",-7,j(["Fed Cut","Earnings Up"],"SPX500 Buy"),j(["DXY +7","Hawk"],"SPX500 Sell"),"FOMC Sep17 + NFP Oct2"),("BTCUSD",-7,j(["Fed Cut","ETF Inflow"],"BTC Buy"),j(["DXY +7","Risk Off"],"BTC Sell"),"ETF"),("ETHUSD",-7,j(["Fed Cut","ETH ETF"],"ETH Buy"),j(["DXY +7","BTC Sell"],"ETH Sell"),"BTC")]

all_assets={}
for p,s,bu,be,ne in forex+commod+indices: all_assets[p]=(s,bu,be,ne)
all_assets["DXY"]=(DXY,dxy_bu,dxy_be,dxy_ne)
PRO_NEWS=[["GDP","5.6%","5.6%","0.0%","Jun 05","BULL"],["PMI","53.0","52.0","+1.0%","May 23","BULL"],["Retail Sales","0.8%","0.6%","+0.2%","May 29","BULL"],["JOLTS Job","8.06M","8.34M","-0.28M","Jun 04","BEAR"],["ADP Employ","152K","175K","-23K","Jun 05","BEAR"]]
PRO_CPI=[["CPI","3.4%","3.4%","0.0%","Aug 12","NEU"]]

if st.session_state.page=="home":
 st.markdown("### HOME - ALL PAIRS + DXY")
 c1,c2=st.columns(2)
 if c1.button("SCORE FINDER - PRO", use_container_width=True): st.session_state.page="pro"; st.rerun()
 if c2.button("COT + SCHOOLS", use_container_width=True): st.session_state.page="tables"; st.rerun()
 st.markdown(gauge("DXY AMBUSH",DXY,dxy_bu,dxy_be,dxy_ne,280), unsafe_allow_html=True)
 cols=st.columns(2); i=0
 for p in all_assets:
  if p=="DXY": continue
  s,bu,be,ne=all_assets[p]
  with cols[i%2]: st.markdown(gauge(p,s,bu,be,ne,280), unsafe_allow_html=True)
  i+=1
elif st.session_state.page=="pro":
 if st.button("← HOME - ALL PAIRS"): st.session_state.page="home"; st.rerun()
 pair=st.selectbox("SELECT PAIR - SEE IF BULL OR BEAR", ["GOLD","EURUSD","GBPUSD","USDJPY","AUDUSD","USDCHF","USDCAD","US30","NAS100","SPX500","BTCUSD","ETHUSD"])
 s,bu,be,ne=all_assets[pair]
 bias="BULLISH BUY" if s>=1 else "BEARISH SELL"
 col="#00ff66" if s>=1 else "#ff4444"
 st.markdown(f"<div style='border:2px solid {col};border-radius:16px;padding:14px;background:#0a1414;text-align:center'><div style='font-size:24px;color:{col};font-weight:900'>{pair} - {bias} {s:+d}</div><div style='color:#aaa'>DXY +7 = {pair} {'SELL' if s<0 else 'BUY'} | NFP Oct 2</div></div>", unsafe_allow_html=True)
 st.markdown(gauge(f"{pair} GAUGE",s,bu,be,ne,300), unsafe_allow_html=True)
 st.markdown(f"<div style='border:1px solid #333;border-radius:20px;padding:20px;background:#111616;margin-top:10px'><div style='color:#00ffd0;font-weight:900'>EdgeFinder Score for {pair}: 2</div><div>Technical: {s} (Very Bearish)</div><div>Sentiment: 1 | Macro: 4 | DXY: {DXY}</div><hr style='border-color:#222'><div>Very Bearish | 4H: Bearish | Seasonality: Bearish</div><hr style='border-color:#222'><div>Support: $2450 | Resistance: $2550 | ATR: $18 | RSI: 68</div><hr style='border-color:#222'><div>Long 88.95% | Short 11.05% | Change -0.17% | Sep 04</div></div>", unsafe_allow_html=True)
 html="<table style='width:100%;font-size:12px;border-collapse:collapse;margin-top:12px'><tr style='color:#888'><th>Indicator</th><th>Actual</th><th>Forecast</th><th>Surprise</th><th>Date</th><th>Bias</th></tr>"
 for r in PRO_NEWS+PRO_CPI:
  c="#00ff66" if r[5]=="BULL" else "#ff4444" if r[5]=="BEAR" else "#ffcc00"
  html+=f"<tr style='border-top:1px solid #222'><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td><td>{r[4]}</td><td style='color:{c}'>{r[5]}</td></tr>"
 html+="</table>"
 st.markdown(html, unsafe_allow_html=True)
elif st.session_state.page=="tables":
 if st.button("← HOME"): st.session_state.page="home"; st.rerun()
 st.info("COT + Retail + Schools - DXY 71% Long BULL | NFP Oct 2 + CPI Oct3 are HIGH impact")

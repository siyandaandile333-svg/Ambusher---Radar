import streamlit as st
import datetime
st.set_page_config(page_title="FX AMBUSHERS PRO",layout="wide")
TM=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
if "page" not in st.session_state: st.session_state.page="home"
def gauge(p,s,bu,be,ne,h=260):
 c="#00ff66" if s>=4 else "#ff4444" if s<=-4 else "#ffcc00"
 pct=int((s+8)/16*100)
 return f"<div style='border:1px solid #222;border-radius:14px;padding:10px;margin:6px;background:#0f1414;height:{h}px'><b>{p}</b> <span style='color:{c}'>{s:+d}</span><div style='height:6px;background:#222;border-radius:3px;margin:6px 0'><div style='width:{pct}%;height:6px;background:{c};border-radius:3px'></div></div><div style='font-size:11px;color:#aaa'>{bu}<br><br>{be}<br><span style='color:#666'>{ne}</span></div></div>"
def j(a,b): return f"BUY: {a} | SELL: {b}"
forex=[("EURUSD",-7,j("Fed Cut",""),j("DXY +7 + Hawk",""),"FOMC"),("GBPUSD",-7,j("Fed Cut",""),j("DXY +7",""),"BoE"),("USDJPY",7,j("DXY +7 + BoJ Dovish",""),j("Fed Cut",""),"BoJ"),("AUDUSD",-7,j("Fed Cut + Risk On",""),j("DXY +7",""),"China"),("USDCHF",7,j("DXY +7",""),j("Fed Cut",""),"SNB"),("USDCAD",7,j("DXY +7 + Oil Down",""),j("Oil Up",""),"Oil")]
commod=[("GOLD",-7,j("Fed Cut + DXY -7",""),j("DXY +7 + Yield Up",""),"CPI"),("SILVER",-7,j("Gold Up",""),j("DXY +7",""),"Gold"),("OIL",-2,j("Demand Up",""),j("Supply Up",""),"OPEC")]
indices=[("US30",-7,j("Fed Cut",""),j("DXY +7",""),"FOMC"),("NAS100",-7,j("Fed Cut",""),j("Yield Up",""),"Earnings"),("SPX500",-7,j("Fed Cut",""),j("Hawk",""),"NFP")]
crypto=[("BTCUSD",-7,j("ETF Inflow",""),j("Risk Off",""),"ETF"),("ETHUSD",-7,j("ETF In",""),j("BTC Sell",""),"BTC")]
all_assets={}
for p,s,bu,be,ne in forex+commod+indices+crypto: all_assets[p]=(s,bu,be,ne)

import streamlit as st
import datetime
st.set_page_config(page_title="FX AMBUSHERS RADAR", layout="wide")
TM=datetime.datetime.now().strftime("%Y-%m-%d %H:%M UTC")
if "page" not in st.session_state: st.session_state.page="home"
def j(a,b): return f"BUY: {a} | SELL: {b}"
def gauge(p,s,bu,be,ne,h=260):
    c="#00ff66" if s>=4 else "#ff4444" if s<=-4 else "#ffcc00" if s>0 else "#ffaa00"
    pct=int((s+8)/16*100)
    return f"<div style='border:1px solid #222;border-radius:14px;padding:10px;margin:6px;background:#0f1414;height:{h}px'><b>{p}</b> <span style='color:{c}'>{s:+d}</span><div style='height:6px;background:#222;border-radius:3px;margin:6px 0'><div style='width:{pct}%;height:6px;background:{c};border-radius:3px'></div></div><div style='font-size:11px;color:#aaa'>{bu}<br><br>{be}<br><br><span style='color:#888'>{ne}</span></div></div>"
DXY=7
dxy_bu="Powell Hawk + CPI 3.2% Hot + US10Y 4.2% Up"
dxy_be="Fed Cut + CPI Down + Risk On"
dxy_ne="FOMC Sep29 + NFP Oct3 + CPI Oct4"
forex=[("EURUSD",-7,j("Fed Cut + DXY -7",""),j("DXY +7 + Powell Hawk",""),"DXY + ECB"),("GBPUSD",-7,j("Fed Cut",""),j("DXY +7 + Hawk",""),"DXY + BoE"),("USDJPY",7,j("DXY +7 + BoJ Dovish",""),j("Fed Cut + BoJ Hawk",""),"BoJ + FOMC"),("AUDUSD",-7,j("Fed Cut + Risk On",""),j("DXY +7 + China Down",""),"China + DXY"),("USDCHF",7,j("DXY +7 + SNB Dovish",""),j("Fed Cut",""),"SNB"),("USDCAD",7,j("DXY +7 + Oil Down",""),j("Fed Cut + Oil Up",""),"Oil")]
commod=[("GOLD",-7,j("Fed Cut + DXY -7",""),j("DXY +7 + US10Y Up",""),"DXY + CPI"),("SILVER",-7,j("Fed Cut + Gold Up",""),j("DXY +7 + Gold Sell",""),"Gold"),("OIL",-2,j("Fed Cut + Demand",""),j("DXY +7 + Supply",""),"OPEC")]
indices=[("US30",-7,j("Fed Cut + Dow Earnings",""),j("DXY +7 + Hawk",""),"FOMC"),("NAS100",-7,j("Fed Cut + NVDA Beat",""),j("DXY +7 + Yield Up",""),"Earnings"),("SPX500",-7,j("Fed Cut + Earnings Up",""),j("DXY +7 + Hawk",""),"FOMC + NFP")]
crypto=[("BTCUSD",-7,j("Fed Cut + ETF Inflow",""),j("DXY +7 + Risk Off",""),"ETF"),("ETHUSD",-7,j("Fed Cut + ETF In",""),j("DXY +7 + BTC Sell",""),"ETF + BTC")]

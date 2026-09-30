import streamlit as st
from datetime import datetime, timedelta
st.set_page_config(page_title="FX AMBUSHERS", layout="wide")
if "page" not in st.session_state:
    st.session_state.page="home"
DXY=7
st.success("LIVE v2.3 FULL EDGEFINDER - FIXED")
def j(p,e):
    return " + ".join(p) + " = " + e
def gauge(t,s,bu,be,ne,sz=260):
    ang=s*9
    col="#00ff66" if s>=1 else "#ff4444" if s<=-1 else "#ffcc00"
    bcol=col
    bias="BULL" if s>=1 else "BEAR" if s<=-1 else "NEU"
    a="<div style='border:1px solid #222;border-radius:18px;padding:12px;background:#0f1414;border-left:4px solid "+bcol+";margin-bottom:12px'>"
    b="<div style='text-align:center;color:#888;font-size:11px'>"+t+"</div>"
    c="<div style='text-align:center;color:"+col+";font-weight:900;font-size:20px'>"+bias+" "+str(s)+"</div>"
    d="<div style='width:"+str(sz)+"px;height:"+str(sz//2)+"px;margin:8px auto;position:relative;background:conic-gradient(from 270deg at 50% 100%,#ff2b2b 0 60deg,#ffcc00 60deg 120deg,#00cc66 120deg 180deg);border-radius:"+str(sz)+"px "+str(sz)+"px 0 0'>"
    e="<div style='width:3px;height:120px;background:white;position:absolute;bottom:0;left:50%;transform-origin:bottom;transform:rotate("+str(ang)+"deg)'></div></div>"
    f="<div style='font-size:11px;color:#00ff66'>Bull: "+bu+"</div><div style='font-size:11px;color:#ff6666'>Bear: "+be+"</div><div style='font-size:11px;color:#888'>Neu: "+ne+"</div></div>"
    return a+b+c+d+e+f
def badge(label):
    l=str(label)
    if "Very Bearish" in l:
        return "<span style='background:#7f1d1d;color:#fecaca;padding:2px 6px;border-radius:4px'>"+l+"</span>"
    if "Bearish" in l or "BEAR" in l or "SELL" in l:
        return "<span style='background:#450a0a;color:#fca5a5;padding:2px 6px;border-radius:4px'>"+l+"</span>"
    if "Very Bullish" in l:
        return "<span style='background:#1e3a8a;color:#bfdbfe;padding:2px 6px;border-radius:4px'>"+l+"</span>"
    if "Bullish" in l or "BULL" in l or "BUY" in l:
        return "<span style='background:#172554;color:#93c5fd;padding:2px 6px;border-radius:4px'>"+l+"</span>"
    return "<span style='background:#1f2937;color:#9ca3af;padding:2px 6px;border-radius:4px'>"+l+"</span>"

dxy_bu=j(["Powell Hawk No Cut","US CPI 3.2% Hot","US10Y 4.2% Up","BoJ Dovish"],"USD Buy")
dxy_be=j(["Powell Cut 25bps","Gold 2600 Risk On","BoJ Hawk Hike","Yield Down"],"USD Sell")
dxy_ne="FOMC Sep29 HIGH + NFP Oct3 + CPI Oct4"
st.markdown(gauge("DXY AMBUSH",DXY,dxy_bu,dxy_be,dxy_ne,280), unsafe_allow_html=True)

forex=[
 ("EURUSD",-7,j(["ECB Hawk","EU CPI

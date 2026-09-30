import streamlit as st
st.set_page_config(page_title="FX AMBUSHERS", layout="wide")
if "page" not in st.session_state:
    st.session_state.page="home"
DXY=7
st.success("LIVE v2.4 NO NESTED QUOTES - FIXED")

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

def badge(l):
    l=str(l)
    if "Very Bearish" in l:
        return "<span style='background:#7f1d1d;color:#fecaca;padding:2px 6px;border-radius:4px'>"+l+"</span>"
    if "Bearish" in l or "BEAR" in l or "SELL" in l:
        return "<span style='background:#450a0a;color:#fca5a5;padding:2px 6px;border-radius:4px'>"+l+"</span>"
    if "Very Bullish" in l:
        return "<span style='background:#1e3a8a;color:#bfdbfe;padding:2px 6px;border-radius:4px'>"+l+"</span>"
    if "Bullish" in l or "BULL" in l or "BUY" in l:
        return "<span style='background:#172554;color:#93c5fd;padding:2px 6px;border-radius:4px'>"+l+"</span>"
    return "<span style='background:#1f2937;color:#9ca3af;padding:2px 6px;border-radius:4px'>"+l+"</span>"

dxy_bu="Powell Hawk No Cut + US CPI 3.2 Hot + US10Y 4.2 Up + BoJ Dovish = USD Buy"
dxy_be="Powell Cut 25bps + Gold 2600 Risk On + BoJ Hawk Hike + Yield Down = USD Sell"
dxy_ne="FOMC Sep29 HIGH + NFP Oct3 + CPI Oct4"
st.markdown(gauge("DXY AMBUSH",DXY,dxy_bu,dxy_be,dxy_ne,280), unsafe_allow_html=True)

forex=[
 ("EURUSD",-7,"ECB Hawk + EU CPI 2.4 Hot + EU GDP Strong + Fed Cut = EUR Buy","Powell Hawk No Cut + DXY +7 Bull + US10Y 4.2 Up + CPI 3.2 = EUR Sell","ECB Oct5 + CPI Oct4"),
 ("GBPUSD",-7,"BoE Hawk + UK CPI 3.8 Hot + UK Wage Up + Fed Cut = GBP Buy","Fed Hawk No Cut + DXY +7 + Yield Up + UK Recession = GBP Sell","BoE Oct5 + FOMC"),
 ("USDJPY",7,"DXY +7 Bull + BoJ Dovish + US-JP Gap 4.2 = USDJPY Buy","BoJ Hawk Hike + Ueda Hawk + Fed Cut + Risk Off = Sell","BoJ Oct4 HIGH"),
 ("AUDUSD",-7,"RBA Hawk + Gold 2600 Up + China Stimulus + Iron Up = AUD Buy","DXY +7 + Risk Off + China PMI Weak + Iron Down = AUD Sell","RBA + China PMI"),
 ("USDCHF",7,"DXY +7 Bull + SNB Dovish + Safe Off + Gold Down = Buy","SNB Hawk + Fed Cut + Gold 2600 Up + Risk Off = Sell","SNB + Gold"),
 ("USDCAD",6,"DXY +7 Bull + Oil 70 Down + BoC Dovish = Buy","Oil 85

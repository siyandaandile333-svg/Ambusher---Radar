import streamlit as st
st.set_page_config(layout="wide")
if "page" not in st.session_state:
    st.session_state.page="home"
DXY=7
st.success("LIVE v2.6 AMBUSH-FINDER - FIXED")

def gauge(t,s,bu,be,ne,sz=200):
    col="#0f6" if s>=1 else "#f44" if s<=-1 else "#fc0"
    a="<div style='border:1px solid #222;"
    a+="border-radius:12px;padding:8px'>"
    b="<div style='color:"+col+"'>"+t+" "+str(s)+"</div>"
    c="<div style='font-size:10px'>"+bu+"</div>"
    d="<div style='font-size:10px'>"+be+"</div></div>"
    return a+b+c+d

def badge(l):
    l=str(l)
    if "Bearish" in l or "BEAR" in l or "SELL" in l:
        return "<span style='background:#450a0a;color:#fca5a5;padding:2px 6px'>"+l+"</span>"
    if "Bullish" in l or "BULL" in l or "BUY" in l:
        return "<span style='background:#172554;color:#93c5fd;padding:2px 6px'>"+l+"</span>"
    return "<span style='background:#1f2937;color:#aaa;padding:2px 6px'>"+l+"</span>"

dxy_bu="Powell Hawk = USD Buy"
dxy_be="Powell Cut = USD Sell"
dxy_ne="FOMC HIGH"
st.markdown(gauge("DXY",DXY,dxy_bu,dxy_be,dxy_ne,260),unsafe_allow_html=True)

forex=[]
forex.append(("EURUSD",-7,"EUR Buy","EUR Sell","ECB"))
forex.append(("GBPUSD",-7,"GBP Buy","GBP Sell","BoE"))
forex.append(("USDJPY",7,"JPY Sell","JPY Buy","BoJ"))
forex.append(("AUDUSD",-7,"AUD Buy","AUD Sell","RBA"))
forex.append(("USDCHF",7,"CHF Sell","CHF Buy","SNB"))
forex.append(("USDCAD",6,"CAD Sell","CAD Buy","BoC"))

commod=[]
commod.append(("GOLD",-8,"Gold Buy","Gold Sell","GPR"))
commod.append(("SILVER",-7,"Silver Buy","Silver Sell","Gold"))
commod.append(("OIL",-3,"Oil Buy","Oil Sell","OPEC"))

indices=[]
indices.append(("US30",-7,"US30 Buy","US30 Sell","FOMC"))
indices.append(("NAS100",-7,"NAS Buy","NAS Sell","FOMC"))
indices.append(("SPX500",-7,"SPX Buy","SPX Sell","FOMC"))

crypto=[]
crypto.append(("BTCUSD",-7,"BTC Buy","BTC Sell","ETF"))
crypto.append(("ETHUSD",-7,"ETH Buy","ETH Sell","ETF"))

cot=[]
cot.append(["DXY","71%","29%","+3% Long","BULL","Hawk"])
cot.append(["EURUSD","29%","71%","+4% Short","BEAR","DXY"])
cot.append(["GBPUSD","30%","70%","+2% Short","BEAR","DXY"])
cot.append(["USDJPY","71%","29%","+2% Long","BULL","BoJ"])
cot.append(["GOLD","25%","75%","+5% Short","BEAR","DXY"])
cot.append(["BTCUSD","30%","70%","+2% Short","BEAR","Risk"])

retail=[]
retail.append(["EURUSD","70%","30%","SELL","Crowd Long"])
retail.append(["GOLD","75%","25%","SELL","Top"])
retail.append(["BTCUSD

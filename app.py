import streamlit as st
import pandas as pd
import os, glob

st.set_page_config(page_title="FX AMBUSHERS", layout="wide")
st.markdown("<style>.stApp{background:#080a0a}</style>", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page="home"

def rerun():
    try:
        st.rerun()
    except:
        st.experimental_rerun()

SCORE=71
BIAS="BULL"
ANGLE=-90+(SCORE*1.8)

def show():
    # LOGO - find any image
    img=None
    for f in ["logo.png","logo.jpg","IMG-20260929-WA1810.jpg","IMG-20260929-WA1810.jpeg"]:
        if os.path.exists(f):
            img=f
            break
    if not img:
        all_imgs=glob.glob("*.jpg")+glob.glob("*.png")+glob.glob("*.jpeg")
        if all_imgs:
            img=all_imgs[0]
    if img:
        st.image(img, use_container_width=True)
    else:
        st.markdown("<h2 style='color:#d4af37;text-align:center'>FX AMBUSHERS</h2>", unsafe_allow_html=True)

    st.markdown(f"""
<div style='border:1px solid #222;border-radius:20px;padding:15px;background:#0f1414;border-left:4px solid #00ff66'>
<div style='text-align:center;color:#888;letter-spacing:2px'>DXY AMBUSH</div>
<div style='text-align:center;color:#00ff66;font-size:32px;font-weight:900'>{BIAS} {SCORE}</div>
<div style='width:260px;height:130px;margin:0 auto;position:relative;background:conic-gradient(from 270deg at 50% 100%, #ff2b2b 0deg 60deg, #ffcc00 60deg 120deg, #00cc66 120deg 180deg);border-radius:130px 130px 0 0'>
<div style='width:3px;height:110px;background:white;position:absolute;bottom:0;left:50%;transform-origin:bottom;transform:rotate({ANGLE}deg)'></div>
<div style='width:12px;height:12px;background:white;border-radius:50%;position:absolute;bottom:-6px;left:calc(50% - 6px)'></div>
</div>
<div style='font-size:12px;margin-top:10px;color:#00ff66'>Bull: Fed Hawk No Cut Dot High + Yield 4.2 Up = USD Buy</div>
<div style='font-size:12px;color:#ff4444'>Bear: Fed Cut + Gold Risk On = USD Sell</div>
<div style='font-size:12px;color:#888'>Neu: GPR Oil BoJ Rate</div>
</div>
""", unsafe_allow_html=True)

show()

if st.session_state.page=="home":
    if st.button("FOREX 6"):
        st.session_state.page="forex"
        rerun()
    if st.button("INDICES"):
        st.session_state.page="indices"
        rerun()
    if st.button("INTEL NEWS"):
        st.session_state.page="news"
        rerun()
    if st.button("FUND DATES"):
        st.session_state.page="fund"
        rerun()
    if st.button("LEARN WORDS"):
        st.session_state.page="words"
        rerun()
    if st.button("GOLD OIL"):
        st.session_state.page="gold"
        rerun()
    if st.button("CRYPTO"):
        st.session_state.page="crypto"
        rerun()
    if st.button("COT TABLE"):
        st.session_state.page="cot"
        rerun()
else:
    if st.button("BACK RADAR"):
        st.session_state.page="home"
        rerun()
    show()
    if st.session_state.page=="forex":
        st.markdown("### FOREX 6 - WHY BULLISH / BEARISH")
        st.table(pd.DataFrame([["EURUSD","SELL","DXY Bull 71 + Fed Hawk = USD Buy"],["GBPUSD","SELL","DXY Bull + Yield 4.2 Up"],["USDJPY","BUY","DXY Bull + BoJ Dovish"],["AUDUSD","SELL","DXY Bull + Risk Off"],["USDCHF","BUY","DXY Bull 71"],["USDCAD","BUY","DXY Bull + Oil Down"]], columns=["Pair","Bias","Why"]))
    if st.session_state.page=="gold":
        st.table(pd.DataFrame([["GOLD","SELL","DXY Bull 71 + Yield Up"],["OIL","SELL","GPR Low"]], columns=["Pair","Bias","Why"]))
    if st.session_state.page=="indices":
        st.table(pd.DataFrame([["US30","SELL","DXY Bull"]], columns=["Pair","Bias","Why"]))
    if st.session_state.page=="crypto":
        st.table(pd.DataFrame([["BTCUSD","SELL","DXY Bull"]], columns=["Pair","Bias","Why"]))
    if st.session_state.page=="cot":
        st.table(pd.DataFrame([["DXY","LONG 71%","Fed Hawk"]], columns=["Asset","COT","Why"]))
    if st.session_state.page=="news":
        st.write("INTEREST RATE: High = DXY UP. CPI: High CPI = DXY UP. FOMC = Biggest move. NFP = Jobs")
    if st.session_state.page=="fund":
        st.table(pd.DataFrame([["2026-09-29","FOMC","HIGH"]], columns=["Date","News","Impact"]))
    if st.session_state.page=="words":
        st.write("BOS=Break of Structure, CHoCH=Change of Character, OB=Order Block, FVG=Gap")

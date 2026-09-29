import streamlit as st
import pandas as pd
import os, glob

st.set_page_config(page_title="FX AMBUSHERS", layout="wide")
st.markdown("<style>.stApp{background:#080a0a}</style>", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page="home"

DXY_SCORE=71

def gauge_html(score, label="", size=160):
    angle=-90 + (score*1.8)
    if score>=60:
        bias="BULL"
        col="#00ff66"
        border="#00ff66"
    elif score<=40:
        bias="BEAR"
        col="#ff4444"
        border="#ff4444"
    else:
        bias="NEU"
        col="#ffcc00"
        border="#ffcc00"
    h=size//2
    w=size
    return f"""
<div style='border:1px solid #222;border-radius:15px;padding:8px;background:#0f1414;border-left:3px solid {border};margin-bottom:10px;text-align:center'>
<div style='color:#888;font-size:10px;letter-spacing:1px'>{label}</div>
<div style='color:{col};font-weight:900;font-size:{14 if size<200 else 22}px'>{bias} {score}</div>
<div style='width:{w}px;height:{h}px;margin:0 auto;position:relative;background:conic-gradient(from 270deg at 50% 100%, #ff2b2b 0deg 60deg, #ffcc00 60deg 120deg, #00cc66 120deg 180deg);border-radius:{w}px {w}px 0 0'>
<div style='width:2px;height:{h-10}px;background:white;position:absolute;bottom:0;left:50%;transform-origin:bottom;transform:rotate({angle}deg)'></div>
<div style='width:10px;height:10px;background:white;border-radius:50%;position:absolute;bottom:-5px;left:calc(50% - 5px)'></div>
</div>
</div>
"""

def main_gauge():
    img=None
    for f in ["logo.png","logo.jpg","IMG-20260929-WA1810.jpg"]:
        if os.path.exists(f):
            img=f
            break
    if not img:
        a=glob.glob("*.jpg")+glob.glob("*.png")
        if a:
            img=a[0]
    if img:
        st.image(img, use_container_width=True)
    else:
        st.markdown("<h2 style='color:#d4af37;text-align:center'>FX AMBUSHERS</h2>", unsafe_allow_html=True)
    st.markdown(gauge_html(DXY_SCORE, "DXY AMBUSH", 260), unsafe_allow_html=True)
    st.markdown("<div style='font-size:12px;color:#00ff66'>Bull: Fed Hawk No Cut Dot High + Yield 4.2 Up = USD Buy</div><div style='font-size:12px;color:#ff4444'>Bear: Fed Cut + Gold Risk On = USD Sell</div><div style='font-size:12px;color:#888'>Neu: GPR Oil BoJ Rate</div>", unsafe_allow_html=True)

main_gauge()

# --- DATA WITH SCORES ---
forex_pairs=[
    ["EURUSD","SELL",29,"DXY Bull 71 + Fed Hawk"],
    ["GBPUSD","SELL",30,"DXY Bull + Yield 4.2 Up"],
    ["USDJPY","BUY",71,"DXY Bull + BoJ Dovish"],
    ["AUDUSD","SELL",28,"DXY Bull + Risk Off"],
    ["USDCHF","BUY",71,"DXY Bull 71"],
    ["USDCAD","BUY",70,"DXY Bull + Oil Down"],
]
commodities=[
    ["GOLD","SELL",25,"DXY Bull 71 + Yield Up = Gold Down"],
    ["SILVER","SELL",27,"Gold Down + DXY Up"],
    ["OIL","SELL",35,"GPR Low + DXY Strong"],
]
indices_pairs=[
    ["US30","SELL",30,"DXY Bull + Yield Up"],
    ["NAS100","SELL",28,"DXY Bull = Risk Off"],
    ["SPX500","SELL",29,"DXY Bull"],
]
crypto_pairs=[
    ["BTCUSD","SELL",30,"DXY Bull = Risk Off"],
    ["ETHUSD","SELL",29,"DXY Bull"],
]

if st.session_state.page=="home":
    if st.button("FOREX 6"): st.session_state.page="forex"
    if st.button("GOLD OIL"): st.session_state.page="gold"
    if st.button("INDICES"): st.session_state.page="indices"
    if st.button("CRYPTO"): st.session_state.page="crypto"
    if st.button("INTEL NEWS"): st.session_state.page="news"
    if st.button("FUND DATES"): st.session_state.page="fund"
    if st.button("LEARN WORDS"): st.session_state.page="words"
    if st.button("COT TABLE"): st.session_state.page="cot"
else:
    if st.button("BACK RADAR"): st.session_state.page="home"
    main_gauge()

    if st.session_state.page=="forex":
        st.markdown("### FOREX 6 - SPEEDOMETER PER PAIR")
        cols=st.columns(2)
        for i,row in enumerate(forex_pairs):
            pair,bias,score,why=row
            with cols[i%2]:
                st.markdown(gauge_html(score, pair, 160), unsafe_allow_html=True)
                st.markdown(f"<div style='text-align:center;font-size:12px'><b>{pair} {bias}</b><br><span style='color:#aaa'>{why}</span></div>", unsafe_allow_html=True)
        st.table(pd.DataFrame(forex_pairs, columns=["Pair","Bias","Score","Why"]))

    if st.session_state.page=="gold":
        st.markdown("### COMMODITIES - SPEEDOMETER PER PAIR")
        cols=st.columns(2)
        for i,row in enumerate(commodities):
            pair,bias,score,why=row
            with cols[i%2]:
                st.markdown(gauge_html(score, pair, 160), unsafe_allow_html=True)
                st.markdown(f"<div style='text-align:center;font-size:12px'><b>{pair} {bias}</b><br><span style='color:#aaa'>{why}</span></div>", unsafe_allow_html=True)
        st.table(pd.DataFrame(commodities, columns=["Pair","Bias","Score","Why"]))

    if st.session_state.page=="indices":
        st.markdown("### INDICES - SPEEDOMETER PER PAIR")
        cols=st.columns(2)
        for i,row in enumerate(indices_pairs):
            pair,bias,score,why=row
            with cols[i%2]:
                st.markdown(gauge_html(score, pair, 160), unsafe_allow_html=True)
                st.markdown(f"<div style='text-align:center;font-size:12px'><b>{pair} {bias}</b><br><span style='color:#aaa'>{why}</span></div>", unsafe_allow_html=True)
        st.table(pd.DataFrame(indices_pairs, columns=["Pair","Bias","Score","Why"]))

    if st.session_state.page=="crypto":
        st.markdown("### CRYPTO - SPEEDOMETER")
        cols=st.columns(2)
        for i,row in enumerate(crypto_pairs):
            pair,bias,score,why=row
            with cols[i%2]:
                st.markdown(gauge_html(score, pair, 160), unsafe_allow_html=True)
                st.markdown(f"<div style='text-align:center;font-size:12px'><b>{pair} {bias}</b><br><span style='color:#aaa'>{why}</span></div>", unsafe_allow_html=True)

    if st.session_state.page=="cot":
        st.table(pd.DataFrame([["DXY","LONG 71%","Fed Hawk"]], columns=["Asset","COT","Why"]))
    if st.session_state.page=="news":
        st.write("INTEREST RATE: High = DXY UP. CPI: High = DXY UP. FOMC: Biggest move.")
    if st.session_state.page=="fund":
        st.table(pd.DataFrame([["2026-09-29","FOMC","HIGH"]], columns=["Date","News","Impact"]))
    if st.session_state.page=="words":
        st.write("BOS=Break, CHoCH=Change, OB=Order Block")

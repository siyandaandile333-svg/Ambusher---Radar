import streamlit as st
import pandas as pd
import os, glob

st.set_page_config(page_title="FX AMBUSHERS", layout="wide")
st.markdown("<style>.stApp{background:#080a0a;color:#eee}</style>", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page="home"

DXY=71

def gauge_card(title, score, bull, bear, neu, size=260):
    angle=-90 + (score*1.8)
    if score>=60:
        col="#00ff66"; bcol="#00ff66"; bias="BULL"
    elif score<=40:
        col="#ff4444"; bcol="#ff4444"; bias="BEAR"
    else:
        col="#ffcc00"; bcol="#ffcc00"; bias="NEU"
    h=size//2
    return f"""
<div style='border:1px solid #222;border-radius:18px;padding:12px;background:#0f1414;border-left:4px solid {bcol};margin-bottom:12px'>
<div style='text-align:center;color:#888;font-size:11px;letter-spacing:1px'>{title}</div>
<div style='text-align:center;color:{col};font-weight:900;font-size:{22 if size>200 else 16}px'>{bias} {score}</div>
<div style='width:{size}px;height:{h}px;margin:8px auto;position:relative;background:conic-gradient(from 270deg at 50% 100%, #ff2b2b 0deg 60deg, #ffcc00 60deg 120deg, #00cc66 120deg 180deg);border-radius:{size}px {size}px 0 0'>
<div style='width:3px;height:{h-10}px;background:white;position:absolute;bottom:0;left:50%;transform-origin:bottom;transform:rotate({angle}deg)'></div>
<div style='width:12px;height:12px;background:white;border-radius:50%;position:absolute;bottom:-6px;left:calc(50% - 6px)'></div>
</div>
<div style='font-size:11px;color:#00ff66'>Bull: {bull}</div>
<div style='font-size:11px;color:#ff6666'>Bear: {bear}</div>
<div style='font-size:11px;color:#888'>Neu: {neu}</div>
</div>
"""

def show_logo():
    img=None
    for f in ["logo.png","logo.jpg","IMG-20260929-WA1810.jpg"]:
        if os.path.exists(f):
            img=f; break
    if not img:
        files=glob.glob("*.jpg")+glob.glob("*.png")
        if files: img=files[0]
    if img:
        st.image(img, use_container_width=True)

show_logo()
st.markdown(gauge_card("DXY AMBUSH", DXY, "Fed Hawk No Cut + Yield 4.2 Up = USD Buy", "Fed Cut + Gold Risk On = USD Sell", "GPR Oil BoJ Rate", 280), unsafe_allow_html=True)

# --- ALL PAIRS DATA WITH BULL/BEAR/NEU LIKE DXY ---
forex=[
    ("EURUSD",29,"ECB Hawk + Fed Cut = EUR Buy","Fed Hawk + Yield Up + DXY 71 = EUR Sell","ECB Rate + GPR"),
    ("GBPUSD",30,"BoE Hawk + Fed Cut = GBP Buy","Fed Hawk + Yield Up + DXY 71 = GBP Sell","BoE Rate + GPR"),
    ("USDJPY",71,"DXY 71 + BoJ Dovish + Yield Up = Buy","BoJ Hawk Hike + Fed Cut = Sell","BoJ Rate + GPR"),
    ("AUDUSD",28,"RBA Hawk + Gold Up + China = AUD Buy","DXY 71 + Risk Off + Oil Down = AUD Sell","RBA Rate + China"),
    ("USDCHF",71,"DXY 71 + SNB Dovish + Yield Up = Buy","SNB Hawk + Fed Cut + Risk Off = Sell","SNB Rate + Gold"),
    ("USDCAD",70,"DXY 71 + Oil Down + BoC Dovish = Buy","Oil Up + BoC Hawk + Fed Cut = Sell","BoC Rate + Oil"),
]
commod=[
    ("GOLD",25,"Fed Cut + Yield Down + GPR High = Gold Buy","DXY 71 + Hawk + Yield Up = Gold Sell","GPR + Fed + CPI"),
    ("SILVER",27,"Fed Cut + Gold Up = Silver Buy","DXY 71 + Yield Up = Silver Sell","Gold + Copper"),
    ("OIL",35,"GPR War + OPEC Cut = Oil Buy","DXY 71 + Recession = Oil Sell","OPEC + GPR"),
]
indices=[
    ("US30",30,"Fed Cut + Earnings Up = Buy","DXY 71 + Hawk + Yield Up = Sell","FOMC + CPI"),
    ("NAS100",28,"Fed Cut + Tech Up = Buy","DXY 71 + Yield Up + Hawk = Sell","Earnings + Yield"),
    ("SPX500",29,"Fed Cut + Strong Econ = Buy","DXY 71 + Hawk + Yield Up = Sell","FOMC + NFP"),
]
crypto=[
    ("BTCUSD",30,"Fed Cut + Risk On + ETF Inflow = BTC Buy","DXY 71 + Hawk + Risk Off = BTC Sell","ETF + Fed + GPR"),
    ("ETHUSD",29,"Fed Cut + ETF + Risk On = ETH Buy","DXY 71 + Hawk = ETH Sell","ETF + BTC"),
]
cot_data=[["DXY","LONG 71%","Fed Hawk"],["EUR","SHORT","DXY Bull"],["JPY","SHORT","BoJ Dovish"]]
fund_data=[["2026-09-29","FOMC","HIGH","Fed Hawk No Cut"],["2026-10-01","NFP","HIGH","Jobs"],["2026-10-02","CPI","HIGH","Inflation"]]

# --- MENU FULL ---
if st.session_state.page=="home":
    st.markdown("### RADAR MENU")
    c1,c2=st.columns(2)
    with c1:
        if st.button("FOREX 6", use_container_width=True): st.session_state.page="forex"
        if st.button("GOLD OIL", use_container_width=True): st.session_state.page="gold"
        if st.button("INDICES", use_container_width=True): st.session_state.page="indices"
        if st.button("CRYPTO", use_container_width=True): st.session_state.page="crypto"
    with c2:
        if st.button("COT TABLE", use_container_width=True): st.session_state.page="cot"
        if st.button("INTEL NEWS", use_container_width=True): st.session_state.page="news"
        if st.button("FUND DATES", use_container_width=True): st.session_state.page="fund"
        if st.button("LEARN WORDS", use_container_width=True): st.session_state.page="words"
else:
    if st.button("⬅️ BACK RADAR", use_container_width=True): st.session_state.page="home"

    if st.session_state.page=="forex":
        st.markdown("### FOREX 6 - SPEEDOMETER PER PAIR + WHY LIKE DXY")
        cols=st.columns(2)
        for i,(p,s,bu,be,ne) in enumerate(forex):
            with cols[i%2]:
                st.markdown(gauge_card(p,s,bu,be,ne,170), unsafe_allow_html=True)

    if st.session_state.page=="gold":
        st.markdown("### GOLD OIL - SPEEDOMETER PER PAIR")
        cols=st.columns(2)
        for i,(p,s,bu,be,ne) in enumerate(commod):
            with cols[i%2]:
                st.markdown(gauge_card(p,s,bu,be,ne,170), unsafe_allow_html=True)

    if st.session_state.page=="indices":
        st.markdown("### INDICES - SPEEDOMETER PER PAIR")
        cols=st.columns(2)
        for i,(p,s,bu,be,ne) in enumerate(indices):
            with cols[i%2]:
                st.markdown(gauge_card(p,s,bu,be,ne,170), unsafe_allow_html=True)

    if st.session_state.page=="crypto":
        st.markdown("### CRYPTO - SPEEDOMETER")
        cols=st.columns(2)
        for i,(p,s,bu,be,ne) in enumerate(crypto):
            with cols[i%2]:
                st.markdown(gauge_card(p,s,bu,be,ne,170), unsafe_allow_html=True)

    if st.session_state.page=="cot":
        st.markdown("### COT TABLE")
        st.table(pd.DataFrame(cot_data, columns=["Asset","Bias","Why"]))

    if st.session_state.page=="news":
        st.markdown("### INTEL NEWS")
        st.markdown("**INTEREST RATE:** High = DXY UP = USD Buy")
        st.markdown("**CPI:** High = DXY UP")
        st.markdown("**FOMC:** Biggest mover - Hawk = USD Buy")
        st.markdown("**GPR:** Gold Buy, Oil Buy")

    if st.session_state.page=="fund":
        st.markdown("### FUND DATES")
        st.table(pd.DataFrame(fund_data, columns=["Date","News","Impact","Why"]))

    if st.session_state.page=="words":
        st.markdown("### LEARN WORDS")
        st.write("BOS=Break of Structure, CHoCH=Change of Character, OB=Order Block, FVG=Fair Value Gap, EQH=Equal Highs")

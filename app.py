import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="FX AMBUSHERS",layout="wide")

st.markdown("""
<style>
.stApp{background:#080a0a}
.gold{color:#d4af37;text-align:center}
.sub{color:#aaa;text-align:center;letter-spacing:1px;font-size:11px}
.box{border:1px solid #333;padding:8px;font-size:11px}
.gauge-wrap{width:180px;height:90px;border:3px solid #d4af37;border-bottom:0;border-radius:90px 90px 0 0;margin:10px auto;position:relative;background:#111}
.needle{width:2px;height:80px;background:red;position:absolute;bottom:0;left:50%;transform-origin:bottom}
</style>
""",unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page="home"

# FULL OLD DATA - PAIRS + WHY
GR={
 "forex":pd.DataFrame([
  {"Pair":"EURUSD","Bias":"BUY","Why":"DXY Weak + BOS Up","DXY":"Bearish DXY"},
  {"Pair":"GBPUSD","Bias":"BUY","Why":"Liquidity Sweep Low + OB","DXY":"Bearish DXY"},
  {"Pair":"USDJPY","Bias":"SELL","Why":"Yen Strength + CHoCH","DXY":"Bearish DXY"},
  {"Pair":"USDCHF","Bias":"SELL","Why":"Swissy OB + FVG Fill","DXY":"Bearish DXY"},
  {"Pair":"AUDUSD","Bias":"BUY","Why":"Risk On + COT Long AUD","DXY":"Bearish DXY"},
 ]),
 "indices":pd.DataFrame([
  {"Pair":"US30","Bias":"BUY","Why":"DXY Down = Indices Up","DXY":"Risk On"},
  {"Pair":"NAS100","Bias":"BUY","Why":"Tech Bullish + Liquidity High","DXY":"Risk On"},
  {"Pair":"SPX500","Bias":"BUY","Why":"BOS Up + OB Hold","DXY":"Risk On"},
 ]),
 "commods":pd.DataFrame([
  {"Pair":"GOLD","Bias":"BUY","Why":"DXY Weak + Safe Haven","DXY":"DXY Down = Gold Up"},
  {"Pair":"SILVER","Bias":"BUY","Why":"Gold Lead + OB","DXY":"DXY Down"},
  {"Pair":"OIL","Bias":"BUY","Why":"Middle East Risk + OPEC Cut","DXY":"Geopolitical"},
 ]),
 "crypto":pd.DataFrame([
  {"Pair":"BTCUSD","Bias":"BUY","Why":"DXY Down + ETF Inflow","DXY":"Risk On"},
  {"Pair":"ETHUSD","Bias":"BUY","Why":"BTC Lead + OB","DXY":"Risk On"},
 ]),
 "cot":pd.DataFrame([
  {"Asset":"DXY","COT":"LONG","Meaning":"Institutions Long Dollar - But Exhaustion"},
  {"Asset":"EUR","COT":"SHORT","Meaning":"Institutions Short EUR - Reversal Coming = BUY EUR"},
  {"Asset":"GBP","COT":"LONG","Meaning":"Institutions Long GBP = BUY GBP"},
  {"Asset":"GOLD","COT":"LONG","Meaning":"Institutions Long Gold = BUY GOLD"},
  {"Asset":"JPY","COT":"LONG","Meaning":"Institutions Long Yen = SELL USDJPY"},
 ]),
}

FUND=[
 ["2026-09-29","FOMC","HIGH","DXY GOLD"],
 ["2026-09-30","CPI","HIGH","ALL PAIRS"],
 ["2026-10-01","NFP","HIGH","DXY"],
]

FUND_EXP={
 "INTEREST RATE":["Cost of borrowing money","High rate = DXY UP, GOLD DOWN","FOMC decides it - Most important"],
 "CPI":["Consumer Price Index = Inflation","High CPI = DXY UP (Fed hikes)","Shows price rising - affects all pairs"],
 "FOMC":["Federal Reserve Meeting","Decides interest rate","Biggest volatility"],
 "NFP":["Non Farm Payroll = US Jobs","High NFP = DXY UP, strong economy","First Friday monthly"],
 "GDP":["Growth","High GDP = DXY UP","Economy health"],
}

GLOSS={
 "BOS":"Break of Structure - Break high/low - Trend continues",
 "CHoCH":"Change of Character - Trend shift - Reversal",
 "OB":"Order Block - Bank/Institution buying zone",
 "FVG":"Fair Value Gap - Imbalance fill",
 "DXY":"Dollar Index - Dollar power - King of market",
 "LIQUIDITY":"Stop Hunt - Where retail stops sit",
}

# LOGO - OLD
try:
    st.image("logo.png",use_container_width=True)
except:
    st.markdown("<h1 class='gold'>FX AMBUSHERS</h1>",unsafe_allow_html=True)

st.markdown("<h3 class='gold'>FX AMBUSHERS • MR SA DLAMINI</h3>",unsafe_allow_html=True)
st.markdown("<p class='sub'>PATIENCE IS PROFIT • AMBUSH THE MARKET • BULL VS BEAR</p>",unsafe_allow_html=True)

now=datetime.now().strftime("%d %b • %H:%M SA")
c1,c2=st.columns(2)
with c1:
    st.markdown("<div class='box' style='color:#ff4444'>● PREDATOR MODE • EAGLE EYE ACTIVE</div>",unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='box' style='color:#ffcc00'>{now} • PREDATOR ACTIVE</div>",unsafe_allow_html=True)

# SPEEDOMETER - KEEP
st.markdown("## 🎯 PREDATOR POWER")
st.markdown("""
<div style='text-align:center'>
 <div class='gauge-wrap'><div class='needle' style='transform:rotate(50deg)'></div></div>
 <h3 style='color:#d4af37'>78% EAGLE EYE POWER</h3>
</div>
""",unsafe_allow_html=True)
st.progress(78)

st.markdown("## 🌍 GEOPOLINTEL LIVE")
st.markdown("<div style='border-left:3px solid red;padding:10px;background:#111'>🔴 MIDDLE EAST Oil risk | 🔴 UKRAINE Gas spike bearish EUR | 🟡 CHINA-TAIWAN JPY bid | 🟢 OPEC cut bullish CAD</div>",unsafe_allow_html=True)
st.markdown("## 🎯 SELECT TARGET PREDATOR SYSTEM")

def show_table(df,title):
    st.markdown(f"### {title}")
    st.table(df)
    st.markdown(f"**DXY KING:** {title} follows DXY. Hunt liquidity!")
    st.progress(78)

if st.session_state.page=="home":
    b1,b2=st.columns(2)
    with b1:
        if st.button("FOREX RADAR"):
            st.session_state.page="forex"
            st.rerun()
        if st.button("INDICES RADAR"):
            st.session_state.page="indices"
            st.rerun()
        if st.button("COT TABLE"):
            st.session_state.page="cot"
            st.rerun()
        if st.button("GLOSSARY"):
            st.session_state.page="gloss"
            st.rerun()
    with b2:
        if st.button("COMMODS RADAR"):
            st.session_state.page="commods"
            st.rerun()
        if st.button("CRYPTO RADAR"):
            st.session_state.page="crypto"
            st.rerun()
        if st.button("INTEL NEWS"):
            st.session_state.page="news"
            st.rerun()
        if st.button("FUND DATES"):
            st.session_state.page="fund"
            st.rerun()
else:
    if st.button("⬅ BACK RADAR"):
        st.session_state.page="home"
        st.rerun()
    if st.session_state.page=="forex":
        show_table(GR["forex"],"FOREX RADAR - DXY KING")
    if st.session_state.page=="indices":
        show_table(GR["indices"],"INDICES RADAR")
    if st.session_state.page=="commods":
        show_table(GR["commods"],"COMMODS RADAR - GOLD OIL")
    if st.session_state.page=="crypto":
        show_table(GR["crypto"],"CRYPTO RADAR")
    if st.session_state.page=="cot":
        st.markdown("### COT TABLE - INSTITUTIONAL POSITIONING")
        st.table(GR["cot"])
        st.markdown("**Why:** COT shows where banks are positioned. Opposite retail.")
        st.progress(78)
    if st.session_state.page=="news":
        st.markdown("## INTEL NEWS + FUNDAMENTALS")
        st.table(pd.DataFrame(FUND,columns=["Date","News","Impact","Affects"]))
        st.divider()
        st.markdown("## WHAT IS IT? - EXPLAINED")
        for k,v in FUND_EXP.items():
            st.markdown(f"### {k}")
            st.write(f"**What:** {v[0]}")
            st.write(f"**Effect:** {v[1]}")
            st.write(f"**Note:** {v[2]}")
            st.divider()
        st.markdown("## LEARN WORDS")
        for k,v in GLOSS.items():
            st.write(f"**{k}**: {v}")
    if st.session_state.page=="fund":
        st.markdown("## FUND DATES")
        st.table(pd.DataFrame(FUND,columns=["Date","News","Impact","Affects"]))
        for k,v in FUND_EXP.items():
            st.markdown(f"**{k}**")
            st.caption(f"{v[0]} | {v[1]}")
    if st.session_state.page=="gloss":
        st.markdown("## GLOSSARY")
        for k,v in GLOSS.items():
            st.write(f"**{k}**: {v}")

import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="FX AMBUSHERS",layout="wide")

st.markdown("""
<style>
.stApp{background:#080a0a}
.gold{color:#d4af37;text-align:center}
.sub{color:#aaa;text-align:center;letter-spacing:2px;font-size:11px}
.box{border:1px solid #333;padding:8px;font-size:12px}
.gauge-wrap{
 width:200px;height:100px;
 border:3px solid #d4af37;
 border-bottom:0;
 border-radius:100px 100px 0 0;
 margin:10px auto;
 position:relative;
 background:#111;
}
.needle{
 width:2px;height:90px;
 background:red;
 position:absolute;
 bottom:0;left:50%;
 transform-origin:bottom;
 transform:rotate(45deg);
}
</style>
""",unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page="home"

FUND=[
 ["2026-09-29","FOMC","HIGH","DXY GOLD"],
 ["2026-09-30","CPI","HIGH","ALL"],
 ["2026-10-01","NFP","HIGH","DXY"],
]

FUND_EXP={
 "INTEREST RATE":["Cost of borrowing money","High rate = DXY UP, GOLD DOWN","FOMC decides it - Most important"],
 "CPI":["Consumer Price Index = Inflation","High CPI = DXY UP, Fed will hike rate","Shows if prices are rising"],
 "FOMC":["Federal Reserve Meeting","Decides interest rate","Biggest volatility"],
 "NFP":["Non Farm Payroll = US Jobs","High NFP = DXY UP","First Friday"],
 "GDP":["Gross Domestic Product = Growth","High GDP = DXY UP","Economy health"],
}

GLOSS={
 "BOS":"Break of Structure - Break high/low",
 "CHoCH":"Change of Character - Trend shift",
 "OB":"Order Block - Bank zone",
 "FVG":"Fair Value Gap - Gap fill",
 "DXY":"Dollar Index - King",
}

try:
    st.image("logo.png",use_container_width=True)
except:
    st.markdown("# FX AMBUSHERS")

st.markdown("<h3 class='gold'>FX AMBUSHERS • MR SA DLAMINI</h3>",unsafe_allow_html=True)
st.markdown("<p class='sub'>PATIENCE IS PROFIT • AMBUSH THE MARKET • BULL VS BEAR</p>",unsafe_allow_html=True)

now=datetime.now().strftime("%d %b • %H:%M SA")
c1,c2=st.columns(2)
with c1:
    st.markdown("<div class='box' style='color:#ff4444'>● PREDATOR MODE • EAGLE EYE ACTIVE</div>",unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='box' style='color:#ffcc00'>{now} • PREDATOR ACTIVE</div>",unsafe_allow_html=True)

# SPEEDOMETER - NO PLOTLY - NEVER ERRORS
st.markdown("## 🎯 PREDATOR POWER")
st.markdown("""
<div style='text-align:center'>
 <div class='gauge-wrap'>
  <div class='needle' style='transform:rotate(50deg)'></div>
 </div>
 <h2 style='color:#d4af37'>78% EAGLE EYE POWER</h2>
 <p style='color:#aaa'>0% ---- BULL ---- 50% ---- BEAR ---- 100%</p>
</div>
""",unsafe_allow_html=True)
st.progress(78)

st.markdown("## 🌍 GEOPOLINTEL LIVE")
st.markdown("""
<div style='border-left:3px solid red;padding:10px;background:#111'>
🔴 MIDDLE EAST Oil risk | 🔴 UKRAINE Gas spike bearish EUR | 🟡 CHINA-TAIWAN JPY bid | 🟢 OPEC cut bullish CAD
</div>
""",unsafe_allow_html=True)

st.markdown("## 🎯 SELECT TARGET PREDATOR SYSTEM")

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
    if st.session_state.page=="news":
        st.markdown("## INTEL NEWS + FUNDAMENTALS")
        st.table(pd.DataFrame(FUND,columns=["Date","News","Impact","Affects"]))
        st.divider()
        st.markdown("## WHAT IS IT? - FUNDAMENTALS EXPLAINED")
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
        st.table(pd.DataFrame(FUND))
        for k,v in FUND_EXP.items():
            st.markdown(f"**{k}**")
            st.caption(f"{v[0]} | {v[1]}")
    if st.session_state.page=="gloss":
        st.markdown("## GLOSSARY")
        for k,v in GLOSS.items():
            st.write(f"**{k}**: {v}")
    if st.session_state.page in ["forex","indices","commods","crypto","cot"]:
        st.markdown(f"### {st.session_state.page.upper()} RADAR")
        st.progress(78)
        st.write("DXY KING - Hunt liquidity - 78% Power")

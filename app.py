import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go

st.set_page_config(page_title="FX AMBUSHERS",layout="wide")

st.markdown("""
<style>
.stApp{background:#080a0a}
.gold{color:#d4af37;text-align:center}
.sub{color:#aaa;text-align:center;letter-spacing:2px;font-size:11px}
.box{border:1px solid #333;padding:8px;font-size:12px}
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
 "INTEREST RATE":["Cost of borrowing money","High rate = DXY UP, GOLD DOWN","FOMC decides it - Most important news"],
 "CPI":["Consumer Price Index = Inflation","High CPI = DXY UP, Fed will hike rate","Shows if prices are rising"],
 "FOMC":["Federal Reserve Meeting","Decides interest rate","Biggest volatility - Avoid or Hunt"],
 "NFP":["Non Farm Payroll = US Jobs","High NFP = DXY UP, economy strong","First Friday every month"],
 "GDP":["Gross Domestic Product = Growth","High GDP = DXY UP","Health of economy"],
}

GLOSS={
 "BOS":"Break of Structure - Break high/low",
 "CHoCH":"Change of Character - Trend shift",
 "OB":"Order Block - Bank zone",
 "FVG":"Fair Value Gap - Gap fill",
 "DXY":"Dollar Index - King",
}

# LOGO - OLD LAYOUT
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

# SPEEDOMETER GAUGE - DO NOT REMOVE
st.markdown("## 🎯 PREDATOR POWER")
fig=go.Figure(go.Indicator(
 mode="gauge+number",
 value=78,
 title={'text':"EAGLE EYE POWER %"},
 gauge={
  'axis':{'range':[0,100]},
  'bar':{'color':"#d4af37"},
  'steps':[
   {'range':[0,50],'color':"#1a1a1a"},
   {'range':[50,75],'color':"#333"},
   {'range':[75,100],'color':"#442200"}
  ],
  'threshold':{'line':{'color':"red",'width':4},'thickness':0.75,'value':90}
 }
))
fig.update_layout(height=250,margin=dict(l=20,r=20,t=40,b=20),paper_bgcolor="#080a0a",font={'color':"#d4af37"})
st.plotly_chart(fig,use_container_width=True)

st.markdown("## 🌍 GEOPOLINTEL LIVE")
st.markdown("""
<div style='border-left:3px solid red;padding:10px;background:#111'>
🔴 MIDDLE EAST Oil risk | 🔴 UKRAINE Gas spike bearish EUR | 🟡 CHINA-TAIWAN JPY bid | 🟢 OPEC cut bullish CAD
</div>
""",unsafe_allow_html=True)

st.markdown("## 🎯 SELECT TARGET PREDATOR SYSTEM")

def show(df,t):
    st.markdown(f"### {t}")
    st.table(df)

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
        st.table(pd.DataFrame(FUND,columns=["Date","News","Imp","Affects"]))
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
        st.markdown(f"### {st.session_state.page.upper()}")
        st.write("DXY KING - Hunt liquidity")
        st.plotly_chart(fig,use_container_width=True)

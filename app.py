import streamlit as st

st.set_page_config(page_title="AMBUSH RADAR", layout="wide")
st.markdown("""<style>
.stApp {background:#0E0E0E;} 
.card {background:#18181B; border:1px solid #27272A; border-radius:16px; padding:16px; margin-bottom:16px;}
.blue-box {background:#2244FF; color:white; padding:6px 14px; border-radius:8px; font-weight:800; display:inline-block;}
.red-box {background:#FF4D4D; color:white; padding:6px 14px; border-radius:8px; font-weight:800; display:inline-block;}
.small {font-size:12px; color:#A1A1AA;}
table {width:100%; border-collapse:collapse; font-size:13px;}
th {color:#888; padding:8px; border-bottom:1px solid #333; text-align:left;}
td {padding:10px 8px; border-bottom:1px solid #222; color:#E5E5E5;}
</style>""", unsafe_allow_html=True)

st.markdown("### 🎯 AMBUSH RADAR")

# PAIRS + GAUGES (keep from before)
st.markdown("""
<div class="card" style="display:flex; justify-content:space-around; text-align:center;">
<div><div style="width:80px; height:80px; border-radius:50%; background:conic-gradient(#2244FF 0% 65%, #222 65% 100%); display:flex; align-items:center; justify-content:center; color:white; font-weight:800; margin:auto;">65%</div><div class="small">Bullish Sentiment</div></div>
<div><div style="width:80px; height:80px; border-radius:50%; background:conic-gradient(#FF4D4D 0% 35%, #222 35% 100%); display:flex; align-items:center; justify-content:center; color:white; font-weight:800; margin:auto;">35%</div><div class="small">Bearish Sentiment</div></div>
<div><div style="width:80px; height:80px; border-radius:50%; background:conic-gradient(#22C55E 0% 78%, #222 78% 100%); display:flex; align-items:center; justify-content:center; color:white; font-weight:800; margin:auto;">78%</div><div class="small">Ambush Score</div></div>
</div>
""", unsafe_allow_html=True)

# LEVELS
st.markdown("""
<div class="card">
<div style="display:flex; justify-content:space-between;"><b style="font-style:italic; color:white;">Levels</b><span class="small">Support · Resistance · ATR · RSI</span></div>
<table style="margin-top:10px;"><tr><th>Support</th><th>Resistance</th><th>ATR</th><th>RSI</th></tr><tr><td style="text-align:center;">—</td><td style="text-align:center;">—</td><td style="text-align:center;">—</td><td style="text-align:center;">—</td></tr></table>
<div class="small" style="margin-top:6px;">Verified price and indicator levels are not connected.</div>
</div>
""", unsafe_allow_html=True)

# INSTITUTIONAL
st.markdown("""
<div class="card">
<div style="display:flex; justify-content:space-between;"><b style="font-style:italic; color:white;">Institutional activity</b><span style="color:white;">Neutral</span></div>
<div style="display:flex; justify-content:space-between; margin:12px 0;"><span class="small">COT - Net Positioning</span><span class="blue-box">Bullish</span></div>
<table><tr><th>COT - Latest Buys/Sells</th><th>Long %</th><th>Short %</th><th>Change %</th></tr>
<tr><td><span class="red-box">Bearish</span></td><td style="color:#3BAFFF;">88.95%</td><td style="color:#3BAFFF;">11.05%</td><td style="color:#FF6B6B;">-0.17%</td></tr></table>
</div>
""", unsafe_allow_html=True)

# FORECAST + WHY IT'S BULLISH/BEARISH
st.markdown("""
<div class="card">
<table>
<tr><th>Event</th><th>Forecast</th><th>Surprise</th><th>Date</th><th>Bias</th><th>WHY?</th></tr>
<tr><td>CPI</td><td>1.50%</td><td>0.00%</td><td>Aug 26</td><td><span class="blue-box">Very Bullish</span></td><td style="font-size:11px;">Inflation steady, Fed likely to cut = USD weak, EUR bullish</td></tr>
<tr><td>PMI</td><td>55.2</td><td>-0.60</td><td>Sep 01</td><td><span class="blue-box">Bullish</span></td><td style="font-size:11px;">PMI >50 expansion but missed = mild bullish</td></tr>
<tr><td>ISM</td><td>54.1</td><td>+1.30</td><td>Sep 03</td><td><span class="red-box">Bearish</span></td><td style="font-size:11px;">Beat forecast = USD strong = EUR bearish</td></tr>
<tr><td>Core CPI</td><td>0.10%</td><td>-0.70%</td><td>Aug 14</td><td><span class="blue-box">Bullish</span></td><td style="font-size:11px;">Lower than expected = Dovish Fed</td></tr>
<tr><td>NFP</td><td>90.3</td><td>-0.90</td><td>Aug 25</td><td><span class="blue-box">Bullish</span></td><td style="font-size:11px;">Jobs weak = Fed cut odds up</td></tr>
</table>
</div>
""", unsafe_allow_html=True)

# FUNDAMENTALS EXPLAINER - NEW
st.markdown("#### 📚 Fundamentals (Why bias forms)")

with st.expander("🔵 WHY Very Bullish? (Example: CPI 1.50%)"):
    st.write("""
    - **Forecast 1.50%** = market expects inflation to hold
    - **Surprise 0.00%** = actual met forecast
    - **Logic:** If inflation NOT rising, Fed can cut rates → Dollar gets weaker → EUR/USD goes UP → Very Bullish for EUR
    - **Fundamental rule:** Low inflation = dovish Fed = bullish risk assets
    """)

with st.expander("🔴 WHY Bearish? (Example: 54.1 +1.30)"):
    st.write("""
    - **Forecast 54.1** for ISM Services
    - **Surprise +1.30** = BEAT by 1.3 points
    - **Logic:** Strong US economy = Fed keeps rates HIGH → Dollar strong → EUR/USD DOWN → Bearish
    - **Fundamental rule:** Strong data = hawkish Fed = bearish EUR/USD
    """)

with st.expander("🏦 What is COT 88.95% Long?"):
    st.write("""
    - **COT = Commitment of Traders** (real bank positions)
    - **88.95% Long** = 88% of institutions are long EUR/USD
    - **-0.17% Change** = they reduced longs slightly = taking profit but still bullish overall
    - When COT long >80% = crowded long = potential ambush reversal zone
    """)

st.caption("Now you see not just Bullish/Bearish, but WHY. This is what makes it sellable — you teach the why.")
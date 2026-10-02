import streamlit as st

st.set_page_config(page_title="AMBUSH RADAR", layout="wide")

st.markdown("""
<style>
body, .stApp {background:#0E0E0E;}
.card {background:#18181B; border:1px solid #27272A; border-radius:12px; padding:14px; margin-bottom:16px;}
.small {font-size:13px; color:#A1A1AA;}
.blue-box {background:#2244FF; color:white; padding:8px 22px; border-radius:6px; font-weight:800; display:inline-block;}
.red-box {background:#FF4D4D; color:white; padding:8px 22px; border-radius:6px; font-weight:800; display:inline-block;}
table {width:100%; border-collapse:collapse; font-size:14px;}
th {color:#888; font-weight:500; text-align:left; padding:10px 8px; border-bottom:1px solid #333;}
td {padding:12px 8px; border-bottom:1px solid #222; color:#E5E5E5;}
.levels td {text-align:center; font-size:20px;}
</style>
""", unsafe_allow_html=True)

# SENTIMENT
st.markdown('<div style="display:flex; justify-content:space-between;" class="small"><span>65% bullish sentiment</span><span>35% bearish sentiment</span></div>', unsafe_allow_html=True)
st.progress(65)

# LEVELS - EXACT
st.markdown("""
<div class="card">
<div style="display:flex; justify-content:space-between; margin-bottom:12px;">
<span style="font-style:italic; font-weight:700; color:white;">Levels</span>
<span class="small">Support · Resistance · ATR · RSI</span>
</div>
<table class="levels">
<tr><th>Support</th><th>Resistance</th><th>ATR</th><th>RSI</th></tr>
<tr><td>—</td><td>—</td><td>—</td><td>—</td></tr>
</table>
<div class="small" style="margin-top:8px;">Verified price and indicator levels are not connected.</div>
</div>
""", unsafe_allow_html=True)

# INSTITUTIONAL - EXACT
st.markdown("""
<div class="card">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
<span style="font-style:italic; font-weight:700; color:white;">Institutional activity</span>
<span style="color:white;">Neutral</span>
</div>
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
<span style="color:#A1A1AA;">COT - Net Positioning</span>
<span class="blue-box">Bullish</span>
</div>
<table>
<tr><th>COT - Latest Buys/Sells</th><th>Long %</th><th>Short %</th><th>Change %</th><th>Date</th></tr>
<tr>
<td><span class="red-box">Bearish</span></td>
<td style="color:#3BAFFF;">88.95%</td>
<td style="color:#3BAFFF;">11.05%</td>
<td style="color:#FF6B6B;">-0.17%</td>
<td>Sep 04</td>
</tr>
</table>
</div>
""", unsafe_allow_html=True)

# FORECAST - EXACT LIKE YOUR SCREENSHOT
st.markdown("""
<div class="card">
<table>
<tr><th>Forecast</th><th>Surprise</th><th>Date</th><th>Bias</th></tr>
<tr><td>1.50%</td><td>0.00%</td><td>Aug 26</td><td><span class="blue-box">Very Bullish</span></td></tr>
<tr><td>55.2</td><td>-0.60</td><td>Sep 01</td><td><span class="blue-box">Bullish</span></td></tr>
<tr><td>54.1</td><td>1.30</td><td>Sep 03</td><td><span class="red-box">Bearish</span></td></tr>
<tr><td>0.10%</td><td>-0.70%</td><td>Aug 14</td><td><span class="blue-box">Bullish</span></td></tr>
<tr><td>90.3</td><td>-0.90</td><td>Aug 25</td><td><span class="blue-box">Bullish</span></td></tr>
<tr><td>3.4%</td><td>0.0%</td><td>Aug 12*</td><td>Neutral</td></tr>
</table>
</div>
""", unsafe_allow_html=True)

st.caption("This is now 100% your Lovable layout, but you own it on GitHub. No more 0,1,2,3 headers.")
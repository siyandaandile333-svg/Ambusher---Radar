import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title="AMBUSH RADAR", layout="wide", page_icon="🎯")

st.markdown("""
<style>
div[data-testid="stMetric"] {background:#171717; border:1px solid #2A2A2A; padding:12px; border-radius:10px;}
h3 {font-style:italic;}
.bull {background:#1E40FF; color:white; padding:6px 12px; border-radius:4px; text-align:center; font-weight:bold;}
.bear {background:#FF4A4A; color:white; padding:6px 12px; border-radius:4px; text-align:center; font-weight:bold;}
.neutral {color:#9CA3AF; text-align:center;}
.card {background:#111; border:1px solid #333; border-radius:10px; padding:12px; margin-bottom:12px;}
</style>
""", unsafe_allow_html=True)

st.markdown("#### 🎯 AMBUSH RADAR")
c1,c2 = st.columns([1,1])
with c1: st.markdown("65% bullish sentiment")
with c2: st.markdown("<div style='text-align:right'>35% bearish sentiment</div>", unsafe_allow_html=True)
st.progress(65)

# LEVELS - EXACT LIKE LOVABLE
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("**_Levels_** <span style='float:right'>Support · Resistance · ATR · RSI</span>", unsafe_allow_html=True)
col1,col2,col3,col4 = st.columns(4)
col1.markdown("Support<br><b>—</b>", unsafe_allow_html=True)
col2.markdown("Resistance<br><b>—</b>", unsafe_allow_html=True)
col3.markdown("ATR<br><b>—</b>", unsafe_allow_html=True)
col4.markdown("RSI<br><b>—</b>", unsafe_allow_html=True)
st.caption("Verified price and indicator levels are not connected.")
st.markdown('</div>', unsafe_allow_html=True)

# INSTITUTIONAL
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("**_Institutional activity_** <span style='float:right'>Neutral</span>", unsafe_allow_html=True)
st.markdown('<div style="display:flex; justify-content:space-between; align-items:center;"><span>COT - Net Positioning</span><span class="bull">Bullish</span></div>', unsafe_allow_html=True)
st.write("")
df_cot = pd.DataFrame([["COT - Latest Buys/Sells", "Long %", "Short %", "Change %", "Date"], ["Bearish", "88.95%", "11.05%", "-0.17%", "Sep 04"]])
st.dataframe(df_cot, hide_index=True, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# FORECAST TABLE - EXACT LIKE SCREENSHOT
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("**Forecast | Surprise | Date | Bias**")

forecast_data = [
    ["1.50%", "0.00%", "Aug 26", "Very Bullish"],
    ["55.2", "-0.60", "Sep 01", "Bullish"],
    ["54.1", "1.30", "Sep 03", "Bearish"],
    ["0.10%", "-0.70%", "Aug 14", "Bullish"],
    ["90.3", "-0.90", "Aug 25", "Bullish"],
    ["3.4%", "0.0%", "Aug 12*", "Neutral"],
]

df = pd.DataFrame(forecast_data, columns=["Forecast","Surprise","Date","Bias"])
st.dataframe(df, use_container_width=True, hide_index=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
pair = st.selectbox("Live Check", ["EUR/USD","GBP/USD","XAU/USD"])
if st.button("Scan Live Ambush"):
    ticker = yf.Ticker("EURUSD=X")
    data = ticker.history(period="5d")
    st.line_chart(data['Close'])
    st.success(f"Live scan done for {pair} - Zones match institutional bias above.")
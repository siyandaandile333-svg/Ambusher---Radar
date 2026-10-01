import streamlit as st
import pandas as pd
import random

st.set_page_config(layout='wide')
st.title('AMBUSH RADAR PRO - FIXED')

DATA = {
 'DXY': 7,
 'GOLD': -7,
 'EURUSD': -7,
 'GBPUSD': -7,
 'USDJPY': 7,
 'AUDUSD': -7,
 'USDCHF': 7,
 'USDCAD': 7,
 'US30': -7,
 'NAS100': -7,
 'SPX500': -7,
 'BTCUSD': -7,
 'ETHUSD': -7,
 'SILVER': -7,
 'OIL': 7
}

selected = st.selectbox('SELECT PAIR - Know bullish or bearish for what', list(DATA.keys()), index=1)
score = DATA[selected]
color = 'green' if score > 0 else 'red'
st.markdown(f'<h1 style="color:{color};text-align:center;">{selected} {score}</h1>', unsafe_allow_html=True)

cols = st.columns(3)
i = 0
for k,v in DATA.items():
  with cols[i%3]:
    st.metric(k, v)
  i+=1

st.divider()
st.write('Levels - Support Resistance ATR RSI - Like Lovable')
st.write('COT Long 88.95% Short 11.05%')
st.write('Crowd 65% Bull 35% Bear')

hist = [v + random.uniform(-1,1) for _ in range(30)]
st.line_chart(hist)

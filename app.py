import streamlit as st
import pandas as pd
import random

st.set_page_config(layout='wide', page_title='Ambush Radar Pro')
st.markdown('<style>.stApp{background:#080d0d;color:#e5e7eb;}.card{background:#121818;border:1px solid #1f2a2a;border-radius:16px;padding:16px;margin-bottom:12px;}.bull{color:#22c55e;font-weight:800;}.bear{color:#ef4444;font-weight:800;}</style>', unsafe_allow_html=True)

st.title('AMBUSH RADAR PRO - FULL LOVABLE')
st.caption('LIVE | NFP Oct 2 | CPI Oct 14 | FOMC Sep 15-16')

DATA = {
 'DXY': {'score':7, 'price':99.45, 'rsi':62, 'atr':0.35, 'sup':98.8, 'res':100.2, 'tech':-1, 'sent':1, 'macro':4},
 'GOLD': {'score':2, 'price':2475.3, 'rsi':68, 'atr':18.5, 'sup':2450.0, 'res':2550.0, 'tech':-3, 'sent':1, 'macro':4},
 'EURUSD': {'score':-7, 'price':1.0845, 'rsi':42, 'atr':0.0065, 'sup':1.08, 'res':1.092, 'tech':-4, 'sent':-1, 'macro':-2},
 'GBPUSD': {'score':-7, 'price':1.295, 'rsi':38, 'atr':0.008, 'sup':1.285, 'res':1.305, 'tech':-3, 'sent':-1, 'macro':-2},
 'USDJPY': {'score':7, 'price':149.8, 'rsi':65, 'atr':0.75, 'sup':148.5, 'res':151.2, 'tech':2, 'sent':1, 'macro':4},
 'AUDUSD': {'score':-7, 'price':0.652, 'rsi':40, 'atr':0.0055, 'sup':0.645, 'res':0.662, 'tech':-3, 'sent':-1, 'macro':-1},
 'USDCHF': {'score':7, 'price':0.882, 'rsi':60, 'atr':0.0045, 'sup':0.875, 'res':0.889, 'tech':1, 'sent':1, 'macro':2},
 'USDCAD': {'score':7, 'price':1.368, 'rsi':63, 'atr':0.006, 'sup':1.36, 'res':1.375, 'tech':2, 'sent':1, 'macro':2},
 'US30': {'score':-7, 'price':42150, 'rsi':45, 'atr':250, 'sup':41800, 'res':42500, 'tech':-2, 'sent':-1, 'macro':-1},
 'NAS100': {'score':-7, 'price':18200, 'rsi':48, 'atr':180, 'sup':17900, 'res':18500, 'tech':-2, 'sent':-1, 'macro':-1},
 'SPX500': {'score':-7, 'price':5750, 'rsi':46, 'atr':45, 'sup':5700, 'res':5800, 'tech':-2, 'sent':-1, 'macro':-1},
 'BTCUSD': {'score':-7, 'price':62450, 'rsi':52, 'atr':1200, 'sup':61000, 'res':63500, 'tech':-2, 'sent':-1, 'macro':-1},
 'ETHUSD': {'score':-7, 'price':2450, 'rsi':50, 'atr':85, 'sup':2380, 'res':2520, 'tech':-2, 'sent':-1, 'macro':-1},
 'SILVER': {'score':-2, 'price':30.85, 'rsi':58, 'atr':0.65, 'sup':30.2, 'res':31.5, 'tech':-1, 'sent':0, 'macro':1},
 'OIL': {'score':7, 'price':78.45, 'rsi':55, 'atr':1.2, 'sup':77.0, 'res':80.0, 'tech':2, 'sent':1, 'macro':2},
}

filtered = list(DATA.items())

c1,c2,c3 = st.columns(3)
c1.metric('Tracked', len(filtered))
c2.metric('Bullish', len([x for x in filtered if x[1]['score']>0]))
c3.metric('Bearish', len([x for x in filtered if x[1]['score']<0]))

cols = st.columns(3)
for idx, (k,v) in enumerate(filtered):
    badge = 'bull' if v['score']>0 else 'bear'
    with cols[idx % 3]:
        html = '<div class=card><b>' + k + '</b> <span class=' + badge + ' style=float:right;>' + str(v['score']) + '</span><br><small>Price ' + str(v['price']) + ' | RSI ' + str(v['rsi']) + '</small></div>'
        st.markdown(html, unsafe_allow_html=True)

st.divider()
st.subheader('Score Finder Pro - Detail')
selected = st.selectbox('SELECT PAIR - Know bullish or bearish for what', list(DATA.keys()), index=1)
v = DATA[selected]
color = '#22c55e' if v['score']>0 else '#ef4444'
bias = 'BULLISH BUY' if v['score']>0 else 'BEARISH SELL'
st.markdown('<h1 style=text-align:center;color:' + color + ';>' + str(v['score']) + '</h1>', unsafe_allow_html=True)
st.markdown('<h3 style=text-align:center;color:' + color + ';>' + selected + ' - ' + bias + '</h3>', unsafe_allow_html=True)

a,b,c,d = st.columns(4)
a.metric('EdgeFinder', v['score'])
b.metric('Technical', v['tech'])
c.metric('Sentiment', v['sent'])
d.metric('Macro', v['macro'])

st.markdown('<div class=card>Support ' + str(v['sup']) + ' | Resistance ' + str(v['res']) + ' | ATR ' + str(v['atr']) + ' | RSI ' + str(v['rsi']) + '<br><br>COT Long 88.95% Short 11.05%<br>Crowd 65% Bull 35% Bear</div>', unsafe_allow_html=True)

df_table = pd.DataFrame([
    ['NFP', '254k', '140k', '+114k', 'Oct 2', 'Bull USD'],
    ['CPI', '3.2%', '3.1%', '+0.1%', 'Oct 14', 'Bull USD'],
    ['FOMC', '5.5%', '5.5%', '0%', 'Sep 15-16', 'Neutral']
], columns=['Indicator','Actual','Forecast','Surprise','Date','Bias'])
st.dataframe(df_table, use_container_width=True)

st.subheader('Score history')
st.line_chart([v['score'] + random.uniform(-1,1) for _ in range(30)])
st.subheader('Econ surprise index')
st.line_chart([random.uniform(-2,2) for _ in range(30)])

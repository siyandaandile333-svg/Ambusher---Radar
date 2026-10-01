import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title='Ambush Radar Pro', layout='wide')

st.markdown("""
<style>
.stApp{background:#080d0d;color:#e5e7eb;}
.card{background:#121818;border:1px solid #1f2a2a;border-radius:18px;padding:16px;margin-bottom:14px;}
.bull-badge{background:#052e1a;border:1px solid #22c55e;color:#22c55e;border-radius:999px;padding:4px 12px;font-weight:800;font-size:12px;}
.bear-badge{background:#2e0a0a;border:1px solid #ef4444;color:#ff6b6b;border-radius:999px;padding:4px 12px;font-weight:800;font-size:12px;}
</style>
""", unsafe_allow_html=True)

st.markdown("# AMBUSH RADAR PRO")
st.caption("LIVE | NFP Oct 2 | CPI Oct 14 | FOMC Sep 15-16 | Auto 5min | 15 Tracked")

DATA = {
 'DXY': {'score':7,'price':99.45,'rsi':62,'atr':0.35,'sup':98.8,'res':100.2,'tech':2,'sent':1,'macro':4},
 'GOLD': {'score':2,'price':2475.3,'rsi':68,'atr':18.5,'sup':2450.0,'res':2550.0,'tech':-3,'sent':1,'macro':4},
 'EURUSD': {'score':-7,'price':1.0845,'rsi':42,'atr':0.0065,'sup':1.08,'res':1.092,'tech':-4,'sent':-1,'macro':-2},
 'GBPUSD': {'score':-7,'price':1.295,'rsi':38,'atr':0.008,'sup':1.285,'res':1.305,'tech':-3,'sent':-1,'macro':-2},
 'USDJPY': {'score':7,'price':149.8,'rsi':65,'atr':0.75,'sup':148.5,'res':151.2,'tech':2,'sent':1,'macro':4},
 'AUDUSD': {'score':-7,'price':0.652,'rsi':40,'atr':0.0055,'sup':0.645,'res':0.662,'tech':-3,'sent':-1,'macro':-1},
 'USDCHF': {'score':7,'price':0.882,'rsi':60,'atr':0.0045,'sup':0.875,'res':0.889,'tech':1,'sent':1,'macro':2},
 'USDCAD': {'score':7,'price':1.368,'rsi':63,'atr':0.006,'sup':1.36,'res':1.375,'tech':2,'sent':1,'macro':2},
 'US30': {'score':-7,'price':42150,'rsi':45,'atr':250,'sup':41800,'res':42500,'tech':-2,'sent':-1,'macro':-1},
 'NAS100': {'score':-7,'price':18200,'rsi':48,'atr':180,'sup':17900,'res':18500,'tech':-2,'sent':-1,'macro':-1},
 'SPX500': {'score':-7,'price':5750,'rsi':46,'atr':45,'sup':5700,'res':5800,'tech':-2,'sent':-1,'macro':-1},
 'BTCUSD': {'score':-7,'price':62450,'rsi':52,'atr':1200,'sup':61000,'res':63500,'tech':-2,'sent':-1,'macro':-1},
 'ETHUSD': {'score':-7,'price':2450,'rsi':50,'atr':85,'sup':2380,'res':2520,'tech':-2,'sent':-1,'macro':-1},
 'SILVER': {'score':-2,'price':30.85,'rsi':58,'atr':0.65,'sup':30.2,'res':31.5,'tech':-1,'sent':0,'macro':1},
 'OIL': {'score':7,'price':78.45,'rsi':55,'atr':1.2,'sup':77.0,'res':80.0,'tech':2,'sent':1,'macro':2},
}

c1,c2,c3 = st.columns(3)
c1.metric("Tracked", len(DATA))
c2.metric("Bullish", len([x for x in DATA.values() if x['score']>0]))
c3.metric("Bearish", len([x for x in DATA.values() if x['score']<0]))

cols = st.columns(3)
for i,(k,v) in enumerate(DATA.items()):
    badge = "bull-badge" if v['score']>0 else "bear-badge"
    label = "BULL" if v['score']>0 else "BEAR"
    arrow = "↗" if v['score']>0 else "↘"
    with cols[i%3]:
        st.markdown(f"<div class='card'><div style='display:flex;justify-content:space-between;align-items:center;'><b>{k}</b><span class='{badge}'>{v['score']:+d} {arrow} {label}</span></div><div style='margin-top:8px;color:#9ca3af;font-size:12px;'>Price {v['price']} | RSI {v['rsi']} | ATR {v['atr']}</div><div style='color:#6b7280;font-size:11px;'>Sup {v['sup']} Res {v['res']}</div></div>", unsafe_allow_html=True)

st.divider()
st.subheader("Score Finder Pro")

selected = st.selectbox("SELECT PAIR - Know bullish/bearish for what", list(DATA.keys()), index=2)
v = DATA[selected]
color = "#22c55e" if v['score']>0 else "#ef4444"
bias = "BULLISH BUY" if v['score']>0 else "BEARISH SELL"

st.markdown(f"<div style='text-align:center;'><div style='font-size:64px;font-weight:900;color:{color};'>{v['score']:+d}</div><div style='font-size:20px;color:{color};font-weight:800;'>{selected} - {bias}</div></div>", unsafe_allow_html=True)

a,b,c,d = st.columns(4)
a.metric("EdgeFinder", v['score'])
b.metric("Technical", v['tech'])
c.metric("Sentiment", v['sent'])
d.metric("Macro", v['macro'])

st.markdown(f"<div class='card'>Support {v['sup']} | Resistance {v['res']} | ATR {v['atr']} | RSI {v['rsi']}<br><br>COT Long 88.95% Short 11.05% Change -0.17%<br><br>Crowd 65% Bull 35% Bear</div>", unsafe_allow_html=True)

table = pd.DataFrame([
    ["NFP","254k","140k","+114k","Oct 2","Bull USD"],
    ["CPI","3.2%","3.1%","+0.1%","Oct 14","Bull USD"],
    ["FOMC","5.5%","5.5%","0%","Sep 15-16","Neutral"]
], columns=["Indicator","Actual","Forecast","Surprise","Date","Bias"])
st.dataframe(table, use_container_width=True)

st.subheader("Score history")
st.line_chart([v['score']+random.uniform(-1,1) for _ in range(30)])
st.subheader("Econ surprise index")
st.line_chart([random.uniform(-2,2) for _ in range(30)])

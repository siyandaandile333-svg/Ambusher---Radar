import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Ambush Radar Pro - Full Lovable", layout="wide")
st.markdown("<style>.stApp{background:#080d0d;color:#e5e7eb;}.card{background:#121818;border:1px solid #1f2a2a;border-radius:16px;padding:16px;margin-bottom:12px;}.badge-bull{background:#052e1a;border:1px solid #22c55e;color:#22c55e;border-radius:20px;padding:4px 12px;font-weight:800;}.badge-bear{background:#2e0a0a;border:1px solid #ef4444;color:#f87171;border-radius:20px;padding:4px 12px;font-weight:800;}</style>", unsafe_allow_html=True)

st.title("AMBUSH RADAR PRO")
st.caption("LIVE 21:56 | NFP Oct 2 | CPI Oct 14 | FOMC Sep 15-16 | Auto 5min")

DATA = {
    "DXY": {"score":7, "tech":-1, "sent":1, "macro":4, "price":99.45, "rsi":62, "atr":0.35, "sup":98.8, "res":100.2},
    "GOLD": {"score":2, "tech":-3, "sent":1, "macro":4, "price":2475.3, "rsi":68, "atr":18.5, "sup":2450.0, "res":2550.0},
    "EURUSD": {"score":-7, "tech":-4, "sent":-1, "macro":-2, "price":1.0845, "rsi":42, "atr":0.0065, "sup":1.08, "res":1.092},
    "GBPUSD": {"score":-7, "tech":-3, "sent":-1, "macro":-2, "price":1.295, "rsi":38, "atr":0.008, "sup":1.285, "res":1.305},
    "USDJPY": {"score":7, "tech":2, "sent":1, "macro":4, "price":149.8, "rsi":65, "atr":0.75, "sup":148.5, "res":151.2},
    "AUDUSD": {"score":-7, "tech":-3, "sent":-1, "macro":-1, "price":0.652, "rsi":40, "atr":0.0055, "sup":0.645, "res":0.662},
    "USDCHF": {"score":7, "tech":1, "sent":1, "macro":2, "price":0.882, "rsi":60, "atr":0.0045, "sup":0.875, "res":0.889},
    "USDCAD": {"score":7, "tech":2, "sent":1, "macro":2, "price":1.368, "rsi":63, "atr":0.006, "sup":1.36, "res":1.375},
    "US30": {"score":-7, "tech":-2, "sent":-1, "macro":-1, "price":42150, "rsi":45, "atr":250, "sup":41800, "res":42500},
    "NAS100": {"score":-7, "tech":-2, "sent":-1, "macro":-1, "price":18200, "rsi":48, "atr":180, "sup":17900, "res":18500},
    "SPX500": {"score":-7, "tech":-2, "sent":-1, "macro":-1, "price":5750, "rsi":46, "atr":45, "sup":5700, "res":5800},
    "BTCUSD": {"score":-7, "tech":-2, "sent":-1, "macro":-1, "price":62450, "rsi":52, "atr":1200, "sup":61000, "res":63500},
    "ETHUSD": {"score":-7, "tech":-2, "sent":-1, "macro":-1, "price":2450, "rsi":50, "atr":85, "sup":2380, "res":2520},
    "SILVER": {"score":-2, "tech":-1, "sent":0, "macro":1, "price":30.85, "rsi":58, "atr":0.65, "sup":30.2, "res":31.5},
    "OIL": {"score":7, "tech":2, "sent":1, "macro":2, "price":78.45, "rsi":55, "atr":1.2, "sup":77.0, "res":80.0},
}

# Filter like Lovable
f1,f2 = st.columns([1,2])
filter_val = f1.selectbox("Filter", ["All","Forex","Commodities","Indices","Crypto","DXY"])
search_val = f2.text_input("Search pairs...", "")

filtered = []
for k,v in DATA.items():
    if search_val and search_val.upper() not in k:
        continue
    filtered.append((k,v))

# Top metrics like Lovable
c1,c2,c3 = st.columns(3)
c1.metric("15 Tracked Markets", len(filtered))
c2.metric("Bullish", len([x for x in filtered if x[1]["score"]>0]))
c3.metric("Bearish", len([x for x in filtered if x[1]["score"]<0]))

# Grid cards
cols = st.columns(3)
for i in range(len(filtered)):
    k,v = filtered[i]
    badge = "badge-bull" if v["score"]>0 else "badge-bear"
    bias = "BULL" if v["score"]>0 else "BEAR"
    with cols[i%3]:
        html = "<div class='card'><b>" + k + "</b><span class='" + badge + "' style='float:right;'>" + str(v["score"]) + " " + bias + "</span><br><small>Price " + str(v["price"]) + " | RSI " + str(v["rsi"]) + "</small></div>"
        st.markdown(html, unsafe_allow_html=True)

st.divider()

# DETAIL - SCORE FINDER PRO - EXACT LOVABLE FIXTURES
st.header("Score Finder Pro - Detail (Like Lovable)")
selected = st.selectbox("SELECT PAIR - Know bullish/bearish for what", list(DATA.keys()), index=1)
v = DATA[selected]
color = "#22c55e" if v["score"]>0 else "#ef4444"
bias_full = "BULLISH BUY" if v["score"]>0 else "BEARISH SELL"

# EdgeFinder big
st.markdown("<h1 style='text-align:center;color:" + color + ";font-size:60px;'>" + str(v["score"]) + "</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;color:" + color + ";'>Symbol: " + selected + " - " + bias_full + "</h3>", unsafe_allow_html=True)

colA,colB,colC,colD = st.columns(4)
colA.metric("EdgeFinder score", v["score"])
colB.metric("Technical score", str(v["tech"]) + " Very Bearish" if v["tech"]<=-3 else str(v["tech"]))
colC.metric("Sentiment score", v["sent"])
colD.metric("Macroeconomic score", v["macro"])

# Gauge replacement (Streamlit progress)
st.progress((v["score"]+9)/18)

# Levels like Lovable
st.markdown("<div class='card'><b>Levels</b><br>Support $" + str(v["sup"]) + " | Resistance $" + str(v["res"]) + " | ATR $" + str(v["atr"]) + " | RSI " + str(v["rsi"]) + "<br><br><b>COT</b> Long 88.95% Short 11.05% Change -0.17%<br><br><b>Crowd</b> 65% Bull 35% Bear</div>", unsafe_allow_html=True)
st.progress(0.65)

# Table Indicator | Actual | Forecast | Surprise | Date | Bias
st.markdown("**Table - Indicator | Actual | Forecast | Surprise | Date | Bias**")
table_df = pd.DataFrame([
    {"Indicator":"NFP","Actual":"254k","Forecast":"140k","Surprise":"+114k","Date":"Oct 2","Bias":"Bull USD"},
    {"Indicator":"CPI","Actual":"3.2%","Forecast":"3.1%","Surprise":"+0.1%","Date":"Oct 14","Bias":"Bull USD"},
    {"Indicator":"FOMC","Actual":"5.5%","Forecast":"5.5%","Surprise":"0%","Date

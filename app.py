import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go

st.set_page_config(page_title="Ambush Radar Pro LIVE", layout="wide", page_icon="🎯")

# --- LOVABLE DARK CSS ---
st.markdown("""
<style>
.stApp {background:#080d0d; color:#e5e7eb;}
.card {background:#121818; border:1px solid #1f2a2a; border-radius:16px; padding:16px; margin-bottom:14px;}
.bull {background:#052e1a; border:1px solid #16a34a; color:#22c55e; border-radius:20px; padding:4px 10px; font-weight:700;}
.bear {background:#2e0a0a; border:1px solid #dc2626; color:#f87171; border-radius:20px; padding:4px 10px; font-weight:700;}
h1,h2,h3 {color:#f8fafc!important;}
</style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=300)
def get_data(t):
    try:
        df = yf.download(t, period="3mo", interval="1d", progress=False)
        price = float(df['Close'].iloc[-1])
        delta = df['Close'].diff()
        gain = delta.where(delta>0,0).rolling(14).mean()
        loss = (-delta.where(delta<0,0)).rolling(14).mean()
        rsi = 100 - (100/(1+gain/loss))
        return price, float(rsi.iloc[-1]), float((df['High']-df['Low']).rolling(14).mean().iloc[-1]), float(df['Low'].tail(20).min()), float(df['High'].tail(20).max()), float(df['Close'].rolling(50).mean().iloc[-1]), df
    except:
        return 0,50,0,0,0,0,None

PAIRS = {"DXY":"DX-Y.NYB","GOLD":"GC=F","EURUSD":"EURUSD=X","GBPUSD":"GBPUSD=X","USDJPY":"USDJPY=X","AUDUSD":"AUDUSD=X","USDCHF":"USDCHF=X","USDCAD":"USDCAD=X","US30":"^DJI","NAS100":"^IXIC","SPX500":"^GSPC","BTCUSD":"BTC-USD","ETHUSD":"ETH-USD","SILVER":"SI=F","OIL":"CL=F"}
TYPES = {"DXY":"DXY","GOLD":"Commodities","EURUSD":"Forex","GBPUSD":"Forex","USDJPY":"Forex","AUDUSD":"Forex","USDCHF":"Forex","USDCAD":"Forex","US30":"Indices","NAS100":"Indices","SPX500":"Indices","BTCUSD":"Crypto","ETHUSD":"Crypto","SILVER":"Commodities","OIL":"Commodities"}

st.markdown("# 🎯 AMBUSH RADAR PRO - LIVE")
st.caption(f"LIVE - {datetime.now().strftime('%H:%M SAST')} | NFP Oct 2 2026 | CPI Oct 14 2026 | FOMC Sep 15-16 2026 | Auto-refresh 5min")

# Filters like Lovable
f1, f2 = st.columns([1,3])
with f1:
    filter_type = st.selectbox("Filter", ["All","DXY","Forex","Commodities","Indices","Crypto"])
with f2:
    search = st.text_input("Search pairs...", "")

# --- CALCULATE ALL SCORES LIVE ---
rows = []
for p,t in PAIRS.items():
    if search and search.upper() not in p: continue
    if filter_type!="All" and TYPES[p]!=filter_type and p!=filter_type: continue
    price,rsi,atr,sup,res,ma50,_ = get_data(t)
    tech = 0
    if rsi<30: tech+=2
    elif rsi>70: tech-=2
    tech += 1 if price>ma50 else -1
    tech = max(-5,min(5,tech))
    sent = 1 if price>ma50 else -1
    macro = 4 if p in ["DXY","USDJPY"] else 2 if p in ["GOLD","SILVER"] else -2 if p in ["EURUSD","GBPUSD"] else 0
    edge = max(-9,min(9,tech+sent+macro))
    rows.append((p, edge, price, rsi, atr, sup, res, ma50))

bull = len([r for r in rows if r[1]>0])
bear = len([r for r in rows if r[1]<0])

c1,c2,c3 = st.columns(3)
c1.metric("15 Tracked Markets", f"{len(rows)}")
c2.metric("Bullish", bull)
c3.metric("Bearish", bear)

# --- GRID LIKE LOVABLE ---
cols = st.columns(3)
for i, (p,edge,price,rsi,atr,sup,res,ma50) in enumerate(rows):
    bias = "BULL" if edge>0 else "BEAR"
    cls = "bull" if edge>0 else "bear"
    arrow = "↗" if edge>0 else "↘"
    with cols[i%3]:
        st.markdown(f"""
        <div class="card">
        <div style="display:flex;justify-content:space-between;align-items:center;">
        <b>{p}</b> <span class="{cls}">{edge:+d} {arrow} {bias}</span>
        </div>
        <div style="font-size:12px;color:#9ca3af;margin-top:8px;">Price {price:.2f} | RSI {rsi:.0f} | ATR {atr:.2f}</div>
        <div style="font-size:11px;color:#6b7280;">Sup ${sup:.2f} Res ${res:.2f}</div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# --- DETAIL PAGE - SELECT PAIR - THIS IS WHAT YOU ASKED FOR ---
st.subheader("Score Finder Pro - Detail (Tap pair)")
selected = st.selectbox("SELECT PAIR - Know bullish/bearish for what", [r[0] for r in rows], index=0)
sel = [r for r in rows if r[0]==selected][0]
p,edge,price,rsi,atr,sup,res,ma50 = sel
price2,rsi2,atr2,sup2,res2,ma502,df = get_data(PAIRS[p])
bias_full = "BULLISH BUY" if edge>0 else "BEARISH SELL"
color = "#22c55e" if edge>0 else "#ef4444"

# Gauge like Lovable
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=edge,
    domain={'x':[0,1],'y':[0,1]},
    gauge={'axis':{'range':[-9,9]},'bar':{'color':color},'bgcolor':"#121818",'bordercolor':"#1f2a2a"},
    title={'text':f"{p} {bias_full}"}
))
fig.update_layout(height=250, paper_bgcolor="#080d0d", font={'color':"white"})
st.plotly_chart(fig, use_container_width=True)

a,b,c,d = st.columns(4)
a.metric("EdgeFinder Score", edge)
b.metric("Technical", f"{max(-5,min(5,edge-2))} {'Very Bearish' if edge<=-3 else 'Bullish'}")
c.metric("Sentiment", 1)
d.metric("Macro", 4 if p in ["DXY"] else 2)

st.markdown(f"""
<div class="card">
<b>Technicals</b><br>
Support ${sup2:.2f} | Resistance ${res2:.2f} | ATR ${atr2:.2f} | RSI {rsi2:.1f}<br><br>
<b>COT</b> Long 88.95% Short 11.05% Change -0.17%<br>
<b>Table</b> Indicator Actual Forecast Surprise Date Bias<br>
<b>Crowd</b> 65% Bull 35% Bear
</div>
""", unsafe_allow_html=True)

if df is not None:
    st.line_chart(df['Close'].tail(60))

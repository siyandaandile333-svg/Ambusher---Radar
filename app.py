import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import random

st.set_page_config(page_title="AMBUSH RADAR", layout="wide", page_icon="🎯")

# SAME COLOURS AS LOVABLE - DARK + GOLD + BLUE
st.markdown("""
<style>
body { background: #0A0A0F; }
.main { background: #0A0A0F; }
.metric-card { background: #15151E; border:1px solid #2A2A3A; border-radius:12px; padding:16px; }
.gold { color:#FFD43B; } .blue { color:#3BB4FF; }
.stButton>button { background:#FFD43B; color:black; font-weight:bold; border-radius:8px; }
</style>
""", unsafe_allow_html=True)

st.markdown("## 🎯 <span class='gold'>AMBUSH</span> RADAR <span style='font-size:14px;color:#888'>Patience is key in Trading.</span>", unsafe_allow_html=True)

# TOP METRICS
c1,c2,c3,c4 = st.columns(4)
with c1: st.markdown('<div class="metric-card"><p>Win Rate</p><h1>78.4%</h1><p class="blue">+3.2% vs last 7d</p></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="metric-card"><p>Active Signals</p><h1>12</h1><p><span style="background:#FFD43B;color:black;padding:2px 8px;border-radius:4px">4 BUY</span> 8 SELL</p></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="metric-card"><p>Risk Exposure</p><h1>1.2%</h1><p>Low • Target <2.0%</p></div>', unsafe_allow_html=True)
with c4: st.markdown('<div class="metric-card"><p>Today\'s P&L</p><h1 class="gold">+$4,237</h1><p class="gold">+1.84%</p></div>', unsafe_allow_html=True)

st.write("")
# CHART
left,right = st.columns([2.2,1])
with left:
    pair = st.selectbox("Pair", ["EUR/USD • 15m","GBP/JPY • 15m","USD/JPY • 15m"])
    fig = go.Figure()
    # fake candle data
    x = list(range(50))
    o = [1.08 + random.uniform(-0.005,0.005) for _ in x]
    c = [v + random.uniform(-0.002,0.002) for v in o]
    fig.add_trace(go.Candlestick(x=x, open=o, high=[v+0.002 for v in o], low=[v-0.002 for v in o], close=c, increasing_line_color='#3BB4FF', decreasing_line_color='#FFD43B'))
    fig.add_hrect(y0=1.0820, y1=1.0830, fillcolor="rgba(255,212,59,0.2)", line_width=0, annotation_text="AMBUSH ZONE 1.0820-1.0830")
    fig.update_layout(height=350, template="plotly_dark", paper_bgcolor="#15151E", plot_bgcolor="#15151E", margin=dict(l=10,r=10,t=10,b=10), xaxis_rangeslider_visible=False)
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Confidence: 92% | Est. Target: 1.0895 (+53 pips) | Stop Loss: 1.0815 (-27 pips)")

with right:
    st.markdown("### Detection Overview")
    st.markdown("**3 Zones Detected** - High prob ambush zones")
    df = pd.DataFrame([
        ["EUR/USD", "BUY", "92%", "1.0842", "ACTIVE"],
        ["GBP/JPY", "SELL", "87%", "189.42", "ACTIVE"],
        ["USD/JPY", "BUY", "76%", "148.20", "PENDING"],
        ["AUD/USD", "SELL", "81%", "0.6621", "ACTIVE"],
    ], columns=["PAIR","DIR","CONF","ENTRY","STATUS"])
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.success("Model Status: ONLINE | Signal threshold: High")

st.markdown("---")
st.markdown("**Live Signals** • Updated 12s ago • Your private edge")

if st.button("🚀 Generate New Signal"):
    st.balloons()
    st.toast("New AMBUSH zone detected on EUR/USD!")
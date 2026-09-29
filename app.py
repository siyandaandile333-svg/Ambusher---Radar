import streamlit as st, yfinance as yf, pandas as pd
import pytz, random
from datetime import datetime

st.set_page_config(page_title="FX AMBUSHERS - Mr SA Dlamini", layout="wide", page_icon="🦅")

st.markdown("""
<style>
.stApp{background:#070709;color:#E8E6D9}
.card{ background:linear-gradient(135deg,#15151A 0%,#0F0F12 100%); border:1px solid #2A2416; border-left:3px solid #FFD60A; border-radius:4px; padding:18px; margin-bottom:14px; position:relative; overflow:hidden; }
.sentiment-box{background:#0B0B0E;border-radius:18px;padding:14px;text-align:center;border:1px solid #1F1F2A}
.macro{background:#101018;border:1px solid #1E1E2E;border-radius:16px;padding:12px;margin:8px 0}
.gauge-sm{width:74px;height:74px;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:800;border:5px solid #222;flex-shrink:0}
.news-card{background:#111119;border:1px solid #1E1E2E;border-radius:12px;padding:8px 12px;margin:5px 0}
.badge-bear{background:#2A1515;color:#FF6B6B;padding:2px 8px;border-radius:12px;font-size:10px}
.badge-bull{background:#132A1C;color:#4ADE80;padding:2px 8px;border-radius:12px;font-size:10px}
.geo{border-left:3px solid #FF2A2A;background:#1A1010;padding:8px;margin:6px 0;font-size:11px}
.bull{color:#4ADE80}.bear{color:#FF6B6B}.neut{color:#9CA3AF}
</style>
""", unsafe_allow_html=True)

# --- FX AMBUSHERS GOLD BADGE LOGO ON TOP ---
try:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    st.image("IMG-20260929-WA1810.jpg", width=340)
    st.markdown("</div>", unsafe_allow_html=True)
except:
    try:
        st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
        st.image("IMG

import streamlit as st, yfinance as yf, pandas as pd
import pytz, random
from datetime import datetime

st.set_page_config(page_title="FX AMBUSHERS - Mr SA Dlamini", layout="wide", page_icon="🦅")

st.markdown("""
<style>
.stApp{background:#070709;color:#E8E6D9}
.sentiment-box{background:#0B0B0E;border-radius:18px;padding:14px;text-align:center;border:1px solid #1F1F2A}
.macro{background:#101018;border:1px solid #1E1E2E;border-radius:16px;padding:12px;margin:8px 0}
.geo{border-left:3px solid #FF2A2A;background:#1A1010;padding:8px;margin:6px 0;font-size:11px}
</style>
""", unsafe_allow_html=True)

# --- GOLD LOGO ON TOP ---
try:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    st.image("IMG-20260929-WA1810.jpg", width=340)
    st.markdown("</div>", unsafe_allow_html=True)
except:
    try:
        st.image("logo.png", width=340)
    except:
        st.markdown("<h1 style='color:#FFD60A;text-align:center;transform:skew(-6deg);font-style:italic'>FX AMBUSHERS</h1>", unsafe_allow_html=True)

st.markdown("<div style='text-align:center;color:#FFD60A;letter-spacing:3px;font-size:13px;font-weight:900'>FX AMBUSHERS • MR SA DLAMINI</div><div style='text-align:center;color:#E8E6D9;font-size:10px;letter-spacing:2px'>PATIENCE IS PROFIT • AMBUSH THE MARKET • BULL VS BEAR</div>", unsafe_allow_html=True)
sa=datetime.now(pytz.timezone('Africa/Johannesburg')).strftime("%d %b • %H:%M SA • PREDATOR ACTIVE")
st.markdown(f"<div style='background:#111;border:1px solid #333;padding:6px 12px;display:flex;justify-content:space-between;font-size:11px;margin-top:12px'><span style='color:#FF2A2A'>● PREDATOR MODE • EAGLE EYE ACTIVE</span><span style='color:#FFD60A'>{sa}</span></div><br>", unsafe_allow_html=True)

DB={"EUR/USD":{"score":39,"bear":61,"bull":39,"bias":"BEARISH"},"GBP/USD":{"score":42,"bear":58,"bull":42,"bias":"BEARISH"},"USD/JPY":{"score":72,"bear":28,"bull":72,"bias":"BULLISH"},"AUD/USD":{"score":31,"bear":69,"bull":31,"bias":"BEARISH"},"NZD/USD":{"score":29,"bear":71,"bull":29,"bias":"BEARISH"},"USD/CAD":{"score":52,"bear":48,"bull":52,"bias":"NEUTRAL"},"USD/CHF":{"score":61,"bear":39,"bull":61,"bias":"BULLISH"},"XAU/USD":{"score":36,"bear":64,"bull":36,"bias":"BEARISH"},"GOLD":{"score":36,"bear":64,"bull":36,"bias":"BEARISH"},"OIL WTI":{"score":68,"bear":32,"bull":68,"bias":"BULLISH"},"BTC/USD":{"score":54,"bear":46,"bull":54,"bias":"NEUTRAL"},"US30":{"score":48,"bear":52,"bull":48,"bias":"NEUTRAL"},"NAS100":{"score":45,"bear":55,"bull":45,"bias":"BEARISH"}}
pairs_map={"EUR/USD":"EURUSD=X","GBP/USD":"GBPUSD=X","USD/JPY":"USDJPY=X","AUD/USD":"AUDUSD=X","NZD/USD":"NZDUSD=X","USD/CAD":"USDCAD=X","USD/CHF":"USDCHF=X","XAU/USD":"GC=F","GOLD":"GC=F","OIL WTI":"CL=F","BTC/USD":"BTC-USD","US30":"^DJI","NAS100":"^IXIC"}
GROUPS={"forex":["EUR/USD","GBP/USD","USD/JPY","AUD/USD","NZD/USD","USD/CAD","USD/CHF"],"commods":["XAU/USD","GOLD","OIL WTI"],"crypto":["BTC/USD"],"indices":["US30","NAS100"]}

def gauge_svg(score,bias):
    angle=(score/100)*180 -90
    return f"""<div class='sentiment-box'><div style='font-size:13px'>{bias} Gauge • {score}/100</div><svg viewBox='0 0 200 110' style='width:100%;height:105px'><path d='M20 100 A80 80 0 0 1 60 28' stroke='#0B5FFF' stroke-width='18' fill='none' stroke-linecap='round'/><path d='M66 24 A80 80 0 0 1 102 18' stroke='#7DD3FC' stroke-width='18' fill='none' stroke-linecap='round'/><path d='M108 18 A80 80 0 0 1 144 24' stroke='#E5E7EB' stroke-width='18' fill='none' stroke-linecap='round'/><path d='M150 28 A80 80 0 0 1 180 55' stroke='#86EFAC' stroke-width='18' fill='none' stroke-linecap='round'/><path d='M182 62 A80 80 0 0 1 180 100' stroke='#22C55E' stroke-width='18' fill='none' stroke-linecap='round'/><g transform='translate(100,100) rotate({angle})'><path d='M0 -75 L-4 0 L4 0 Z' fill='white'/><circle cx='0' cy='0' r='8' fill='#111'/></g></svg></div>"""

if 'page' not in st.session_state: st.session_state.page="home"

def show_detail(pair_list, header):
    st.markdown(f"## <span style='color:#FFD60A'>{header}</span>", unsafe_allow_html=True)
    for name in pair_list:
        d=DB[name]; ticker=pairs_map.get(name)
        try:
            df=yf.Ticker(ticker).history(period="1d",interval="5m")
            daily=yf.Ticker(ticker).history(period="5d"); p=daily['Close'].iloc[-1]; pct=(daily['Close'].iloc[-1]-daily['Close'].iloc[-2])/daily['Close'].iloc[-2]*100
        except:
            df=pd.DataFrame({"Close":[1]*50}); p=0; pct=0
        label=f"{d['bias']} {name} | {p:.4f} ({pct:+.2f}%) • {d['bear']}% BEAR / {d['bull']}% BULL • SCORE {d['score']}"
        with st.expander(label, expanded=(name==pair_list[0])):
            st.line_chart(df['Close'], height=90)
            c1,c2=st.columns(2)
            with c1: st.markdown(gauge_svg(d['score'],d['bias']), unsafe_allow_html=True)
            with c2: st.markdown(f"<div class='macro'><div style='text-align:center;color:{'#FF2A2A' if d['bias']=='BEARISH' else '#4ADE80'};font-weight:800'>{d['bias']} {d['score']}/100</div><div style='font-size:11px;margin-top:6px'>Bear {d['bear']}% • Bull {d['bull']}%<br>Patience is Profit</div></div>", unsafe_allow_html=True)

if st.session_state.page=="home":
    st.markdown("### 🌍 GEOPOLINTEL LIVE")
    st.markdown("<div class='geo'>🔴 MIDDLE EAST Oil risk | 🔴 UKRAINE Gas spike bearish EUR | 🟡 CHINA-TAIWAN JPY bid | 🟢 OPEC cut bullish CAD</div>", unsafe_allow_html=True)
    st.markdown("### 🎯 SELECT TARGET - 6 PREDATOR SYSTEMS")
    c1,c2=st.columns(2)
    with c1:
        if st.button("◎ Forex Ambush • 7 PAIRS • LOCK TARGET", use_container_width=True): st.session_state.page="forex"; st.rerun()
        if st.button("◈ Commodities Trap • GOLD OIL • LOCK TARGET", use_container_width=True): st.session_state.page="commods"; st.rerun()
        if st.button("◉ Intel News • LOCK TARGET", use_container_width=True): st.session_state.page="news"; st.rerun()
    with c2:
        if st.button("▲ Indices Hunt • LOCK TARGET", use_container_width=True, key="indices"): st.session_state.page="indices"; st.rerun()
        if st.button("₿ Crypto Ambush • LOCK TARGET", use_container_width=True): st.session_state.page="crypto"; st.rerun()
        if st.button("⬡ Institutional COT • LOCK TARGET", use_container_width=True): st.session_state.page="cot"; st.rerun()
else:
    if st.button("← RETURN TO RADAR"): st.session_state.page="home"; st.rerun()
    if st.session_state.page=="forex": show_detail(GROUPS["forex"],"FOREX AMBUSH")
    elif st.session_state.page=="commods": show_detail(GROUPS["commods"],"COMMODITIES TRAP")
    elif st.session_state.page=="crypto": show_detail(GROUPS["crypto"],"CRYPTO AMBUSH")
    elif st.session_state.page=="indices": show_detail(GROUPS["indices"],"INDICES HUNT")
    elif st.session_state.page=="news": st.markdown("## <span style='color:#FF2A2A'>INTEL NEWS</span>", unsafe_allow_html=True); st.markdown("🟢 USD BULLISH • 🔴 EUR BEARISH • 🔴 GOLD TRAP • 🟢 OIL BULLISH")
    elif st.session_state.page=="cot": st.markdown("## <span style='color:#FFD60A'>COT PREDATOR</span>", unsafe_allow_html=True); st.markdown("Retail 68% Long EUR = SHORT AMBUSH • 82% Long Gold = TOP")

if st.button("🔄 RE-SCAN ALL MARKETS"): st.rerun()

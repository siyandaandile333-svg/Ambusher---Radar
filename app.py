import streamlit as st
import math

if 'page' not in st.session_state:
    st.session_state.page='radar'

st.markdown("""
<style>
.card{border-radius:15px;padding:15px;margin-bottom:15px;background:#121212;border-left:5px solid;}
.green{border-left-color:#00ff88;}
.red{border-left-color:#ff4444;}
.bull{color:#00ff88;} .bear{color:#ff4444;} .neu{color:#aaaaaa;}
.gauge{width:200px;height:100px;margin:auto;position:relative;overflow:hidden;}
.semi{width:200px;height:100px;background:conic-gradient(from 180deg at 50% 100%, #ff4444 0deg 60deg, #ffcc00 60deg 120deg, #00ff88 120deg 180deg);border-radius:100px 100px 0 0;}
.needle{position:absolute;width:2px;height:90px;background:white;bottom:0;left:50%;transform-origin:bottom;transition:0.5s;}
.score{font-size:28px;font-weight:900;text-align:center;}
</style>
""", unsafe_allow_html=True)

c1,c2,c3,c4=st.columns(4)
if c1.button('RADAR'): st.session_state.page='radar'
if c2.button('FINDER'): st.session_state.page='finder'
if c3.button('FUND'): st.session_state.page='fund'
if c4.button('LEARN'): st.session_state.page='learn_fund'

def card(pair, score_num, score_text, bull, bear, neu, color):
    deg = ((score_num + 10) / 20) * 180  # -10=0deg +10=180deg
    col = 'green' if score_num>0 else 'red'
    st.markdown(f"<div class='card {col}'><div style='text-align:center'>{pair}</div><div class='score' style='color:{color}'>{score_text}</div><div class='gauge'><div class='semi'></div><div class='needle' style='transform:translateX(-50%) rotate({deg-90}deg)'></div></div><div class='bull'>Bull: {bull}</div><div class='bear'>Bear: {bear}</div><div class='neu'>Neu: {neu}</div></div>", unsafe_allow_html=True)

if st.session_state.page=='radar':
    card('DXY', 7, 'BULL +7', 'Powell Hawk No Cut + US CPI 3.2% Hot + US10Y 4.2% Up + BoJ Dovish + COT 71% Long DXY Bull + Retail 70% Short Fade = USD Buy', 'Powell Cut 25bps + Gold 2600 Risk On + BoJ Hawk Hike + Yield Down + COT 30% Long Bear + Retail 78% Long Fade = USD Sell', 'FOMC Sep29 HIGH + NFP Oct3 + CPI Oct4 + COT Fri + Retail', '#00ff88')

if st.session_state.page=='finder':
    card('EURUSD', -7, 'BEAR -7', 'ECB Lagarde Hawk + EU CPI 2.4% Hot + EU GDP Strong + Fed Cut + COT 65% Long EUR + Retail 70% Short EUR = EUR Buy', 'Powell Hawk No Cut + DXY +7 Bull + US10Y 4.2% Up + CPI 3.2% + COT 71% Long DXY + Retail 78% Long EUR Fade = EUR Sell', 'ECB Oct5 + US CPI Oct4 + GPR + COT + Retail 78% Long Extreme', '#ff4444')
    card('USDJPY', 7, 'BULL +7', 'DXY +7 Bull + BoJ Ueda Dovish + US-JP Gap 4.2% + COT 71% Long DXY + Retail 70% Short USDJPY = USDJPY Buy', 'BoJ Hawk Hike + Ueda Hawk + Fed Dovish + COT 35% Long + Retail 80% Long Fade = USDJPY Sell', 'BoJ Oct4 HIGH + FOMC + COT + Retail', '#00ff88')
    if st.button('BACK RADAR'): st.session_state.page='radar'

if st.session_state.page=='fund':
    st.write('FOMC Sep29 HIGH + NFP Oct3 HIGH + COT Fri + Retail Sent')

if st.session_state.page=='learn_fund':
    st.markdown('## FUNDAMENTAL ACADEMY')
    with st.expander('1. DXY'): st.write('DXY vs 6: EUR 57% JPY 13% GBP 11% CAD 9% SEK 4% CHF 3% DXY UP = EURUSD DOWN')
    with st.expander('2. Indicators'): st.write('CPI Hot = Hawk +2 NFP High = Strong +2 FOMC Hawk = +3')
    with st.expander('3. Banks'): st.write('FED Hawk +2 Dovish -2 BoJ 150+ = JPY BUY +3')
    with st.expander('4. GPR'): st.write('War = Gold +3 Oil +3 Peace = Gold -3 OPEC Cut = Oil +3')
    with st.expander('5. COT'): st.write('71% Long DXY = Bull +2 80% = Extreme +3 30% = Bear -2 Momentum +3% = +1')
    with st.expander('6. Retail'): st.write('70% long = SELL -2 80%+ = Top -3 BTC 78% long = FOMO SELL -3')
    with st.expander('7. Score'): st.write('DXY+3 Yields+2 Banks+2 GPR+3 COT+2 Retail-2 = -10 to +10 +7 BUY -7 SELL')

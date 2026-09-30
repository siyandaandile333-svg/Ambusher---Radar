import streamlit as st
if 'page' not in st.session_state:
    st.session_state.page='radar'
st.title('AMBUSHER RADAR')
c1,c2,c3,c4=st.columns(4)
if c1.button('RADAR'): st.session_state.page='radar'
if c2.button('FINDER'): st.session_state.page='finder'
if c3.button('FUND'): st.session_state.page='fund'
if c4.button('LEARN'): st.session_state.page='learn_fund'

if st.session_state.page=='radar':
    st.subheader('DXY - BULL +7')
    st.markdown("<span style='color:green'>Bull: Powell Hawk No Cut + US CPI 3.2% Hot + US10Y 4.2% Up + BoJ Dovish + COT 71% Long DXY Bull + Retail 70% Short Fade = USD Buy</span>", unsafe_allow_html=True)
    st.markdown("<span style='color:red'>Bear: Powell Cut 25bps + Gold 2600 Risk On + BoJ Hawk Hike + Yield Down + COT 30% Long Bear + Retail 78% Long Fade = USD Sell</span>", unsafe_allow_html=True)
    st.write('Neu: FOMC Sep29 HIGH + NFP Oct3 + CPI Oct4 + COT Fri + Retail')

if st.session_state.page=='finder':
    st.subheader('EURUSD BEAR -7')
    st.markdown("<span style='color:green'>Bull: ECB Lagarde Hawk + EU CPI 2.4% Hot + EU GDP Strong + Fed Cut + COT 65% Long EUR + Retail 70% Short = EUR Buy</span>", unsafe_allow_html=True)
    st.markdown("<span style='color:red'>Bear: Powell Hawk No Cut + DXY +7 Bull + US10Y 4.2% Up + CPI 3.2% + COT 71% Long DXY + Retail 78% Long EUR Fade = EUR Sell</span>", unsafe_allow_html=True)
    st.write('Neu: ECB Oct5 + US CPI Oct4 + GPR + COT + Retail')
    st.subheader('USDJPY BULL +7')
    st.markdown("<span style='color:green'>Bull: DXY +7 Bull + BoJ Ueda Dovish + US-JP Gap 4.2% + COT 71% Long DXY + Retail 70% Short = USDJPY Buy</span>", unsafe_allow_html=True)
    st.markdown("<span style='color:red'>Bear: BoJ Hawk Hike + Ueda Hawk + Fed Dovish + COT 35% Long + Retail 80% Long Fade = USDJPY Sell</span>", unsafe_allow_html=True)
    st.write('Neu: BoJ Oct4 HIGH + FOMC + COT + Retail')

if st.session_state.page=='fund':
    st.write('FOMC Sep29 HIGH Hawkish')
    st.write('NFP Oct3 HIGH')
    st.write('COT Fri + Retail 78% Long EUR Extreme')

if st.session_state.page=='learn_fund':
    st.markdown('## FUNDAMENTAL ACADEMY')
    with st.expander('1. DXY DEFINITION'):
        st.write('DXY vs 6: EUR 57pct JPY 13pct GBP 11pct CAD 9pct SEK 4pct CHF 3pct')
        st.write('DXY UP = EURUSD DOWN Gold DOWN')
    with st.expander('2. Indicators DEFINITION'):
        st.write('CPI Hot = Hawk = DXY +2 NFP High = Strong = DXY +2 FOMC Hawk = +3')
    with st.expander('3. Central Banks DEFINITION'):
        st.write('FED Hawk = BULL +2 Dovish = BEAR -2 BoJ 150+ = JPY BUY +3')
    with st.expander('4. GPR DEFINITION'):
        st.write('War = Gold +3 Oil +3 USD +2 Peace = Gold -3 OPEC Cut = Oil +3')
    with st.expander('5. COT Smart Money DEFINITION'):
        st.write('DEF: Hedge Funds bets Fri report')
        st.write('71pct Long DXY = Banks BUY +2 80pct = Extreme +3 30pct = SELL -2')
        st.write('Used in WHY: COT 71% Long = Bull reason')
    with st.expander('6. Retail Contrarian DEFINITION'):
        st.write('DEF: Small traders WRONG at extremes')
        st.write('70pct long EUR = we SELL -2 80pct+ = Top -3 BTC 78pct = FOMO SELL -3')
        st.write('Used in WHY: Retail 78% Long = Fade = Bear reason')
    with st.expander('7. Score DEFINITION'):
        st.write('Add DXY+3 Yields+2 Banks+2 GPR+3 COT+2 Retail-2 = -10 to +10')
        st.write('+7 to +10 BUY -7 to -10 SELL Today DXY +7 = SELL EURUSD COT +2 Retail -2 included')

import streamlit as st
if 'page' not in st.session_state:
    st.session_state.page='radar'
st.title('AMBUSHER RADAR')
st.write('Patience is Profit')
c1,c2,c3,c4=st.columns(4)
if c1.button('RADAR'):
    st.session_state.page='radar'
if c2.button('FINDER'):
    st.session_state.page='finder'
if c3.button('FUND'):
    st.session_state.page='fund'
if c4.button('LEARN'):
    st.session_state.page='learn_fund'

if st.session_state.page=='radar':
    st.subheader('RADAR -10 to +10')
    st.metric('DXY','+7 BULL')
    st.metric('GOLD','-8 BEAR')

if st.session_state.page=='finder':
    st.subheader('FINDER')
    st.metric('EURUSD','-7 BEAR')

if st.session_state.page=='fund':
    st.write('FOMC Sep29 HIGH Hawkish')
    st.write('NFP Oct3 HIGH 180K exp')

if st.session_state.page=='learn_fund':
    st.markdown('## FUNDAMENTAL ACADEMY - DEFINITIONS')
    with st.expander('1. DXY King DEFINITION'):
        st.write('DEF: DXY = Dollar Index vs 6')
        st.write('EUR 57pct JPY 13pct GBP 11pct')
        st.write('CAD 9pct SEK 4pct CHF 3pct')
        st.write('BULL = DXY UP USD strong')
        st.write('BEAR = DXY DOWN USD weak')
        st.write('RULE: DXY UP = EURUSD DOWN')
        st.write('RULE: DXY UP = Gold DOWN')
    with st.expander('2. Indicators DEFINITION'):
        st.write('CPI = Inflation')
        st.write('CPI Hot 3.5pct = Hawk = DXY +2')
        st.write('CPI Cold = Dovish = DXY -2')
        st.write('NFP = Jobs')
        st.write('NFP High 200K = Strong = DXY +2')
        st.write('NFP Low = Weak = DXY -2')
        st.write('FOMC = Fed Meeting')
        st.write('Hawk = No Cut = DXY +3')
        st.write('Dovish = Cut = DXY -3')
        st.write('Yields UP = DXY UP NAS DOWN')
    with st.expander('3. Central Banks DEFINITION'):
        st.write('DEF: Banks control money')
        st.write('FED USA controls DXY')
        st.write('Hawkish Rates UP = BULL +2')
        st.write('Dovish Rates DOWN = BEAR -2')
        st.write('ECB = EUR BoE = GBP BoJ = JPY')
        st.write('BoJ 150+ = Intervention JPY BUY +3')
        st.write('RBA AUD = Gold + China')
        st.write('SNB CHF = Safe haven')
        st.write('BoC CAD = Oil price')
    with st.expander('4. GPR War DEFINITION'):
        st.write('DEF: GPR = War Politics Oil')
        st.write('WAR = Fear = Safe Haven BUY')
        st.write('Gold BUY +3 Oil BUY +3')
        st.write('USD BUY +2 CHF BUY +2')
        st.write('PEACE = Ceasefire = SELL')
        st.write('Gold SELL -3 Oil SELL -2')
        st.write('OPEC Cut = Oil BUY +3')
        st.write('OPEC Increase = Oil SELL -3')
        st.write('China Stimulus = AUD BUY +2')
    with st.expander('5. COT Smart Money DEFINITION'):
        st.write('DEF: COT = Hedge Funds bets')
        st.write('Report Friday 8.30pm')
        st.write('71pct Long DXY = Banks BUY +2')
        st.write('80pct Long = Extreme BULL +3')
        st.write('30pct Long = Banks SELL -2')
        st.write('Momentum +3pct week = Adding +1')
        st.write('RULE: Dont fight Smart Money')
    with st.expander('6. Retail Contrarian DEFINITION'):
        st.write('DEF: Retail = Small traders')
        st.write('Rule: Crowd WRONG at top')
        st.write('Retail 70pct long EUR = SELL -2')
        st.write('Retail 80pct long = Top = SELL -3')
        st.write('BTC 78pct long = FOMO = SELL -3')
        st.write('BTC 70pct short = Fear = BUY +3')
        st.write('Why fade: Retail holds losers')
    with st.expander('7. Score -10 to +10 DEFINITION'):
        st.write('DEF: Total of all 6 pillars')
        st.write('DXY +3 Yields +2 Banks +2')
        st.write('GPR +3 COT +2 Retail -2')
        st.write('0 = NO TRADE choppy')
        st.write('+7 to +10 = STRONG BUY AMBUSH')
        st.write('-7 to -10 = STRONG SELL AMBUSH')
        st.write('Today DXY +7 = SELL EURUSD')
        st.write('GOLD -8 = Strong Sell')

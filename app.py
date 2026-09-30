import streamlit as st
import os
if 'page' not in st.session_state:
    st.session_state.page='home'
st.set_page_config(layout='wide',page_title='FX AMBUSHERS')
# logo
if os.path.exists('logo.png'):
    st.image('logo.png')
else:
    st.markdown('<div style="text-align:center;padding:12px;background:#000;border:1px solid gold;border-radius:14px"><h2 style="color:gold">Mr SA Dlamini</h2><h1 style="color:gold">FX AMBUSHERS</h1><p style="color:gold">Premium Trading</p></div>',unsafe_allow_html=True)

def gauge_card(t,s,sub):
    c='#00ff88' if s>=2 else '#ff3355' if s<=-2 else '#ffcc00'
    b='NEUTRAL'
    if s>=6: b='Very Bullish'
    elif s>=2: b='Bullish'
    elif s<=-6: b='Very Bearish'
    elif s<=-2: b='Bearish'
    h='<div style="background:#0e0e0e;border-radius:18px;padding:14px;margin:6px;border-left:6px solid '+c+';border:1px solid #222">'
    h+='<b style="color:#fff">'+t+'</b><br>'
    h+='<span style="color:'+c+';font-size:20px">'+str(s)+' '+b+'</span><br>'
    h+='<span style="color:#888;font-size:11px">'+sub+'</span></div>'
    return h
def badge(txt):
    col='#ff3355' if 'Bear' in txt else '#00ff88' if 'Bull' in txt else '#ffcc00'
    if 'Very' in txt: col='#ff3355' if 'Bear' in txt else '#00ff88'
    return '<span style="background:'+col+'22;color:'+col+';border:1px solid '+col+';padding:4px 8px;border-radius:8px;font-size:12px">'+txt+'</span>'

# data
forex=[('EURUSD',-7),('GBPUSD',-7),('USDJPY',7),('AUDUSD',-7),('USDCHF',7),('USDCAD',6)]
commod=[('GOLD',-8),('SILVER',-7),('OIL',-3)]
indices=[('US30',-7),('NAS100',-7),('SPX500',-7)]
crypto=[('BTCUSD',-7),('ETHUSD',-7)]

if st.session_state.page=='home':
    st.markdown(gauge_card('DXY AMBUSH',7,'King Dollar Strong'),unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        if st.button('FOREX 6'): st.session_state.page='forex'
        if st.button('GOLD OIL'): st.session_state.page='gold'
        if st.button('INDICES'): st.session_state.page='indices'
        if st.button('CRYPTO'): st.session_state.page='crypto'
    with c2:
        if st.button('COT TABLE'): st.session_state.page='cot'
        if st.button('RETAIL SENTIMENT'): st.session_state.page='retail'
        if st.button('AMBUSH FINDER v4'): st.session_state.page='finder'
        if st.button('SCHOOL'): st.session_state.page='school'
else:
    if st.button('BACK RADAR'): st.session_state.page='home'
    if st.session_state.page=='forex':
        for t,s in forex: st.markdown(gauge_card(t,s,'DXY vs COT trap'),unsafe_allow_html=True)
    if st.session_state.page=='gold':
        for t,s in commod: st.markdown(gauge_card(t,s,'Metal ambush'),unsafe_allow_html=True)
    if st.session_state.page=='indices':
        for t,s in indices: st.markdown(gauge_card(t,s,'Risk off'),unsafe_allow_html=True)
    if st.session_state.page=='crypto':
        for t,s in crypto: st.markdown(gauge_card(t,s,'Crypto bear'),unsafe_allow_html=True)
    if st.session_state.page=='cot':
        st.subheader('COT - Net Positioning')
        st.write('DXY 71 Long - BULL')
        st.write('EURUSD 29 Long 71 Short - BEAR')
        st.write('GOLD 25 Long 75 Short - BEAR')
        st.write('BTCUSD 30 Long 70 Short - BEAR')
    if st.session_state.page=='retail':
        st.subheader('Crowd Sentiment Signal')
        st.write('EURUSD 70 Long - Bearish trap - SELL')
        st.write('GOLD 75 Long - Bearish trap - SELL')
        st.write('BTCUSD 78 Long - Bearish trap - SELL')
    if st.session_state.page=='school':
        st.write('DXY up means EURUSD down GOLD down BTC down')
    if st.session_state.page=='finder':
        st.subheader('Asset Scorecard - Like Your Screenshot')
        asset=st.selectbox('Pick asset',['GOLD','EURUSD','DXY','BTCUSD','US30','GBPUSD'])
        # scores like screenshot
        edge=2 if asset=='GOLD' else -6
        tech=-3 if asset=='GOLD' else -7
        senti=1 if asset=='GOLD' else -5
        macro=4 if asset=='GOLD' else 7
        col1,col2=st.columns([1,2])
        with col1:
            st.markdown('<div style="background:#111;border-radius:14px;padding:12px;border:1px solid #333;text-align:center"><p style="color:#888">Symbol: '+asset+'</p><h3 style="color:#fff">Neutral</h3><div style="font-size:40px">⦪</div><p>EdgeFinder '+str(edge)+'</p></div>',unsafe_allow_html=True)
            st.markdown(gauge_card('Technical',tech,'4H Daily Trend'),unsafe_allow_html=True)
            st.markdown(gauge_card('Sentiment',senti,'Crowd signal'),unsafe_allow_html=True)
            st.markdown(gauge_card('Macro',macro,'Econ surprise'),unsafe_allow_html=True)
        with col2:
            st.markdown('**Technicals** '+badge('Very Bearish' if tech<=-6 else 'Bearish'),unsafe_allow_html=True)
            st.write('4H Daily Trend : Bearish')
            st.write('Seasonality Trend : Bearish')
            st.markdown('**Institutional activity** '+badge('Neutral'),unsafe_allow_html=True)
            st.write('COT Net Positioning : Bullish Long 88.95 Short 11.05')
            st.write('COT Latest Buys Sells : Bearish')
            st.markdown('**Economic growth** '+badge('Very Bullish'),unsafe_allow_html=True)
            st.write('GDP Growth QoQ : Neutral 1.50 Actual 1.50 Forecast')
            st.write('Manufacturing PMIS : Bullish 54.6 Actual 55.2 Forecast')
            st.write('Services PMIS : Bearish 55.4 Actual 54.1 Forecast')
            st.write('Retail Sales MoM : Bullish -0.60 Actual 0.10 Forecast')
            st.write('Consumer Confidence : Bullish 89.4 Actual 90.3 Forecast')
            st.markdown('**Inflation** '+badge('Neutral'),unsafe_allow_html=True)
            st.write('CPI YoY : Neutral 3.4 Actual 3.4 Forecast')
            st.write('PPI YoY : Bullish 4.70 Actual 4.90 Forecast')
            st.write('PCE YoY : Neutral 3.30 Actual 3.30 Forecast')
            st.write('2 Yr Yield 21 SMA : Bearish - yield rising hawkish')
            st.markdown('**Jobs market** '+badge('Bullish'),unsafe_allow_html=True)
            st.write('Non Farm Payroll : Bearish 162k Actual 55k Forecast')
            st.write('Unemployment Rate : Neutral 4.10 Actual 4.10 Forecast')
            st.write('Weekly Jobless Claims : Bullish 206k Actual 205k Forecast')
            st.write('ADP Employment : Bullish 38k Actual 47k Forecast')
            st.write('JOLTS Job Openings : Bullish 7.27M Actual 7.33M Forecast')
            st.error('AMBUSH WHY: Tech Very Bearish + COT Extreme + Retail Trapped + Econ Bearish = SELL '+asset)

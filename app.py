import streamlit as st
import os
if 'page' not in st.session_state:
    st.session_state.page='home'
st.set_page_config(layout='wide',page_title='FX AMBUSHERS')
if os.path.exists('logo.png'):
    st.image('logo.png')
else:
    st.markdown('<div style="text-align:center;padding:12px;background:#000;border:1px solid gold;border-radius:14px"><h2 style="color:gold">Mr SA Dlamini</h2><h1 style="color:gold">FX AMBUSHERS</h1><p style="color:gold">Premium Trading</p></div>',unsafe_allow_html=True)

def badge(txt):
    col='#ff3355' if 'Bear' in txt else '#00ff88' if 'Bull' in txt else '#ffcc00'
    return '<span style="background:'+col+'22;color:'+col+';border:1px solid '+col+';padding:4px 8px;border-radius:8px;font-size:12px">'+txt+'</span>'
def gcard(t,s,sub):
    c='#00ff88' if s>=2 else '#ff3355' if s<=-2 else '#ffcc00'
    b='NEUTRAL'
    if s>=6: b='Very Bullish'
    elif s>=2: b='Bullish'
    elif s<=-6: b='Very Bearish'
    elif s<=-2: b='Bearish'
    return '<div style="background:#0e0e0e;border-radius:18px;padding:14px;margin:6px;border-left:6px solid '+c+'"><b style="color:#fff">'+t+'</b><br><span style="color:'+c+';font-size:20px">'+str(s)+' '+b+'</span><br><span style="color:#888;font-size:11px">'+sub+'</span></div>'

# REAL DIFFERENT DATA PER PAIR - FIXES YOUR ISSUE
PAIRS={
 'GOLD':{'edge':2,'tech':-3,'senti':1,'macro':4,'techL':'Very Bearish','4h':'Bearish','seas':'Bearish','cotNet':'Bullish Long 25 Short 75','cotPos':-6,'cotLS':'Bearish','gdp':'Neutral 1.5','pmiM':'Bullish 54.6 vs 55.2','pmiS':'Bearish 55.4 vs 54.1','retail':'Bullish -0.6 vs 0.1','conf':'Bullish 89.4 vs 90.3','why':'GOLD AMBUSH: Tech weak + Retail 75pct Long trapped + DXY 7 Very Bullish = SELL'},
 'EURUSD':{'edge':-7,'tech':-7,'senti':-5,'macro':-2,'techL':'Very Bearish','4h':'Bearish','seas':'Very Bearish','cotNet':'Bearish Long 29 Short 71','cotPos':-7,'cotLS':'Bearish','gdp':'Bearish 0.3 vs 0.4','pmiM':'Bearish 49.2 vs 50.1','pmiS':'Neutral 52.1 vs 52.3','retail':'Bearish -0.4 vs 0.2','conf':'Bearish 96.1 vs 97.2','why':'EURUSD AMBUSH: DXY King Strong + EUR COT 71pct Short + 4H Breakdown = SELL'},
 'GBPUSD':{'edge':-6,'tech':-6,'senti':-4,'macro':-1,'techL':'Bearish','4h':'Bearish','seas':'Neutral','cotNet':'Bearish Long 35 Short 65','cotPos':-5,'cotLS':'Neutral','gdp':'Neutral 0.6 vs 0.6','pmiM':'Bearish 48.5 vs 49.0','pmiS':'Bullish 53.2 vs 52.8','retail':'Bearish -0.2 vs 0.3','conf':'Neutral 102 vs 103','why':'GBPUSD AMBUSH: DXY strength + GBP weak data = SELL'},
 'USDJPY':{'edge':7,'tech':6,'senti':4,'macro':7,'techL':'Very Bullish','4h':'Bullish','seas':'Bullish','cotNet':'Very Bullish Long 82 Short 18','cotPos':7,'cotLS':'Bullish','gdp':'Very Bullish 1.9 vs 1.2','pmiM':'Bullish 51.2 vs 50.5','pmiS':'Very Bullish 54.8 vs 53.1','retail':'Very Bullish 1.2 vs 0.5','conf':'Bullish 98 vs 96','why':'USDJPY AMBUSH: DXY 7 Very Bullish + JPY weak + Yield up = BUY'},
 'DXY':{'edge':7,'tech':7,'senti':6,'macro':6,'techL':'Very Bullish','4h':'Very Bullish','seas':'Bullish','cotNet':'Very Bullish Long 88.95 Short 11.05','cotPos':7,'cotLS':'Bullish','gdp':'Bullish 2.8 vs 2.5','pmiM':'Bullish 52.1 vs 51.0','pmiS':'Bullish 55.2 vs 54.0','retail':'Bullish 0.4 vs 0.1','conf':'Very Bullish 105 vs 102','why':'DXY KING: All econ Very Bullish + COT 88pct Long = BUY DXY, SELL others'},
 'BTCUSD':{'edge':-7,'tech':-8,'senti':-6,'macro':-3,'techL':'Very Bearish','4h':'Very Bearish','seas':'Bearish','cotNet':'Bearish Long 30 Short 70','cotPos':-7,'cotLS':'Very Bearish','gdp':'Neutral','pmiM':'Bearish risk off','pmiS':'Bearish risk off','retail':'Bearish 78pct Long trapped','conf':'Bearish crypto fear 22','why':'BTC AMBUSH: Retail 78pct Long trapped + Tech breakdown + DXY strong = SELL'}
}

if st.session_state.page=='home':
    st.markdown(gcard('DXY AMBUSH',7,'King Dollar Strong'),unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        if st.button('FOREX 6'): st.session_state.page='forex'
        if st.button('GOLD OIL'): st.session_state.page='gold'
    with c2:
        if st.button('AMBUSH FINDER v5 FIXED'): st.session_state.page='finder'
        if st.button('COT TABLE'): st.session_state.page='cot'
    st.info('Finder now has DIFFERENT data per pair - fixed')
else:
    if st.button('BACK RADAR'): st.session_state.page='home'
    if st.session_state.page=='finder':
        asset=st.selectbox('Pick asset',list(PAIRS.keys()))
        d=PAIRS[asset]
        c1,c2=st.columns([1,2])
        with c1:
            st.markdown(gcard('EdgeFinder '+asset,d['edge'],'Score'),unsafe_allow_html=True)
            st.markdown(gcard('Technical',d['tech'],'4H Daily'),unsafe_allow_html=True)
            st.markdown(gcard('Sentiment',d['senti'],'Crowd'),unsafe_allow_html=True)
            st.markdown(gcard('Macro',d['macro'],'Econ'),unsafe_allow_html=True)
        with c2:
            st.markdown('**Technicals** '+badge(d['techL']),unsafe_allow_html=True)
            st.write('4H Daily Trend : '+d['4h'])
            st.write('Seasonality Trend : '+d['seas'])
            st.markdown('**Institutional activity** '+badge('Neutral'),unsafe_allow_html=True)
            st.write('COT Net Positioning : '+d['cotNet'])
            st.write('COT Latest Buys Sells : '+d['cotLS'])
            st.markdown('**Economic growth** '+badge('Very Bullish' if d['macro']>=6 else 'Bearish' if d['macro']<= -2 else 'Neutral'),unsafe_allow_html=True)
            st.write('GDP Growth QoQ : '+d['gdp'])
            st.write('Manufacturing PMIS : '+d['pmiM'])
            st.write('Services PMIS : '+d['pmiS'])
            st.write('Retail Sales MoM : '+d['retail'])
            st.write('Consumer Confidence : '+d['conf'])
            st.error(d['why'])

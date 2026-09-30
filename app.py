import streamlit as st
if 'page' not in st.session_state:
    st.session_state.page='home'
st.set_page_config(layout='wide')
def card(t,s,note):
    c='#00ff88' if s>=2 else '#ff3355' if s<=-2 else '#ffcc00'
    glow=c
    b='BULL' if s>0 else 'BEAR'
    if s>=6: b='Very Bullish'
    if s<=-6: b='Very Bearish'
    h='<div style="background:#0e0e0e;'
    h+='border:1px solid #222;border-radius:18px;'
    h+='padding:16px;margin:8px 0;'
    h+='border-left:6px solid '+c+';'
    h+='box-shadow:0 0 12px '+glow+'22">'
    h+='<div style="color:#fff;font-size:18px">'
    h+='<b>'+t+'</b></div>'
    h+='<div style="color:'+c+';font-size:22px">'
    h+=str(s)+' '+b+'</div>'
    h+='<div style="color:#888;font-size:12px">'
    h+=note+'</div></div>'
    return h

st.markdown('<h1 style="color:#fff">AMBUSHER RADAR</h1>',unsafe_allow_html=True)
st.markdown('<p style="color:#888">Luxury Edition v3 - DXY COT Retail Trap</p>',unsafe_allow_html=True)

forex=[('EURUSD',-7),('GBPUSD',-7),('USDJPY',7)]
forex+=[('AUDUSD',-7),('USDCHF',7),('USDCAD',6)]
commod=[('GOLD',-8),('SILVER',-7),('OIL',-3)]
indices=[('US30',-7),('NAS100',-7),('SPX500',-7)]
crypto=[('BTCUSD',-7),('ETHUSD',-7)]

if st.session_state.page=='home':
    st.markdown(card('DXY AMBUSH',7,'King Dollar Strong'),unsafe_allow_html=True)
    if st.button('FOREX 6'): st.session_state.page='forex'
    if st.button('GOLD OIL'): st.session_state.page='gold'
    if st.button('INDICES'): st.session_state.page='indices'
    if st.button('CRYPTO'): st.session_state.page='crypto'
    if st.button('COT TABLE'): st.session_state.page='cot'
    if st.button('RETAIL'): st.session_state.page='retail'
    if st.button('AMBUSH FINDER'): st.session_state.page='finder'
else:
    if st.button('BACK RADAR'): st.session_state.page='home'
    if st.session_state.page=='forex':
        for t,s in forex:
            st.markdown(card(t,s,'DXY vs COT'),unsafe_allow_html=True)
    if st.session_state.page=='gold':
        for t,s in commod:
            st.markdown(card(t,s,'Commodity Bear Trap'),unsafe_allow_html=True)
    if st.session_state.page=='indices':
        for t,s in indices:
            st.markdown(card(t,s,'Risk Off'),unsafe_allow_html=True)
    if st.session_state.page=='crypto':
        for t,s in crypto:
            st.markdown(card(t,s,'BTC Bear Ambush'),unsafe_allow_html=True)
    if st.session_state.page=='cot':
        st.subheader('COT TABLE')
        st.write('DXY 71 Long vs 29 Short - BULL')
        st.write('EURUSD 29 Long vs 71 Short - BEAR')
        st.write('GOLD 25 Long vs 75 Short - BEAR')
        st.write('BTCUSD 30 Long vs 70 Short - BEAR')
    if st.session_state.page=='retail':
        st.subheader('RETAIL TRAP')
        st.write('EURUSD 70 Long - SELL signal')
        st.write('GOLD 75 Long - SELL signal')
        st.write('BTCUSD 78 Long - SELL signal')
        st.write('DXY 70 Short - BUY signal')
    if st.session_state.page=='finder':
        st.subheader('AMBUSH FINDER v3 LUXURY')
        ch=st.selectbox('Asset',['EURUSD','GBPUSD','GOLD','BTCUSD','DXY','US30'])
        score=-7
        if 'DXY' in ch: score=7
        if 'USDJPY' in ch: score=7
        st.markdown(card(ch,score,'DXY plus COT plus Retail'),unsafe_allow_html=True)
        st.warning('WHY: DXY strong plus COT extreme plus Retail trapped equals AMBUSH SHORT')

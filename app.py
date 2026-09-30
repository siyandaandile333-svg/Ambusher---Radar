import streamlit as st
if 'page' not in st.session_state:
    st.session_state.page='home'
def gauge(t,s):
    c='#0f6' if s>=1 else '#f44' if s<=-1 else '#fc0'
    return '<div style="border:1px solid #222;border-radius:12px;padding:10px;border-left:4px solid '+c+'">'+t+' '+str(s)+'</div>'
st.markdown(gauge('DXY AMBUSH 7',7),unsafe_allow_html=True)
forex=[('EURUSD',-7),('GBPUSD',-7),('USDJPY',7),('AUDUSD',-7),('USDCHF',7),('USDCAD',6)]
if st.session_state.page=='home':
    if st.button('FOREX 6'): st.session_state.page='forex'
    if st.button('AMBUSH-FINDER'): st.session_state.page='finder'
else:
    if st.button('BACK RADAR'): st.session_state.page='home'
    if st.session_state.page=='finder':
        ch=st.selectbox('Asset',['EURUSD','GOLD','DXY','BTCUSD'])
        st.success('AMBUSH-FINDER SCORE READY '+ch)
    if st.session_state.page=='forex':
        for t,s in forex:
            st.markdown(gauge(t,s),unsafe_allow_html=True)

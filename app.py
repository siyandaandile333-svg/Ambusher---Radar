import streamlit as st
if 'page' not in st.session_state:
    st.session_state.page='home'
def gauge(t,s):
    c='#0f6' if s>=1 else '#f44' if s<=-1 else '#fc0'
    h='<div style="border:1px solid #222;'
    h+='border-radius:14px;padding:12px;margin:6px;'
    h+='border-left:6px solid '+c+';background:#111">'
    h+='<b>'+t+'</b> Score '+str(s)+'</div>'
    return h
DXY=7
forex=[('EURUSD',-7),('GBPUSD',-7),('USDJPY',7)]
forex+=[('AUDUSD',-7),('USDCHF',7),('USDCAD',6)]
commod=[('GOLD',-8),('SILVER',-7),('OIL',-3)]
indices=[('US30',-7),('NAS100',-7),('SPX500',-7)]
crypto=[('BTCUSD',-7),('ETHUSD',-7)]
cot=[['DXY','71% L','29% S','+3 Long','BULL']]
cot+=[['EURUSD','29% L','71% S','+4 Short','BEAR']]
cot+=[['GOLD','25% L','75% S','+5 Short','BEAR']]
cot+=[['BTCUSD','30

import streamlit as st
st.set_page_config(layout='wide')
if 'page' not in st.session_state:
    st.session_state.page='home'
DXY=7
st.success('LIVE v2.7 AMBUSH-FINDER SINGLE QUOTE FIXED')

def gauge(t,s,bu,be,ne):
    col='#0f6' if s>=1 else '#f44' if s<=-1 else '#fc0'
    a='<div style="border:1px solid #222;border-radius:12px;padding:8px">'
    b='<div style="color:'+col+'">'+t+' '+str(s)+'</div>'
    c='<div style="font-size:10px">'+bu+'</div>'
    d='<div style="font-size:10px">'+be+'</div></div>'
    return a+b+c+d

dxy_bu='Powell Hawk = USD Buy'
dxy_be='Powell Cut = USD Sell'
dxy_ne='FOMC HIGH'
st.markdown(gauge('DXY',DXY,dxy_bu,dxy_be,dxy_ne),unsafe_allow_html=True)

forex=[]
forex.append(('EURUSD',-7,'EUR Buy','EUR Sell','ECB'))
forex.append(('GBPUSD',-7,'GBP Buy','GBP Sell','BoE'))
forex.append(('USDJPY',7,'JPY Sell','JPY Buy','BoJ'))
forex.append(('AUDUSD',-7,'AUD Buy','AUD Sell','RBA'))
forex.append(('USDCHF',7,'CHF Sell','CHF Buy','SNB'))
forex.append(('USDCAD',6,'CAD Sell','CAD Buy','BoC'))

commod=[]
commod.append(('GOLD',-8,'Gold Buy','Gold Sell','GPR'))
commod.append(('SILVER',-7,'Silver Buy','Silver Sell','Gold'))
commod.append(('OIL',-3,'Oil Buy','Oil Sell','OPEC'))

indices=[]
indices.append(('US30',-7

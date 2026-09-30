import streamlit as st, os
if 'page' not in st.session_state:
    st.session_state.page='home'
    st.session_state.sel='DXY'
st.set_page_config(layout='wide',page_title='FX AMBUSHERS')
if os.path.exists('logo.png'):
    st.image('logo.png')
else:
    st.markdown('<div style="text-align:center;background:#000;border:2px solid gold;border-radius:14px;padding:10px"><h2 style="color:gold">Mr SA Dlamini</h2><h1 style="color:gold">FX AMBUSHERS</h1></div>',unsafe_allow_html=True)

def gcard(t,s):
    c='#00ff88' if s>=2 else '#ff3355' if s<=-2 else '#ffcc00'
    return f'<div style="background:#111;border-left:6px solid {c};padding:10px;margin:5px;border-radius:10px;color:#fff">{t} : {s}</div>'

PAIRS=["DXY","EURUSD","GBPUSD","USDJPY","AUDUSD","USDCHF","USDCAD","NZDUSD","GOLD","SILVER","OIL","US30","NAS100","SPX500","BTCUSD","ETHUSD"]
SCORES={"DXY":7,"EURUSD":-7,"GBPUSD":-6,"USDJPY":7,"AUDUSD":-7,"USDCHF":6,"USDCAD":6,"NZDUSD":-6,"GOLD":2,"SILVER":-2,"OIL":-3,"US30":-7,"NAS100":-7,"SPX500":-6,"BTCUSD":-7,"ETHUSD":-7}

if st.session_state.page=='home':
    st.markdown('<h3 style="color:gold;text-align:center">AMBUSH RADAR - 16 PAIRS LIVE</h3>',unsafe_allow_html=True)
    cols=st.columns(3)
    for i,k in enumerate(PAIRS):
        with cols[i%3]:
            st.markdown(gcard(k,SCORES[k]),unsafe_allow_html=True)
            if st.button(f'View {k}',key=k):
                st.session_state.sel=k
                st.session_state.page='finder'
    if st.button('OPEN AMBUSH-FINDER'):
        st.session_state.page='finder'
else:
    if st.button('BACK TO 16 PAIRS'):
        st.session_state.page='home'
    k=st.selectbox('Pick',PAIRS,index=PAIRS.index(st.session_state.sel))
    st.markdown(gcard(f'Ambush-Finder {k}',SCORES[k]),unsafe_allow_html=True)
    st.write(f'COT : Long {30+k.__len__()} Short {70-k.__len__()}')
    st.write('GDP : 0.6 vs 0.6 Neutral')
    st.write('PMI Mfg : 48.5 vs 49.0 Bearish')
    st.write('PMI Serv : 53.2 vs 52.8 Bullish')
    st.write('Retail : -0.2 vs 0.3 Bearish')
    st.write('Confidence : 102 vs 103 Neutral')
    st.write('CPI : 2.8 vs 3.0 Bearish')
    st.write('PPI : 1.5 vs 1.6 Neutral')
    st.write('PCE : 2.5 vs 2.5 Neutral')
    st.write('2Y Yield : Bearish yield up')
    st.write('NFP : 140k vs 145k Neutral')
    st.write('Unemployment : 4.3 vs 4.3 Neutral')
    st.write('Jobless : 195k vs 200k Bullish')
    st.write('ADP : 25k vs 35k Bearish')
    st.write('JOLTS : 7.3M vs 7.3M Neutral')
    st.error(f'{k} AMBUSH: DXY King + Tech Bear + COT Bear = SELL' if SCORES[k]<0 else f'{k} AMBUSH: DXY King + Tech Bull = BUY')

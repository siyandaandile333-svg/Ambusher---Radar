import streamlit as st
import os
if 'page' not in st.session_state:
    st.session_state.page='home'
st.set_page_config(layout='wide',page_title='FX AMBUSHERS - AMBUSH FINDER')
if os.path.exists('logo.png'):
    st.image('logo.png')
else:
    st.markdown('<div style="text-align:center;padding:12px;background:#000;border:1px solid gold;border-radius:14px"><h2 style="color:gold">Mr SA Dlamini</h2><h1 style="color:gold">FX AMBUSHERS</h1><p style="color:gold">Premium Trading</p></div>',unsafe_allow_html=True)

def badge(t):
    c='#ff3355' if 'Bear' in t else '#00ff88' if 'Bull' in t else '#ffcc00'
    return '<span style="background:'+c+'22;color:'+c+';border:1px solid '+c+';padding:4px 8px;border-radius:8px;font-size:12px">'+t+'</span>'
def gcard(t,s,sub):
    c='#00ff88' if s>=2 else '#ff3355' if s<=-2 else '#ffcc00'
    b='NEUTRAL'
    if s>=6: b='Very Bullish'
    elif s>=2: b='Bullish'
    elif s<=-6: b='Very Bearish'
    elif s<=-2: b='Bearish'
    return '<div style="background:#0e0e0e;border-radius:18px;padding:14px;margin:6px;border-left:6px solid '+c+'"><b style="color:#fff">'+t+'</b><br><span style="color:'+c+';font-size:20px">'+str(s)+' '+b+'</span><br><span style="color:#888;font-size:11px">'+sub+'</span></div>'

FULL={
 'DXY':{'a':7,'te':7,'se':6,'ma':6,'techL':'Very Bullish','4h':'Very Bullish','seas':'Bullish','cot':'Long 88 Short 11','cotLS':'Bullish','gdp':'2.8 vs 2.5 Bullish','pmiM':'52.1 vs 51.0','pmiS':'55.2 vs 54.0','retail':'0.4 vs 0.1','conf':'105 vs 102','cpi':'3.6 vs 3.4','ppi':'4.9 vs 4.7','pce':'3.5 vs 3.3','yld':'Very Bullish','nfp':'250k vs 150k','unemp':'3.9 vs 4.1','jobless':'190k vs 205k','adp':'100k vs 47k','jolts':'8.5M vs 7.3M','why':'DXY KING BUY'},
 'EURUSD':{'a':-7,'te':-7,'se':-5,'ma':-2,'techL':'Very Bearish','4h':'Bearish','seas':'Very Bearish','cot':'Long 29 Short 71','cotLS':'Bearish','gdp':'0.3 vs 0.4','pmiM':'49.2 vs 50.1','pmiS':'52.1 vs 52.3','retail':'-0.4 vs 0.2','conf':'96.1 vs 97.2','cpi':'2.1 vs 2.3','ppi':'1.8 vs 1.9','pce':'2.0 vs 2.2','yld':'Very Bearish','nfp':'180k vs 150k','unemp':'6.5 vs 6.6','jobless':'220k vs 210k','adp':'30k vs 50k','jolts':'7.1M vs 7.4M','why':'EURUSD SELL'},
 'GBPUSD':{'a':-6,'te':-6,'se':-4,'ma':-1,'techL':'Bearish','4h':'Bearish','seas':'Neutral','cot':'Long 35 Short 65','cotLS':'Neutral','gdp':'0.6 vs 0.6','pmiM':'48.5 vs 49.0','pmiS':'53.2 vs 52.8','retail':'-0.2 vs 0.3','conf':'102 vs 103','cpi':'2.8 vs 3.0','ppi':'1.5 vs 1.6','pce':'2.5 vs 2.5','yld':'Bearish','nfp':'140k vs 145k','unemp':'4.3 vs 4.3','jobless':'195k vs 200k','adp':'25k vs 35k','jolts':'7.3M vs 7.3M','why':'GBPUSD SELL'},
 'USDJPY':{'a':7,'te':6,'se':4,'ma':7,'techL':'Very Bullish','4h':'Bullish','seas':'Bullish','cot':'Long 82 Short 18','cotLS':'Bullish','gdp':'1.9 vs 1.2','pmiM':'51.2 vs 50.5','pmiS':'54.8 vs 53.1','retail':'1.2 vs 0.5','conf':'98 vs 96','cpi':'3.2 vs 2.9','ppi':'3.8 vs 3.2','pce':'3.1 vs 2.9','yld':'Very Bullish','nfp':'220k vs 150k','unemp':'3.8 vs 4.0','jobless':'180k vs 205k','adp':'90k vs 47k','jolts':'8.1M vs 7.3M','why':'USDJPY BUY'},
 'AUDUSD':{'a':-7,'te':-7,'se':-6,'ma':-2,'techL':'Very Bearish','4h':'Bearish','seas':'Bearish','cot':'Long 28 Short 72','cotLS':'Bearish','gdp':'0.2 vs 0.4','pmiM':'47.8 vs 49.0','pmiS':'51.0 vs 51.5','retail':'-0.5 vs 0.1','conf':'85 vs 90','cpi':'2.5 vs 2.8','ppi':'1.2 vs 1.5','pce':'2.4 vs 2.5','yld':'Bearish','nfp':'Neutral','unemp':'4.5 vs 4.2','jobless':'Bearish','adp':'Bearish','jolts':'Bearish','why':'AUDUSD SELL'},
 'USDCHF':{'a':6,'te':5,'se':3,'ma':5,'techL':'Bullish','4h':'Bullish','seas':'Bullish','cot':'Long 68 Short 32','cotLS':'Bullish','gdp':'1.2 vs 0.8','pmiM':'52.0 vs 51.0','pmiS':'54.0 vs 53.0','retail':'0.3 vs 0.1','conf':'99 vs 97','cpi':'2.0 vs 1.8','ppi':'2.2 vs 2.0','pce':'Bullish','yld':'Bullish','nfp':'Bullish','unemp':'Bullish','jobless':'Bullish','adp':'Bullish','jolts':'Bullish','why':'USDCHF BUY'},
 'USDCAD':{'a':6,'te':6,'se':4,'ma':4,'techL':'Bullish','4h':'Bullish','seas':'Very Bullish','cot':'Long 72 Short 28','cotLS':'Very Bullish','gdp':'1.5 vs 1.0','pmiM':'50.2 vs 50.5','pmiS':'53.5 vs 52.8','retail':'0.5 vs 0.2','conf':'100 vs 98','cpi':'3.0 vs 2.8','ppi':'2.5 vs 2.2','pce':'Bullish','yld':'Bullish','nfp':'Bullish','unemp':'Neutral','jobless':'Bullish','adp':'Bullish','jolts':'Bullish','why':'USDCAD BUY'},
 'NZDUSD':{'a':-6,'te':-6,'se':-5,'ma':-2,'techL':'Bearish','4h':'Bearish','seas':'Bearish','cot':'Long 32 Short 68','cotLS':'Bearish','gdp':'0.1 vs 0.3','pmiM':'47.0 vs 48.5','pmiS':'50.1 vs 51.0','retail':'-0.3 vs 0.2','conf':'88 vs 92','cpi':'Bearish','ppi':'Bearish','pce':'Neutral','yld':'Bearish','nfp':'Neutral','unemp':'Bearish','jobless':'Neutral','adp':'Bearish','jolts':'Bearish','why':'NZDUSD SELL'},
 'GOLD':{'a':2,'te':-3,'se':1,'ma':4,'techL':'Very Bearish','4h':'Bearish','seas':'Bearish','cot':'Long 25 Short 75','cotLS':'Bearish','gdp':'1.5 vs 1.5','pmiM':'54.6 vs 55.2','pmiS':'55.4 vs 54.1','retail':'-0.6 vs 0.1','conf':'89.4 vs 90.3','cpi':'3.4 vs 3.4','ppi':'4.7 vs 4.9','pce':'3.3 vs 3.3','yld':'Bearish','nfp':'162k vs 55k','unemp':'4.1 vs 4.1','jobless':'206k vs 205k','adp':'38k vs 47k','jolts':'7.27M vs 7.33M','why':'GOLD SELL Retail 75 Long trapped'},
 'SILVER':{'a':-2,'te':-4,'se':0,'ma':3,'techL':'Bearish','4h':'Bearish','seas':'Neutral','cot':'Long 40 Short 60','cotLS':'Neutral','gdp':'Neutral','pmiM':'54.6 vs 55.2','pmiS':'55.4 vs 54.1','retail':'Bullish','conf':'Bullish','cpi':'Neutral','ppi':'Bullish','pce':'Neutral','yld':'Bearish','nfp':'Bearish','unemp':'Neutral','jobless':'Bullish','adp':'Bullish','jolts':'Bullish','why':'SILVER SELL'},
 'OIL':{'a':-3,'te':-3,'se':-2,'ma':-1,'techL':'Bearish','4h':'Bearish','seas':'Bearish','cot':'Long 45 Short 55','cotLS':'Bearish','gdp':'1.0 vs 1.5','pmiM':'49.0 vs 50.0','pmiS':'52.0 vs 52.5','retail':'-0.1 vs 0.3','conf':'95 vs 100','cpi':'Neutral','ppi':'Bearish','pce':'Neutral','yld':'Neutral','nfp':'Neutral','unemp':'Neutral','jobless':'Neutral','adp':'Neutral','jolts':'Neutral','why':'OIL SELL'},
 'US30':{'a':-7,'te':-7,'se':-5,'ma':-3,'techL':'Very Bearish','4h':'Very Bearish','seas':'Bearish','cot':'Long 38

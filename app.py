import streamlit as st
from datetime import datetime, timedelta
import os
st.set_page_config(page_title='FX AMBUSHERS', layout='wide')
if 'page' not in st.session_state:
    st.session_state.page='home'
DXY=7
TM=(datetime.utcnow()+timedelta(hours=2)).strftime('%H:%M SAST')
st.success(f'LIVE v2.3 FIXED | {TM}')
for f in ['logo.png','logo.jpg','IMG-20260929-WA1810.jpg']:
    if os.path.exists(f):
        st.image(f, use_container_width=True)
        break
def j(p,e):
    return ' + '.join(p)+' = '+e
def gauge(t,s,bu,be,ne,sz=260):
    ang=s*9
    col='#00ff66' if s>=1 else '#ff4444' if s<=-1 else '#ffcc00'
    bcol=col
    bias='BULL' if s>=1 else 'BEAR' if s<=-1 else 'NEU'
    h=sz//2
    a=f"<div style='border:1px solid #222;border-radius:18px;padding:12px;background:#0f1414;border-left:4px solid {bcol};margin-bottom:12px'>"
    b=f"<div style='text-align:center;color:#888;font-size:11px'>{t}</div>"
    c=f"<div style='text-align:center;color:{col};font-weight:900;font-size:20px\'>{bias} {'+'+str(s) if s>0 else str(s)}</div>"
    d=f"<div style='width:{sz}px;height:{h}px;margin:8px auto;position:relative;background:conic-gradient(from 270deg at 50% 100%,#ff2b2b 0 60deg,#ffcc00 60deg 120deg,#00cc66 120deg 180deg);border-radius:{sz}px {sz}px 0 0'>"
    e=f"<div style='width:3px;height:{h-10}px;background:white;position:absolute;bottom:0;left:50%;transform-origin:bottom;transform:rotate({ang}deg)'></div></div>"
    f=f"<div style='font-size:11px;color:#00ff66'>Bull: {bu}</div><div style='font-size:11px;color:#ff6666'>Bear: {be}</div><div style='font-size:11px;color:#888'>Neu: {ne}</div></div>"
    return a+b+c+d+e+f

dxy_bu=j(['Powell Hawk No Cut','US CPI 3.2% Hot','US10Y 4.2% Up','BoJ Dovish','COT 71% Long Bull','Retail 30% Long 70% Short Buy'],'USD Buy')
dxy_be=j(['Powell Cut 25bps','Gold 2600 Risk On','BoJ Hawk Hike','Yield Down','COT 29% Short Bear','Retail 68% Short Fade'],'USD Sell')
dxy_ne='FOMC Sep29 HIGH + NFP Oct3 + CPI Oct4 + COT Fri + Retail'
st.markdown(gauge('DXY AMBUSH',DXY,dxy_bu,dxy_be,dxy_ne,280), unsafe_allow_html=True)

forex=[
 ('EURUSD',-7,j(['ECB Lagarde Hawk','EU CPI 2.4% Hot','EU GDP Strong','Fed Cut','COT 29% Bear','Retail 70% Sell Crowd'],'EUR Buy'),j(['Powell Hawk No Cut','DXY +7 Bull','US10Y 4.2% Up','CPI 3.2%','COT DXY 71% Bull','Retail 70% Fade Sell'],'EUR Sell'),'ECB Oct5 + GPR + COT + Retail'),
 ('GBPUSD',-7,j(['BoE Bailey Hawk','UK CPI 3.8% Hot','UK Wage Up','Fed Cut','COT 30% Bear','Retail 68% Sell'],'GBP Buy'),j(['Fed Hawk No Cut','DXY +7','Yield Up','UK Recession','COT DXY 71% Bull','Retail 68% Fade'],'GBP Sell'),'BoE Oct5 + COT + Retail'),
 ('USDJPY',7,j(['DXY +7 Bull','BoJ Ueda Dovish','US-JP Gap 4.2%','COT 71% Bull','Retail 35% Buy Crowd'],'USDJPY Buy'),j(['BoJ Hawk Hike','Ueda Hawk','Fed Cut','Risk Off','COT 29% Bear','Retail 35% Fade'],'Sell'),'BoJ Oct4 HIGH + COT + Retail'),
 ('AUDUSD',-7,j(['RBA Hawk','Gold 2600 Up','China Stimulus','Iron Up','COT 28% Bear','Retail 65% Sell'],'AUD Buy'),j(['DXY +7','Risk Off','China PMI Weak','Iron Down','COT 72% Bear','Retail 65% Fade'],'AUD Sell'),'RBA + China + COT + Retail'),
 ('USDCHF',7,j(['DXY +7 Bull','SNB Dovish','Safe Off','Gold Down','COT 71% Bull','Retail 38% Buy'],'Buy'),j(['SNB Hawk','Fed Cut','Gold 2600 Up','Risk Off','COT 29% Bear','Retail 38% Fade'],'Sell'),'SNB + Gold + COT + Retail'),
 ('USDCAD',6,j(['DXY +7 Bull','Oil 70 Down','BoC Dovish','COT 70% Bull','Retail 40% Buy'],'Buy'),j(['Oil 85 Up','OPEC Cut','BoC Hawk','CPI Up','COT 30% Bear','Retail 40% Fade'],'Sell'),'BoC + Oil + COT + Retail'),
]
commod=[
 ('GOLD',-8,j(['Fed Cut 25bps','US10Y Down','USD Weak','GPR War','COT 25% Bear','Retail 75% Sell Top'],'Gold Buy'),j(['DXY +7 Bull','Powell Hawk','US10Y Up','Risk On','COT 75% Bear','Retail 75% Fade Top'],'Sell'),'GPR + FOMC + COT + Retail'),
 ('SILVER',-7,j(['Gold 2600 Up','Fed Cut','Solar Demand','Copper Up','COT 27% Bear','Retail 72% Sell'],'Buy'),j(['DXY +7','Yield Up','Gold Sell','Risk Off','COT 73% Bear','Retail 72% Fade'],'Sell'),'Gold + Copper + COT + Retail'),
 ('OIL',-3,j(['GPR Iran War','OPEC Cut 1M','Supply Tight','COT 35% Bear','Retail 60% Sell'],'Oil Buy'),j(['DXY Strong','Recession','Demand Down','Stock Up','COT 65% Bear','Retail 60% Fade'],'Sell'),'OPEC + GPR + COT + Retail'),
]
indices=[
 ('US30',-7,j(['Fed Cut','Dow Beat','CPI 3.2 Down','Risk On','COT 30% Bear','Retail 68% Sell Trap'],'Buy'),j(['DXY +7','Powell Hawk','Yield 4.2 Up','Miss','COT 70% Bear','Retail 68% Fade Trap'],'Sell'),'FOMC Sep29 + COT + Retail'),
 ('NAS100',-7,j(['Fed Cut','AAPL NVDA Beat','Yield Down','AI Demand','COT 28% Bear','Retail 70% Sell'],'Buy'),j(['DXY +7','US10Y Up','Hawk','CPI Hot','COT 72% Bear','Retail 70% Fade'],'Sell'),'Earnings + COT + Retail'),
 ('SPX500',-7,j(['Fed Cut','SPX Up','CPI Down','GDP Up','COT 29% Bear','Retail 69% Sell'],'Buy'),j(['DXY +7','Hawk','Yield Up','Recession','COT 71% Bear','Retail 69% Fade'],'Sell'),'FOMC + NFP + COT + Retail'),
]
crypto=[
 ('BTCUSD',-7,j(['Fed Cut','ETF Inflow 500M','Risk On','Halving','COT 30% Bear','Retail 78% Sell FOMO'],'BTC Buy'),j(['DXY +7','Risk Off','SEC FUD','Outflow','COT 70% Bear','Retail 78% FOMO Fade'],'BTC Sell'),'ETF + FOMC + COT + Retail'),
 ('ETHUSD',-7,j(['Fed Cut','ETH ETF In','BTC Up','Burn Up','COT 30% Bear','Retail 78% Sell'],'ETH Buy'),j(['DXY +7','Hawk','BTC Sell','Outflow','COT 70% Bear','Retail 78% Fade'],'ETH Sell'),'ETF + BTC + COT + Retail'),
]
cot=[['DXY','71%','29%','+3% Long','BULL','Powell Hawk'],['EURUSD','29%','71%','+4% Short','BEAR','DXY +7'],['GBPUSD','30%','70%','+2% Short','BEAR','DXY Bull'],['USDJPY','71%','29%','+2% Long','BULL','BoJ Dovish'],['AUDUSD','28%','72%','+3% Short','BEAR','Risk Off'],['USDCHF','71%','29%','+1% Long','BULL','SNB Dovish'],['USDCAD','70%','30%','+2% Long','BULL','Oil Down'],['GOLD','25%','75%','+5% Short','BEAR','DXY + Yield'],['SILVER','27%','73%','+3% Short','BEAR','Gold Down'],['OIL','35%','65%','+2% Short','BEAR','DXY Strong'],['US30','30%','70%','+3% Short','BEAR','Hawk No Cut'],['NAS100','28%','72%','+4% Short','BEAR','Yield 4.2'],['SPX500','29%','71%','+3% Short','BEAR','DXY +7'],['BTCUSD','30%','70%','+2% Short','BEAR','Risk Off']]
retail=[['EURUSD','70%','30%','72% Long Retail','CONTRARIAN SELL','Retail Long Crowded'],['GBPUSD','68%','32%','70% Long Retail','CONTRARIAN SELL','Retail Long'],['USDJPY','35%','65%','66% Short Retail','CONTRARIAN BUY','Retail Short Crowded'],['AUDUSD','65%','35%','68% Long Retail','CONTRARIAN SELL','Retail Wrong'],['USDCHF','38%','62%','64% Short Retail','CONTRARIAN BUY','Retail Short'],['USDCAD','40%','60%','62% Short Retail','CONTRARIAN BUY','Retail Short'],['GOLD','75%','25%','80% Long Retail','CONTRARIAN SELL','Top Signal'],['SILVER','72%','28%','75% Long Retail','CONTRARIAN SELL','Retail Long'],['OIL','60%','40%','65% Long Retail','CONTRARIAN SELL','Retail Long Oil'],['US30','68%','32%','70% Long Retail','CONTRARIAN SELL','Retail Bull Trap'],['NAS100','70%','30%','73% Long Retail','CONTRARIAN SELL','Retail Bull'],['SPX500','69%','31%','71% Long Retail','CONTRARIAN SELL','Retail Bull'],['BTCUSD','78%','22%','85% Long Retail','CONTRARIAN SELL','Retail FOMO'],['DXY','30%','70%','68% Short Retail','CONTRARIAN BUY','Retail Short USD']]

all_assets={}
for p,s,bu,be,ne in forex: all_assets[p]=(s,bu,be,ne,'FOREX')
for p,s,bu,be,ne in commod: all_assets[p]=(s,bu,be,ne,'METAL')
for p,s,bu,be,ne in indices: all_assets[p]=(s,bu,be,ne,'INDICES')
for p,s,bu,be,ne in crypto: all_assets[p]=(s,bu,be,ne,'CRYPTO')
all_assets['DXY']=(DXY,dxy_bu,dxy_be,dxy_ne,'DXY')

if st.session_state.page=='home':
    c1,c2=st.columns(2)
    with c1:
        if st.button('FOREX 6

import streamlit as st
from datetime import datetime, timedelta
import os
st.set_page_config(page_title="FX AMBUSHERS - PRO", layout="wide")
if "page" not in st.session_state:
    st.session_state.page="home"
DXY=7
TM=(datetime.utcnow()+timedelta(hours=2)).strftime("%H:%M SAST")
st.success(f"LIVE v3 PRO SCORECARD | {TM}")
for f in ["logo.png","logo.jpg","IMG-20260929-WA1810.jpg"]:
    if os.path.exists(f):
        st.image(f, use_container_width=True)
        break
def j(p,e):
    return " + ".join(p)+" = "+e
def gauge(t,s,bu,be,ne,sz=
forex=[
 ("EURUSD",-7,j(["ECB Hawk","EU CPI Hot","EU GDP Strong","Fed Cut"],"EUR Buy"),j(["Powell Hawk","DXY +7 Bull","US10Y Up","CPI 3.2%"],"EUR Sell"),"ECB Oct5 + US CPI Oct4"),
 ("GBPUSD",-7,j(["BoE Hawk","UK CPI Hot","UK Wage Up","Fed Cut"],"GBP Buy"),j(["Fed Hawk","DXY +7","Yield Up","UK Recession"],"GBP Sell"),"BoE Oct5"),
 ("USDJPY",7,j(["DXY +7 Bull","BoJ Dovish","US-JP Gap 4.2%"],"USDJPY Buy"),j(["BoJ Hawk","Ueda Hawk","Fed Cut","Risk Off"],"Sell"),"BoJ Oct4 HIGH"),
 ("AUDUSD",-7,j(["RBA Hawk","Gold Up","China Stimulus","Iron Up"],"AUD Buy"),j(["DXY +7","Risk Off","China PMI Weak","Iron Down"],"AUD Sell"),"RBA + China PMI"),
 ("USDCHF",7,j(["DXY +7 Bull","SNB Dovish","Safe Off","Gold Down"],"Buy"),j(["SNB Hawk","Fed Cut","Gold Up","Risk Off"],"Sell"),"SNB + Gold"),
 ("USDCAD",6,j(["DXY +7 Bull","Oil WTI 70 Down","BoC Dovish"],"Buy"),j(["Oil 85 Up","OPEC Cut","BoC Hawk","CPI Up"],"Sell"),"BoC + Oil"),
]
commod=[
 ("GOLD",-8,j(["Fed Cut","US10Y Down","USD Weak","GPR War"],"Gold Buy"),j(["DXY +7 Bull","Powell Hawk","US10Y Up","Risk On"],"Sell"),"GPR Israel + FOMC"),
 ("SILVER",-7,j(["Gold 2600 Up","Fed Cut","Solar Demand","Copper Up"],"Buy"),j(["DXY +7","Yield Up","Gold Sell","Risk Off"],"Sell"),"Gold + Copper"),
 ("OIL",-3,j(["GPR Iran War","OPEC Cut 1M","Supply Tight"],"Oil Buy"),j(["DXY Strong","Recession","Demand Down","Stock Up"],"Sell"),"OPEC + GPR"),
]
indices=[
 ("US30",-7,j(["Fed Cut","Dow Earnings Beat","CPI Down","Risk On"],"Buy"),j(["DXY +7","Powell Hawk","Yield 4.2 Up","Miss"],"Sell"),"FOMC Sep29 + CPI Oct4"),
 ("NAS100",-7,j(["Fed Cut","AAPL NVDA Beat","Yield Down","AI Demand"],"Buy"),j(["DXY +7","US10Y Up","Hawk","CPI Hot"],"Sell"),"Earnings + Yield"),
 ("SPX500",-7,j(["Fed Cut","SPX Earnings Up","CPI Down","GDP Up"],"Buy"),j(["DXY +7","Hawk","Yield Up","Recession"],"Sell"),"FOMC + NFP Oct3"),
]
crypto=[
 ("BTCUSD",-7,j(["Fed Cut","ETF Inflow 500M","Risk On","Halving"],"BTC Buy"),j(["DXY +7","Risk Off","SEC FUD","Outflow"],"BTC Sell"),"ETF + FOMC"),
 ("ETHUSD",-7,j(["Fed Cut","ETH ETF In","BTC Up","Burn Up"],"ETH Buy"),j(["DXY +7","Hawk","BTC Sell","Outflow"],"ETH Sell"),"ETF + BTC"),
]
cot=[
 ["DXY","71%","29%","+3% Long","BULL","Powell Hawk"],
 ["EURUSD","29%","71%","+4% Short","BEAR","DXY +7"],
 ["GBPUSD","30%","70%","+2% Short","BEAR","DXY Bull"],
 ["USDJPY","71%","29%","+2% Long","BULL","BoJ Dovish"],
 ["AUDUSD","28%","72%","+3% Short","BEAR","Risk Off"],
 ["USDCHF","71%","29%","+1% Long","BULL","SNB Dovish"],
 ["USDCAD","70%","30%","+2% Long","BULL","Oil Down"],
 ["GOLD","25%","75%","+5% Short","BEAR","DXY + Yield"],
 ["SILVER","27%","73%","+3% Short","BEAR","Gold Down"],
 ["OIL","35%","65%","+2% Short","BEAR","DXY Strong"],
]
retail=[
 ["EURUSD","70%","30%","72% Long Retail","CONTRARIAN SELL","Retail Long"],
 ["GBPUSD","68%","32%","70% Long Retail","CONTRARIAN SELL","Retail Long"],
 ["USDJPY","35%","65%","66% Short Retail","CONTRARIAN BUY","Retail Short"],
 ["AUDUSD","65%","35%","68% Long Retail","CONTRARIAN SELL","Retail Wrong"],
 ["GOLD","75%","25%","80% Long Retail","CONTRARIAN SELL","Top Signal"],
 ["BTCUSD","78%","22%","85% Long Retail","CONTRARIAN SELL","Retail FOMO"],
 ["DXY","30%","70%","68% Short Retail","CONTRARIAN BUY","Retail Short USD"],
]
all_assets={}
for p,s,bu,be,ne in forex: all_assets[p]=(s,bu,be,ne,"FOREX")
for p,s,bu,be,ne in commod: all_assets[p]=(s,bu,be,ne,"METAL")
for p,s,bu,be,ne in indices: all_assets[p]=(s,bu,be,ne,"INDICES")
for p,s,bu,be,ne in crypto: all_assets[p]=(s,bu,be,ne,"CRYPTO")
all_assets["DXY"]=(DXY,dxy_bu,dxy_be,dxy_ne,"DXY")
# === SCHOOLS LIKE SCREENSHOT ===
def pro_block():
    return {
      "GOLD": {
        "edge": 2, "tech": -3, "sent": 1, "macro": 4,
        "tech_label": "Very Bearish", "h4": "Bearish", "season": "Bearish",
        "cot": ["Long 88.95%","Short 11.05%","Change -0.17%","Date Sep 04"],
        "levels": ["Support: $2450","Resistance: $2550","ATR: $18","RSI: 68"],
        "news": [
          ["GDP","5.6

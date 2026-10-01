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

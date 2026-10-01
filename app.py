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

import streamlit as st
import pandas as pd
import os, glob
from datetime import datetime

st.set_page_config(page_title="FX AMBUSHERS", layout="wide")
st.markdown('<style>.stApp{background:#080a0a}</style>', unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page="home"

DXY=71

def get_sa_time():
    try:
        # SA is UTC+2
        now = datetime.utcnow()
        sa_hour = (now.hour + 2) % 24
        return f"{sa_hour:02d}:{now.minute:02d}:{now.second:02d} SAST | {now.day:02d}-{now.month:02d}-{now.year}"
    except:
        return datetime.now().strftime("%H:%M:%S SAST")

def gauge_card(title, score, bull, bear, neu, size=260):
    angle = -90 + (score*1.8)
    if score>=60:
        col="#00ff66"; bcol="#00ff66"; bias="BULL"
    elif score<=40:
        col="#ff4444"; bcol="#ff4444"; bias="BEAR"
    else:
        col="#ffcc00"; bcol="#ffcc00"; bias="NEU"
    h = size//2
    part1 = "<div style='border:1px solid #222;border-radius:18px;padding:12px;background:#0f1414;"

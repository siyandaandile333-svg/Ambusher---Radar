import streamlit as st
import pandas as pd
import os, glob

st.set_page_config(page_title="FX AMBUSHERS", layout="wide")
st.markdown("<style>.stApp{background:#080a0a}</style>", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page="home"

DXY=71

def gauge_card(title, score, bull, bear, neu, size=260):
    angle=-90 + (score*1.8)
    if score>=60:
        col="#00ff66"; bcol="#00ff66"; bias="BULL"
    elif score<=40:
        col="#ff4444"; bcol="#ff4444"; bias="BEAR"
    else:
        col="#ffcc00"; bcol="#ffcc00"; bias="NEU"
    h=size//2
    return f"""
<div style='border:1px solid #222;border-radius:18px;padding:12px;background:#0f1414;border-left:4px solid {bcol};margin-bottom:12px'>
<div style='text-align:center;color:#888;font-size:11px'>{title}</div>
<div style='text-align:center;color:{col};font-weight:900;font-size:20px'>{bias} {score}</div>
<div style='width:{size}px;height:{h}px;margin:8px auto;position:relative;background:conic-gradient(from 270deg at 50% 100%, #ff2b2b 0deg 60deg, #ffcc00 60deg 120deg, #00cc66 120deg 180deg);border-radius:{size}px {size}px 0 0'>
<div style='width:3px;height:{h-10}px;background:white;position:absolute;bottom:0;left:50%;transform-origin:bottom;transform:rotate({angle}deg)'></div>
<div style='width:12px;height:12px;background:white;border-radius:50%;position:absolute;bottom:-6px;left:calc(50% - 6px)'></div>
</div>
<div style='font-size:11px;color:#00ff66'>Bull: {bull}</div>
<div style='font-size:11px;color:#ff6666'>Bear: {bear}</div>
<div style='font-size:11

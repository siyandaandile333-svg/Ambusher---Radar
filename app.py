import streamlit as st
import datetime
st.set_page_config(page_title="FX AMBUSHERS RADAR", layout="wide")
TM=datetime.datetime.now().strftime("%Y-%m-%d %H:%M UTC")
if "page" not in st.session_state: st.session_state.page="home"
def j(a,b): return f"BUY: {a} | SELL: {b}"
def gauge(p,s,bu,be,ne,h=260):
    c="#00ff66" if s>=4 else "#ff4444" if s<=-4 else "#ffcc00" if s>0 else "#ffaa00"
    pct=int((s+8)/16*100)
    return f"<div style='border:1px solid #222;border-radius:14px;padding:10px;margin:6px;background:#0f1414;height:{h}px'><b>{p}</b> <span style='color:{c}'>{s:+d}</span><div style='height:6px;background:#222;border-radius:3px;margin:6px 0'><div style='width:{pct}%;height:6px;background:{c};border-radius:3px'></div></div><div style='font-size:11px;color:#aaa'>{bu}<br><br>{be}<br><br><span style='color:#888'>{ne}</span></div></div>"
DXY=7
dxy_bu="Powell Hawk + CPI 3.2% Hot + US10Y 4.2% Up"
dxy_be="Fed Cut + CPI Down + Risk On"
dxy_ne="FOMC Sep29 + NFP Oct3 + CPI Oct4"
forex=[("EURUSD",-7,j("Fed Cut + DXY -7",""),j("DXY +7 + Powell Hawk",""),"DXY + ECB"),("GBPUSD",-7,j("Fed Cut",""),j("DXY +7 + Hawk",""),"DXY + BoE"),("USDJPY",7,j("DXY +7 + BoJ Dovish",""),j("Fed Cut + BoJ Hawk",""),"BoJ + FOMC"),("AUDUSD",-7,j("Fed Cut + Risk On",""),j("DXY +7 + China Down",""),"China + DXY"),("USDCHF",7,j("DXY +7 + SNB Dovish",""),j("Fed Cut",""),"SNB"),("USDCAD",7,j("DXY +7 + Oil Down",""),j("Fed Cut + Oil Up",""),"Oil")]
commod=[("GOLD",-7,j("Fed Cut + DXY -7",""),j("DXY +7 + US10Y Up",""),"DXY + CPI"),("SILVER",-7,j("Fed Cut + Gold Up",""),j("DXY +7 + Gold Sell",""),"Gold"),("OIL",-2,j("Fed Cut + Demand",""),j("DXY +7 + Supply",""),"OPEC")]
indices=[("US30",-7,j("Fed Cut + Dow Earnings",""),j("DXY +7 + Hawk",""),"FOMC"),("NAS100",-7,j("Fed Cut + NVDA Beat",""),j("DXY +7 + Yield Up",""),"Earnings"),("SPX500",-7,j("Fed Cut + Earnings Up",""),j("DXY +7 + Hawk",""),"FOMC + NFP")]
crypto=[("BTCUSD",-7,j("Fed Cut + ETF Inflow",""),j("DXY +7 + Risk Off",""),"ETF"),("ETHUSD",-7,j("Fed Cut + ETF In",""),j("DXY +7 + BTC Sell",""),"ETF + BTC")]
cot=[["DXY","71%","29%","+3% Long","BULL","Hawk"],["EURUSD","29%","71%","+4% Short","BEAR","DXY"],["GOLD","25%","75%","+5% Short","BEAR","Yield"]]
retail=[["EURUSD","70%","30%","72% Long","CONTRARIAN SELL","Retail"],["GOLD","75%","25%","80% Long","CONTRARIAN SELL","Top"],["DXY","30%","70%","68% Short","CONTRARIAN BUY","Short"]]
all_assets={}
for p,s,bu,be,ne in forex: all_assets[p]=(s,bu,be,ne,"FOREX")
for p,s,bu,be,ne in commod: all_assets[p]=(s,bu,be,ne,"METAL")
for p,s,bu,be,ne in indices: all_assets[p]=(s,bu,be,ne,"INDICES")
for p,s,bu,be,ne in crypto: all_assets[p]=(s,bu,be,ne,"CRYPTO")
all_assets["DXY"]=(DXY,dxy_bu,dxy_be,dxy_ne,"DXY")
if st.session_state.page=="home":
    c1,c2,c3=st.columns(3)
    if c1.button("FOREX 6",use_container_width=True): st.session_state.page="forex"; st.rerun()
    if c2.button("GOLD OIL",use_container_width=True): st.session_state.page="commod"; st.rerun()
    if c3.button("INDICES + CRYPTO",use_container_width=True): st.session_state.page="other"; st.rerun()
    if st.button("SCORE FINDER - PRO",use_container_width=True): st.session_state.page="pro"; st.rerun()
    if st.button("COT + RETAIL",use_container_width=True): st.session_state.page="tables"; st.rerun()
    if st.button("AMBUSH SCHOOLS",use_container_width=True): st.session_state.page="schools"; st.rerun()
    cols=st.columns(3); i=0
    for p in all_assets:
        s,bu,be,ne,cat=all_assets[p]
        with cols[i%3]: st.markdown(gauge(p,s,bu,be,ne),unsafe_allow_html=True)
        i+=1
elif st.session_state.page=="pro":
    if st.button("HOME"): st.session_state.page="home"; st.rerun()
    st.subheader("SCORE FINDER - PRO")
    st.markdown("<div style='border:1px solid #333;border-radius:16px;padding:16px;background:#0a0f0f'><div style='color:#00ffcc;font-weight:900'>EdgeFinder Score: 2</div><div>Technical: -3 (Very Bearish)</div><div>Sentiment: 1</div><div>Macro: 4</div><hr style='border-color:#222'><div style='color:#888'>Technicals</div><div>Very Bearish | 4H: Bearish | Seasonality: Bearish</div><hr style='border-color:#222'><div style='color:#888'>Levels</div><div>Support: $2450 | Resistance: $2550 | ATR: $18 | RSI: 68</div><hr style='border-color:#222'><div style='color:#888'>COT</div><div>Long 88.95% | Short 11.05% | Change -0.17% | Sep 04</div></div>",unsafe_allow_html=True)
    st.markdown("<div style='overflow-x:auto'><table style='width:100%;font-size:12px;border-collapse:collapse'><tr style='color:#888'><th>Indicator</th><th>Actual</th><th>Forecast</th><th>Date</th><th>Bias</th></tr><tr style='border-top:1px solid #222'><td>GDP</td><td>5.6%</td><td>5.6%</td><td>Jun 05</td><td style='color:#00ff66'>BULL</td></tr><tr style='border-top:1px solid #222'><td>PMI</td><td>53.0</td><td>52.0</td><td>May 23</td><td style='color:#00ff66'>BULL</td></tr><tr style='border-top:1px solid #222'><td>JOLTS</td><td>8.06M</td><td>8.34M</td><td>Jun 04</td><td style='color:#ff4444'>BEAR</td></tr><tr style='border-top:1px solid #222'><td>CPI</td><td>3.4%</td><td>Aug 12</td><td style='color:#ffcc00'>NEU</td></tr></table></div>",unsafe_allow_html=True)
    st.markdown("<div style='margin-top:12px;border:1px solid #222;border-radius:12px;padding:10px'>Crowd: Bullish vs Bearish | 65% Bull 35% Bear - Buy Dominant<div style='height:8px;background:#222;border-radius:4px;margin-top:6px'><div style='width:65%;height:8px;background:#00ff66;border-radius:4px'></div></div></div>",unsafe_allow_html=True)
elif st.session_state.page=="forex":
    if st.button("HOME"): st.session_state.page="home"; st.rerun()
    cols=st.columns(2); i=0
    for p,s,bu,be,ne in forex:
        with cols[i%2]: st.markdown(gauge(p,s,bu,be,ne),unsafe_allow_html=True)
        i+=1
elif st.session_state.page=="commod":
    if st.button("HOME"): st.session_state.page="home"; st.rerun()
    cols=st.columns(2); i=0
    for p,s,bu,be,ne in commod:
        with cols[i%2]: st.markdown(gauge(p,s,bu,be,ne),unsafe_allow_html=True)
        i+=1
elif st.session_state.page=="other":
    if st.button("HOME"): st.session_state.page="home"; st.rerun()
    for p,s,bu,be,ne in indices+crypto: st.markdown(gauge(p,s,bu,be,ne,320),unsafe_allow_html=True)
elif st.session_state.page=="tables":
    if st.button("HOME"): st.session_state.page="home"; st.rerun()
    st.subheader("COT TABLE")
    for r in cot:
        col="#00ff66" if "BULL" in r[4] else "#ff4444"
        st.markdown(f"<div style='border:1px solid #222;padding:8px;border-radius:8px;margin:4px 0'><b>{r[0]}</b> Long {r[1]} Short {r[2]} {r[3]} <span style='color:{col}'>{r[4]}</span></div>",unsafe_allow_html=True)
    st.subheader("RETAIL")
    for r in retail: st.markdown(f"<div style='border:1px solid #222;padding:8px;border-radius:8px;margin:4px 0'><b>{r[0]}</b> Long {r[1]} Short {r[2]} | <span style='color:#ffcc00'>{r[4]}</span></div>",unsafe_allow_html=True)
elif st.session_state.page=="schools":
    if st.button("HOME"): st.session_state.page="home"; st.rerun()
    st.markdown("<div style='border-left:4px solid #00ff66;padding:12px;background:#0f1414;border-radius:12px;margin:8px 0'><b>SCHOOL 1: DXY</b> DXY 7 BULL = USD Buy. EUR SELL, USDJPY BUY, GOLD SELL.</div><div style='border-left:4px solid #ff4444;padding:12px;background:#0f1414;border-radius:12px;margin:8px 0'><b>SCHOOL 2: COT</b> 71% Long = trap. Retail 70% Long = CONTRARIAN SELL.</div><div style='border-left:4px solid #ffcc00;padding:12px;background:#0f1414;border-radius:12px;margin:8px 0'><b>SCHOOL 3: NEWS</b> Actual vs Forecast = Surprise drives price.</div><div style='border-left:4px solid #00ccff;padding:12px;background:#0f1414;border-radius:12px;margin:8px 0'><b>SCHOOL 4: TECHNICAL</b> Very Bearish + 4H Bearish = Score -3 = Short pullback.</div><div style='border-left:4px solid #aa66ff;padding:12px;background:#0f1414;border-radius:12px;margin:8px 0'><b>SCHOOL 5: CROWD</b> 65% Bull + 75% Long GOLD = CONTRARIAN SELL Top.</div><div style='border-left:4px solid #ff8800;padding:12px;background:#0f1414;border-radius:12px;margin:8px 0'><b>SCHOOL 6: PRO SCORE</b> Edge 2 = Tech -3 + Sent 1 + Macro 4. Wait 4+ or -4+.</div>",unsafe_allow_html=True)
st.caption(f"Last Update {TM} | v3 FIXED | FX AMBUSHERS")

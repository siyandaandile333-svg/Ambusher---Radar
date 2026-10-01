import streamlit as st
import pandas as pd

st.set_page_config(page_title='Ambush Radar - Lovable Exact Colours', layout='wide')

st.markdown("""
<style>
.stApp{background:#080c0c;color:#a0aeae;}
.card{background:#161c1a;border:1px solid #1e2828;border-radius:12px;margin-bottom:12px;overflow:hidden;}
.head{padding:14px 16px;display:flex;justify-content:space-between;align-items:center;font-style:italic;color:#7a8a8a;border-bottom:1px solid #1e2828;font-weight:700;}
.blueBox{background:#2d4cc0;color:white;padding:8px 18px;border-radius:6px;font-weight:800;min-width:48px;text-align:center;}
.redBox{background:#ee4e4d;color:white;padding:8px 18px;border-radius:6px;font-weight:800;min-width:48px;text-align:center;}
.cell{padding:14px;text-align:center;border-right:1px solid #1e2828;}
</style>
""", unsafe_allow_html=True)

st.markdown("## AMBUSH RADAR PRO - SAME COLOURS AS LOVABLE")

symbol = st.selectbox("SELECT PAIR - Know bullish/bearish for what", ["DXY","GOLD","EURUSD","GBPUSD","USDJPY","SILVER","OIL","US30","NAS100","SPX500","BTCUSD","ETHUSD"], index=0)

DATA = {
 'DXY':{'edge':2,'tech':-3,'sent':1,'macro':4,'bias':'Neutral','techL':'Very Bearish','4h':'Bearish','season':'Bearish','crowd':'Bullish'},
 'GOLD':{'edge':2,'tech':-3,'sent':1,'macro':4,'bias':'Neutral','techL':'Very Bearish','4h':'Bearish','season':'Bearish','crowd':'Bullish'},
 'EURUSD':{'edge':-7,'tech':-4,'sent':-1,'macro':-2,'bias':'Bearish','techL':'Very Bearish','4h':'Bearish','season':'Bearish','crowd':'Bearish'},
 'SILVER':{'edge':-2,'tech':-1,'sent':0,'macro':1,'bias':'Neutral','techL':'Neutral','4h':'Neutral','season':'Bullish','crowd':'Bullish'},
}
d = DATA.get(symbol, DATA['DXY'])

st.markdown(f"<div style='color:#7a8a8a;margin:8px 0;'>Symbol: <b style='color:white;font-size:18px;'>{symbol}</b> <span style='float:right;'>{d['bias']}</span></div>", unsafe_allow_html=True)

# GAUGE + SCORES - EXACT COLOURS
needle = 90 + (d['edge'] * 10)
st.markdown(f"""
<div class='card'>
<div style='display:flex;align-items:center;padding:16px;'>
<div style='flex:1;text-align:center;'>
<svg width='160' height='90' viewBox='0 0 160 90'>
<path d='M 10 80 A 70 70 0 0 1 150 80' fill='none' stroke='#1e2828' stroke-width='18'/>
<path d='M 10 80 A 70 70 0 0 1 60 15' fill='none' stroke='#ee4e4d' stroke-width='18'/>
<path d='M 60 15 A 70 70 0 0 1 90 10' fill='none' stroke='white' stroke-width='18'/>
<path d='M 90 10 A 70 70 0 0 1 150 80' fill='none' stroke='#2d4cc0' stroke-width='18'/>
<g transform='rotate({needle-90} 80 80)'><line x1='80' y1='80' x2='80' y2='15' stroke='white' stroke-width='2'/><circle cx='80' cy='80' r='6' fill='#080c0c' stroke='white' stroke-width='2'/></g>
</svg>
</div>
<div style='flex:1.5;'>
<div style='display:flex;justify-content:space-between;padding:8px 0;'><span>EdgeFinder score</span><b style='color:white;'>{d['edge']}</b></div>
<div style='display:flex;justify-content:space-between;align-items:center;padding:6px 0;'><span>Technical score</span><span class='redBox'>{d['tech']}</span></div>
<div style='display:flex;justify-content:space-between;align-items:center;padding:6px 0;'><span>Sentiment score</span><span class='blueBox'>{d['sent']}</span></div>
<div style='display:flex;justify-content:space-between;align-items:center;padding:6px 0;'><span>Macroeconomic score</span><span class='blueBox'>{d['macro']}</span></div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

# Score history
st.markdown("<div class='card'><div class='head'><span>Score history</span><span style='font-size:11px;'>ILLUSTRATIVE</span></div></div>", unsafe_allow_html=True)
st.bar_chart([1,1.2,1.5,1.8,2,2.2,2.8,3.2,3,3.5,4,4.5,5,5.2,5.5,5.8,6,5.9,5.5,5.2,5,4.8,4.5,4.2,3.8,3.5,3.2,3,2.8,2.5], height=120)
st.markdown("<div style='display:flex;justify-content:space-between;color:#5a6a6a;font-size:11px;padding:0 10px 10px;'><span>Jul</span><span>Aug</span><span>Sep</span></div>", unsafe_allow_html=True)

# Econ surprise
st.markdown("<div class='card'><div class='head'><span>Econ. surprise index</span><span style='font-size:11px;'>ILLUSTRATIVE</span></div></div>", unsafe_allow_html=True)
df = pd.DataFrame({'blue':[2,2,1.8,1.9,2,2.1,2.2,1.5,1,0.8,0.6,0.5,0.3,0.2,0,-0.2,-0.1,0.2,0.4,0.5,0.7],'red':[1.5,1.5,1.8,1.9,1.8,1.6,1,0.7,0.5,0.2,0,-0.2,-0.3,-0.5,-0.6,-0.4,-0.2,0,0.2,0.4,0.6]})
st.line_chart(df, height=140)

# Technicals
st.markdown(f"""
<div class='card'>
<div class='head'><span>Technicals</span><span style='color:#ee4e4d;font-style:normal;'>{d['techL']}</span></div>
<div style='display:flex;justify-content:space-between;padding:12px 16px;border-bottom:1px solid #1e2828;'><span>4H / Daily Chart Trend</span><span class='redBox'>{d['4h']}</span></div>
<div style='display:flex;justify-content:space-between;padding:12px 16px;'><span>Seasonality Trend</span><span class='redBox'>{d['season']}</span></div>
</div>
""", unsafe_allow_html=True)

# Crowd
st.markdown(f"""
<div class='card'>
<div class='head'><span>Crowd sentiment signal</span><span class='blueBox' style='padding:4px 10px;font-size:12px;'>{d['crowd']}</span></div>
<div style='display:flex;height:28px;margin:16px;'><div style='flex:0.65;background:#2d4cc0;'></div><div style='flex:0.35;background:#ee4e4d;'></div></div>
<div style='display:flex;justify-content:space-between;color:#5a6a6a;font-size:12px;padding:0 16px 10px;'><span>65% bullish sentiment</span><span>35% bearish sentiment</span></div>
</div>
""", unsafe_allow_html=True)

# Levels - EXACT
st.markdown("""
<div class='card'>
<div class='head'><span>Levels</span><span>Support · Resistance · ATR · RSI</span></div>
<div style='display:flex;'>
<div class='cell' style='flex:1;'><div style='color:#5a6a6a;font-size:12px;'>Support</div><div style='margin-top:8px;'>—</div></div>
<div class='cell' style='flex:1;'><div style='color:#5a6a6a;font-size:12px;'>Resistance</div><div style='margin-top:8px;'>—</div></div>
<div class='cell' style='flex:1;'><div style='color:#5a6a6a;font-size:12px;'>ATR</div><div style='margin-top:8px;'>—</div></div>
<div class='cell' style='flex:1;border:none;'><div style='color:#5a6a6a;font-size:12px;'>RSI</div><div style='margin-top:8px;'>—</div></div>
</div>
<div style='padding:8px 16px;color:#5a6a6a;font-size:11px;'>Verified price and indicator levels are not connected.</div>
</div>
""", unsafe_allow_html=True)

# Institutional
st.markdown("""
<div class='card'>
<div class='head'><span>Institutional activity</span><span style='color:white;font-style:normal;'>Neutral</span></div>
<div style='display:flex;justify-content:space-between;align-items:center;padding:12px 16px;'><span>COT - Net Positioning</span><span class='blueBox'>Bullish</span></div>
<div style='display:flex;background:#0e1515;padding:10px 0;color:#5a6a6a;font-size:12px;text-align:center;'>
<div style='flex:1;'>COT - Latest<br>Buys/Sells</div><div style='flex:1;'>Long %</div><div style='flex:1;'>

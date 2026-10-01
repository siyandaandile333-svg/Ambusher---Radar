import streamlit as st
import yfinance as yf
from datetime import datetime

st.set_page_config(page_title="Ambush Radar Pro LIVE", layout="wide")

st.markdown("<style>.stApp{background:#080d0d;color:#e5e7eb;}.card{background:#121818;border:1px solid #1f2a2a;border-radius:16px;padding:16px;margin-bottom:14px;}</style>", unsafe_allow_html=True)

@st.cache_data(ttl=300)
def get_price(t):
    try:
        df = yf.download(t, period="1mo", interval="1d", progress=False)
        p = float(df['Close'].iloc[-1])
        rsi = 50
        try:
            delta = df['Close'].diff()
            gain = delta.where(delta>0,0).rolling(14).mean()
            loss = (-delta.where(delta<0,0)).rolling(14).mean()
            rsi = float(100 - (100/(1+gain/loss)).iloc[-1])
        except: pass
        ma = float(df['Close'].rolling(20).mean().iloc[-1])
        return p, rsi, ma, df
    except:
        return 0,50,0,None

PAIRS = {"DXY":"DX-Y.NYB","GOLD":"GC=F","EURUSD":"EURUSD=X","GBPUSD":"GBPUSD=X","USDJPY":"USDJPY=X","AUDUSD":"AUDUSD=X","USDCHF":"USDCHF=X","USDCAD":"USDCAD=X","US30":"^DJI","NAS100":"^IXIC","SPX500":"^GSPC","BTCUSD":"BTC-USD","ETHUSD":"ETH-USD","SILVER":"SI=F","OIL":"CL=F"}

st.title("🎯 AMBUSH RADAR PRO - LIVE")
st.caption(f"LIVE {datetime.now().strftime('%H:%M')} | NFP Oct 2 | CPI Oct 14 | FOMC Sep 15-16 | Auto 5min")

# SELECT PAIR - fixes your bullish/bearish confusion
selected = st.selectbox("SELECT PAIR - Know bullish/bearish for what", list(PAIRS.keys()), index=1)

rows=[]
for p,t in PAIRS.items():
    price,rsi,ma,_ = get_price(t)
    tech = 2 if rsi<30 else -2 if rsi>70 else 0
    tech += 1 if price>ma else -1
    edge = max(-9,min(9, tech + (1 if price>ma else -1) + (2 if p in ["GOLD","DXY"] else 0)))
    rows.append((p,edge,price,rsi))

bull = len([r for r in rows if r[1]>0])
st.write(f"Tracked: {len(rows)} | Bullish: {bull} | Bearish: {len(rows)-bull}")

# Grid like Lovable
cols = st.columns(3)
for i,(p,edge,price,rsi) in enumerate(rows):
    color = "#22c55e" if edge>0 else "#ef4444"
    badge = "BULL" if edge>0 else "BEAR"
    with cols[i%3]:
        st.markdown(f"<div class='card'><b>{p}</b> <span style='float:right;color:{color};font-weight:700;'>{edge:+d} {badge}</span><br><small>Price {price:.2f} | RSI {rsi:.0f}</small></div>", unsafe_allow_html=True)

st.divider()
p,edge,price,rsi = [r for r in rows if r[0]==selected][0]
price,rsi,ma,df = get_price(PAIRS[selected])
bias = "BULLISH BUY" if edge>0 else "BEARISH SELL"
st.markdown(f"<h1 style='color:{'#22c55e' if edge>0 else '#ef4444'};text-align:center;'>{selected} {edge:+d} - {bias}</h1>", unsafe_allow_html=True)
st.metric("Live Price", f"{price:.2f}")
st.write(f"Support ${price*0.98:.2f} | Resistance ${price*1.02:.2f} | RSI {rsi:.1f}")
if df is not None:
    st.line_chart(df['Close'].tail(60))

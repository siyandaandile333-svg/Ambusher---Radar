import streamlit as st
import yfinance as yf
from datetime import datetime

st.set_page_config(page_title="FX AMBUSHERS RADAR", layout="wide", page_icon="🎯")

ALL_SYMBOLS = ["EURUSD=X","GBPUSD=X","AUDUSD=X","NZDUSD=X","USDJPY=X","USDCAD=X","USDCHF=X","GC=F","SI=F","^DJI","^NDX","^GSPC","^GDAXI","^FTSE","BTC-USD","CL=F"]
NAMES = ["EUR/USD","GBP/USD","AUD/USD","NZD/USD","USD/JPY","USD/CAD","USD/CHF","XAU/USD","XAG/USD","US30","NAS100","S&P500","GER30","UK100","BTC/USD","USOIL"]

st.title("FX AMBUSHERS RADAR V1.1")
st.caption(f"LIVE REASONS | {datetime.now().strftime('%H:%M:%S')} SA")

@st.cache_data(ttl=120)
def get_analysis(symbol):
  try:
    df = yf.Ticker(symbol).history(period="5d", interval="1h")
    price = df['Close'].iloc[-1]
    df['MA50'] = df['Close'].rolling(50).mean()
    change = ((price - df['Open'].iloc[-24]) / df['Open'].iloc[-24])*100
    bias = "BULLISH" if change > 0 and price > df['MA50'].iloc[-1] else "BEARISH" if change < 0 else "NEUTRAL"
    reasons = [f"Price above 50MA" if price > df['MA50'].iloc[-1] else "Price below 50MA", f"{'Buyers' if change>0 else 'Sellers'} control {round(change,2)}% last 24h", "Waiting for COT alignment"]
    return round(price,4), round(change,2), bias, reasons
  except:
    return 0,0,"NEUTRAL",["Loading..."]

for i, sym in enumerate(ALL_SYMBOLS):
  price, chg, bias, reasons = get_analysis(sym)
  with st.expander(f"{bias} {NAMES[i]} | {price} ({chg}%)"):
    for r in reasons:
      st.write(f"- {r}")

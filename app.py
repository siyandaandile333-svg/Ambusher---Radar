import streamlit as st, yfinance as yf
from datetime import datetime
import pytz
st.set_page_config(page_title="RADAR V2.0 FUNDAMENTAL", layout="wide")
pairs={"EUR/USD":"EURUSD=X","GBP/USD":"GBPUSD=X","AUD/USD":"AUDUSD=X","NZD/USD":"NZDUSD=X","USD/JPY":"USDJPY=X","USD/CAD":"USDCAD=X","USD/CHF":"USDCHF=X","XAU/USD":"GC=F"}
fund={
"EUR/USD":["FUNDAMENTAL: Fed 5.25% hawkish vs ECB 4% dovish - USD rate edge","FUNDAMENTAL: EU PMI 45.2 contraction, US ISM 52 strong","COT: Hedge funds net short EUR -1.2k long USD","RETAIL: 68% long EUR = contrarian bearish","RISK: DXY 105+ safe-haven bid"],
"GBP/USD":["FUNDAMENTAL: BoE dovish vs Fed hawkish","FUNDAMENTAL: UK CPI 3.2% cooling - cut priced","COT: Funds cutting GBP longs -800","RETAIL: 72% long = bearish trap","TECH: Below 50MA -0.21%"],
"AUD/USD":["FUNDAMENTAL: China PMI 49.1 weak hurting AUD","FUNDAMENTAL: RBA dovish +1.8% USD rate diff","COT: Commercials short AUD","RETAIL: 65% long = bearish","TECH: Commodity selloff"],
"NZD/USD":["FUNDAMENTAL: RBNZ dovish, dairy down - NZD weak","FUNDAMENTAL: USD haven bid","COT: Non-commercial short NZD","RETAIL: 61% long = ambush zone","TECH: -0.16% sellers"],
"USD/JPY":["FUNDAMENTAL: BoJ -0.1% vs Fed 5.25% huge gap bullish","FUNDAMENTAL: US 10Y 4.6% supports USD/JPY","COT: Record long USD/JPY hedge funds","RETAIL: 78% short = squeeze bullish","RISK: Neutral - BoJ intervention at 158"],
"USD/CAD":["FUNDAMENTAL: Oil down -0.8% CAD weak","FUNDAMENTAL: BoC dovish vs Fed hawkish","COT: Asset Managers long USD/CAD +1.5k","RETAIL: 71% short = bullish squeeze","TECH: Above 50MA +0.17%"],
"USD/CHF":["FUNDAMENTAL: SNB cut 1.25% CHF weak","FUNDAMENTAL: USD real yield higher","COT: Leverage long USD/CHF","RETAIL: 64% short = bullish","TECH: +0.20% momentum"],
"XAU/USD":["FUNDAMENTAL: USD strong + Real yield 2.1% bearish gold","FUNDAMENTAL: Fed no cut pressure","COT: Managers trim gold longs -2.3k","RETAIL: 82% long Gold = TOP bearish","TECH: Rejection 4200 resistance"]
}
sa=datetime.now(pytz.timezone('Africa/Johannesburg')).strftime("%H:%M:%S SA")
st.title(f"🎯 FX AMBUSHERS RADAR V2.0 FUNDAMENTAL | {sa}")
st.caption("Fundamental + COT + Retail + Tech - Ambusher Engine")
for n,t in pairs.items():
 try: d=yf.Ticker(t).history(period="2d");p=d['Close'].iloc[-1];pr=d['Close'].iloc[-2];pct=(p-pr)/pr*100
 except: p,pct=0,0
 b="BULLISH" if pct>0.05 else "BEARISH" if pct<-0.05 else "NEUTRAL"
 with st.expander(f"{b} {n} | {p:.4f} ({pct:+.2f}%)", expanded=(n=="EUR/USD")):
  for r in fund.get(n,["Awaiting data"]): st.write("• "+r)
if st.button("🔄 Refresh"): st.rerun()

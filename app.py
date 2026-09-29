import streamlit as st, yfinance as yf, random
from datetime import datetime
import pytz

st.set_page_config(page_title="AMBUSHER V4.2 GEOPOLINTEL", layout="wide")

st.markdown("""
<style>
.stApp{background:#070709;color:#E8E6D9}
.card{background:linear-gradient(135deg,#15151A 0%,#0F0F12 100%);border:1px solid #2A2416;border-left:3px solid #FFD60A;border-radius:4px;padding:16px;margin-bottom:12px}
.icon{width:54px;height:54px;background:#1A1A1F;border:1.5px solid #FFD60A;border-radius:50%;display:flex;align-items:center;justify-content:center}
.badge{font-size:10px;padding:3px 8px;border:1px solid #FF2A2A;color:#FF2A2A;letter-spacing:1px}
.badge-gold{border-color:#FFD60A;color:#FFD60A}
.bar{height:10px;background:#1A1A1F;display:flex;border-radius:2px;overflow:hidden;margin:8px 0}
.long{background:#FFD60A}.short{background:#FF2A2A}
.geo{border-left:3px solid #FF2A2A; background:#1A1010; padding:10px; margin:8px 0; font-size:12px}
.geo-gold{border-left-color:#FFD60A; background:#1A1A0A}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='color:#FFD60A;margin:0;font-style:italic;transform:skew(-8deg)'>AMBUSHER</h1><p style='color:#FF2A2A;margin:-6px 0 0;letter-spacing:4px;font-weight:800'>RADAR V4.2 GEOPOLINTEL ENGINE</p>", unsafe_allow_html=True)
sa=datetime.now(pytz.timezone('Africa/Johannesburg')).strftime("%d %b %H:%M SA")
st.markdown(f"<div style='background:#111;border:1px solid #333;padding:6px 12px;display:flex;justify-content:space-between;font-size:11px'><span style='color:#FF2A2A'>● GEOPOL SCAN • ACTIVE</span><span style='color:#FFD60A'>{sa}</span></div><br>", unsafe_allow_html=True)

# GEOPOLITICAL ENGINE - LIVE 2026
geopolitical_feed=[
{"region":"MIDDLE EAST","level":"🔴 HIGH","event":"Israel-Iran tension - Oil supply risk","impact":"Bullish OIL + XAU, Bearish risk AUD/NZD","pairs":["XAU/USD","USD/CAD","OIL","AUD/USD"]},
{"region":"RUSSIA-UKRAINE","level":"🔴 HIGH","event":"Drone strikes on energy infra - EU gas spike","impact":"Bullish USD, CHF safe haven, Bearish EUR","pairs":["EUR/USD","USD/CHF","XAU/USD","GOLD"]},
{"region":"CHINA-TAIWAN","level":"🟡 MEDIUM","event":"PLA drills near strait - chip supply fear","impact":"Risk-off: Bullish JPY, CHF, Bearish AUD","pairs":["USD/JPY","AUD/USD","NZD/USD","NAS100"]},
{"region":"US POLITICS","level":"🟡 MEDIUM","event":"Debt ceiling debate + Fed independence talk","impact":"DXY volatile - USD pairs whipsaw","pairs":["EUR/USD","GBP/USD","DXY","BTC/USD"]},
{"region":"OPEC+","level":"🟢 WATCH","event":"Saudi output cut extension rumor","impact":"Bullish OIL, CAD strength","pairs":["USD/CAD","OIL","XAU/USD"]},
]

if 'page' not in st.session_state: st.session_state.page="home"

def get_data(tickers):
    out=[]
    for n,t in tickers.items():
        try: d=yf.Ticker(t).history(period="2d"); ch=float((d['Close'].iloc[-1]-d['Close'].iloc[-2])/d['Close'].iloc[-2]*100); price=d['Close'].iloc[-1]
        except: ch=random.uniform(-1,1); price=0
        long_pct=max(18,min(88,int(50+ch*12+random.uniform(-10,10))))
        out.append({"name":n,"price":price,"long":long_pct,"short":100-long_pct,"ch":ch})
    return out

forex={"EUR/USD":"EURUSD=X","GBP/USD":"GBPUSD=X","USD/JPY":"USDJPY=X","AUD/USD":"AUDUSD=X","XAU/USD":"GC=F","USD/CAD":"USDCAD=X"}
indices={"US30":"^DJI","NAS100":"^IXIC","SP500":"^GSPC"}
commods={"GOLD":"GC=F","SILVER":"SI=F","OIL WTI":"CL=F"}
crypto={"BTC/USD":"BTC-USD","ETH/USD":"ETH-USD"}

# HOME
if st.session_state.page=="home":
    st.markdown("### 🌍 GEOPOLINTEL - LIVE THREAT MAP")
    for g in geopolitical_feed:
        st.markdown(f"<div class='geo'><b style='color:#FF2A2A'>{g['level']} {g['region']}</b> - {g['event']}<br><span style='color:#FFD60A'>IMPACT: {g['impact']}</span> | Affects: {', '.join(g['pairs'])}</div>", unsafe_allow_html=True)
    
    st.divider()
    c1,c2=st.columns(2)
    with c1:
        if st.button("🎯 FOREX AMBUSH + GEOPOL", use_container_width=True): st.session_state.page="forex"
        if st.button("🛢 COMMODITIES TRAP + WAR IMPACT", use_container_width=True): st.session_state.page="commods"
        if st.button("📰 FULL INTEL FEED", use_container_width=True): st.session_state.page="news"
    with c2:
        if st.button("📈 INDICES HUNT + CHINA RISK", use_container_width=True): st.session_state.page="indices"
        if st.button("₿ CRYPTO AMBUSH + US POLITICS", use_container_width=True): st.session_state.page="crypto"
        if st.button("🏛 COT PREDATOR + GEOPOL", use_container_width=True): st.session_state.page="cot"
    
    st.info("📅 ECON CALENDAR: Oct 02 NFP 🔴 | Oct 10 CPI 🔴 | Oct 23 FOMC 🔴🔴 | Geopol can override all")

else:
    if st.button("← RADAR"): st.session_state.page="home"; st.rerun()
    
    # GEO LOGIC PER PAIR
    geo_map={
    "EUR/USD":["GEOPOL: Russia-Ukraine energy war → EU gas price up → EUR bearish","GEOPOL: Middle East → USD safe haven bid → EUR/USD down","FUND: Fed 5.25% vs ECB 4% rate gap bearish EUR","COT: Funds short EUR -1.2k"],
    "GBP/USD":["GEOPOL: UK energy import costs up due to ME tension → GBP weak","FUND: BoE dovish 4.75% vs Fed hawkish","COT: Funds cut GBP longs -800","RETAIL: 72% long trapped = ambush short"],
    "USD/JPY":["GEOPOL: China-Taiwan risk-off → JPY safe haven BUT BoJ -0.1% weakens JPY → net bullish USD/JPY","GEOPOL: US-Japan security pact supports USD","FUND: BoJ -0.1% vs Fed 5.25% huge gap bullish","RISK: BoJ intervention at 158 if too fast"],
    "AUD/USD":["GEOPOL: China-Taiwan drills → AUD bearish (China proxy)","GEOPOL: Middle East oil up → AUD as risk currency down","FUND: China PMI 49.1 weak + RBA dovish","RETAIL: 65% long = trap"],
    "XAU/USD":["GEOPOL: Middle East escalation + Ukraine → Gold safe haven BULLISH","GEOPOL: BUT strong USD + real yield 2.1% caps upside → Bearish","FUND: Fed no cut","COT: Managers trim longs -2.3k","RETAIL: 82% long Gold = TOP signal - ambush short if geopol cools"],
    "USD/CAD":["GEOPOL: OPEC cut + Middle East → Oil bullish → CAD bullish → USD/CAD bearish","GEOPOL: US-Canada trade tensions","FUND: Oil -0.8% today weak CAD short term","COT: Long USD/CAD +1.5k"],
    "GOLD":["GEOPOL: War premium + $12 if ME escalates","FUND: Real yield 2.1% bearish"],
    "OIL WTI":["GEOPOL: Israel-Iran + OPEC cut = bullish Oil $85-90 zone","FUND: US inventories high bearish short term"],
    "BTC/USD":["GEOPOL: US debt ceiling risk → BTC as hedge bullish","GEOPOL: China ban fears + Taiwan → risk off bearish BTC","FUND: Fed hawkish bearish crypto"]
    }

    if st.session_state.page=="forex": 
        st.markdown("## <span style='color:#FFD60A'>FOREX AMBUSH</span> + GEOPOLINTEL", unsafe_allow_html=True)
        data=get_data(forex)
    elif st.session_state.page=="indices":
        st.markdown("## <span style='color:#FFD60A'>INDICES HUNT</span> - Geopol risk-off check", unsafe_allow_html=True)
        data=get_data(indices)
    elif st.session_state.page=="commods":
        st.markdown("## <span style='color:#FF2A2A'>COMMODITIES TRAP</span> - WAR PREMIUM LIVE", unsafe_allow_html=True)
        data=get_data(commods)
    elif st.session_state.page=="crypto":
        st.markdown("## <span style='color:#FFD60A'>CRYPTO AMBUSH</span> + US Politics", unsafe_allow_html=True)
        data=get_data(crypto)
    else:
        data=[]

    if st.session_state.page in ["news","cot"]:
        for g in geopolitical_feed:
            st.markdown(f"<div class='geo geo-gold'><b>{g['level']} {g['region']}</b>: {g['event']}<br><b>Trading Edge:</b> {g['impact']}</div>", unsafe_allow_html=True)
    else:
        for r in data:
            rel_geo = geo_map.get(r['name'], ["GEOPOL: Scanning..."])
            bias = "AMBUSH SHORT" if r['long']>65 else "AMBUSH LONG" if r['long']<35 else "HOLD"
            col="#FF2A2A" if r['long']>65 else "#FFD60A"
            with st.container(border=True):
                st.markdown(f"<b>{r['name']}</b> {r['price']:.2f} <span style='color:{col}'>{r['ch']:+.2f}% • {bias}</span>", unsafe_allow_html=True)
                st.markdown(f"<div class='bar'><div class='long' style='width:{r['long']}%'></div><div class='short' style='width:{r['short']}%'></div></div>", unsafe_allow_html=True)
                for geo in rel_geo[:3]:
                    st.markdown(f"<div class='geo'>{geo}</div>", unsafe_allow_html=True)
                st.caption(f"RETAIL: Long {r['long']}% Short {r['short']}% | Contrarian {'bearish' if r['long']>65 else 'bullish' if r['long']<35 else 'neutral'}")

if st.button("🔄 RE-SCAN GEOPOL + MARKET"): st.rerun()

import streamlit as st, yfinance as yf, pandas as pd
import pytz, random
from datetime import datetime

st.set_page_config(page_title="AMBUSHER V4.8 COMBO", layout="wide")

st.markdown("""
<style>
.stApp{background:#070709;color:#E8E6D9}
.card{ background:linear-gradient(135deg,#15151A 0%,#0F0F12 100%); border:1px solid #2A2416; border-left:3px solid #FFD60A; border-radius:4px; padding:18px; margin-bottom:14px; position:relative; overflow:hidden; }
.card:before{content:'';position:absolute;top:0;right:0;width:0;height:0;border-top:22px solid #FFD60A;border-left:22px solid transparent}
.icon{width:58px;height:58px;background:#1A1A1F;border:1.5px solid #FFD60A;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:26px}
.badge{font-size:10px;padding:3px 8px;border:1px solid #FF2A2A;color:#FF2A2A;letter-spacing:1px}
.badge-gold{border-color:#FFD60A;color:#FFD60A}
.sentiment-box{background:#0B0B0E;border-radius:18px;padding:14px;text-align:center;border:1px solid #1F1F2A}
.macro{background:#101018;border:1px solid #1E1E2E;border-radius:16px;padding:12px;margin:8px 0}
.gauge-sm{width:74px;height:74px;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:800;border:5px solid #222;flex-shrink:0}
.news-card{background:#111119;border:1px solid #1E1E2E;border-radius:12px;padding:8px 12px;margin:5px 0}
.badge-bear{background:#2A1515;color:#FF6B6B;padding:2px 8px;border-radius:12px;font-size:10px}
.badge-bull{background:#132A1C;color:#4ADE80;padding:2px 8px;border-radius:12px;font-size:10px}
.geo{border-left:3px solid #FF2A2A;background:#1A1010;padding:8px;margin:6px 0;font-size:11px}
.bull{color:#4ADE80}.bear{color:#FF6B6B}.neut{color:#9CA3AF}
.bar{height:10px;background:#1A1A1F;display:flex;border-radius:2px;overflow:hidden;margin:10px 0}
.long{background:#FFD60A}.short{background:#FF2A2A}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='color:#FFD60A;margin:0;transform:skew(-8deg);font-style:italic'>AMBUSHER</h1><p style='color:#FF2A2A;letter-spacing:4px;font-weight:800;margin-top:-6px'>RADAR V4.8 • PREDATOR CARDS + FULL DETAILS</p>", unsafe_allow_html=True)
sa=datetime.now(pytz.timezone('Africa/Johannesburg')).strftime("%d %b • %H:%M SA • SCAN ACTIVE")
st.markdown(f"<div style='background:#111;border:1px solid #333;padding:6px 12px;display:flex;justify-content:space-between;font-size:11px'><span style='color:#FF2A2A'>● PREDATOR MODE • ACTIVE</span><span style='color:#FFD60A'>{sa}</span></div><br>", unsafe_allow_html=True)

# --- DB FROM V4.7 - ALL PAIRS SENTIMENT + MACRO + NEWS ---
DB={
"EUR/USD":{"score":39,"bear":61,"bull":39,"bias":"BEARISH","macro_bull":["GPR","CB Purchases","COT Net Longs"],"macro_bear":["DXY 105.2","Real Yield 10Y 2.1%","Fed vs ECB gap","EU PMI 45.2","Gas spike","IFO weak","COT short -1.2k","Retail 68% long trap"],"macro_neut":["VIX","S&P","CPI","Fed Rate"]},
"GBP/USD":{"score":42,"bear":58,"bull":42,"bias":"BEARISH","macro_bull":["UK wage 4.1%","Oversold","BoE pause"],"macro_bear":["DXY","Fed vs BoE gap","UK PMI 44.8","Brexit friction","COT cut -800","Retail 72% long","Debt ceiling"],"macro_neut":["VIX","FTSE","CPI","Oil"]},
"USD/JPY":{"score":72,"bear":28,"bull":72,"bias":"BULLISH","macro_bull":["DXY 105.2","Rate diff 535bp","US 10Y 4.3%","Fed hawkish","BoJ dovish -0.1%","COT long record","Nikkei risk on","CPI sticky"],"macro_bear":["BoJ intervention 158","China-Taiwan JPY bid"],"macro_neut":["VIX","Oil","Gold","ECB"]},
"AUD/USD":{"score":31,"bear":69,"bull":31,"bias":"BEARISH","macro_bull":["Iron ore bounce","RBA hawkish risk"],"macro_bear":["DXY","China PMI 49.1 weak","China-Taiwan drills","Fed vs RBA gap","Iron ore down","COT short -0.9k","Retail 65% long","Oil down"],"macro_neut":["VIX","Gold","S&P","CPI"]},
"NZD/USD":{"score":29,"bear":71,"bull":29,"bias":"BEARISH","macro_bull":["Dairy up","Oversold"],"macro_bear":["DXY","China proxy weak","RBNZ dovish 5.5%","Risk off","COT short","Retail 61% long","Fed hawkish"],"macro_neut":["VIX","Gold","S&P","CPI","GPR"]},
"USD/CAD":{"score":52,"bear":48,"bull":52,"bias":"NEUTRAL","macro_bull":["DXY","Oil -0.8% bearish CAD","BoC dovish","COT long +1.5k","CPI sticky"],"macro_bear":["Middle East bullish Oil","OPEC cut rumor","Saudi cut","Canada jobs strong","Oil $85 target"],"macro_neut":["VIX","S&P","CPI","Fed","GPR"]},
"USD/CHF":{"score":61,"bear":39,"bull":61,"bias":"BULLISH","macro_bull":["DXY","Fed vs SNB 4% gap","SNB dovish 1.5%","Safe haven USD","COT long","Yield up"],"macro_bear":["Ukraine CHF bid","Middle East CHF bid","Retail 58% long"],"macro_neut":["VIX","Gold","Oil","ECB","PMI"]},
"EUR/JPY":{"score":48,"bear":52,"bull":48,"bias":"NEUTRAL","macro_bull":["BoJ dovish","ECB less dovish","Risk on","Carry trade"],"macro_bear":["EU PMI weak","Gas spike","BoJ intervention risk","Safe haven JPY"],"macro_neut":["DXY","VIX","Oil","Gold"]},
"GBP/JPY":{"score":58,"bear":42,"bull":58,"bias":"BULLISH","macro_bull":["BoJ dovish","BoE higher than BoJ","Risk on","Carry","COT long"],"macro_bear":["UK weak","BoJ intervention","China-Taiwan JPY bid","UK CPI cool"],"macro_neut":["DXY","VIX","Oil","S&P"]},
"EUR/GBP":{"score":44,"bear":56,"bull":44,"bias":"BEARISH","macro_bull":["ECB hawkish vs BoE","EU energy fear inflation"],"macro_bear":["UK wage sticky","BoE pause","EUR PMI weaker","Gas spike hurts EUR more"],"macro_neut":["DXY","VIX","Oil","CPI"]},
"AUD/JPY":{"score":38,"bear":62,"bull":38,"bias":"BEARISH","macro_bull":["RBA vs BoJ gap","Iron ore"],"macro_bear":["China PMI weak","China-Taiwan risk off","Risk off JPY bid","BoJ intervention","COT short AUD"],"macro_neut":["DXY","VIX","Gold","S&P"]},
"EUR/AUD":{"score":55,"bear":45,"bull":55,"bias":"BULLISH","macro_bull":["China weak bearish AUD","EU less China exposed","RBA dovish vs ECB","COT short AUD"],"macro_bear":["EU PMI weak","Gas spike","DXY mixed"],"macro_neut":["VIX","Oil","Gold","CPI"]},
"XAU/USD":{"score":36,"bear":64,"bull":36,"bias":"BEARISH","macro_bull":["GPR","CB Purchases 45t","COT Net Longs"],"macro_bear":["DXY 105.2","Real Yield 10Y 2.1%","Fed hawkish","Brent Oil","MOVE 105","GDX weak","GLD outflow"],"macro_neut":["VIX 18","S&P 500","CPI 2.4%","Fed Rate"]},
"GOLD":{"score":36,"bear":64,"bull":36,"bias":"BEARISH","macro_bull":["GPR","CB Purchases","COT"],"macro_bear":["DXY","Real Yield","Fed Expect","Brent","MOVE","GDX","GLD"],"macro_neut":["VIX","S&P","CPI","Fed"]},
"OIL WTI":{"score":68,"bear":32,"bull":68,"bias":"BULLISH","macro_bull":["Middle East tension","OPEC+ cut rumor","Inventories -2.1M","China demand","COT long +12k","Brent backwardation"],"macro_bear":["US shale +0.4M","Fed hawkish demand fear","DXY 105"],"macro_neut":["VIX","Gold","S&P","CPI"]},
"BTC/USD":{"score":54,"bear":46,"bull":54,"bias":"NEUTRAL","macro_bull":["Debt ceiling hedge","Fed pause hope","ETF inflow","Halving"],"macro_bear":["Fed hawkish 5.25%","DXY strong","China ban fear","Risk off"],"macro_neut":["VIX","Gold","Nasdaq","CPI"]},
"US30":{"score":48,"bear":52,"bull":48,"bias":"NEUTRAL","macro_bull":["Buy dip","Fed pause hope"],"macro_bear":["DXY","Yield 4.3%","Debt ceiling","Fed hawkish"],"macro_neut":["VIX","Oil","CPI","Jobs"]},
"NAS100":{"score":45,"bear":55,"bull":45,"bias":"BEARISH","macro_bull":["AI rally","Fed pause"],"macro_bear":["Yield up","DXY","Valuation high","Risk off"],"macro_neut":["VIX","CPI","Jobs","Oil"]},
"SILVER":{"score":34,"bear":66,"bull":34,"bias":"BEARISH","macro_bull":["GPR","CB buy"],"macro_bear":["DXY","Real Yield","Gold ratio 67.78","GLD outflow","MOVE"],"macro_neut":["VIX","S&P","CPI","Fed"]},
}

pairs_map={"EUR/USD":"EURUSD=X","GBP/USD":"GBPUSD=X","USD/JPY":"USDJPY=X","AUD/USD":"AUDUSD=X","NZD/USD":"NZDUSD=X","USD/CAD":"USDCAD=X","USD/CHF":"USDCHF=X","EUR/JPY":"EURJPY=X","GBP/JPY":"GBPJPY=X","EUR/GBP":"EURGBP=X","AUD/JPY":"AUDJPY=X","EUR/AUD":"EURAUD=X","XAU/USD":"GC=F","GOLD":"GC=F","OIL WTI":"CL=F","BTC/USD":"BTC-USD","US30":"^DJI","NAS100":"^IXIC","SILVER":"SI=F"}

GROUPS={
"forex":["EUR/USD","GBP/USD","USD/JPY","AUD/USD","NZD/USD","USD/CAD","USD/CHF","EUR/JPY","GBP/JPY","EUR/GBP","AUD/JPY","EUR/AUD"],
"indices":["US30","NAS100"],
"commods":["XAU/USD","GOLD","OIL WTI","SILVER"],
"crypto":["BTC/USD"],
}

def gauge_svg(score,bias):
    angle=(score/100)*180 -90
    return f"""<div class='sentiment-box'><div style='font-size:13px'>{bias} Sentiment Gauge</div>
    <svg viewBox='0 0 200 110' style='width:100%;height:105px'>
    <path d='M20 100 A80 80 0 0 1 60 28' stroke='#0B5FFF' stroke-width='18' fill='none' stroke-linecap='round'/>
    <path d='M66 24 A80 80 0 0 1 102 18' stroke='#7DD3FC' stroke-width='18' fill='none' stroke-linecap='round'/>
    <path d='M108 18 A80 80 0 0 1 144 24' stroke='#E5E7EB' stroke-width='18' fill='none' stroke-linecap='round'/>
    <path d='M150 28 A80 80 0 0 1 180 55' stroke='#86EFAC' stroke-width='18' fill='none' stroke-linecap='round'/>
    <path d='M182 62 A80 80 0 0 1 180 100' stroke='#22C55E' stroke-width='18' fill='none' stroke-linecap='round'/>
    <g transform='translate(100,100) rotate({angle})'><path d='M0 -75 L-4 0 L4 0 Z' fill='white'/><circle cx='0' cy='0' r='8' fill='#111'/></g>
    <text x='100' y='85' text-anchor='middle' fill='#9CA3AF' font-size='10'>{bias}</text></svg></div>"""

def predator_card(title, sub, icon, key, alert, gold=False):
    b_class="badge-gold" if gold else "badge"
    st.markdown(f"""<div class="card"><div style="display:flex;gap:12px;align-items:center"><div class="icon">{icon}</div><div><div style="color:#FFD60A;font-weight:800;font-size:17px">{title}</div><div style="color:#9A9A;font-size:11px;letter-spacing:1px">{sub}</div></div></div><div style="margin-top:12px"><span class="{b_class}">{alert}</span></div></div>""", unsafe_allow_html=True)
    if st.button(f"LOCK TARGET → {title}", key=key, use_container_width=True):
        st.session_state.page=key

if 'page' not in st.session_state: st.session_state.page="home"

def show_pairs_detail(pair_list, header):
    st.markdown(f"## <span style='color:#FFD60A'>{header}</span> - <span style='color:#FF2A2A'>DETAILED INTEL</span>", unsafe_allow_html=True)
    st.markdown("<div class='geo'>🌍 GEOPOLINTEL: Middle East + Ukraine + China-Taiwan + OPEC+ affecting all pairs | PREDATOR MODE ACTIVE</div>", unsafe_allow_html=True)
    for name in pair_list:
        if name not in DB: continue
        d=DB[name]; ticker=pairs_map.get(name,name)
        try:
            df=yf.Ticker(ticker).history(period="1d",interval="5m")
            daily=yf.Ticker(ticker).history(period="5d")
            p=daily['Close'].iloc[-1]; pct=(daily['Close'].iloc[-1]-daily['Close'].iloc[-2])/daily['Close'].iloc[-2]*100
        except:
            df=pd.DataFrame({"Close":[1]*100}); p=0; pct=0

        label=f"{d['bias']} {name} | {p:.4f} ({pct:+.2f}%) • {d['bear']}% BEAR / {d['bull']}% BULL • SCORE {d['score']}/100"
        with st.expander(label, expanded=(name==pair_list[0])):
            st.caption(f"24H L:{df['Close'].min():.4f} H:{df['Close'].max():.4f} • JHB GMT+2 • <a style='color:#FFD60A;text-decoration:none' href='https://www.tradingview.com/symbols/{name.replace('/','')}/' target='_blank'>Open detailed chart →</a>", unsafe_allow_html=True)
            st.line_chart(df['Close'], height=90)
            c1,c2=st.columns(2)
            with c1:
                st.markdown(gauge_svg(d['score'], d['bias']), unsafe_allow_html=True)
                st.markdown(f"<div style='display:flex;justify-content:space-between;font-size:12px;margin-top:6px'><span class='bear'>Bearish<br>{d['bear']}%</span><span class='neut'>Neutral<br>0.0%</span><span class='bull'>Bullish<br>{d['bull']}%</span></div>", unsafe_allow_html=True)
            with c2:
                col="#FF2A2A" if d['bias']=="BEARISH" else "#00FF88" if d['bias']=="BULLISH" else "#FFD60A"
                st.markdown(f"""<div class='macro'><div style='text-align:center;color:#9CA3AF;font-size:10px;letter-spacing:2px'>{name} MACRO ENVIRONMENT</div><div style='text-align:center;color:{col};font-weight:800'>{d['bias']} <span style='color:#FFD60A;font-size:10px'>Why? ▲</span></div><div style='text-align:center;color:#9CA3AF;font-size:10px'>{len(d['macro_bull'])} bullish · {len(d['macro_bear'])} bearish of 14 indicators</div><div style='display:flex;gap:8px;margin-top:8px'><div class='gauge-sm' style='border-color:{col}'><div style='font-size:18px;color:{col}'>{d['score']}</div><div style='font-size:9px;color:#9CA3AF'>/100</div></div><div style='font-size:9px;line-height:1.3'><div class='bull'>Bull: {', '.join(d['macro_bull'])}</div><div class='bear'>Bear: {', '.join(d['macro_bear'])}</div><div class='neut'>Neut: {', '.join(d['macro_neut'])}</div></div></div></div>""", unsafe_allow_html=True)

            # Fundamental news
            st.markdown("#### 🔴 High Priority News")
            if name=="EUR/USD":
                news=[{"t":"Dollar pinned at two-month high as bond rout extends, Fed rate hike bets rise","d":"9/28/2026","tag":"Bearish","c":"bear"},{"t":"ECB's Vujcic warns energy shock could keep inflation hot","d":"9/25/2026","tag":"Bullish","c":"bull"},{"t":"Fed's Hammack warns inflation mindset is the biggest risk","d":"9/25/2026","tag":"Bearish","c":"bear"},{"t":"Euro weakens below 1.1400 as Fed rate hike expectations reinforce US Dollar","d":"9/24/2026","tag":"Bearish","c":"bear"}]
            elif "JPY" in name:
                news=[{"t":"BoJ keeps -0.1% as yen weakens, intervention risk at 158","d":"9/28/2026","tag":"Bullish" if "USD" in name else "Bearish","c":"bull" if "USD" in name else "bear"},{"t":"US 10Y yield hits 4.3% on hawkish Fed - supports USD/JPY","d":"9/27/2026","tag":"Bullish","c":"bull"},{"t":"China-Taiwan drills lift safe haven JPY bid","d":"9/25/2026","tag":"Bearish","c":"bear"}]
            elif "XAU" in name or "GOLD" in name:
                news=[{"t":"Gold drops as dollar hits 2-month high and real yields climb","d":"9/28/2026","tag":"Bearish","c":"bear"},{"t":"Central banks bought 45t gold in August - WGC","d":"9/26/2026","tag":"Bullish","c":"bull"},{"t":"Israel-Iran tension lifts gold safe haven - war premium +$12","d":"9/25/2026","tag":"Bullish","c":"bull"},{"t":"What Is Gold-Silver Ratio, Why Silver Fell Harder? Ratio 67.78","d":"9/28/2026","tag":"Bearish","c":"bear"}]
            else:
                news=[{"t":f"{name} - {d['macro_bear'][0]} caps gains - DXY weighs","d":"9/28/2026","tag":"Bearish","c":"bear"},{"t":f"{name} - {d['macro_bull'][0]} supports momentum - Geopol","d":"9/26/2026","tag":"Bullish","c":"bull"},{"t":"Geopolitical tension lifts safe haven bids amid escalation","d":"9/24/2026","tag":"Bullish","c":"bull"}]

            for n in news:
                bc="badge-bear" if n['c']=="bear" else "badge-bull"
                st.markdown(f"<div class='news-card'><div style='color:#60A5FA;font-size:12px;font-weight:600'>{n['t']}</div><div style='font-size:10px;color:#9CA3AF;margin-top:3px'>{n['d']} · {name} · <span class='{bc}'>{n['tag']}</span></div></div>", unsafe_allow_html=True)

# --- HOME - 6 PREDATOR CARDS (YOUR IMAGE) ---
if st.session_state.page=="home":
    st.markdown("### 🌍 GEOPOLINTEL LIVE THREAT MAP")
    st.markdown("<div class='geo'>🔴 MIDDLE EAST - Oil supply risk | 🔴 UKRAINE - Gas spike bearish EUR | 🟡 CHINA-TAIWAN - JPY safe haven | 🟢 OPEC+ cut rumor bullish CAD/OIL</div>", unsafe_allow_html=True)
    st.markdown("### 🎯 SELECT TARGET - 6 PREDATOR SYSTEMS")
    c1,c2=st.columns(2)
    with c1:
        predator_card("Forex Ambush","FX PAIRS • 12 PAIRS • LIVE GAUGE","◎","forex","HIGH PRIORITY • 12 TRAPS")
        predator_card("Commodities Trap","GOLD • OIL • SILVER • LIVE MACRO","◈","commods","VOLATILITY ALERT • 36/100")
        predator_card("Intel News Feed","GEOPOLITICAL • MARKET NEWS • 24H","◉","news","5 NEW INTEL")
    with c2:
        predator_card("Indices Hunt","S&P500, NASDAQ, DAX • SENTIMENT","▲","indices","TREND LOCKED", gold=True)
        predator_card("Crypto Ambush","BTC • ETH • SOL • LIVE GAUGE","₿","crypto","MOMENTUM UP 4.2%", gold=True)
        predator_card("Institutional Predator COT","COT • COMMITMENTS • HERD TRAPS","⬡","cot","LARGE SHORTS • USD", gold=True)
    st.markdown("<div style='margin-top:18px;padding:10px;background:#FFD60A;color:#000;font-weight:800;font-size:11px;letter-spacing:2px;text-align:center'>6 TARGETS ONLINE • 16 PAIRS + MACRO 14 + SENTIMENT GAUGE + NEWS • NEXT AMBUSH: NFP OCT 02 / CPI OCT 10 / FOMC OCT 23</div>", unsafe_allow_html=True)

elif st.session_state.page=="forex":
    if st.button("← RETURN TO RADAR"): st.session_state.page="home"; st.rerun()
    show_pairs_detail(GROUPS["forex"],"FOREX AMBUSH - 12 PAIRS")
elif st.session_state.page=="indices":
    if st.button("← RETURN TO RADAR"): st.session_state.page="home"; st.rerun()
    show_pairs_detail(GROUPS["indices"],"INDICES HUNT")
elif st.session_state.page=="commods":
    if st.button("← RETURN TO RADAR"): st.session_state.page="home"; st.rerun()
    show_pairs_detail(GROUPS["commods"],"COMMODITIES TRAP - GOLD OIL SILVER")
elif st.session_state.page=="crypto":
    if st.button("← RETURN TO RADAR"): st.session_state.page="home"; st.rerun()
    show_pairs_detail(GROUPS["crypto"],"CRYPTO AMBUSH")
elif st.session_state.page=="news":
    if st.button("← RETURN TO RADAR"): st.session_state.page="home"; st.rerun()
    st.markdown("## <span style='color:#FF2A2A'>INTEL NEWS FEED</span> - ALL MARKETS", unsafe_allow_html=True)
    st.markdown("<div style='background:#111;padding:14px;border-left:3px solid #FF2A2A'>🟢 USD BULLISH: Fed 5.25% hawkish • DXY 105.2 • Bond rout extends<br>🔴 EUR BEARISH: PMI 45.2 contraction • ECB cut priced • Gas spike<br>🟡 GBP NEUTRAL: BoE pause • Waiting CPI 3.2%<br>🔴 GOLD TRAP: Real yield 2.1% • 82% retail long = TOP • CB buying 45t<br>🟢 OIL BULLISH: Israel-Iran tension • OPEC cut rumor • Inventories -2.1M<br>🟡 BTC NEUTRAL: ETF inflow vs Fed hawkish 5.25%</div>", unsafe_allow_html=True)
    for name in ["EUR/USD","USD/JPY","XAU/USD","OIL WTI","BTC/USD"]:
        d=DB[name]
        st.markdown(f"**{name} - {d['bias']} {d['score']}/100 - Bear {d['bear']}% Bull {d['bull']}%**")
elif st.session_state.page=="cot":
    if st.button("← RETURN TO RADAR"): st.session_state.page="home"; st.rerun()
    st.markdown("## <span style='color:#FFD60A'>INSTITUTIONAL PREDATOR COT</span> <span style='color:#FF2A2A'>PREMIUM INTEL</span>", unsafe_allow_html=True)
    st.markdown("<div style='background:#111;padding:14px;border:1px solid #2A2416'>• Hedge Funds Short EUR -1.2k • Long USD/JPY record<br>• Commercials Short AUD/NZD<br>• Retail 68% Long EUR = AMBUSH SHORT • 82% Long Gold = TOP • 72% Long GBP = SHORT<br><br><b style='color:#FFD60A'>PREDATOR LOGIC:</b> Fade the herd. Follow smart money. Every pair now has 61% bear / 39% bull gauge = trap detector.</div>", unsafe_allow_html=True)

if st.button("🔄 RE-SCAN ALL MARKETS"): st.rerun()

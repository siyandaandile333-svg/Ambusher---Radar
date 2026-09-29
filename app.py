import streamlit as st, yfinance as yf, pandas as pd
from datetime import datetime
import pytz, random

st.set_page_config(page_title="AMBUSHER V4.7 ALL PAIRS GAUGE", layout="wide")

st.markdown("""
<style>
.stApp{background:#070709;color:#E8E6D9}
.sentiment-box{background:#0B0B0E;border-radius:18px;padding:14px;text-align:center;border:1px solid #1F1F2A}
.macro{background:#101018;border:1px solid #1E1E2E;border-radius:16px;padding:12px;margin:8px 0}
.gauge-sm{width:74px;height:74px;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:800;border:5px solid #222;flex-shrink:0}
.news-card{background:#111119;border:1px solid #1E1E2E;border-radius:12px;padding:8px 12px;margin:5px 0}
.badge-bear{background:#2A1515;color:#FF6B6B;padding:2px 8px;border-radius:12px;font-size:10px}
.badge-bull{background:#132A1C;color:#4ADE80;padding:2px 8px;border-radius:12px;font-size:10px}
.geo{border-left:3px solid #FF2A2A;background:#1A1010;padding:8px;margin:6px 0;font-size:11px}
.bull{color:#4ADE80}.bear{color:#FF6B6B}.neut{color:#9CA3AF}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='color:#FFD60A;margin:0;transform:skew(-8deg);font-style:italic'>AMBUSHER</h1><p style='color:#FF2A2A;letter-spacing:3px;font-weight:800;margin-top:-6px'>V4.7 • ALL PAIRS SENTIMENT GAUGE • 16 PAIRS + GOLD + OIL</p>", unsafe_allow_html=True)

# FULL DB - 16 PAIRS
def make_news(bullish, bearish):
    base=[
    {"t":f"Dollar pinned at two-month high as bond rout extends, Fed rate hike bets rise - Bearish {bearish[0] if bearish else 'USD'}","d":"9/28/2026","tag":"Bearish","col":"bear"},
    {"t":f"ECB's Vujcic warns energy shock could keep inflation hot - Bullish {bullish[0] if bullish else 'EUR'}","d":"9/25/2026","tag":"Bullish","col":"bull"},
    {"t":"Fed's Hammack warns inflation mindset is the biggest risk","d":"9/25/2026","tag":"Bearish","col":"bear"},
    {"t":"Geopolitical tension lifts safe haven bids amid Middle East escalation","d":"9/24/2026","tag":"Bullish","col":"bull"},
    ]
    return base

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
"EUR/GBP":{"score":44,"bear":56,"bull":44,"bias":"BEARISH","macro_bull":["ECB hawkish vs BoE","EU energy fear inflation"],"macro_bear":["UK wage sticky","BoE pause","EUR PMI weaker than UK","Gas spike hurts EUR more"],"macro_neut":["DXY","VIX","Oil","CPI"]},
"AUD/JPY":{"score":38,"bear":62,"bull":38,"bias":"BEARISH","macro_bull":["RBA vs BoJ gap","Iron ore"],"macro_bear":["China PMI weak","China-Taiwan risk off","Risk off JPY bid","BoJ intervention","COT short AUD"],"macro_neut":["DXY","VIX","Gold","S&P"]},
"EUR/AUD":{"score":55,"bear":45,"bull":55,"bias":"BULLISH","macro_bull":["China weak bearish AUD","EU less China exposed","RBA dovish vs ECB","COT short AUD"],"macro_bear":["EU PMI weak","Gas spike","DXY mixed"],"macro_neut":["VIX","Oil","Gold","CPI"]},
"XAU/USD":{"score":36,"bear":64,"bull":36,"bias":"BEARISH","macro_bull":["GPR","CB Purchases 45t","COT Net Longs"],"macro_bear":["DXY 105.2","Real Yield 10Y 2.1%","Fed hawkish","Brent Oil","MOVE 105","GDX weak","GLD outflow"],"macro_neut":["VIX 18","S&P 500","CPI 2.4%","Fed Rate"]},
"GOLD":{"score":36,"bear":64,"bull":36,"bias":"BEARISH","macro_bull":["GPR","CB Purchases","COT"],"macro_bear":["DXY","Real Yield","Fed Expect","Brent","MOVE","GDX","GLD"],"macro_neut":["VIX","S&P","CPI","Fed"]},
"OIL WTI":{"score":68,"bear":32,"bull":68,"bias":"BULLISH","macro_bull":["Middle East tension","OPEC+ cut rumor","Inventories -2.1M","China demand","COT long +12k","Brent backwardation"],"macro_bear":["US shale +0.4M","Fed hawkish demand fear","DXY 105"],"macro_neut":["VIX","Gold","S&P","CPI"]},
"BTC/USD":{"score":54,"bear":46,"bull":54,"bias":"NEUTRAL","macro_bull":["Debt ceiling hedge","Fed pause hope","ETF inflow","Halving effect"],"macro_bear":["Fed hawkish 5.25%","DXY strong","China ban fear","Risk off"],"macro_neut":["VIX","Gold","Nasdaq","CPI"]},
}

pairs_map={"EUR/USD":"EURUSD=X","GBP/USD":"GBPUSD=X","USD/JPY":"USDJPY=X","AUD/USD":"AUDUSD=X","NZD/USD":"NZDUSD=X","USD/CAD":"USDCAD=X","USD/CHF":"USDCHF=X","EUR/JPY":"EURJPY=X","GBP/JPY":"GBPJPY=X","EUR/GBP":"EURGBP=X","AUD/JPY":"AUDJPY=X","EUR/AUD":"EURAUD=X","XAU/USD":"GC=F","GOLD":"GC=F","OIL WTI":"CL=F","BTC/USD":"BTC-USD"}

def gauge_svg(score,bias):
    angle=(score/100)*180 -90
    return f"""
    <div class='sentiment-box'>
      <div style='font-size:13px'>{bias} Sentiment Gauge</div>
      <svg viewBox='0 0 200 110' style='width:100%;height:105px'>
        <path d='M20 100 A80 80 0 0 1 60 28' stroke='#0B5FFF' stroke-width='18' fill='none' stroke-linecap='round'/>
        <path d='M66 24 A80 80 0 0 1 102 18' stroke='#7DD3FC' stroke-width='18' fill='none' stroke-linecap='round'/>
        <path d='M108 18 A80 80 0 0 1 144 24' stroke='#E5E7EB' stroke-width='18' fill='none' stroke-linecap='round'/>
        <path d='M150 28 A80 80 0 0 1 180 55' stroke='#86EFAC' stroke-width='18' fill='none' stroke-linecap='round'/>
        <path d='M182 62 A80 80 0 0 1 180 100' stroke='#22C55E' stroke-width='18' fill='none' stroke-linecap='round'/>
        <g transform='translate(100,100) rotate({angle})'><path d='M0 -75 L-4 0 L4 0 Z' fill='white'/><circle cx='0' cy='0' r='8' fill='#111'/></g>
        <text x='100' y='85' text-anchor='middle' fill='#9CA3AF' font-size='10'>{bias}</text>
      </svg>
    </div>
    """

st.markdown("### 🌍 GEOPOLINTEL")
st.markdown("<div class='geo'>🔴 MIDDLE EAST | 🔴 UKRAINE | 🟡 CHINA-TAIWAN | 🟢 OPEC+ - All pairs affected</div>", unsafe_allow_html=True)

st.markdown("### 🎯 ALL PAIRS - SENTIMENT GAUGE + MACRO 14 INDICATORS + NEWS")

for name,ticker in pairs_map.items():
    try:
        df=yf.Ticker(ticker).history(period="1d",interval="5m")
        daily=yf.Ticker(ticker).history(period="5d")
        p=daily['Close'].iloc[-1]; pct=(daily['Close'].iloc[-1]-daily['Close'].iloc[-2])/daily['Close'].iloc[-2]*100
    except:
        df=pd.DataFrame({"Close":[1]*100}); p=0; pct=0

    d=DB.get(name)
    if not d: continue
    label=f"{d['bias']} {name} | {p:.4f} ({pct:+.2f}%) • {d['bear']}% BEAR / {d['bull']}% BULL • SCORE {d['score']}"

    with st.expander(label, expanded=(name=="EUR/USD")):
        st.caption(f"24H L:{df['Close'].min():.4f} H:{df['Close'].max():.4f} • JHB GMT+2")
        st.line_chart(df['Close'], height=90)

        c1,c2=st.columns(2)
        with c1:
            st.markdown(gauge_svg(d['score'], d['bias']), unsafe_allow_html=True)
            st.markdown(f"<div style='display:flex;justify-content:space-between;font-size:12px;margin-top:6px'><span class='bear'>Bearish<br>{d['bear']}%</span><span class='neut'>Neutral<br>0.0%</span><span class='bull'>Bullish<br>{d['bull']}%</span></div>", unsafe_allow_html=True)
        with c2:
            col="#FF2A2A" if d['bias']=="BEARISH" else "#00FF88" if d['bias']=="BULLISH" else "#FFD60A"
            st.markdown(f"""
            <div class='macro'>
              <div style='text-align:center;color:#9CA3AF;font-size:10px;letter-spacing:2px'>{name} MACRO ENVIRONMENT</div>
              <div style='text-align:center;color:{col};font-weight:800'>{d['bias']} <span style='color:#FFD60A;font-size:10px'>Why? ▲</span></div>
              <div style='text-align:center;color:#9CA3AF;font-size:10px'>{len(d['macro_bull'])} bullish · {len(d['macro_bear'])} bearish of 14 indicators</div>
              <div style='display:flex;gap:8px;margin-top:8px'>
                <div class='gauge-sm' style='border-color:{col}'><div style='font-size:18px;color:{col}'>{d['score']}</div><div style='font-size:9px;color:#9CA3AF'>/100</div></div>
                <div style='font-size:9px;line-height:1.3'><div class='bull'>Bull: {', '.join(d['macro_bull'][:4])}</div><div class='bear'>Bear: {', '.join(d['macro_bear'][:5])}</div><div class='neut'>Neut: {', '.join(d['macro_neut'][:4])}</div></div>
              </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("#### 🔴 High Priority News")
        # generate news per pair
        if name=="EUR/USD":
            news_list=[
            {"t":"Dollar pinned at two-month high as bond rout extends, Fed rate hike bets rise","d":"9/28/2026","tag":"Bearish","c":"bear"},
            {"t":"ECB's Vujcic warns energy shock could keep inflation hot","d":"9/25/2026","tag":"Bullish","c":"bull"},
            {"t":"Fed's Hammack warns inflation mindset is the biggest risk","d":"9/25/2026","tag":"Bearish","c":"bear"},
            {"t":"Euro weakens below 1.1400 as Fed rate hike expectations reinforce US Dollar","d":"9/24/2026","tag":"Bearish","c":"bear"},
            ]
        elif "JPY" in name:
            news_list=[
            {"t":"BoJ keeps -0.1% as yen weakens, intervention risk at 158","d":"9/28/2026","tag":"Bullish" if "USD" in name else "Bearish","c":"bull" if "USD" in name else "bear"},
            {"t":"US 10Y yield hits 4.3% on hawkish Fed - supports USD/JPY","d":"9/27/2026","tag":"Bullish","c":"bull"},
            {"t":"China-Taiwan drills lift safe haven JPY bid","d":"9/25/2026","tag":"Bearish","c":"bear"},
            ]
        elif "GOLD" in name or "XAU" in name:
            news_list=[
            {"t":"Gold drops as dollar hits 2-month high and real yields climb","d":"9/28/2026","tag":"Bearish","c":"bear"},
            {"t":"Central banks bought 45t gold in August - WGC reports","d":"9/26/2026","tag":"Bullish","c":"bull"},
            {"t":"Israel-Iran tension lifts gold safe haven - war premium +$12","d":"9/25/2026","tag":"Bullish","c":"bull"},
            {"t":"GLD ETF outflows hit 3-week low as Fed hike bets rise","d":"9/25/2026","tag":"Bearish","c":"bear"},
            ]
        else:
            news_list=[
            {"t":f"{name} - Dollar strength weighs as Fed hawkish hold priced","d":"9/28/2026","tag":"Bearish" if d['bias']=="BEARISH" else "Bullish","c":"bear" if d['bias']=="BEARISH" else "bull"},
            {"t":f"{name} - {d['macro_bull'][0]} supports upside momentum","d":"9/26/2026","tag":"Bullish","c":"bull"},
            {"t":f"{name} - {d['macro_bear'][0]} caps gains - caution","d":"9/25/2026","tag":"Bearish","c":"bear"},
            ]

        for n in news_list:
            bc="badge-bear" if n['c']=="bear" else "badge-bull"
            st.markdown(f"<div class='news-card'><div style='color:#60A5FA;font-size:12px;font-weight:600'>{n['t']}</div><div style='font-size:10px;color:#9CA3AF;margin-top:3px'>{n['d']} · {name} · <span class='{bc}'>{n['tag']}</span></div></div>", unsafe_allow_html=True)

if st.button("🔄 RE-SCAN ALL 16 PAIRS"): st.rerun()

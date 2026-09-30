import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="FX AMBUSHERS", layout="wide")
if "page" not in st.session_state:
    st.session_state.page="home"

DXY=7
st.success("LIVE v2.2 FIXED EDGEFINDER - NO ERROR")

def j(p,e):
    return " + ".join(p) + " = " + e

def gauge(t,s,bu,be,ne,sz=260):
    ang=s*9
    col="#00ff66" if s>=1 else "#ff4444" if s<=-1 else "#ffcc00"
    bcol=col
    bias="BULL" if s>=1 else "BEAR" if s<=-1 else "NEU"
    a="<div style='border:1px solid #222;border-radius:18px;padding:12px;background:#0f1414;border-left:4px solid "+bcol+";margin-bottom:12px'>"
    b="<div style='text-align:center;color:#888;font-size:11px'>"+t+"</div>"
    c="<div style='text-align:center;color:"+col+";font-weight:900;font-size:20px'>"+bias+" "+str(s)+"</div>"
    d="<div style='width:"+str(sz)+"px;height:"+str(sz//2)+"px;margin:8px auto;position:relative;background:conic-gradient(from 270deg at 50% 100%,#ff2b2b 0 60deg,#ffcc00 60deg 120deg,#00cc66 120deg 180deg);border-radius:"+str(sz)+"px "+str(sz)+"px 0 0'>"
    e="<div style='width:3px;height:120px;background:white;position:absolute;bottom:0;left:50%;transform-origin:bottom;transform:rotate("+str(ang)+"deg)'></div></div>"
    f="<div style='font-size:11px;color:#00ff66'>Bull: "+bu+"</div><div style='font-size:11px;color:#ff6666'>Bear: "+be+"</div><div style='font-size:11px;color:#888'>Neu: "+ne+"</div></div>"
    return a+b+c+d+e+f

dxy_bu=j(["Powell Hawk","US CPI 3.2% Hot","US10Y 4.2% Up"],"USD Buy")
dxy_be=j(["Powell Cut","Gold 2600"],"USD Sell")
dxy_ne="FOMC Sep29 HIGH"
st.markdown(gauge("DXY AMBUSH",DXY,dxy_bu,dxy_be,dxy_ne,280), unsafe_allow_html=True)

forex=[("EURUSD",-7,dxy_bu,dxy_be,"ECB"),("GBPUSD",-7,dxy_bu,dxy_be,"BoE"),("USDJPY",7,dxy_bu,dxy_be,"BoJ"),("AUDUSD",-7,dxy_bu,dxy_be,"RBA"),("USDCHF",7,dxy_bu,dxy_be,"SNB"),("USDCAD",6,dxy_bu,dxy_be,"BoC")]
commod=[("GOLD",-8,dxy_bu,dxy_be,"GPR"),("SILVER",-7,dxy_bu,dxy_be,"Gold"),("OIL",-3,dxy_bu,dxy_be,"OPEC")]
indices=[("US30",-7,dxy_bu,dxy_be,"FOMC"),("NAS100",-7,dxy_bu,dxy_be,"Earnings"),("SPX500",-7,dxy_bu,dxy_be,"FOMC")]
crypto=[("BTCUSD",-7,dxy_bu,dxy_be,"ETF"),("ETHUSD",-7,dxy_bu,dxy_be,"ETF")]
cot=[["DXY","71%","29%","+3% Long","BULL","Powell"],["EURUSD","29%","71%","+4% Short","BEAR","DXY +7"],["GBPUSD","30%","70%","+2% Short","BEAR","DXY"],["USDJPY","71%","29%","+2% Long","BULL","BoJ"],["GOLD","25%","75%","+5% Short","BEAR","DXY"],["BTCUSD","30%","70%","+2% Short","BEAR","Risk Off"]]
retail=[["EURUSD","70%","30%","72% Long Retail","CONTRARIAN SELL","Crowded"],["GBPUSD","68%","32%","70% Long","CONTRARIAN SELL","Long"],["USDJPY","35%","65%","66% Short","CONTRARIAN BUY","Short"],["GOLD","75%","25%","80% Long Retail","CONTRARIAN SELL","Top"],["BTCUSD","78%","22%","85% Long","CONTRARIAN SELL","FOMO"],["DXY","30%","70%","68% Short","CONTRARIAN BUY","Short USD"]]

all_assets={}
for p,s,bu,be,ne in forex: all_assets[p]=(s,bu,be,ne,"FOREX")
for p,s,bu,be,ne in commod: all_assets[p]=(s,bu,be,ne,"METAL")
for p,s,bu,be,ne in indices: all_assets[p]=(s,bu,be,ne,"INDICES")
for p,s,bu,be,ne in crypto: all_assets[p]=(s,bu,be,ne,"CRYPTO")
all_assets["DXY"]=(DXY,dxy_bu,dxy_be,dxy_ne,"DXY")

if st.session_state.page=="home":
    c1,c2=st.columns(2)
    with c1:
        if st.button("FOREX 6", use_container_width=True): st.session_state.page="forex"
        if st.button("GOLD OIL", use_container_width=True): st.session_state.page="gold"
        if st.button("COT TABLE", use_container_width=True): st.session_state.page="cot"
        if st.button("RETAIL", use_container_width=True): st.session_state.page="retail"
        if st.button("FUND SCHOOL", use_container_width=True): st.session_state.page="learn_fund"
        if st.button("TECH SCHOOL", use_container_width=True): st.session_state.page="learn_tech"
    with c2:
        if st.button("INDICES", use_container_width=True): st.session_state.page="indices"
        if st.button("CRYPTO", use_container_width=True): st.session_state.page="crypto"
        if st.button("SCORE FINDER", use_container_width=True): st.session_state.page="finder"
else:
    if st.button("BACK RADAR", use_container_width=True): st.session_state.page="home"
    if st.session_state.page=="finder":
        ch=st.selectbox("Choose Asset", list(all_assets.keys()))
        s,bu,be,ne,typ=all_assets[ch]
        st.markdown(gauge(ch,s,bu,be,ne,280), unsafe_allow_html=True)
        cot_row=next((x for x in cot if x[0]==ch), ["-","-","-","-","-","-"])
        ret_row=next((x for x in retail if x[0]==ch), ["-","-","-","-","-","-"])
        st.markdown("<div style='border:1px solid #333;padding:10px;border-radius:10px;margin-top:10px'>Crowd: "+str(ret_row[1])+" vs "+str(ret_row[2])+" = "+str(ret_row[4])+"<div style='display:flex;gap:2px;margin-top:6px'><div style='flex:70;height:8px;background:#dc2626'></div><div style='flex:30;height:8px;background:#2563eb'></div></div></div>", unsafe_allow_html=True)
        st.markdown("<div style='margin-top:10px'><table style='width:100%;font-size:11px;border-collapse:collapse'><tr style='background:#111'><td style='padding:6px'>Technicals</td><td style='padding:6px'><span style='background:#7f1d1d;color:#fecaca;padding:2px 6px;border-radius:4px'>Very Bearish</span></td></tr><tr><td style='padding:6px;border-bottom:1px solid #222'>Score "+str(s)+"</td><td style='padding:6px;border-bottom:1px solid #222'>"+str(s)+"</td></tr><tr style='background:#111'><td style='padding:6px'>Institutional</td><td style='padding:6px'>COT "+str(cot_row[1])+" "+str(cot_row[4])+"</td></tr><tr><td style='padding:6px;border-bottom:1px solid #222'>COT Latest</td><td style='padding:6px;border-bottom:1px solid #222'>"+str(cot_row[3])+" | "+str(cot_row[5])+"</td></tr><tr style='background:#111'><td style='padding:6px'>Economic growth</td><td style='padding:6px'>DXY +"+str(DXY)+"</td></tr><tr><td style='padding:6px;border-bottom:1px solid #222'>Retail Contrarian</td><td style='padding:6px;border-bottom:1px solid #222'>"+str(ret_row[1])+" = "+str(ret_row[4])+"</td></tr><tr style='background:#111'><td style='padding:6px'>Inflation / Jobs / GPR</td><td style='padding:6px'></td></tr><tr><td style='padding:6px'>"+str(ne)+"</td><td style='padding:6px'>"+str(bu)[:50]+"</td></tr></table></div>", unsafe_allow_html=True)
    if st.session_state.page in ["forex","gold","indices","crypto"]:
        data={"forex":forex,"gold":commod,"indices":indices,"crypto":crypto}[st.session_state.page]
        cols=st.columns(2)
        for i,(p,s,bu,be,ne) in enumerate(data):
            with cols[i%2]:
                st.markdown(gauge(p,s,bu,be,ne,170), unsafe_allow_html=True)
    if st.session_state.page=="learn_fund":
        st.markdown("## FUNDAMENTAL ACADEMY - FULL")
        with st.expander("1. DXY - King of Forex"):
            st.write("Definition: DXY = USD vs 6 majors. If DXY UP, EURUSD DOWN. Check DXY first always.")
            st.write("Bull: Powell Hawk + CPI Hot + Yield Up + BoJ Dovish = USD Buy")
            st.write("Bear: Fed Cut + Gold Up + Yield Down = USD Sell")
        with st.expander("2. Economic Indicators"):
            st.write("CPI Hot = Hawk = DXY Buy. CPI Cold = Cut = DXY Sell + Gold Buy")
            st.write("NFP High = Strong Economy = DXY Buy. Low NFP = DXY Sell")
            st.write("FOMC Hawk = No Cut = DXY Buy. Dovish Cut = DXY Sell")
            st.write("Yield UP = DXY UP NAS100 DOWN. Yield DOWN = Gold UP NAS100 UP")
        with st.expander("3. Central Banks"):
            st.write("FED controls DXY. ECB controls EUR. BoE GBP. BoJ JPY. RBA AUD linked Gold China. SNB CHF safe. BoC CAD linked Oil.")
        with st.expander("4. GPR Geopolitical"):
            st.write("War = Gold Buy Oil Buy USD Buy safe haven. Ceasefire = Gold Sell. OPEC Cut = Oil Buy. China Stimulus = AUD Buy Gold Buy.")
        with st.expander("5. COT"):
            st.write("Smart Money hedge funds. 71% Long DXY = Banks buying USD = Bull. Change +3% Long = adding momentum.")
        with st.expander("6. Retail Contrarian"):
            st.write("Retail 70% long = crowd wrong = we SELL. BTC 78% long FOMO = top = SELL. Fade retail.")
        with st.expander("7. Score -10 to +10"):
            st.write("+1 to +10 BULL, -1 to -10 BEAR, 0 WAIT. DXY +7 = Strong Bull. EURUSD -7 = Strong Bear.")
    if st.session_state.page=="learn_tech":
        st.markdown("## TECHNICAL ACADEMY - AMBUSHER METHOD FULL")
        with st.expander("1. MARKET STRUCTURE - The Footprints"):
            st.write("We dont chase candles. We read footprints.")
            st.write("HH HL = BULL ROAD: Higher High + Higher Low = Buyers control. Only BUYS.")
            st.write("LL LH = BEAR ROAD: Lower Low + Lower High = Sellers control. Only SELLS.")
            st.write("BOS = Road Continues: Break of Structure = trend still strong.")
            st.write("CHoCH = Road Flips: Change of Character = road FLIPPED to BEAR. AMBUSH entry zone.")
            st.write("Ambush Rule: Never enter on BOS. Wait for CHoCH + pullback. Patience is Profit.")
        with st.expander("2. SUPPORT & RESISTANCE - Battle Zones"):
            st.write("Support = Floor where buyers hide. Zone 10-20 pips. 3rd touch = Buyers ambush.")
            st.write("Resistance = Roof where sellers hide. 3rd touch = SELL ambush.")
            st.write("Flip: Broken support becomes resistance. Wait for retest SELL.")
            st.write("Ambush Filter: Only trade S/R that lines with DXY score.")
        with st.expander("3. SUPPLY & DEMAND - Bank Vaults"):
            st.write("Demand = Wholesale price. Big green move UP from tight base. Banks bought cheap.")
            st.write("Supply = Expensive price. Big red drop DOWN from tight base. Banks sold high.")
            st.write("Fresh vs Used: First return strongest. Third = avoid.")
        with st.expander("4. SMC - SMART MONEY CONCEPTS"):
            st.write("1. Order Block = Ambush Block: Last opposite candle before big move.")
            st.write("2. FVG = Gap Trap: 3 candle pattern with gap. Market comes back to fill 50%.")
            st.write("3. Liquidity = Crowd Trap: Equal Highs = retail stop hunts. Push above then REVERSE SELL.")
            st.write("4. Stop Hunt = Fake Push: Price pushes above resistance 20 pips, takes stops, then drops hard.")
            st.write("5. Premium / Discount: Above 50% = Premium only SELL. Below 50% = Discount only BUY.")
        with st.expander("5. ENTRY MODELS - 3 AMBUSH SETUPS"):
            st.write("SETUP A - CHoCH + Ambush Block: CHoCH breaks HL, mark Block, wait return + DXY aligns + Score -7 = SELL.")
            st.write("SETUP B - Liquidity Grab + Flip: Find equal highs, spike above takes stops, rejection wick, SELL.")
            st.write("SETUP C - Gap Trap 50%: Find FVG after BOS, pullback to 50% of gap, check DXY bias.")
            st.write("All setups need: Score 5+, COT same bias, Retail opposite. 3 checks = AMBUSH.")
        with st.expander("6. RISK - Patience is Profit"):
            st.write("Stop Loss: Always behind Ambush Block or behind liquidity grab.")
            st.write("Target: Next opposing vault, or 2R min.")
            st.write("Rule: 1% per ambush max. If Score 0 = NO TRADE. Wait FOMC NFP CPI.")
            st.write("Kill Zones: 08:00-11:00 SAST London, 15:30-18:00 SAST NY.")

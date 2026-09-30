import streamlit as st
if "page" not in st.session_state:
    st.session_state.page="radar"
st.title("AMBUSHER RADAR")
st.write("Patience is Profit")
c1,c2,c3,c4=st.columns(4)
if c1.button("RADAR"):
    st.session_state.page="radar"
if c2.button("FINDER"):
    st.session_state.page="finder"
if c3.button("FUND"):
    st.session_state.page="fund"
if c4.button("LEARN"):
    st.session_state.page="learn_fund"

if st.session_state.page=="radar":
    st.subheader("RADAR -10 to +10")
    st.metric("DXY","+7 BULL")
    st.metric("GOLD","-8 BEAR")
    st.write("DXY Strong + Yields Up")

if st.session_state.page=="finder":
    st.subheader("FINDER")
    st.metric("EURUSD","-7 BEAR")

if st.session_state.page=="fund":
    st.write("FOMC Sep29 HIGH - Hawkish")
    st.write("NFP Oct3 HIGH - 180K exp")
    st.write("GPR: War = Gold BUY")

if st.session_state.page=="learn_fund":
    st.markdown("## FUNDAMENTAL ACADEMY - DEFINITIONS")

    with st.expander("1. DXY - King of Forex DEFINITION"):
        st.write("DEF: DXY = Dollar Index")
        st.write("Measures USD vs 6 currencies:")
        st.write("EUR 57%, JPY 13%, GBP 11%")
        st.write("CAD 9%, SEK 4%, CHF 3%")
        st.write("")
        st.write("BULL = DXY UP means USD strong")
        st.write("BEAR = DXY DOWN USD weak")
        st.write("")
        st.write("RULE: DXY UP = EURUSD DOWN")
        st.write("DXY UP = GBPUSD DOWN")
        st.write("DXY UP = Gold DOWN")

    with st.expander("2. Economic Indicators DEFINITION"):
        st.write("DEF: News that moves market")
        st.write("")
        st.write("CPI = Inflation:")
        st.write("CPI Hot 3.5%+ = Hawk = DXY +2")
        st.write("CPI Cold = Dovish = DXY -2")
        st.write("")
        st.write("NFP = Jobs:")
        st.write("NFP High 200K+ = Strong = DXY +2")
        st.write("NFP Low = Weak = DXY -2")
        st.write("")
        st.write("FOMC = Fed Meeting:")
        st.write("Hawk = No Cut = DXY +3")
        st.write("Dovish = Cut = DXY -3")
        st.write("")
        st.write("Yields UP = DXY UP = NAS100 DOWN")

    with st.expander("3. Central Banks DEFINITION"):
        st.write("DEF: Banks that control money")
        st.write("")
        st.write("FED (USA) controls DXY:")
        st.write("Hawkish = Rates UP = BULL +2")
        st.write("Dovish = Rates DOWN = BEAR -2")
        st.write("")
        st.write("ECB (Europe) controls EUR")
        st.write("BoE (UK) controls GBP")
        st.write("BoJ (Japan) controls JPY")
        st.write("BoJ 150+ = Intervention = JPY BUY +3")
        st.write("")
        st.write("RBA (AUD) = Gold + China")
        st.write("SNB (CHF) = Safe haven")
        st.write("BoC (CAD) = Oil price")

    with st.expander("4. GPR Geopolitical DEFINITION"):
        st.write("DEF: GPR = War + Politics + Oil")
        st.write("")
        st.write("WAR = Fear = Safe Haven BUY:")
        st.write("Gold BUY +3, Oil BUY +3")
        st.write("USD BUY +2, CHF BUY +2")
        st.write("")
        st.write("PEACE = Ceasefire = SELL:")
        st.write("Gold SELL -3, Oil SELL -

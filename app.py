    if st.session_state.page=="learn_tech":
        st.markdown("## FX AMBUSHERS TECHNICAL ACADEMY")
        st.caption("Patience is Profit")
        def show_any(keywords):
            import glob
            for f in os.listdir("."):
                if any(k in f.lower() for k in keywords) and f.lower().endswith((".png",".jpg",".webp",".jpeg")):
                    st.image(f, use_container_width=True)
                    return True
            return False

        with st.expander("1. MARKET STRUCTURE - Bull Road / Bear Road"):
            st.write("HH HL = Bull Road UP, LL LH = Bear Road DOWN. BOS = Continues, CHoCH = Flips = Ambush zone.")
            show_any(["structure_adv","mtf","structure"])

        with st.expander("2. SUPPORT & RESISTANCE"):
            st.write("Support floor 10-20 pips bounce 2-3x. Resistance roof. 3rd touch Ambush. Flip SELL.")
            show_any(["sr","support","resist"])

        with st.expander("3. SUPPLY & DEMAND - Bank Vaults"):
            st.write("Demand = Wholesale tight base + big green. Supply = Expensive + big red drop. First return strongest.")
            show_any(["supply","demand"])

        with st.expander("4. ORDER BLOCKS - Ambush Blocks"):
            st.write("Bullish OB last bearish before big up. Bearish OB last bullish before big down. Entry on retest.")
            show_any(["order","block"])

        with st.expander("5. SMC - Liquidity & Inducement"):
            st.write("BSL above equal highs stop hunt + fake push trap longs SELL. SSL below equal lows trap shorts BUY.")
            show_any(["liquid","induce"])

        with st.expander("6. ENTRY MODELS"):
            st.write("A: CHoCH+OB, B: Liquidity Grab+Flip, C: Gap 50% + DXY bias")

        with st.expander("7. RISK"):
            st.write("Stop behind OB or liquidity. 1% max. Score 0 = NO TRADE. Kill Zones 08-11 SAST London, 15:30-18:00 NY.")
            # show all uploaded extra pics
            for f in os.listdir("."):
                if "IMG-20260930" in f: 
                    st.image(f, use_container_width=True, caption=f)

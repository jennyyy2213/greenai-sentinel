import streamlit as st


def hotspot_panel():

    st.subheader("🔥 Global Climate Risk Hotspots")

    hotspots = [
        ("Arctic", "High", "Rapid ice loss detected"),
        ("Amazon Basin", "Moderate", "Forest moisture decline"),
        ("Antarctica", "High", "Ice shelf instability signals"),
        ("North Atlantic", "Watch", "Circulation weakening signals"),
        ("Coral Triangle", "Moderate", "Ocean heat stress rising")
    ]

    for region, risk, note in hotspots:

        col1, col2, col3 = st.columns([2, 1, 3])

        col1.write(region)
        col2.write(risk)
        col3.write(note)

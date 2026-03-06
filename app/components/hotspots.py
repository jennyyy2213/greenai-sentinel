import streamlit as st
import pandas as pd


def hotspot_panel():

    st.header("🔥 Global Climate Risk Hotspots")

    data = {
        "Region": [
            "Indian Monsoon Zone",
            "Amazon Rainforest",
            "Arctic Sea Ice",
            "Coral Triangle",
            "West Antarctic Ice Sheet"
        ],
        "Risk Score": [0.42, 0.68, 0.74, 0.51, 0.63],
        "Status": [
            "Watch",
            "Elevated",
            "High Risk",
            "Watch",
            "Elevated"
        ]
    }

    df = pd.DataFrame(data)

    st.dataframe(df, use_container_width=True)

    st.write("""
    AI ranks regions based on instability indicators derived from climate signals.
    Higher scores indicate approaching tipping behavior.
    """)

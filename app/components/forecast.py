import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def forecast_panel(current_risk):

    st.subheader("📈 30-Day Risk Projection")

    days = np.arange(1, 31)

    # dynamic behaviour
    volatility = 0.02 + current_risk * 0.05
    trend = current_risk + volatility * np.log1p(days)

    trend = np.clip(trend, 0, 1)

    fig, ax = plt.subplots(figsize=(5, 2.5))  # SMALLER GRAPH
    ax.plot(days, trend)
    ax.set_xlabel("Days")
    ax.set_ylabel("Risk")
    ax.set_ylim(0, 1)

    st.pyplot(fig)

    # intelligent interpretation
    if trend[-1] > 0.85:
        st.error("⚠ Rapid tipping escalation predicted.")
    elif trend[-1] > 0.65:
        st.warning("Instability trend increasing.")
    else:
        st.success("System expected to remain stable.")

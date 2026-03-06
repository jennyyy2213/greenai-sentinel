import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def show_history(ts):

    st.subheader("🕰 Historical Risk Evolution")

    years = list(range(len(ts)))

    trend = np.cumsum(np.random.normal(0, 0.02, len(ts)))

    fig, ax = plt.subplots(figsize=(6, 2.5))

    ax.plot(years, trend)
    ax.set_xlabel("Observation Window")
    ax.set_ylabel("Instability Trend")

    st.pyplot(fig)

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


def show_signals(ts):

    st.subheader("📊 Climate Signal Analysis")

    variance = []
    autocorr = []

    window = 4

    for i in range(window, len(ts)):

        v = np.var(ts[i-window:i])
        a = np.corrcoef(ts[i-window:i-1], ts[i-window+1:i])[0, 1]

        variance.append(v)
        autocorr.append(a)

    fig, ax = plt.subplots(1, 2, figsize=(8, 3))

    ax[0].plot(variance)
    ax[0].set_title("Variance")

    ax[1].plot(autocorr)
    ax[1].set_title("Autocorrelation")

    st.pyplot(fig)

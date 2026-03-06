import numpy as np
import streamlit as st
import xarray as xr


@st.cache_resource
def load_dataset():
    return xr.open_dataset("data/raw/data_stream-oper_stepType-instant.nc")


def analyze_location(lat, lon):

    ds = load_dataset()

    temp = ds["t2m"] - 273.15

    # find nearest grid cell
    region = temp.sel(
        latitude=lat,
        longitude=lon,
        method="nearest"
    )

    ts = region.values

    # Early warning signals
    window = 4

    if len(ts) < window:
        return 0.3, 0.0, 0.0

    variance = np.var(ts[-window:])
    autocorr = np.corrcoef(ts[-window:-1], ts[-window+1:])[0, 1]

    # risk estimation
    # normalize signals (critical fix)
    variance_norm = variance / (variance + 5)
    autocorr_norm = (autocorr + 1) / 2  # map [-1,1] → [0,1]

    risk = 0.5 * variance_norm + 0.5 * autocorr_norm
    risk = float(np.clip(risk, 0, 1))

    return risk, variance, autocorr, ts

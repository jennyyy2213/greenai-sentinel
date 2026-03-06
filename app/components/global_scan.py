import numpy as np
import xarray as xr
import random

DATA_PATH = "data/raw/data_stream-oper_stepType-instant.nc"


def run_global_scan():

    ds = xr.open_dataset(DATA_PATH)
    temp = ds["t2m"] - 273.15

    # random spatial sampling instead of grid lines
    candidate_points = [
        (random.uniform(-60, 70), random.uniform(-180, 180))
        for _ in range(120)
    ]

    hotspots = []

    for lat, lon in candidate_points:

        region = temp.sel(latitude=lat,
                          longitude=lon,
                          method="nearest")

        ts = region.values

        if len(ts) < 4:
            continue

        variance = np.var(ts[-4:])
        autocorr = np.corrcoef(ts[-4:-1], ts[-3:])[0, 1]

        # normalization
        variance_norm = variance/(variance+5)
        autocorr_norm = (autocorr+1)/2

        risk = 0.5*variance_norm + 0.5*autocorr_norm

        # keep only strong signals
        if risk > 0.72:
            hotspots.append((lat, lon, float(risk)))

    # keep only top hotspots
    hotspots = sorted(hotspots, key=lambda x: x[2], reverse=True)[:12]

    return hotspots

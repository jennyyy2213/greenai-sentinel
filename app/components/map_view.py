import streamlit as st
import folium
from streamlit_folium import st_folium
from components.forecast import forecast_panel
from components.real_analysis import analyze_location
from components.global_scan import run_global_scan
from components.impact_analysis import show_impacts
from components.signal_viewer import show_signals
from components.history_analysis import show_history


def render_map():
    st.metric(
        "🌍 Earth Stability Index",
        "0.62",
        "Status: WATCH"
        )
    monitor = st.toggle("🛰 Continuous Earth Monitoring")

    if monitor:

        if "auto_scan" not in st.session_state:
            st.session_state["auto_scan"] = run_global_scan()

        ai_hotspots = st.session_state["auto_scan"]

    else:

        ai_hotspots = st.session_state.get("ai_hotspots", [])
    st.subheader("Global Climate Risk Explorer")
    st.subheader("🌍 Global AI Scan")
    # ensure session state exists
    if "ai_hotspots" not in st.session_state:
        st.session_state["ai_hotspots"] = []
    if st.button("Run Global Tipping Scan"):

        with st.spinner("Scanning Earth for instability signals..."):
            st.session_state["ai_hotspots"] = run_global_scan()
    m = folium.Map(location=[20, 0], zoom_start=2)
    # AI detected hotspots
    ai_hotspots = st.session_state.get("ai_hotspots", [])

    for lat, lon, risk in ai_hotspots:

        folium.CircleMarker(
            location=[lat, lon],
            radius=6 + risk*8,
            color="purple",
            fill=True,
            fill_opacity=0.9,
            popup=f"AI Detected Hotspot | Risk {risk:.2f}"
        ).add_to(m)

    # Static high-risk zones (realistic examples)
    hotspots = [
        ("Indian Monsoon", 20, 78, 0.6),
        ("Amazon Basin", -5, -60, 0.75),
        ("Arctic Sea Ice", 70, -40, 0.85),
        ("Coral Triangle", -15, 130, 0.55),
        ("West Antarctica", -75, -100, 0.8)
    ]

    for name, lat, lon, risk in hotspots:

        color = "green"
        if risk > 0.7:
            color = "red"
        elif risk > 0.4:
            color = "orange"

        folium.CircleMarker(
            location=[lat, lon],
            radius=6 + risk*8,
            color=color,
            fill=True,
            fill_opacity=0.8,
            popup=f"{name} | Risk: {risk}"
        ).add_to(m)

    map_data = st_folium(m, width=1000, height=550)

    if map_data["last_clicked"]:

        lat = map_data["last_clicked"]["lat"]
        lon = map_data["last_clicked"]["lng"]

    st.success(f"Analyzing Region at ({lat:.2f}, {lon:.2f})")

    # run real analysis
    risk, variance, autocorr, ts = analyze_location(lat, lon)

    # region classification
    if lat > 60:
        region_name = "Arctic"
    elif lat < -60:
        region_name = "Antarctica"
    elif -15 < lat < 5 and -80 < lon < -40:
        region_name = "Amazon"
    elif -30 < lat < 30:
        region_name = "Ocean"
    else:
        region_name = "Continental Region"

    st.info(f"Detected Region: {region_name}")

    # metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Risk", round(risk, 3))
    col2.metric("Variance", round(variance, 3))
    col3.metric("Autocorrelation", round(autocorr, 3))

    # panels
    show_signals(ts)
    show_history(ts)
    show_impacts(region_name)
    forecast_panel(risk)
    if not map_data["last_clicked"]:
        st.info("Click anywhere on the map to analyze climate instability risk for that region.")
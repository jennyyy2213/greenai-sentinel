import streamlit as st

st.set_page_config(layout="wide")
st.title("🌍 GreenAI Sentinel — Climate Tipping Early Warning System")

st.caption("AI-driven platform for detecting early climate instability signals and forecasting potential tipping events using ERA5 Earth system data.")
tab1, tab2 = st.tabs([
    "🗺 Global Risk Map",
    "🔥 Risk Intelligence"
])

# MAP
with tab1:
    from components.map_view import render_map
    render_map()

# HOTSPOTS + ANALYTICS
with tab2:
    from components.hotspots import hotspot_panel
    hotspot_panel()
with st.expander("🧠 How the AI Works"):

    st.write("""
    This system analyzes real ERA5 climate data to detect early warning signals of tipping behavior.

    The AI evaluates:

    • Variance — increasing climate fluctuations
    • Autocorrelation — slowing recovery after disturbances

    These signals indicate approaching instability in complex climate systems.

    The platform then:
    - estimates tipping risk
    - forecasts future escalation
    - highlights emerging global hotspots
    """)
st.markdown("---")

st.caption(
    "Data Source: Copernicus Climate Data Store (ERA5 Reanalysis) | "
    "Methodology: Early Warning Signal Theory for Tipping Point Detection"
    )

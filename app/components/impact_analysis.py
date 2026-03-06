import streamlit as st


def show_impacts(region_name=None):

    # fallback if region not detected
    if region_name is None:
        region_name = "Unknown Region"

    impacts = {
        "Arctic": [
            "Accelerated sea level rise",
            "Loss of polar ecosystems",
            "Jet stream destabilization",
            "Global temperature amplification"
        ],

        "Amazon": [
            "Rainfall collapse risk",
            "Carbon sink loss",
            "Large scale forest dieback",
            "Regional drought amplification"
        ],

        "Antarctica": [
            "Ice sheet destabilization",
            "Sea level acceleration",
            "Ocean circulation disruption"
        ],

        "Ocean": [
            "Coral bleaching risk",
            "Marine ecosystem collapse",
            "Ocean heat amplification"
        ],

        "Continental Region": [
            "Increased extreme weather",
            "Ecosystem instability",
            "Regional drought risk",
            "Agricultural disruption"
        ]
    }

    st.subheader("🌎 Potential Climate Impacts")

    # find matching region
    if region_name in impacts:

        for impact in impacts[region_name]:
            st.write("•", impact)

    else:
        for impact in impacts["Continental Region"]:
            st.write("•", impact)

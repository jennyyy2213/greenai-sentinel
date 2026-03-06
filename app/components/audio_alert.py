import base64
from gtts import gTTS
import streamlit as st


def speak_alert(message):

    tts = gTTS(message)
    tts.save("alert.mp3")

    audio_file = open("alert.mp3", "rb")
    audio_bytes = audio_file.read()
    b64 = base64.b64encode(audio_bytes).decode()

    autoplay_audio = f"""
        <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
    """

    st.markdown(autoplay_audio, unsafe_allow_html=True)

import streamlit as st
from utils import transcribe_audio, summarize_transcript
import theme
import os

# Streamlit app
st.set_page_config(**theme.page_config)

title = """
    <h1 style="color:#32CD32; font-family:sans-serif;">🎙️ Audio Transcription and Summarization 🎙️</h1>
"""
st.markdown(title, unsafe_allow_html=True)
st.write("Upload an audio file, transcribe it using Whisper, and summarize the transcription using your selected model.")

# Try to get API key from environment variable first
default_api_key = os.environ.get("OPENAI_API_KEY", "")
api_key = st.text_input("Enter your OpenAI API key:", type="password", value=default_api_key)
models = ["gpt-3.5-turbo", "gpt-3.5-turbo-16k", "gpt-4-0613"]
model = st.selectbox("Select a model:", models)

uploaded_audio = st.file_uploader("Upload an audio file", type=['m4a', 'mp3', 'webm', 'mp4', 'mpga', 'wav', 'mpeg'], accept_multiple_files=False)

custom_prompt = st.text_input("Enter a custom prompt:", value="Summarize the following audio transcription:")

if st.button("Generate Summary"):
    if uploaded_audio:
        if api_key:
            st.markdown("Transcribing the audio...")
            transcript = transcribe_audio(api_key, uploaded_audio)
            st.markdown(f"### Transcription:\n\n<details><summary>Click to view</summary><p><pre><code>{transcript}</code></pre></p></details>", unsafe_allow_html=True)

            st.markdown("Summarizing the transcription...")
            summary = summarize_transcript(api_key, transcript, model, custom_prompt)
                
            st.markdown(f"### Summary:")
            st.write(summary)
        else:
            st.error("Please enter a valid OpenAI API key.")
    else:
        st.error("Please upload an audio file.")



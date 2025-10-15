# Meeting Summarizer

Speech Digest is a Streamlit-based application that converts spoken audio into concise written summaries.
It leverages OpenAI’s Whisper ASR for transcription and GPT models for intelligent summarization.

## Features
Upload audio files in supported formats: m4a, mp3, webm, mp4, mpga, wav, mpeg
Transcribe audio using OpenAI Whisper ASR
Summarize transcribed text using GPT-3.5-Turbo or GPT-4
Configure your own OpenAI API key
Simple Streamlit interface, accessible via browser

### Prerequisites

- Python 3.6 or higher
- Streamlit
- OpenAI Python SDK v0.27.0 or higher


## Usage

1. Open the app in your web browser.

2. Enter your OpenAI API key and select the desired model (GPT-4 or GPT-3.5-Turbo).

3. Upload an audio file in a supported format.

4. The app will:

- Transcribe the audio using Whisper ASR.

- Summarize the transcription using the selected GPT model.

5. View or copy the transcription and summary directly within the interface.

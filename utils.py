import os
import tempfile
from openai import OpenAI

def transcribe_audio(api_key, audio_file):
    """
    Transcribe the uploaded audio file using OpenAI Whisper.
    Works for mp3, wav, m4a, etc.
    """
    client = OpenAI(api_key=api_key)
    
    # Get the original filename and extension
    original_filename = audio_file.name
    file_extension = os.path.splitext(original_filename)[1]
    
    # If no extension, default to .mp3
    if not file_extension:
        file_extension = ".mp3"
    
    # Read the file content
    audio_file.seek(0)
    file_content = audio_file.read()
    
    # Create a temporary file with the correct extension
    with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as tmp_file:
        tmp_file.write(file_content)
        tmp_file_path = tmp_file.name
    
    try:
        # Open and transcribe
        with open(tmp_file_path, "rb") as audio_data:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_data
            )
        
        # Return the text - handle both object and string responses
        if hasattr(transcript, 'text'):
            return transcript.text
        else:
            return str(transcript)
    
    except Exception as e:
        # Clean up and re-raise with more info
        if os.path.exists(tmp_file_path):
            os.remove(tmp_file_path)
        raise Exception(f"Transcription failed: {str(e)}")
    
    finally:
        # Clean up temp file
        if os.path.exists(tmp_file_path):
            os.remove(tmp_file_path)


def summarize_transcript(api_key, transcript_text, model="gpt-3.5-turbo", custom_prompt=None):
    """
    Summarize transcript with key decisions and action items.
    """
    client = OpenAI(api_key=api_key)

    if custom_prompt:
        prompt = f"""
        {custom_prompt}
        
        Transcript:
        {transcript_text}
        """
    else:
        prompt = f"""
        Summarize this meeting transcript into:
        1. Key decisions
        2. Action items

        Transcript:
        {transcript_text}
        """

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes meetings."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.5,
        max_tokens=500
    )

    summary = response.choices[0].message.content
    return summary
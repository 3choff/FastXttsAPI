import requests
import json
import os
import pyaudio
import time

SERVER_URL = 'https://localhost:8000'

SPEAKER_NAME = "default_speaker"

text = "Hi there! This is the voice of the default speaker. I am a voice model created by Coqui."
lang = "en"

def tts_stream(text, speaker_name, lang):
    # Load speaker embeddings from JSON file
    with open(os.path.join(f"{speaker_name}.json"), 'r') as f:
        embeddings = json.load(f)

    # Prepare the request payload
    payload = {
        "text": text,
        "language": lang,
        "speaker_embedding": embeddings["speaker_embedding"],
        "gpt_cond_latent": embeddings["gpt_cond_latent"],
        "add_wav_header": True,
        "stream_chunk_size": "20"
    }
    start_time = time.time()
    # Make POST request to tts_stream endpoint
    response = requests.post(
        SERVER_URL + "/tts_stream",
        json=payload,
        stream=True
    )
    response.raise_for_status()
    time_of_first_byte = None
    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open a PyAudio stream
    stream = p.open(format=p.get_format_from_width(2),  # 2 bytes = 16 bits
                    channels=1,
                    rate=24000,
                    output=True)

    # Read and play chunks as they are received
    for chunk in response.iter_content(chunk_size=512):
        if chunk:
            if time_of_first_byte is None:
                time_of_first_byte = time.time()
                print(f"Time to first byte: {(time_of_first_byte - start_time) * 1000} milliseconds")
            stream.write(chunk)

    # Stop the stream
    stream.stop_stream()
    stream.close()

    # Terminate PyAudio
    p.terminate()

# Generate and stream audio for the specified speaker
tts_stream(text, SPEAKER_NAME, lang)
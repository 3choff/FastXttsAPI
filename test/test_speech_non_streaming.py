import requests
import base64

SERVER_URL = 'https://localhost:8000'

SPEAKER_NAME = "Aaron Dreschner"

text = "As the sun dipped below the horizon, a lone lighthouse stood tall, its beam piercing the darkness."
lang = "en"

def tts(text, speaker_name, lang):
    payload = {
        "text": text,
        "language": lang,
        "voice": speaker_name,
    }
    
    response = requests.post(
        SERVER_URL + "/v1/speech",
        json=payload
    )
    response.raise_for_status()

    audio_data = response.content

    # Decode the base64-encoded audio data
    audio_data = base64.b64decode(audio_data)

    # Save the audio data to a file
    with open('output.wav', 'wb') as f:
        f.write(audio_data)

tts(text, SPEAKER_NAME, lang)
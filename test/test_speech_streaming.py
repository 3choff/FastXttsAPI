import requests
import pyaudio
import time

SERVER_URL = 'https://localhost:8000'

SPEAKER_NAME = "Aaron Dreschner"

text = "Hello there! What a beautiful day."
lang = "en"

def tts_stream(text, speaker_name, lang):

    
    payload = {
        "text": text,
        "language": lang,
        "voice": speaker_name,
        "stream":True
    }
    start_time = time.time()
    
    response = requests.post(
        SERVER_URL + "/v1/speech",
        json=payload,   
    )
    response.raise_for_status()
    time_of_first_byte = None
    
    p = pyaudio.PyAudio()

    
    stream = p.open(format=p.get_format_from_width(2),  # 2 bytes = 16 bits
                    channels=1,
                    rate=24000,
                    output=True)

    
    for chunk in response.iter_content(chunk_size=512):
        if chunk:
            if time_of_first_byte is None:
                time_of_first_byte = time.time()
                print(f"Time to first byte: {(time_of_first_byte - start_time) * 1000} milliseconds")
            stream.write(chunk)

    
    stream.stop_stream()
    stream.close()

    
    p.terminate()


tts_stream(text, SPEAKER_NAME, lang)
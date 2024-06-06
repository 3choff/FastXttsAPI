import requests
import json
import os
import tkinter as tk
from tkinter import filedialog

SERVER_URL = 'http://localhost:8000'

OUTPUT = "./test"

if not os.path.exists(OUTPUT):
    os.mkdir(OUTPUT)
if not os.path.exists(os.path.join(OUTPUT, "cloned_speakers")):
    os.mkdir(os.path.join(OUTPUT, "cloned_speakers"))

def clone_speaker(upload_file):
    clone_speaker_name = os.path.splitext(os.path.basename(upload_file))[0]
    clone_speaker_name = clone_speaker_name.replace(' ', '_')
    files = {"wav_file": ("reference.wav", open(upload_file, "rb"))}
    embeddings = requests.post(SERVER_URL + "/clone_speaker", files=files).json()
    with open(os.path.join(OUTPUT, "cloned_speakers", clone_speaker_name + ".json"), "w") as fp:
        json.dump(embeddings, fp)

root = tk.Tk()
root.withdraw()
upload_file = filedialog.askopenfilename()

clone_speaker(upload_file)
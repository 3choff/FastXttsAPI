# FastXttsAPI

This is a fork from [XTTS-streaming-server](https://github.com/coqui-ai/xtts-streaming-server)

## Added features in this version:

1) A new endpoint capable of receiving both streaming and non-streaming requests, using simpler parameters and offering 62 preset studio voices.

2) A Jupyter Notebook designed to run FastXttsAPI in Google Colab and take advantage of the GPU capabilities of the free tier. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]([FastXttsAPI_notebook.ipynb](https://github.com/3choff/FastXttsAPI/blob/main/FastXttsAPI_notebook.ipynb))


## Planned features:

1) Concurrent streaming requests

2) Improved error handling

3) Migration to the actively maintained [idiap/coqui-ai-TTS](https://github.com/idiap/coqui-ai-TTS) repository, as the original Coqui TTS is discontinued

## Video Demo

https://github.com/coqui-ai/xtts-streaming-server/assets/17219561/7220442a-e88a-4288-8a73-608c4b39d06c


## Run the server

### Build the Docker image

To build the Docker container Pytorch 2.1 and CUDA 11.8 :

`DOCKERFILE` may be `Dockerfile`, `Dockerfile.cpu`, `Dockerfile.cuda121`, or your own custom Dockerfile.

```bash
$ git clone https://github.com/3choff/FastXttsAPI.git
$ cd FastXttsAPI
$ docker build -t fastxttsapi . -f DOCKERFILE
$ docker run --gpus all -e COQUI_TOS_AGREED=1 --rm -p 8000:80 fastxttsapi
```

Setting the `COQUI_TOS_AGREED` environment variable to `1` indicates you have read and agreed to
the terms of the [CPML license](https://coqui.ai/cpml). (Fine-tuned XTTS models also are under the [CPML license](https://coqui.ai/cpml))

## Testing the running server

Once your Docker container is running, you can test that it's working properly. You will need to run the following code from a fresh terminal.

### Using the gradio demo in the video above

```bash
$ cd FastXttsAPI
$ python -m pip install -r test/requirements.txt
$ python demo.py
```

### Using the streaming test script

```bash
$ cd FastXttsAPI/test
$ python -m pip install -r requirements.txt
$ python test_speech_streaming.py
```

### Clone a Voice with the Test Script

To clone a voice using the test script in FastXttsAPI, follow these steps:

```bash
$ cd FastXttsAPI/test
$ python -m pip install -r requirements.txt
$ python test_clone_speaker.py
```

1. Running the Script:

- The script will generate embeddings from the source audio file and save them in a JSON file.
- This JSON file will be stored in the ./test/cloned_speakers/ folder and will be automatically named after the source audio file.

2. Using the Cloned Voice:

- To use the cloned voice with the FastAPI server, move the JSON file to the ./server/studio_speakers/ folder.

3. Testing the Cloned Voice:

- You can test the cloned voices using either test_speech_streaming.py or test_speech_non_streaming.py.
- Make sure to set the SPEAKER_NAME variable to match the name of the JSON file. For example, if the JSON file is named Samantha.json, set SPEAKER_NAME = "Samantha" after copying the file to the studio_speakers folder.
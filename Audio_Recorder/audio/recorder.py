import pyaudio
import numpy as np
import queue
from Audio_Recorder.utils.constants import FORMAT, CHANNELS, RATE, CHUNK

def record_loop(audio_queue: queue.Queue):
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    output=True,
                    frames_per_buffer=CHUNK)
    print("recording...")

    try:
        while True:
            data = stream.read(CHUNK)
            samples = np.frombuffer(data, dtype=np.int16)
            audio_queue.put(samples)
    except KeyboardInterrupt:
        print("exiting...")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
import numpy as np
import queue
import time

def analyze_volume(audio_queue: queue.Queue, volume_queue: queue.Queue):
    while True:
        if not audio_queue.empty():
            samples = audio_queue.get()
            volume = np.sqrt(np.mean(np.square(samples.astype(np.float32))))
            volume_queue.put((volume, samples.astype(np.float32)))
        else:
            time.sleep(0.005)
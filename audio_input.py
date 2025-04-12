import pyaudio
import numpy as np
import queue
import tkinter as tk
from tkinter import ttk
ref = 32768.0


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
DURATION = 1
FRAMES_PER_BUFFER = int(RATE / CHUNK * DURATION)

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

def analyze_volume(audio_queue: queue.Queue, volume_queue: queue.Queue):
    import time
    while True:
        if not audio_queue.empty():
            samples = audio_queue.get()
            volume = np.sqrt(np.mean(np.square(samples.astype(np.float32))))
            volume_queue.put((volume,samples.astype(np.float32)))

        else:
            time.sleep(0.001)

def volume_to_color(volume_percent):
    if volume_percent < 50:
        # zielony → żółty
        r = int(255 * (volume_percent / 50))
        g = 255
    else:
        # żółty → czerwony
        r = 255
        g = int(255 * (1 - (volume_percent - 50) / 50))
    return f'#{r:02x}{g:02x}00'





def gui_loop(volume_queue: queue.Queue):
    root = tk.Tk()
    root.title("Poziom Głośności")
    root.geometry("100x300")

    canvas = tk.Canvas(root, width=60, height=250, bg="white")
    canvas.pack(pady=10)
    bar = canvas.create_rectangle(10, 250, 50, 250, fill='green', width=0)
    signal_buffer = np.zeros(RATE//4)


    osc_canvas = tk.Canvas(root, width=300, height=100, bg='white')
    osc_canvas.pack(pady=10)


    def update_gui():
        if not volume_queue.empty():
            while not volume_queue.empty():
                last = volume_queue.get()
            volume, samples = last
            signal_buffer[:-len(samples)] = signal_buffer[len(samples):]
            signal_buffer[-len(samples):] = samples

            if volume <= 5:
                volume_db = -100
                signal_buffer[-len(samples):] = 0
            else:

                volume_db = 20*np.log10(volume/ref)


            volume_percent = np.clip((volume_db + 60) / 100 * 250, 0, 100)

            color = volume_to_color(volume_percent)
            bar_height = int((volume_percent/ 100)* 250)
            canvas.coords(bar, 10, 250 - bar_height, 50, 250)
            canvas.itemconfig(bar, fill=color)
            osc_canvas.delete('all')
            h = 100
            w = 300
            mean = h // 2

            scaled = signal_buffer[::int(len(signal_buffer)//w)]
            max_val = np.max(np.abs(scaled))
            if max_val == 0:
                scaled = np.zeros_like(scaled)
            else:
                scaled = scaled / max_val * (h / 2 - 1)

            for x in range(w-1):
                y1 = int(mean - scaled[x])
                y2 = int(mean - scaled[x+1])
                osc_canvas.create_rectangle(x, y1, x+1, y2, fill=color)
        root.after(2, update_gui)

    update_gui()
    root.mainloop()

# def update_bar_loop(volume_queue: queue.Queue):
#     root = tk.Tk()
#     root.title("Tylko przebieg sygnału")
#     root.geometry("320x150")
#
#     signal_buffer = np.zeros(RATE)
#
#     # Oscyloskop
#     osc_canvas = tk.Canvas(root, width=300, height=100, bg='white')
#     osc_canvas.pack(pady=10)
#
#     def update_bar():
#         nonlocal signal_buffer
#         latest = None
#         while not volume_queue.empty():
#             try:
#                 latest = volume_queue.get()
#                 if latest is not None:
#                     volume,samples = latest
#                     # przesunięcie bufora
#                     signal_buffer[:-len(samples)] = signal_buffer[len(samples):]
#                     signal_buffer[-len(samples):] = samples
#
#                 # Wygaszenie przebiegu przy ciszy
#
#                 if volume <= 5:
#                     signal_buffer[-len(samples):] = 0
#
#             except queue.Empty:
#                 pass
#
#         # rysowanie wykresu
#         osc_canvas.delete('all')
#         w = 300
#         h = 100
#         mean = h // 2
#         step = max(1, int(len(signal_buffer) / w))
#         scaled = signal_buffer[::step]
#         max_val = np.max(np.abs(scaled))
#
#         if max_val == 0:
#             scaled = np.zeros_like(scaled)
#         else:
#             scaled = scaled / max_val * (h / 2 - 1)
#
#         for x in range(len(scaled) - 1):
#             y1 = int(mean - scaled[x])
#             y2 = int(mean - scaled[x + 1])
#             osc_canvas.create_line(x, y1, x + 1, y2, fill='black')
#
#         root.after(2, update_bar)
#
#     update_bar()
#     root.mainloop()



if __name__ == '__main__':
    import threading

    audio_q = queue.Queue()
    volume_q = queue.Queue()

    t_record = threading.Thread(target=record_loop, args=(audio_q,), daemon=True)
    t_analyze = threading.Thread(target=analyze_volume, args=(audio_q, volume_q), daemon=True)
    t_gui = threading.Thread(target=gui_loop, args=(volume_q,), daemon=True)


    t_record.start()
    t_analyze.start()
    t_gui.start()
    t_gui.join()

import tkinter as tk
import numpy as np
from gui.colors import volume_to_color
from utils.constants import RATE, REF
import queue

def gui_loop(volume_queue: queue.Queue):
    root = tk.Tk()
    root.title("Poziom Głośności")
    root.geometry("100x300")

    canvas = tk.Canvas(root, width=100, height=250, bg="white")
    canvas.pack(pady=10)
    bar = canvas.create_rectangle(10, 250, 50, 250, fill='green', width=0)

    signal_buffer = np.zeros(RATE // 43)

    osc_canvas = tk.Canvas(root, width=300, height=100, bg='white')
    osc_canvas.pack(pady=10)

    fft_canvas = tk.Canvas(root, width=300, height=100, bg='white')
    fft_canvas.pack(pady=10)

    def update_gui():
        if not volume_queue.empty():
            try:
                volume, samples = volume_queue.get_nowait()
            except queue.Empty:
                return

            signal_buffer[-len(samples):] = samples

            volume_db, signal_zero = (-100, 0) if volume <= 5 else (20 * np.log10(volume / REF), samples)
            signal_buffer[-len(samples):] = signal_zero
            volume_percent = np.clip((volume_db + 60) / 100 * 250, 0, 100)

            color = volume_to_color(volume_percent)
            bar_height = int((volume_percent / 100) * 250)
            canvas.coords(bar, 10, 250 - bar_height, 95, 250)
            canvas.itemconfig(bar, fill=color)

            # oscyloskop
            osc_canvas.delete('all')
            h, w = 100, 300
            mean = h // 2
            scaled = signal_buffer[::int(len(signal_buffer) // w)]
            max_val = np.max(np.abs(scaled))
            scaled = scaled / max_val * (h / 2 - 1) if max_val else np.zeros_like(scaled)

            for x in range(w - 1):
                y1 = int(mean - scaled[x])
                y2 = int(mean - scaled[x + 1])
                osc_canvas.create_rectangle(x, y1, x + 1, y2, fill='black')

            # FFT
            fft_canvas.delete('all')
            fft = np.abs(np.fft.rfft(samples * np.hanning(len(samples))))
            fft = fft[:len(fft) // 2]
            bands = 50
            band_bins = np.array_split(fft, bands)
            max_fft = max(np.max(b) for b in band_bins)
            for i, band in enumerate(band_bins):
                amp = np.mean(band)
                height = int((amp / max_fft) * 100) if max_fft > 0 else 0
                x0 = i * (300 // bands)
                x1 = x0 + (300 // bands - 2)
                fft_canvas.create_rectangle(x0, 100 - height, x1, 100, fill='blue')

        root.after(5, update_gui)

    update_gui()
    root.mainloop()
import threading
import queue
from audio.recorder import record_loop
from audio.analyzer import analyze_volume
from gui.volume_display import gui_loop

def main():
    audio_q = queue.Queue()
    volume_q = queue.Queue()

    t_record = threading.Thread(target=record_loop, args=(audio_q,), daemon=True)
    t_analyze = threading.Thread(target=analyze_volume, args=(audio_q, volume_q), daemon=True)

    t_record.start()
    t_analyze.start()
    gui_loop(volume_q)

if __name__ == '__main__':
    main()

### Zadanie 1: Odczyt dźwieku w osobnym wątku

W poniższym kodzie dane z mikrofonu są pobierane i wrzucane do kolejki:

```python
def record_loop(audio_queue: queue.Queue):
    p = pyaudio.PyAudio()
    stream = p.open(...)
    while True:
        data = stream.read(CHUNK)
        samples = np.frombuffer(data, dtype=np.int16)
        audio_queue.put(samples)
```

**Zadanie:** Zmień program tak, by funkcja `record_loop` działała w osobnym wątku (użyj `threading.Thread`). Uruchom ten wątek i sprawdź, czy wszystko działa poprawnie.

**✎ Miejsce na kod:**

```python
# tutaj utwórz i uruchom wątek z record_loop
```

---

### Zadanie 2: Analiza głośności w osobnym wątku

Dane z mikrofonu są analizowane w funkcji `analyze_volume`, która wylicza RMS i wrzuca dane do innej kolejki:

```python
def analyze_volume(audio_queue: queue.Queue, volume_queue: queue.Queue):
    while True:
        if not audio_queue.empty():
            samples = audio_queue.get()
            volume = np.sqrt(np.mean(np.square(samples.astype(np.float32))))
            volume_queue.put((volume, samples.astype(np.float32)))
```

**Zadanie:** Uruchom tę funkcję w osobnym wątku. Upewnij się, że pobiera dane z `audio_queue` i umieszcza wyniki w `volume_queue`.

**✎ Miejsce na kod:**

```python
# tutaj utwórz i uruchom wątek z analyze_volume
```

---

### Zadanie 3: Rozdzielenie GUI na dwa wątki

Twój interfejs GUI rysuje zarówno pasek głośności, jak i oscyloskop w jednej pętli.

**Zadanie:** Podziel odświeżanie GUI na dwie funkcje:

- jedna rysuje tylko pasek głośności,
- druga rysuje tylko przebieg sygnału (oscyloskop).

Użyj osobnych `root.after()` dla każdej funkcji.

**✎ Miejsce na kod:**

```python
def update_volume_bar():
    # odśwież pasek głośności
    root.after(33, update_volume_bar)

def update_oscilloscope():
    # odśwież oscyloskop
    root.after(16, update_oscilloscope)
```

---

### Zadanie 4: Logowanie maksymalnej głośności do pliku

**Zadanie:** Stwórz nowy wątek, który co 1 sekundę odczytuje z kolejki `volume_queue` ostatnią głośność i zapisuje najwyższą wartość z ostatniej sekundy do pliku `log.txt`.

Podpowiedź: użyj `time.sleep(1)` oraz otwierania pliku w trybie `append` ("a").

**✎ Miejsce na kod:**

```python
def log_volume(volume_queue):
    while True:
        # zbierz dane przez sekundę
        # zapisz najwyższy poziom głośności do pliku
        time.sleep(1)

# utwórz i uruchom wątek

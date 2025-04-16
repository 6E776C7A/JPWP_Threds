# 🧠 Projekt: Wielowątkowość i Współbieżność

## 📌 Opis

Projekt edukacyjny mający na celu przedstawienie kluczowych koncepcji związanych z **wielowątkowością**, **współbieżnością** oraz technologiami wspierającymi przetwarzanie równoległe, takimi jak **Hyper-Threading**. Prezentacja obejmuje zarówno teorię, jak i proste implementacje w językach **Java**, **Python**.

## 🎯 Zakres tematyczny

- Czym jest przetwarzanie danych
- Współbieżność vs. wielowątkowość vs. wieloprocesowość
- Race conditions, deadlock, starvation, mutex, async/await
- Global Interpreter Lock (GIL) w Pythonie
- Hyper-Threading Technology (Intel)
- Przykładowe implementacje:
  - Java (Runnable, Thread, ExecutorService)
  - Python (threading, multiprocessing)
  - C++ (std::thread, std::mutex)

## 🗺️ Materiały

- Prezentacja multimedialna (slajdy)
- Mapa pamięciowa (mind map) kluczowych pojęć
- Quiz i zadania sprawdzające wiedzę
- Kody źródłowe w 3 językach programowania

## 💻 Wymagania

- Python 3.10+ (dla przykładów z `async` / `multiprocessing`)
- Java JDK 11+ (dla implementacji wielowątkowości)

## 📁 Struktura katalogów

```
main/
├── prezentacja.pptx             # Slajdy, grafiki, mapa myśli
│
├── zadania.md                  # Quizy, pytania, zadania otwarte
│
├── lorem_ipsum/              # Przykładowe programy testowe
│   ├── python/
│   │   ├── main.py
│   │   ├── metoda_sekfencyjna.py
│   │   └── metoda_wielowątkowa.py
│   ├── java/
│   │   └── KeywordCounter.java
│   └── data/
│       └──Lorem_Ipsum_1GB.txt
│
├── audio_recorder/           # Aplikacja z obsługą współbieżności
│   ├── audo/
│   │   ├── analyzer.py
│   │   └── recorder.py
│   ├── gui/
│   │   ├── colors.py
│   │   └── colume_display.py
│   ├── utils/
│   │   └── constants.py
│   └── main.py
│
└── README.md                 # Plik informacyjny o projekcie
```

## 📬 Autor

Projekt edukacyjny przygotowany w ramach zajęć z języki programowania wysokiego poziomu.  
Autor: *Patryk Pajerski, Szymon Leśniak*
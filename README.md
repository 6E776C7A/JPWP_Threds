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
│
├── Zadania                 # Quizy, pytania, zadania otwarte
│   ├── Quiz.md
│   ├── Zadania.md
│   └── Zadania.py          # Plik przygotowany do wykonywania zadań
│
├── Lorem_ipsum_GLI/              # Przykładowe programy testowe, problem GLI
│   ├── python/
│   │   ├── main.py
│   │   ├── metoda_sekwencyjna.py
│   │   └── metoda_wielowątkowa.py
│   ├── java/
│   │   └── KeywordCounter.java
│   └── data/
│       └──Lorem_Ipsum_1GB.txt
│
├── Audio_Recorder/           # Aplikacja z obsługą współbieżności
│   ├── audio/
│   │   ├── analyzer.py
│   │   └── recorder.py
│   ├── gui/
│   │   ├── colors.py
│   │   └── volume_display.py
│   ├── utils/
│   │   └── constants.py
│   └── main.py
│
├── Prezentacja_JPWP.pptx             # Slajdy, grafiki, mapa myśli
│
├── requirements.txt                  # Biblioteki potrzebne do projektu
│
└── README.md                 # Plik informacyjny o projekcie
```

## 📬 Autor

Projekt edukacyjny przygotowany w ramach zajęć z języki programowania wysokiego poziomu.  
Autor: *Patryk Pajerski, Szymon Leśniak*
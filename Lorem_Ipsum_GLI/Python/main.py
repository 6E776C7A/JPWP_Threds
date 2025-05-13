import asyncio
import time
from metoda_sekwencyjna import text_sequential_method
from metoda_wielowątkowa import text_multithreaded_method
from metoda_asyncio import  text_asyncio_method

# Dane wejściowe
text = open("Lorem_Ipsum_1GB.txt", "r").read()
# 2 GB
# text = text + text
# 500 MB
# text = text[0:len(text)//2]
# 250 MB
text = text[0:len(text)//4]
# 100 MB
# text = text[0:len(text)//10]

# Słowo wyszukiwane
keyword = "sit"

if not text:
    raise ValueError("Tekst nie może być pusty")
if not keyword:
    raise ValueError("Słowo kluczowe nie może być puste")

# Pomiar czasu wykonywania zliczania dla prostego sposobu sekwencyjnego

print(f"Wykonuje poszukiwania słowa {keyword} sposobem sekwencyjnym!")

time_start_sequential = time.perf_counter()

result_sequential = text_sequential_method(text, keyword)

time_end_sequential = time.perf_counter()

print(
    f'\nZnaleziono {keyword.lower()} w ilości: {result_sequential}. W czasie: {time_end_sequential - time_start_sequential} s')

# Pomiar czasu wykonywania zliczania dla wielowątkowości

print(f"\nWykonuje poszukiwania słowa {keyword} sposobem sekwencyjnym z wieloma wątkami!")

time_start_multithreaded = time.perf_counter()

result_multithreaded = text_multithreaded_method(text, keyword)

time_end_multithreaded = time.perf_counter()

print(
    f'\nZnaleziono {keyword.lower()} w ilości: {result_multithreaded}. W czasie: {time_end_multithreaded - time_start_multithreaded} s')

# Pomiar czasu wykonywania zliczania dla asyncio

print(f"\nWykonuje poszukiwania słowa {keyword} sposobem sekwencyjnym za pomocą asyncio!")

time_start_asyncio = time.perf_counter()

result_asyncio = asyncio.run(text_asyncio_method(text, keyword))

time_end_asyncio = time.perf_counter()

print(
    f'\nZnaleziono {keyword.lower()} w ilości: {result_asyncio}. W czasie: {time_end_asyncio - time_start_asyncio} s')
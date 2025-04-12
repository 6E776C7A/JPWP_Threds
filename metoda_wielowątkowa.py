import threading
import time


def count_keyword(fragment: str, keyword: str, result_list: list, index: int) -> None:
    """
    Zlicza wystąpienia słowa kluczowego w fragmencie tekstu.

    Args:
        fragment (str): Tekst do analizy
        keyword (str): Szukane słowo kluczowe
        result_list (list): Współdzielona lista wyników
        index (int): Indeks w liście wyników

    Returns:
        None (wynik zapisywany w result_list[index])
    """

    keyword_lower = keyword.lower()
    keyword_len = len(keyword_lower)
    fragment_lower = fragment.lower()
    count = 0

    # Efektywne przeszukiwanie
    for i in range(len(fragment_lower) - keyword_len + 1):
        if fragment_lower[i:i + keyword_len] == keyword_lower:
            count += 1

    result_list[index] = count


def text_multithreaded_method(text: str, keyword: str, num_threads: int = 4) -> int:
    """
    Przetwarza tekst wielowątkowo w poszukiwaniu słowa kluczowego.

    Args:
        text (str): Tekst do przeszukania
        keyword (str): Szukane słowo kluczowe
        num_threads (int): Liczba wątków (domyślnie 4)

    Returns:
        int: Całkowita liczba wystąpień

    Example:
        # text = "Python " * 1000
        # result = text_multithreaded_method(text, "Python")
    """

    # Przygotowanie fragmentów
    fragment_size = max(len(text) // num_threads, 1)
    fragments = [
                    text[i:i + fragment_size]
                    for i in range(0, len(text), fragment_size)
                ][:num_threads]

    # Struktury danych dla wątków
    result_list = [0] * len(fragments)
    threads = []

    # Uruchamianie wątków
    for i, fragment in enumerate(fragments):
        thread = threading.Thread(
            target=count_keyword,
            args=(fragment, keyword, result_list, i),
            daemon=True
        )
        threads.append(thread)
        thread.start()

    # Oczekiwanie na zakończenie
    for thread in threads:
        thread.join()

    return sum(result_list)

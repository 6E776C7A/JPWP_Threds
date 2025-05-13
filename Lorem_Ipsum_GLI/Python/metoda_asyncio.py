import asyncio

def count_keyword(fragment: str, keyword: str) -> int:
    """
    Zlicza wystąpienia słowa kluczowego w danym fragmencie tekstu.

    Przeszukuje tekst w sposób sekwencyjny, ignorując wielkość liter.
    Jest to funkcja CPU-bound i może być uruchamiana w osobnym wątku
    za pomocą asyncio.to_thread().

    Args:
        fragment (str): Fragment tekstu do przeszukania.
        keyword (str): Słowo kluczowe do znalezienia.

    Returns:
        int: Liczba wystąpień słowa kluczowego w podanym fragmencie.
    """
    keyword_lower = keyword.lower()
    keyword_len = len(keyword_lower)
    fragment_lower = fragment.lower()
    count = 0

    for i in range(len(fragment_lower) - keyword_len + 1):
        if fragment_lower[i:i + keyword_len] == keyword_lower:
            count += 1
    return count


async def text_asyncio_method(text: str, keyword: str, num_tasks: int = 4) -> int:
    """
    Asynchronicznie zlicza wystąpienia słowa kluczowego w tekście,
    dzieląc go na fragmenty i przetwarzając równolegle.

    Funkcja używa asyncio.to_thread() do uruchamiania obliczeń CPU-bound
    w tle, bez blokowania głównej pętli zdarzeń. Jest przydatna, gdy aplikacja
    używa asyncio i potrzebuje współbieżnego przetwarzania tekstu.

    Args:
        text (str): Pełny tekst do przeszukania.
        keyword (str): Słowo kluczowe do znalezienia.
        num_tasks (int, optional): Liczba zadań (fragmentów) do przetworzenia. Domyślnie 4.

    Returns:
        int: Łączna liczba wystąpień słowa kluczowego w całym tekście.
    """
    fragment_size = max(len(text) // num_tasks, 1)
    fragments = [
        text[i:i + fragment_size]
        for i in range(0, len(text), fragment_size)
    ][:num_tasks]

    tasks = [
        asyncio.to_thread(count_keyword, fragment, keyword)
        for fragment in fragments
    ]
    results = await asyncio.gather(*tasks)
    return sum(results)

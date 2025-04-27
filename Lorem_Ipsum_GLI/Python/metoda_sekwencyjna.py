

def count_keyword(fragment: str, keyword: str) -> int:
    """
    Zlicza wystąpienia słowa kluczowego w fragmencie tekstu.

    Args:
        fragment (str): Tekst do analizy
        keyword (str): Szukane słowo kluczowe

    Returns:
        int: Liczba wystąpień słowa kluczowego w fragmencie
    """
    if not fragment or not keyword:
        return 0

    keyword_lower = keyword.lower()
    keyword_len = len(keyword_lower)
    fragment_lower = fragment.lower()
    count = 0

    for i in range(len(fragment_lower) - keyword_len + 1):
        if fragment_lower[i:i + keyword_len] == keyword_lower:
            count += 1

    return count


def text_sequential_method(text: str, keyword: str, chunks: int = 4) -> int:
    """
    Przetwarza tekst sekwencyjnie w poszukiwaniu słowa kluczowego.

    Args:
        text (str): Tekst do przeszukania
        keyword (str): Szukane słowo kluczowe
        chunks (int): Liczba części na jakie dzielimy tekst (domyślnie 4)

    Returns:
        int: Całkowita liczba wystąpień

    Example:
        # text = "Python " * 1000
        # text_sequential_method(text, "Python")
    """

    fragment_size = max(len(text) // chunks, 1)
    fragments = [text[i:i + fragment_size]
                 for i in range(0, len(text), fragment_size)][:chunks]
    total_count = 0

    for fragment in fragments:
        total_count += count_keyword(fragment, keyword)

    return total_count

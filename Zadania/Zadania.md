# Symulator Restauracji - Podział na Zadania

Poniżej znajduje się opis czterech zadań opartych o program symulujący restaurację z klientami i kucharzami.

---

## 🏆 Zadanie 1 – Klienci wrzucają zamówienia do kolejki

**Cel:**
- Stwórz 10 wątków klientów.
- Każdy klient składa **dokładnie jedno zamówienie** (losowe danie z listy).
- Zamówienie jest wrzucane do **wspólnej kolejki**.
- Wyświetl komunikaty o złożony zamówieniach.

**Uwagi:**
- Nie implementujemy jeszcze kucharzy.
- Skupiamy się na poprawnym zapełnieniu kolejki zamówieniami.

---

## 🏆 Zadanie 2 – Kucharze realizują zamówienia

**Cel:**
- Dodaj 3 kucharzy (3 nowe wątki).
- Każdy kucharz pobiera zamówienie z kolejki.
- Symuluj przygotowywanie dania za pomocą `time.sleep` (losowy czas 2-5 sekund).
- Po przygotowaniu wypisz komunikat o gotowym daniu.

**Uwagi:**
- Kucharze nie powinni się jeszcze zatrzymywać automatycznie.
- Program kończy się po przygotowaniu wszystkich zamówień.

---

## 🏆 Zadanie 3 – Obsługa braku zamówień

**Cel:**
- Zmodyfikuj kucharzy, aby:
  - Używali `queue.get(timeout=3)`.
  - Jeśli przez 3 sekundy nie otrzymają zamówienia, **kończą pracę**.
- Dodaj liczenie łącznej liczby obsłużonych zamówień.

**Uwagi:**
- Zabezpiecz program przed zawieszeniem.
- Kucharze mają się naturalnie "rozłączyć" jak kolejka będzie pusta.

---

## 🏆 Zadanie 4 – Statystyki kucharzy

**Cel:**
- Każdy kucharz powinien prowadzić **własny licznik** obsłużonych zamówień.
- Na koniec programu wyświetl:
  - Ilu klientów obsłużył każdy kucharz.
  - Łączną liczbę obsłużonych zamówień.

**Uwagi:**
- Użyj osobnych zmiennych (lub struktur danych) dla każdego kucharza.
- Pamiętaj o odpowiednim synchronizowaniu dostępu, jeśli potrzeba.

---

# 🔄 Uwagi dodatkowe

- Kolejka powinna być jedną wspólną strukturą dla wszystkich wątków.
- Korzystamy z `threading.Thread`, `queue.Queue` oraz `time.sleep`.
- Losowe wybieranie dań oraz czasów przygotowania za pomocą `random.choice` i `random.uniform`.

Powodzenia i smacznego kodowania! 🍝🍽️


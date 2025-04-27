# restaurant_tasks.py

import threading
import queue
import random
import time

# Lista przykładowych dań
menu = [
    "Pizza Margherita", "Pizza Pepperoni", "Burger Classic",
    "Burger Cheese", "Sałatka Grecka", "Makaron Carbonara"
]

# Kolejka zamówień
order_queue = queue.Queue()

# 🏆 Zadanie 1: Klienci wrzucają zamówienia do kolejki

NUM_CLIENTS = 10

#Stwórz funkcję klienta, który:
# - wybiera losowe danie z listy
# - wrzuca zamówienie do kolejki
# - wypisuje komunikat o złożonym zamówieniu

def client(id_):
    pass  # <- tutaj napisz kod klienta

#Stwórz funkcję startującą 10 klientów (wątki)

def start_clients():
    pass  # <- tutaj uruchom wszystkie wątki klientów

# 🏆 Zadanie 2: Kucharze realizują zamówienia

NUM_COOKS = 3

#Stwórz funkcję kucharza, który:
# - pobiera zamówienie z kolejki
# - przygotowuje je (time.sleep losowy 2-5s)
# - wypisuje komunikat o gotowym daniu

def cook(id_):
    pass  # <- tutaj napisz kod kucharza

#Funkcja do startowania kucharzy
def start_cooks():
    pass  # <- tutaj uruchom wszystkie wątki kucharzy

# 🏆 Zadanie 3: Obsługa braku zamówień
# - Skopiuj funkcjonalność kucharza z poprzedniego polecenia

#Zmodyfikowana funkcja kucharza:
# - Użyj queue.get(timeout=3)
# - Jesli brak zamówienia przez 3s, kucharz kończy pracę

def cook_with_timeout(id_):
    pass  # <- tutaj kucharz z timeoutem

#Funkcja startująca kucharzy z timeoutem

def start_cooks_with_timeout():
    pass  # <- tutaj uruchom kucharzy z timeoutem

# 🏆 Zadanie 4: Statystyki kucharzy
# - Skopiuj funkcjonalność kucharza z poprzedniego polecenia


completed_orders = {}
completed_lock = threading.Lock()

#Funkcja kucharza ze zliczaniem zamówień

def cook_with_stats(id_):
    pass  # <- tutaj kucharz, który zlicza swoje zamówienia

#Funkcja startująca kucharzy ze statystykami

def start_cooks_with_stats():
    pass  # <- tutaj start kucharzy ze statystykami

#Funkcja pokazująca wyniki

def show_stats():
    pass  # <- tutaj wypisz kto ile przygotował zamówień

# 🔄 Główna funkcja

def main():
    start_clients()
    # W zależności od zadania, uruchom:
    # start_cooks()
    # lub
    # start_cooks_with_timeout()
    # lub
    # start_cooks_with_stats()
    order_queue.join()
    show_stats()

if __name__ == "__main__":
    main()
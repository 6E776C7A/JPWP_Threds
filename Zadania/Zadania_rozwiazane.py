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

# Liczba klientów
NUM_CLIENTS = 10

# Funkcja klienta
def client(id_):
    dish = random.choice(menu)
    print(f"[Klient {id_}] Składa zamówienie: {dish}")
    order_queue.put((id_, dish))

# Start klientów
def start_clients():
    clients = []
    for i in range(NUM_CLIENTS):
        t = threading.Thread(target=client, args=(i+1,))
        clients.append(t)
        t.start()

    for c in clients:
        c.join()

# Liczba kucharzy
NUM_COOKS = 3

# Funkcja kucharza
def cook(id_):
    while not order_queue.empty():
        try:
            client_id, dish = order_queue.get_nowait()
            prep_time = random.uniform(2.0, 5.0)
            print(f"[Kucharz {id_}] Przygotowuje '{dish}' dla Klienta {client_id} ({prep_time:.2f}s)")
            time.sleep(prep_time)
            print(f"[Kucharz {id_}] GOTOWE: '{dish}' dla Klienta {client_id}")
            order_queue.task_done()
        except queue.Empty:
            break

# Start kucharzy
def start_cooks():
    cooks = []
    for i in range(NUM_COOKS):
        t = threading.Thread(target=cook, args=(i+1,))
        cooks.append(t)
        t.start()

    for c in cooks:
        c.join()

# Nowa wersja kucharza z timeoutem
def cook_with_timeout(id_):
    while True:
        try:
            client_id, dish = order_queue.get(timeout=3)
            prep_time = random.uniform(2.0, 5.0)
            print(f"[Kucharz {id_}] Przygotowuje '{dish}' dla Klienta {client_id} ({prep_time:.2f}s)")
            time.sleep(prep_time)
            print(f"[Kucharz {id_}] GOTOWE: '{dish}' dla Klienta {client_id}")
            order_queue.task_done()
        except queue.Empty:
            print(f"[Kucharz {id_}] Nie ma więcej zamówień. Kończy pracę.")
            break

# Start kucharzy z timeoutem
def start_cooks_with_timeout():
    cooks = []
    for i in range(NUM_COOKS):
        t = threading.Thread(target=cook_with_timeout, args=(i+1,))
        cooks.append(t)
        t.start()

    for c in cooks:
        c.join()

# Liczniki obsłużonych zamówień przez kucharzy
completed_orders = {}
completed_lock = threading.Lock()

# Kucharz z licznikiem
def cook_with_stats(id_):
    completed_orders[id_] = 0
    while True:
        try:
            client_id, dish = order_queue.get(timeout=3)
            prep_time = random.uniform(2.0, 5.0)
            print(f"[Kucharz {id_}] Przygotowuje '{dish}' dla Klienta {client_id} ({prep_time:.2f}s)")
            time.sleep(prep_time)
            print(f"[Kucharz {id_}] GOTOWE: '{dish}' dla Klienta {client_id}")
            with completed_lock:
                completed_orders[id_] += 1
            order_queue.task_done()
        except queue.Empty:
            print(f"[Kucharz {id_}] Nie ma więcej zamówień. Kończy pracę.")
            break

# Start kucharzy z licznikiem
def start_cooks_with_stats():
    cooks = []
    for i in range(NUM_COOKS):
        t = threading.Thread(target=cook_with_stats, args=(i+1,))
        cooks.append(t)
        t.start()

    for c in cooks:
        c.join()

# Wyświetlenie statystyk
def show_stats():
    print("\n🍽️ Statystyki:")
    total = 0
    for cook_id, count in completed_orders.items():
        print(f"Kucharz {cook_id} przygotował {count} zamówień.")
        total += count
    print(f"\n🍝 Łącznie obsłużono {total} zamówień.")

def main():
    start_clients()
    start_cooks()
    order_queue.join()
    show_stats()

if __name__ == "__main__":
    main()
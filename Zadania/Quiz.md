# Pytania z zakresu współbieżności i równoległości w Pythonie

### 1. Czym różni się współbieżność (concurrency) od równoległości (parallelism)?
- A) Współbieżność działa tylko na GPU, równoległość na CPU  
- B) Współbieżność to przeplatanie zadań, równoległość to ich jednoczesne wykonywanie  
- C) Równoległość dotyczy tylko systemów rozproszonych  
- D) To synonimy – oznaczają to samo  

---

### 2. Jakie podejście najczęściej stosuje się w Pythonie, aby obejść ograniczenia GIL-a w zadaniach CPU-bound?
- A) Wątki systemowe (threading.Thread)  
- B) Korutyny (asyncio)  
- C) Procesy (multiprocessing)  
- D) Wywołania lambda  

---

### 3. Czym jest race condition (wyścig o zasoby)?
- A) Sytuacją, gdy dwa wątki komunikują się bezpośrednio  
- B) Błędem wynikającym z równoczesnego dostępu do współdzielonego zasobu bez synchronizacji  
- C) Efektem zbyt częstych przełączeń kontekstu  
- D) Blokowaniem zasobów przez zbyt wiele procesów  

---

### 4. Na czym polega technologia Hyper-Threading (HTT) firmy Intel?
- A) Na fizycznym podwojeniu liczby rdzeni procesora  
- B) Na zwiększeniu taktowania CPU przy niskim obciążeniu  
- C) Na umożliwieniu jednemu rdzeniowi wykonywania dwóch wątków jednocześnie  
- D) Na uruchamianiu kodu jedynie w trybie jednowątkowym w celu oszczędzania energii  

---

### 5. W programie Python z użyciem threading, uruchamiasz 100 wątków wykonujących intensywne obliczenia. Co najprawdopodobniej zobaczysz na wykresie użycia CPU na komputerze z 8-rdzeniowym procesorem?
- A) Wszystkie rdzenie obciążone w 100%  
- B) 100% wykorzystania GPU  
- C) Użycie jednego rdzenia bliskie 100%, pozostałe niskie  
- D) Python automatycznie rozdzieli obciążenie równo na wszystkie rdzenie  

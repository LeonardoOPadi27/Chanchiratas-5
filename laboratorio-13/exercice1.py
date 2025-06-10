class MinHeap:
    
    def __init__(self):
        self.heap = []  # Inicializa el heap como una lista vacía

    def is_empty(self):
        return len(self.heap) == 0  # Retorna True si la lista está vacía, False si no

# 🧪 Test cases
def test_min_heap_init_and_empty():
    h = MinHeap()  # Crea una nueva instancia del MinHeap
    print("🌱 Test 1:", h.is_empty() == True)  # Verifica que esté vacío al inicio

    h.heap.append(1)  # Agrega manualmente un elemento (sin usar insert aún)
    print("🌱 Test 2:", h.is_empty() == False)  # Verifica que ya no esté vacío

# 🚀 Ejecuta los tests
test_min_heap_init_and_empty()
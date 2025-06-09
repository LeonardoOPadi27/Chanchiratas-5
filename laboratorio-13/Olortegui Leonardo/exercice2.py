# ✅ Clase MinHeap que representa un heap mínimo
class MinHeap:
    def __init__(self):
        # Inicializa la lista vacía donde se almacenarán los elementos del heap
        self.heap = []

    def is_empty(self):
        # Retorna True si el heap está vacío, False si tiene elementos
        return len(self.heap) == 0

    def insert(self, value):
        # Inserta un nuevo valor al final del heap
        self.heap.append(value)  # Se agrega al final de la lista
        # Llama al método que reordena el heap hacia arriba desde la nueva posición
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # Este método mueve el elemento hacia arriba hasta que se cumpla la propiedad del heap mínimo
        while index > 0:
            # Calcula el índice del padre
            parent_index = (index - 1) // 2
            # Si el valor actual es menor que su padre, intercámbialos
            if self.heap[index] < self.heap[parent_index]:
                # Intercambio (swap)
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                # Actualiza el índice para continuar subiendo si es necesario
                index = parent_index
            else:
                # Si ya no es menor que el padre, se detiene el heapify
                break

# ✅ Casos de prueba para verificar que el heap mantiene la propiedad de mínimo
def test_min_heap_insert():
    h = MinHeap()

    h.insert(5)
    print("🍀 Test 1:", h.heap == [5])  # Solo un elemento, debe estar así

    h.insert(3)
    print("🍀 Test 2:", h.heap == [3, 5])  # 3 debe subir arriba de 5

    h.insert(4)
    print("🍀 Test 3:", h.heap == [3, 5, 4])  # 4 entra y queda en la tercera posición

    h.insert(1)
    print("🍀 Test 4:", h.heap == [1, 3, 4, 5])  # 1 debe subir hasta el tope

    # Verifica manualmente que se cumpla la propiedad del heap: padre ≤ hijos
    valid = True
    for i in range(len(h.heap)):
        left = 2 * i + 1  # índice del hijo izquierdo
        right = 2 * i + 2  # índice del hijo derecho
        # Comprobamos si el padre es mayor que sus hijos (lo cual no debe pasar)
        if left < len(h.heap) and h.heap[i] > h.heap[left]:
            valid = False
        if right < len(h.heap) and h.heap[i] > h.heap[right]:
            valid = False
    print("🍀 Test 5:", valid)  # True si todos los padres son menores o iguales a sus hijos

# ✅ Ejecutar los tests
test_min_heap_insert()
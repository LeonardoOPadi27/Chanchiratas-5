class MinHeap:
    def __init__(self):
        # Inicializa el heap como una lista vacía
        self.heap = []

    def insert(self, value):
        # Agrega el valor al final del heap
        self.heap.append(value)
        # Reorganiza hacia arriba para mantener la propiedad de min-heap
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # Mientras no estemos en la raíz (índice 0)
        while index > 0:
            parent = (index - 1) // 2  # Calcula el índice del padre
            # Si el valor actual es menor que su padre, intercambiarlos
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent  # Subir al padre
            else:
                break  # Ya se cumple la propiedad del min-heap

    def delete_min(self):
        # Si el heap está vacío, no hay nada que eliminar
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            # Si solo hay un elemento, lo eliminamos y lo devolvemos
            return self.heap.pop()

        # Guardamos el valor mínimo (raíz)
        min_val = self.heap[0]

        # Reemplazamos la raíz con el último elemento
        self.heap[0] = self.heap.pop()

        # Restauramos la propiedad del min-heap desde la raíz hacia abajo
        self._heapify_down(0)

        return min_val  # Retornamos el valor mínimo eliminado

    def _heapify_down(self, index):
        # Obtiene el tamaño del heap
        size = len(self.heap)

        while True:
            smallest = index  # Suponemos que el más pequeño es el nodo actual
            left = 2 * index + 1  # Hijo izquierdo
            right = 2 * index + 2  # Hijo derecho

            # Comparamos con el hijo izquierdo si existe y es menor
            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            # Comparamos con el hijo derecho si existe y es aún menor
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                # Si el más pequeño no es el nodo actual, intercambiamos
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest  # Bajamos al hijo más pequeño
            else:
                break  # Ya se cumple la propiedad del heap


# 🧪 Pruebas del método delete_min
def test_min_heap_delete_min():
    h = MinHeap()
    print("🧹 Test 1:", h.delete_min() is None)  # Eliminar de heap vacío

    h.heap = [1]
    print("🧹 Test 2:", h.delete_min() == 1 and h.heap == [])  # Eliminar único elemento

    h.heap = [1, 3, 2]
    print("🧹 Test 3:", h.delete_min() == 1 and h.heap == [2, 3])  # Reordenar luego de eliminar raíz

    h.heap = [1, 3, 4, 5]
    print("🧹 Test 4:", h.delete_min() == 1 and h.heap == [3, 5, 4])  # Heap con más nodos

    h.heap = [1, 2, 3, 4, 5]
    min_val = min(h.heap)
    print("🧹 Test 5:", h.delete_min() == min_val)  # Validación general


# 🚀 Ejecutar pruebas
test_min_heap_delete_min()
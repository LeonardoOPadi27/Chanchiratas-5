# ✅ Lista para registrar resultados de pruebas
test_results = []

def record_test(test_name, condition):
    """Registra el resultado de una prueba con emoji y nombre."""
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

# 💻 Implementación de MinHeap con eliminación del mínimo (_heapify_down)
class MinHeap:
    def __init__(self):
        self.heap = []

    def delete_min(self):
        """
        Elimina y retorna el elemento mínimo (la raíz del heap).
        Reemplaza la raíz por el último elemento y reorganiza usando heapify_down.
        """
        if not self.heap:
            return None  # 🧪 Caso: heap vacío
        if len(self.heap) == 1:
            return self.heap.pop()  # 🧪 Caso: un solo elemento

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()  # Reemplaza raíz por último elemento
        self._heapify_down(0)
        return min_value

    def _heapify_down(self, index):
        """Baja el nodo en la jerarquía hasta restaurar la propiedad de heap."""
        while self._has_left_child(index):
            smaller_child_index = self._left_child_index(index)
            if (self._has_right_child(index) and 
                self.heap[self._right_child_index(index)] < self.heap[smaller_child_index]):
                smaller_child_index = self._right_child_index(index)

            if self.heap[index] <= self.heap[smaller_child_index]:
                break  # Ya está en posición correcta

            # Intercambia y continúa bajando
            self.heap[index], self.heap[smaller_child_index] = self.heap[smaller_child_index], self.heap[index]
            index = smaller_child_index

    # 🔢 Métodos auxiliares de navegación
    def _left_child_index(self, index):
        return 2 * index + 1

    def _right_child_index(self, index):
        return 2 * index + 2

    def _has_left_child(self, index):
        return self._left_child_index(index) < len(self.heap)

    def _has_right_child(self, index):
        return self._right_child_index(index) < len(self.heap)

    def size(self):
        return len(self.heap)

# ✅ Función de pruebas del Challenge 1.4
def test_1_4():
    heap = MinHeap()

    # 1.4.1 Eliminación en heap vacío
    result = heap.delete_min()
    record_test("1.4.1 Empty heap deletion", result is None)

    # 1.4.2 Eliminación con un solo elemento
    heap.heap = [5]
    result = heap.delete_min()
    record_test("1.4.2 Single element deletion", result == 5 and heap.size() == 0)

    # 1.4.3 Múltiples eliminaciones
    heap.heap = [1, 3, 2, 7, 4]
    first = heap.delete_min()
    second = heap.delete_min()
    record_test("1.4.3 Multiple deletions", first == 1 and second == 2)

    # 1.4.4 Mantenimiento de la propiedad de heap
    heap.heap = [1, 3, 2, 7, 4, 5]
    heap.delete_min()
    valid_heap = all(
        (heap.heap[i] <= heap.heap[2 * i + 1] if 2 * i + 1 < len(heap.heap) else True) and
        (heap.heap[i] <= heap.heap[2 * i + 2] if 2 * i + 2 < len(heap.heap) else True)
        for i in range(len(heap.heap) // 2)
    )
    record_test("1.4.4 Heap property maintenance", valid_heap)

    # 1.4.5 Verificación de tamaño
    initial_size = heap.size()
    heap.delete_min()
    record_test("1.4.5 Size tracking", heap.size() == initial_size - 1)

# 🚀 Ejecutar pruebas
test_1_4()

# 📋 Mostrar resultados
for r in test_results:
    print(r)
class MaxHeap:
    # 🦁 Estructura de datos MaxHeap usando lista
    def __init__(self):
        self.heap = []  # Inicializa la lista vacía para almacenar el heap

    def insert(self, value):
        # Inserta un nuevo valor al final y luego reordena hacia arriba para mantener propiedad MaxHeap
        self.heap.append(value)  # Añadir valor al final del heap
        self._heapify_up(len(self.heap) - 1)  # Reordenar desde el último índice hacia arriba

    def _heapify_up(self, index):
        # Reordena el heap hacia arriba mientras el padre sea menor que el hijo actual
        parent_index = (index - 1) // 2  # Índice del nodo padre
        while index > 0 and self.heap[parent_index] < self.heap[index]:
            # Mientras no se haya llegado a la raíz y el padre sea menor que el hijo
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]  # Intercambia padre e hijo
            index = parent_index  # Mover el índice hacia arriba
            parent_index = (index - 1) // 2  # Nuevo índice del padre

    def delete_max(self):
        # Elimina y retorna el elemento más grande (raíz del heap)
        if not self.heap:
            return None  # Si el heap está vacío, retorna None
        if len(self.heap) == 1:
            return self.heap.pop()  # Si hay un solo elemento, lo elimina y retorna
        max_value = self.heap[0]  # Guardar valor máximo (raíz)
        self.heap[0] = self.heap.pop()  # Mover último elemento a la raíz
        self._heapify_down(0)  # Reordenar hacia abajo desde la raíz
        return max_value  # Retorna el valor eliminado

    def _heapify_down(self, index):
        # Reordena el heap hacia abajo mientras el nodo actual sea menor que su hijo mayor
        length = len(self.heap)
        while True:
            left = 2 * index + 1  # Índice del hijo izquierdo
            right = 2 * index + 2  # Índice del hijo derecho
            largest = index  # Inicialmente el índice mayor es el actual

            # Si el hijo izquierdo existe y es mayor que el actual, actualizar largest
            if left < length and self.heap[left] > self.heap[largest]:
                largest = left
            # Si el hijo derecho existe y es mayor que el mayor actual, actualizar largest
            if right < length and self.heap[right] > self.heap[largest]:
                largest = right
            # Si largest no cambió, el heap está ordenado
            if largest == index:
                break
            # Intercambiar y continuar bajando en el heap
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest  # Mover índice al hijo mayor


# 🧪 Test cases
def test_max_heap():
    h = MaxHeap()
    h.insert(1)
    print("🦁 Test 1:", h.heap == [1])  # True porque solo hay un elemento
    for val in [3, 2, 8, 5]:
        h.insert(val)
    print("🦁 Test 2:", h.heap[0] == max(h.heap))  # La raíz es el máximo
    h.delete_max()
    print("🦁 Test 3:", h.heap[0] == max(h.heap))  # Después de eliminar, la raíz sigue siendo el máximo
    h = MaxHeap()
    for val in [5, 3, 1]:
        h.insert(val)
    h.delete_max()
    print("🦁 Test 4:", h.heap == [3, 1])  # Después de eliminar 5, quedan [3,1]
    h = MaxHeap()
    h.insert(10)
    print("🦁 Test 5:", h.delete_max() == 10 and h.heap == [])  # Elimina el único elemento y queda vacío

test_max_heap()
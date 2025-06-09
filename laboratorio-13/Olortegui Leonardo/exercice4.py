class MinHeap:
    def __init__(self):
        # Inicializamos el heap como una lista vacía
        self.heap = []

    def build_heap(self, array):
        # Copiamos los elementos del array a nuestro heap
        self.heap = array[:]

        # Comenzamos desde el último nodo que no es hoja
        start_index = (len(self.heap) // 2) - 1

        # Aplicamos _heapify_down desde el último nodo no hoja hasta la raíz
        for i in range(start_index, -1, -1):
            self._heapify_down(i)

    def _heapify_down(self, index):
        # Mientras existan hijos izquierdos
        while 2 * index + 1 < len(self.heap):
            # Calculamos índices de los hijos izquierdo y derecho
            left = 2 * index + 1
            right = 2 * index + 2

            # Suponemos que el hijo izquierdo es el más pequeño
            smallest = left

            # Si el hijo derecho existe y es menor que el izquierdo
            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                smallest = right

            # Si el nodo actual es menor o igual al hijo más pequeño, el heap ya es válido
            if self.heap[index] <= self.heap[smallest]:
                break

            # Intercambiamos el nodo con su hijo más pequeño
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]

            # Continuamos bajando por el árbol
            index = smallest

# 🧪 Test cases
def test_build_heap():
    h = MinHeap()
    h.build_heap([5, 3, 8, 1, 2])
    print("🔨 Test 1:", h.heap[0] == min([5, 3, 8, 1, 2]))  # Espera que el primer elemento sea el menor
    h.build_heap([7, 6, 5, 4, 3, 2, 1])
    print("🔨 Test 2:", h.heap[0] == 1)  # El menor debe estar en la raíz
    h.build_heap([2, 1])
    print("🔨 Test 3:", h.heap == [1, 2])  # Orden esperado en min-heap
    h.build_heap([10])
    print("🔨 Test 4:", h.heap == [10])  # Un solo elemento
    h.build_heap([])
    print("🔨 Test 5:", h.heap == [])  # Heap vacío

# Ejecutamos los tests
test_build_heap()
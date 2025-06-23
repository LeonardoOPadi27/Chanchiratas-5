test_results = []

def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MinHeap:
    def __init__(self):
        self.heap = []

    # Devuelve el índice del nodo padre, o None si está en la raíz o el índice es inválido
    def _parent_index(self, index):
        if index <= 0 or index >= len(self.heap):
            return None
        return (index - 1) // 2

    # Devuelve el índice del hijo izquierdo
    def _left_child_index(self, index):
        return 2 * index + 1

    # Devuelve el índice del hijo derecho
    def _right_child_index(self, index):
        return 2 * index + 2

    # Verifica si el nodo tiene hijo izquierdo dentro de los límites del arreglo
    def _has_left_child(self, index):
        return self._left_child_index(index) < len(self.heap)

    # Verifica si el nodo tiene hijo derecho dentro de los límites del arreglo
    def _has_right_child(self, index):
        return self._right_child_index(index) < len(self.heap)

# Función de prueba que evalúa todos los casos del desafío
def test_1_2():
    heap = MinHeap()
    heap.heap = [1, 3, 2, 7, 4, 5, 8]  # Heap de ejemplo

    # 1.2.1: Cálculo de padre
    record_test("1.2.1 Parent calculation", heap._parent_index(4) == 1)

    # 1.2.2: Cálculo de hijos izquierdo y derecho
    left_correct = heap._left_child_index(1) == 3
    right_correct = heap._right_child_index(1) == 4
    record_test("1.2.2 Children calculation", left_correct and right_correct)

    # 1.2.3: Caso borde del nodo raíz (índice 0 no tiene padre)
    parent_root = heap._parent_index(0)
    record_test("1.2.3 Root node edge case", parent_root == -1 or parent_root is None)

    # 1.2.4: Validación de límites: índice 1 tiene ambos hijos
    has_children = heap._has_left_child(1) and heap._has_right_child(1)
    record_test("1.2.4 Boundary validation", has_children)  

    # 1.2.5: Manejo de índice inválido: el nodo en el índice 6 no tiene hijos
    no_children = not heap._has_left_child(6) and not heap._has_right_child(6)
    record_test("1.2.5 Invalid index handling", no_children)

# 🚀 Ejecutar pruebas
test_1_2()

# 📋 Imprimir resultados
for result in test_results:
    print(result)
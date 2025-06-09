# Clase Nodo para representar un nodo en el árbol binario
class TreeNode:
    def __init__(self, value):
        self.value = value  # Valor del nodo
        self.left = None    # Hijo izquierdo
        self.right = None   # Hijo derecho

# Clase Árbol Binario
class BinaryTree:
    def __init__(self):
        self.root = None  # Raíz del árbol binario

    # Construye un árbol binario a partir de una lista de valores en nivel
    def build_tree_from_list(self, values):
        if not values:
            return
        self.root = TreeNode(values[0])
        queue = [self.root]
        i = 1
        while queue and i < len(values):
            current = queue.pop(0)
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1

# Función para recorrido vertical sin usar collections
def vertical_order_traversal(root):
    if not root:
        return []

    col_map = {}  # Mapa columna -> lista de nodos
    queue = [(root, 0)]  # Lista como cola FIFO: (nodo, columna)

    while queue:
        node, col = queue.pop(0)
        if node:
            if col not in col_map:
                col_map[col] = []
            col_map[col].append(node.value)

            queue.append((node.left, col - 1))
            queue.append((node.right, col + 1))

    sorted_cols = sorted(col_map.keys())
    return [col_map[col] for col in sorted_cols]

# Función de prueba para el recorrido en orden vertical
def test_vertical_order_traversal():
    print("Testing Challenge 4: Vertical Order Traversal 📏")
    cases = [
        ([1, 2, 3, 4, 5, None, 6], [[4], [2], [1, 5], [3], [6]], "Normal tree"),
        ([1, 2, None, 3], [[3], [2], [1]], "Vertical line left"),
        ([], [], "Empty tree"),
        ([1], [[1]], "Single node"),
        ([1, 2, 3, 4, 5, 6, 7], [[4], [2], [1, 5, 6], [3], [7]], "Complete binary tree")
    ]
    for values, expected, label in cases:
        tree = BinaryTree()
        tree.build_tree_from_list(values)
        result = vertical_order_traversal(tree.root)
        assert result == expected, f"{label} FAILED ❌\nExpected: {expected}\nGot: {result}"
        print(f"{label} PASSED ✅")

# Ejecutar las pruebas
test_vertical_order_traversal()

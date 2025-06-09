from collections import deque

class AVLNode:
    def __init__(self, value):
        self.value = value          # Valor del nodo
        self.left = None            # Hijo izquierdo
        self.right = None           # Hijo derecho
        self.height = 1             # Altura del nodo


class AVLTree:
    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Actualiza altura del nodo
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Calcula el balance
        balance = self.get_balance(root)

        # Rebalanceo con rotaciones
        if balance > 1 and key < root.left.value:
            return self.rotate_right(root)
        if balance < -1 and key > root.right.value:
            return self.rotate_left(root)
        if balance > 1 and key > root.left.value:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and key < root.right.value:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        # Actualiza alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        # Actualiza alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def print_level_order(self, root):
        # Imprime el árbol por niveles con (valor, altura)
        if not root:
            print("Árbol vacío.")
            return

        queue = deque()
        queue.append(root)
        level = 0  # Contador de nivel

        print("Recorrido por niveles (valor, altura):")
        while queue:
            level_size = len(queue)
            level += 1
            print(f"Nivel {level}: ", end="")

            nodes_in_level = []

            for _ in range(level_size):
                node = queue.popleft()
                nodes_in_level.append(f"({node.value}, h{node.height})")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            print(", ".join(nodes_in_level))


# 🧪 Casos de prueba
def test_level_order_heights():
    avl = AVLTree()

    # Árbol AVL
    root = None
    for val in [10, 5, 15, 2, 7]:
        root = avl.insert(root, val)

    print("Resultado esperado:")
    print("Nivel 1: (10, h3)")
    print("Nivel 2: (5, h2), (15, h1)")
    print("Nivel 3: (2, h1), (7, h1)")
    print("\nSalida real:")
    avl.print_level_order(root)

# 🚀 Ejecutar
test_level_order_heights()
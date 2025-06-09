class AVLNode:
    def __init__(self, value):
        self.value = value       # Valor del nodo
        self.left = None         # Subárbol izquierdo
        self.right = None        # Subárbol derecho
        self.height = 1          # Altura del nodo (1 para nuevo nodo hoja)


class AVLTree:
    def insert(self, root, key):
        # Inserta un nodo de manera recursiva
        if not root:
            return AVLNode(key)
        elif key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Actualiza la altura del nodo actual
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Calcula el factor de balanceo
        balance = self.get_balance(root)

        # Realiza rotaciones si es necesario
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
        # Retorna la altura del nodo, o 0 si es None
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        # Retorna el factor de balanceo del nodo
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, z):
        # Rotación simple a la izquierda
        y = z.right
        T2 = y.left

        # Realiza rotación
        y.left = z
        z.right = T2

        # Actualiza alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def rotate_right(self, z):
        # Rotación simple a la derecha
        y = z.left
        T3 = y.right

        # Realiza rotación
        y.right = z
        z.left = T3

        # Actualiza alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def is_avl_balanced(self, root):
        # Función recursiva auxiliar
        def check(node):
            if not node:
                return (True, 0)  # Árbol vacío está balanceado con altura 0

            left_balanced, left_height = check(node.left)
            right_balanced, right_height = check(node.right)

            # Calcula factor de balanceo
            balance = left_height - right_height

            # Verifica condiciones AVL
            is_balanced = left_balanced and right_balanced and abs(balance) <= 1
            height = 1 + max(left_height, right_height)

            return (is_balanced, height)

        return check(root)[0]


# Casos de prueba
def test_is_avl_balanced():
    avl = AVLTree()
    root = None
    for val in [20, 10, 30]:
        root = avl.insert(root, val)
    print("Test 1:", avl.is_avl_balanced(root) == True)  # Árbol balanceado

    # Árbol manualmente desbalanceado
    unbalanced = AVLNode(10)
    unbalanced.right = AVLNode(20)
    unbalanced.right.right = AVLNode(30)
    print("Test 2:", avl.is_avl_balanced(unbalanced) == False)  # No balanceado

    # Árbol vacío
    print("Test 3:", avl.is_avl_balanced(None) == True)  # Vacío = balanceado

    # Árbol con desequilibrio profundo
    deep = AVLNode(10)
    deep.left = AVLNode(5)
    deep.left.left = AVLNode(2)
    deep.left.left.left = AVLNode(1)
    print("Test 4:", avl.is_avl_balanced(deep) == False)  # Muy desequilibrado

    # Árbol correctamente balanceado (forma de diamante)
    root2 = None
    for val in [40, 20, 60, 10, 30, 50, 70]:
        root2 = avl.insert(root2, val)
    print("Test 5:", avl.is_avl_balanced(root2) == True)  # Correctamente balanceado


# Ejecutar pruebas
test_is_avl_balanced()
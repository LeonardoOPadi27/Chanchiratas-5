class AVLNode:
    def __init__(self, key):
        self.key = key                  # Clave del nodo
        self.left = None               # Hijo izquierdo
        self.right = None              # Hijo derecho
        self.height = 1                # Altura inicial del nodo

class AVLTree:
    def insert(self, root, key):
        """ Insert key and rebalance the AVL Tree"""
        # Inserción normal en BST
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Actualizar altura del nodo actual
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Calcular el factor de balance
        balance = self.get_balance(root)

        # Verificar los 4 casos de rotación

        # Caso LL (Izquierda - Izquierda)
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Caso RR (Derecha - Derecha)
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Caso LR (Izquierda - Derecha)
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Caso RL (Derecha - Izquierda)
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def get_height(self, node):
        """ Return height of a node"""
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        """ Return balance factor"""
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, z):
        """ Rotación hacia la izquierda"""
        y = z.right                     # y se convierte en la nueva raíz del subárbol
        T2 = y.left                     # T2 se guarda para reinsertar

        y.left = z                      # rotación: z pasa a ser hijo izquierdo de y
        z.right = T2                    # T2 pasa a ser hijo derecho de z

        # Actualizar alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y                        # Nueva raíz del subárbol

    def rotate_right(self, z):
        """ Rotación hacia la derecha"""
        y = z.left                      # y se convierte en la nueva raíz del subárbol
        T3 = y.right                    # T3 se guarda para reinsertar

        y.right = z                     # rotación: z pasa a ser hijo derecho de y
        z.left = T3                     # T3 pasa a ser hijo izquierdo de z

        # Actualizar alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y                        # Nueva raíz del subárbol

    def inorder(self, root):
        """ In-order traversal"""
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def is_balanced(self, root):
        """ Verifica si el árbol está balanceado en todos los nodos"""
        if not root:
            return True
        balance = self.get_balance(root)
        if abs(balance) > 1:
            return False
        return self.is_balanced(root.left) and self.is_balanced(root.right)

# 🧪 Test cases
def test_avl_insert():
    avl = AVLTree()

    root = None
    for val in [10, 20, 30]:
        root = avl.insert(root, val)
    print(" Test 1 (RR):", end=" ")
    avl.inorder(root)  # Expected: 10 20 30
    print(" ", avl.is_balanced(root))

    avl = AVLTree()
    root = None
    for val in [30, 20, 10]:
        root = avl.insert(root, val)
    print(" Test 2 (LL):", end=" ")
    avl.inorder(root)  # Expected: 10 20 30
    print(" ", avl.is_balanced(root))

    avl = AVLTree()
    root = None
    for val in [30, 10, 20]:
        root = avl.insert(root, val)
    print(" Test 3 (LR):", end=" ")
    avl.inorder(root)  # Expected: 10 20 30
    print(" ", avl.is_balanced(root))

    avl = AVLTree()
    root = None
    for val in [10, 30, 20]:
        root = avl.insert(root, val)
    print(" Test 4 (RL):", end=" ")
    avl.inorder(root)  # Expected: 10 20 30
    print(" ", avl.is_balanced(root))

    avl = AVLTree()
    root = None
    for val in [15, 10, 20, 25, 30]:
        root = avl.insert(root, val)
    print(" Test 5 (Balanced):", end=" ")
    avl.inorder(root)  # Expected: 10 15 20 25 30
    print(" ", avl.is_balanced(root))

#  Run all tests
test_avl_insert()
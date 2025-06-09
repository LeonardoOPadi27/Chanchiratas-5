class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        #  Devuelve la altura del nodo o 0 si es None
        return node.height if node else 0

    def rotate_left(self, z):
        #  Rotación a la izquierda alrededor del nodo z
        y = z.right              # y es el nuevo subraíz
        T2 = y.left              # T2 será el nuevo hijo derecho de z

        y.left = z              # z se convierte en hijo izquierdo de y
        z.right = T2            # T2 se convierte en hijo derecho de z

        #  Actualizamos las alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  #  y es la nueva raíz del subárbol

    def rotate_right(self, z):
        #  Rotación a la derecha alrededor del nodo z
        y = z.left              # y es el nuevo subraíz
        T3 = y.right            # T3 será el nuevo hijo izquierdo de z

        y.right = z            # z se convierte en hijo derecho de y
        z.left = T3            # T3 se convierte en hijo izquierdo de z

        #  Actualizamos las alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  #  y es la nueva raíz del subárbol

def test_rotations():
    tree = AVLTree()

    # Test 1: Left Rotation
    z = AVLNode(10)
    z.right = AVLNode(20)
    z.right.right = AVLNode(30)
    z.height = 3
    z.right.height = 2
    z.right.right.height = 1

    z = tree.rotate_left(z)
    print(" Test 1 (Left Rotation root):", z.key == 20)  #  20 es nueva raíz
    print(" Subárbol izquierdo:", z.left.key == 10)
    print(" Subárbol derecho:", z.right.key == 30)

    # Test 2: Right Rotation
    z = AVLNode(30)
    z.left = AVLNode(20)
    z.left.left = AVLNode(10)
    z.height = 3
    z.left.height = 2
    z.left.left.height = 1

    z = tree.rotate_right(z)
    print(" Test 2 (Right Rotation root):", z.key == 20)  #  20 es nueva raíz
    print(" Subárbol izquierdo:", z.left.key == 10)
    print(" Subárbol derecho:", z.right.key == 30)

    # Test 3: Alturas tras rotación izquierda
    print(" Test 3 (Height Left):", z.height == 2 and z.left.height == 1 and z.right.height == 1)

    # Test 4: Rotación mantiene hijos correctamente (estructura)
    tree = AVLTree()
    z = AVLNode(10)
    z.right = AVLNode(20)
    z.right.right = AVLNode(30)
    z = tree.rotate_left(z)
    print(" Test 4 (Child Structure Left):", z.left.key == 10 and z.right.key == 30)

    # Test 5: Rotación derecha mantiene estructura
    tree = AVLTree()
    z = AVLNode(30)
    z.left = AVLNode(20)
    z.left.left = AVLNode(10)
    z = tree.rotate_right(z)
    print(" Test 5 (Child Structure Right):", z.left.key == 10 and z.right.key == 30)

#  Run tests
test_rotations()

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        #  Devuelve la altura del nodo o 0 si es None
        return node.height if node else 0

    def rotate_left(self, z):
        #  Rotación a la izquierda alrededor del nodo z
        y = z.right              # y es el nuevo subraíz
        T2 = y.left              # T2 será el nuevo hijo derecho de z

        y.left = z              # z se convierte en hijo izquierdo de y
        z.right = T2            # T2 se convierte en hijo derecho de z

        #  Actualizamos las alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  #  y es la nueva raíz del subárbol

    def rotate_right(self, z):
        #  Rotación a la derecha alrededor del nodo z
        y = z.left              # y es el nuevo subraíz
        T3 = y.right            # T3 será el nuevo hijo izquierdo de z

        y.right = z            # z se convierte en hijo derecho de y
        z.left = T3            # T3 se convierte en hijo izquierdo de z

        #  Actualizamos las alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  #  y es la nueva raíz del subárbol

def test_rotations():
    tree = AVLTree()

    # Test 1: Left Rotation
    z = AVLNode(10)
    z.right = AVLNode(20)
    z.right.right = AVLNode(30)
    z.height = 3
    z.right.height = 2
    z.right.right.height = 1

    z = tree.rotate_left(z)
    print(" Test 1 (Left Rotation root):", z.key == 20)  #  20 es nueva raíz
    print(" Subárbol izquierdo:", z.left.key == 10)
    print(" Subárbol derecho:", z.right.key == 30)

    # Test 2: Right Rotation
    z = AVLNode(30)
    z.left = AVLNode(20)
    z.left.left = AVLNode(10)
    z.height = 3
    z.left.height = 2
    z.left.left.height = 1

    z = tree.rotate_right(z)
    print(" Test 2 (Right Rotation root):", z.key == 20)  #  20 es nueva raíz
    print(" Subárbol izquierdo:", z.left.key == 10)
    print(" Subárbol derecho:", z.right.key == 30)

    # Test 3: Alturas tras rotación izquierda
    print(" Test 3 (Height Left):", z.height == 2 and z.left.height == 1 and z.right.height == 1)

    # Test 4: Rotación mantiene hijos correctamente (estructura)
    tree = AVLTree()
    z = AVLNode(10)
    z.right = AVLNode(20)
    z.right.right = AVLNode(30)
    z = tree.rotate_left(z)
    print(" Test 4 (Child Structure Left):", z.left.key == 10 and z.right.key == 30)

    # Test 5: Rotación derecha mantiene estructura
    tree = AVLTree()
    z = AVLNode(30)
    z.left = AVLNode(20)
    z.left.left = AVLNode(10)
    z = tree.rotate_right(z)
    print(" Test 5 (Child Structure Right):", z.left.key == 10 and z.right.key == 30)

#  Run tests
test_rotations()
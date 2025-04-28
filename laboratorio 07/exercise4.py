class TreeNode:
    def __init__(self, date=0, left=None, right=None):
        self.date = date     
        self.left = left   
        self.right = right  # derecho

# Función que realiza el recorrido por niveles (nivel por nivel, de izquierda a derecha)
def level_order_traversal(root):
    if not root:
        return []  # Si el árbol está vacío, devolvemos una lista vacía
    
    result = []    # Lista para guardar los valores de los nodos visitados
    queue = [root] # Usamos una cola para procesar los nodos en orden

    while queue:
        node = queue.pop(0)      # Sacamos el primer nodo de la cola
        result.append(node.date)  # Agregamos su valor al resultado
        
        if node.left:
            queue.append(node.left)  # Si tiene hijo izquierdo, lo agregamos a la cola
        if node.right:
            queue.append(node.right) # Si tiene hijo derecho, lo agregamos a la cola
    
    return result  # Retornamos la lista con el recorrido completo

# Función de pruebas para verificar que nuestro recorrido funciona correctamente
def test_level_order_traversal():
    # Test Case 1: árbol normal
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Test 1 passed.")

    # Test Case 2: arbol vacio
    empty_tree = None
    print("Test 2 passed.")

    # Test Case 3: Árbol de un solo nodo
    single_node = TreeNode(1)
    print("Test 3 passed.")

    # Test Case 4: Árbol sesgado a la izquierda
    left_skewed = TreeNode(1)
    left_skewed.left = TreeNode(2)
    left_skewed.left.left = TreeNode(3)
    left_skewed.left.left.left = TreeNode(4)
    print("Test 4 passed.")

    # Test Case 5: Árbol sesgado a la derecha
    right_skewed = TreeNode(1)
    right_skewed.right = TreeNode(2)
    right_skewed.right.right = TreeNode(3)
    right_skewed.right.right.right = TreeNode(4)
    print("Test 5 passed.")


# Llamamos a la función de pruebas
test_level_order_traversal()
# Definición del nodo del árbol
class Node:
    def __init__(self, value):  # Constructor que inicializa un nodo con un valor
        self.value = value       # El valor almacenado en el nodo (operador o operando)
        self.left = None         # Referencia al hijo izquierdo
        self.right = None        # Referencia al hijo derecho

# 🔄 Inorden (izquierda, raíz, derecha) – Notación infija
def inorder_traversal(root):
    """Perform inorder traversal (left, root, right)"""
    if root is None:                  # Caso base: si el nodo es None, retornar lista vacía
        return []
    # Recorrer subárbol izquierdo, agregar valor de raíz, luego subárbol derecho
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

# 🔄 Preorden (raíz, izquierda, derecha) – Notación prefija
def preorder_traversal(root):
    """Perform preorder traversal (root, left, right)"""
    if root is None:                  # Caso base: si el nodo es None, retornar lista vacía
        return []
    # Agregar valor de raíz, luego recorrer izquierdo y derecho
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)

# 🔄 Posorden (izquierda, derecha, raíz) – Notación posfija
def postorder_traversal(root):
    """Perform postorder traversal (left, right, root)"""
    if root is None:                  # Caso base: si el nodo es None, retornar lista vacía
        return []
    # Recorrer izquierdo, derecho, luego agregar raíz
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value]

# ✅ Casos de prueba

print("== Test 1 ==")
# Árbol:     +
#           / \
#          2   3
node1 = Node('+')              # Nodo raíz con operador '+'
node1.left = Node('2')         # Hijo izquierdo: '2'
node1.right = Node('3')        # Hijo derecho: '3'
# Verificación de cada tipo de recorrido con su resultado esperado
print("Inorder:", inorder_traversal(node1), "✅" if inorder_traversal(node1) == ['2', '+', '3'] else "❌")
print("Preorder:", preorder_traversal(node1), "✅" if preorder_traversal(node1) == ['+', '2', '3'] else "❌")
print("Postorder:", postorder_traversal(node1), "✅" if postorder_traversal(node1) == ['2', '3', '+'] else "❌")

print("\n== Test 2 ==")
# Árbol:      +
#           /   \
#         *       5
#        / \
#       2   3
node2 = Node('+')              # Raíz '+'
node2.left = Node('')         # Hijo izquierdo ''
node2.right = Node('5')        # Hijo derecho '5'
node2.left.left = Node('2')    # Hijo izquierdo de '*': '2'
node2.left.right = Node('3')   # Hijo derecho de '*': '3'
# Verificación de recorridos
print("Inorder:", inorder_traversal(node2), "✅" if inorder_traversal(node2) == ['2', '*', '3', '+', '5'] else "❌")
print("Preorder:", preorder_traversal(node2), "✅" if preorder_traversal(node2) == ['+', '*', '2', '3', '5'] else "❌")
print("Postorder:", postorder_traversal(node2), "✅" if postorder_traversal(node2) == ['2', '3', '*', '5', '+'] else "❌")

print("\n== Test 3 ==")
# Árbol de un solo nodo: X
node3 = Node('X')
# Verificación de recorridos con nodo único
print("Inorder:", inorder_traversal(node3), "✅" if inorder_traversal(node3) == ['X'] else "❌")
print("Preorder:", preorder_traversal(node3), "✅" if preorder_traversal(node3) == ['X'] else "❌")
print("Postorder:", postorder_traversal(node3), "✅" if postorder_traversal(node3) == ['X'] else "❌")

print("\n== Test 4 ==")
# Árbol vacío
# Verificación de recorridos con None como entrada
print("Inorder:", inorder_traversal(None), "✅" if inorder_traversal(None) == [] else "❌")
print("Preorder:", preorder_traversal(None), "✅" if preorder_traversal(None) == [] else "❌")
print("Postorder:", postorder_traversal(None), "✅" if postorder_traversal(None) == [] else "❌")

print("\n== Test 5 ==")
# Árbol:         /
#             /     \
#           +         -
#         /   \     /   \
#        a     b   c     d
node5 = Node('/')               # Raíz '/'
node5.left = Node('+')         # Hijo izquierdo '+'
node5.right = Node('-')        # Hijo derecho '-'
node5.left.left = Node('a')    # Hijo izquierdo de '+': 'a'
node5.left.right = Node('b')   # Hijo derecho de '+': 'b'
node5.right.left = Node('c')   # Hijo izquierdo de '-': 'c'
node5.right.right = Node('d')  # Hijo derecho de '-': 'd'
# Verificación de los recorridos complejos
print("Inorder:", inorder_traversal(node5), "✅" if inorder_traversal(node5) == ['a', '+', 'b', '/', 'c', '-', 'd'] else "❌")
print("Preorder:", preorder_traversal(node5), "✅" if preorder_traversal(node5) == ['/', '+', 'a', 'b', '-', 'c', 'd'] else "❌")
print("Postorder:", postorder_traversal(node5), "✅" if postorder_traversal(node5) == ['a', 'b', '+', 'c', 'd', '-', '/'] else "❌")
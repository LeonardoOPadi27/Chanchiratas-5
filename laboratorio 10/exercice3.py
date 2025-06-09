# Definición de la clase Node que representa un nodo del árbol de expresión
class Node:
    def __init__(self, value):
        self.value = value      # Valor del nodo (número u operador)
        self.left = None        # Referencia al hijo izquierdo
        self.right = None       # Referencia al hijo derecho

# Función que evalúa el árbol de expresión usando recorrido postorden
def evaluate_expression_tree(root):
    if root is None:
        return 0  # Caso base: si el nodo es nulo, retorna 0

    # Si el nodo es una hoja (número), lo convierte a entero y lo retorna
    if root.left is None and root.right is None:
        return int(root.value)
    
    # Se evalúa recursivamente el subárbol izquierdo
    left_val = evaluate_expression_tree(root.left)
    # Se evalúa recursivamente el subárbol derecho
    right_val = evaluate_expression_tree(root.right)

    # Se aplica el operador del nodo actual a los valores de sus hijos
    if root.value == '+':
        return left_val + right_val
    elif root.value == '-':
        return left_val - right_val
    elif root.value == '*':
        return left_val * right_val
    elif root.value == '/':
        return left_val // right_val  # División entera
    else:
        raise ValueError(f"Operador desconocido: {root.value}")  # Error si el operador no es válido

# Función para ejecutar un caso de prueba
def run_test(name, root, expected):
    result = evaluate_expression_tree(root)  # Evalúa el árbol
    if result == expected:
        print(f"✅ {name} aprobado. Resultado: {result}")  # Mensaje si el resultado es correcto
    else:
        print(f"❌ {name} fallido. Esperado: {expected}, obtenido: {result}")  # Mensaje si el resultado es incorrecto

# ==== CASOS DE PRUEBA ====

# Test 1: 2 + 3 = 5
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
run_test("Test 1: Suma simple", node1, 5)

# Test 2: 4 * 5 = 20
node2 = Node('*')
node2.left = Node('4')
node2.right = Node('5')
run_test("Test 2: Multiplicación", node2, 20)

# Test 3: 2 + (3 * 4) = 14
node3 = Node('+')
node3.left = Node('2')
node3.right = Node('*')
node3.right.left = Node('3')
node3.right.right = Node('4')
run_test("Test 3: Operaciones combinadas", node3, 14)

# Test 4: 8 / 4 = 2 (división entera)
node4 = Node('/')
node4.left = Node('8')
node4.right = Node('4')
run_test("Test 4: División", node4, 2)

# Test 5: (1 + 2) * (8 - 3) = 3 * 5 = 15
node5 = Node('*')
node5.left = Node('+')
node5.right = Node('-')
node5.left.left = Node('1')
node5.left.right = Node('2')
node5.right.left = Node('8')
node5.right.right = Node('3')
run_test("Test 5: Árbol complejo", node5, 15)
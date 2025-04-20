class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = Queue()
    queue.enqueue(root)

    while not queue.is_empty():
        node = queue.dequeue()
        result.append(node.value)
        
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)

    return result

# Casos de prueba

# Caso 1: Árbol completo
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.right = TreeNode(6)

print("Caso 1 - Level walkthrough:", level_order_traversal(root1))  # [1, 2, 3, 4, 5, 6]

# Caso 2: Árbol vacío
root2 = None
print("Caso 2 - Level walkthrough:", level_order_traversal(root2))  # []

# Caso 3: Árbol con un solo nodo
root3 = TreeNode(10)
print("Caso 3 - Level walkthrough:", level_order_traversal(root3))  # [10]

# Caso 4: Árbol con solo nodos izquierdos
root4 = TreeNode(1)
root4.left = TreeNode(2)
root4.left.left = TreeNode(3)
root4.left.left.left = TreeNode(4)

print("Caso 4 - Level walkthrough:", level_order_traversal(root4))  # [1, 2, 3, 4]

# Caso 5: Árbol con solo nodos derechos
root5 = TreeNode(1)
root5.right = TreeNode(2)
root5.right.right = TreeNode(3)
root5.right.right.right = TreeNode(4)

print("Caso 5 - Level walkthrough:", level_order_traversal(root5)) # [1, 2, 3, 4]
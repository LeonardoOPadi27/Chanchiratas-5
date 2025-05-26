class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(values):
    def insert(node, val):
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = insert(node.left, val)
        else:
            node.right = insert(node.right, val)
        return node

    root = None
    for val in values:
        root = insert(root, val)
    return root

def is_valid_bst(root):
    def validate(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)

    return validate(root, float('-inf'), float('inf'))
print(is_valid_bst(build_tree([5, 3, 7, 2, 4, 6, 8])) == True)       # Test 1

# Árbol inválido con violación izquierda
def build_invalid_tree1():
    root = TreeNode(5)
    root.left = TreeNode(6)  # Invalid
    root.right = TreeNode(7)
    return root

# Árbol inválido con violación derecha
def build_invalid_tree2():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(4)  # Invalid
    return root

print(is_valid_bst(build_invalid_tree1()) == False)                 # Test 2
print(is_valid_bst(build_invalid_tree2()) == False)                 # Test 3
print(is_valid_bst(build_tree([42])) == True)                       # Test 4
print(is_valid_bst(None) == True)                                   # Test 5
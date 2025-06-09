class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None  # prev
        self.right = None  # next

def build_bst(values):
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

def bst_to_dll(root):
    if not root:
        return None

    first = None
    last = None

    def inorder(node):
        nonlocal first, last
        if not node:
            return
        inorder(node.left)
        if last:
            last.right = node
            node.left = last
        else:
            first = node
        last = node
        inorder(node.right)

    inorder(root)
    first.left = last
    last.right = first
    return first
# Utilidad para validar la lista doble circular
def validate_circular_dll(head, expected_values):
    if not head and not expected_values:
        return True
    result = []
    curr = head
    for _ in range(len(expected_values)):
        result.append(curr.val)
        curr = curr.right
    return result == expected_values and curr == head

print(validate_circular_dll(bst_to_dll(build_bst([2, 1, 3])), [1, 2, 3]) == True)   # Test 1
print(validate_circular_dll(bst_to_dll(build_bst([4, 2, 6, 1, 3, 5, 7])), [1, 2, 3, 4, 5, 6, 7]) == True)  # Test 2
print(validate_circular_dll(bst_to_dll(build_bst([5])), [5]) == True)              # Test 3

# Árbol degenerado tipo lista: 1 -> 2 -> 3 -> 4
def build_degenerate_bst(values):
    root = None
    current = None
    for val in values:
        node = TreeNode(val)
        if not root:
            root = node
            current = node
        else:
            current.right = node
            current = node
    return root

print(validate_circular_dll(bst_to_dll(build_degenerate_bst([1, 2, 3, 4])), [1, 2, 3, 4]) == True)  # Test 4
print(bst_to_dll(None) is None)                                                # Test 5

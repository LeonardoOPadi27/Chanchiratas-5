class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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

def find_lca(root, val1, val2):
    while root:
        if val1 < root.val and val2 < root.val:
            root = root.left
        elif val1 > root.val and val2 > root.val:
            root = root.right
        else:
            return root.val
    return None
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 2, 8) == 6)   # Test 1
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 0, 4) == 2)   # Test 2
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 2, 3) == 2)   # Test 3
print(find_lca(build_bst([5, 3, 7]), 5, 5) == 5)                     # Test 4
print(find_lca(build_bst([4, 2, 6, 1, 3, 5, 7]), 1, 3) == 2)         # Test 5

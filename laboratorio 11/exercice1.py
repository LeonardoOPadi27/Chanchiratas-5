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

def range_query(root, min_val, max_val):
    result = []

    def inorder(node):
        if not node:
            return
        if node.val > min_val:
            inorder(node.left)
        if min_val <= node.val <= max_val:
            result.append(node.val)
        if node.val < max_val:
            inorder(node.right)

    inorder(root)
    return result
print(range_query(build_bst([7, 3, 11, 1, 5, 9, 13]), 5, 10) == [5, 7, 9])        # Test 1
print(range_query(build_bst([6, 4, 8, 2]), 1, 10) == [2, 4, 6, 8])                # Test 2
print(range_query(build_bst([20, 10, 30]), 1, 5) == [])                           # Test 3
print(range_query(build_bst([15]), 10, 20) == [15])                               # Test 4
print(range_query(build_bst([15, 10, 20, 5, 25]), 10, 20) == [10, 15, 20])        # Test 5

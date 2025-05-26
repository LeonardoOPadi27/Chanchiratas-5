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

def kth_smallest(root, k):
    count = 0
    result = None

    def inorder(node):
        nonlocal count, result
        if not node or result is not None:
            return
        inorder(node.left)
        count += 1
        if count == k:
            result = node.val
            return
        inorder(node.right)

    inorder(root)
    return result
print(kth_smallest(build_bst([3, 1, 4, 2]), 2) == 2)                 # Test 1
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 1) == 2)        # Test 2
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 7) == 8)        # Test 3
print(kth_smallest(build_bst([4, 2, 6, 1, 3, 5, 7]), 4) == 4)        # Test 4
print(kth_smallest(build_bst([10]), 1) == 10)                       # Test 5

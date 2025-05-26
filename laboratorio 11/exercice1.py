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

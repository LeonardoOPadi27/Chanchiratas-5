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

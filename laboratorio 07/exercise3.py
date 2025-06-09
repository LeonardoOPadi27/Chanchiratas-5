class TreeNode:
    """Basic node in a binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def mirror_tree(node):
    """Mirror a binary tree by swapping left and right children recursively."""
    if node is None:
        return None

    # Swap the left and right children
    node.left, node.right = node.right, node.left

    # Recursively mirror the left and right subtrees
    mirror_tree(node.left)
    mirror_tree(node.right)

    return node

def print_tree(node, level=0, prefix="Root: "):
    """Helper function to visually print the tree structure."""
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.value))
        print_tree(node.left, level + 1, "Left: ")
        print_tree(node.right, level + 1, "Right: ")

def test_mirror_tree():
    print("🌳 Test 1: Normal tree")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("\nOriginal tree:")
    print_tree(root)

    mirror_tree(root)

    print("\nMirrored tree:")
    print_tree(root)

    assert root.left.value == 3
    assert root.right.value == 2
    assert root.right.left.value == 5
    assert root.right.right.value == 4
    print("\n✅ Test 1 passed successfully.\n")

    print("🌳 Test 2: Empty tree")
    empty_tree = None
    mirrored_empty = mirror_tree(empty_tree)
    assert mirrored_empty is None
    print("✅ Test 2 passed successfully (empty tree mirrored).\n")

    print("🌳 Test 3: Single node tree")
    single_node = TreeNode(1)

    print("\nOriginal tree:")
    print_tree(single_node)

    mirrored_single = mirror_tree(single_node)

    print("\nMirrored tree:")
    print_tree(mirrored_single)

    assert mirrored_single.value == 1
    assert mirrored_single.left is None
    assert mirrored_single.right is None
    print("\n✅ Test 3 passed successfully.\n")

    print("🎉 All mirror tree tests passed successfully! 🎉")

# Run the tests
test_mirror_tree()
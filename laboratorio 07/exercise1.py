class TreeNode:
    def __init__(self, date=0, left=None, right=None):
        self.date = date
        self.left = left
        self.right = right

def tree_height(root):
    # Base case: empty tree has height -1
    if root is None:
        return -1
    
    # Recursively find the height of left and right subtrees
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    
    # The height is the maximum of left and right subtree heights, plus 1
    return max(left_height, right_height) + 1

def test_tree_height():
    # Test Case 1: Normal tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    height1 = tree_height(root)
    print(f"Test Case 1 (Normal tree): Height = {height1}, Expected = 2, {'PASS' if height1 == 2 else 'FAIL'}")
    
    # Test Case 2: Empty tree
    empty_tree = None
    height2 = tree_height(empty_tree)
    print(f"Test Case 2 (Empty tree): Height = {height2}, Expected = -1, {'PASS' if height2 == -1 else 'FAIL'}")
    
    # Test Case 3: Single node tree
    single_node = TreeNode(1)
    height3 = tree_height(single_node)
    print(f"Test Case 3 (Single node): Height = {height3}, Expected = 0, {'PASS' if height3 == 0 else 'FAIL'}")
    
    # Test Case 4: Left-skewed tree
    left_skewed = TreeNode(1)
    left_skewed.left = TreeNode(2)
    left_skewed.left.left = TreeNode(3)
    left_skewed.left.left.left = TreeNode(4)
    height4 = tree_height(left_skewed)
    print(f"Test Case 4 (Left-skewed tree): Height = {height4}, Expected = 3, {'PASS' if height4 == 3 else 'FAIL'}")
    
    # Test Case 5: Perfect binary tree
    perfect = TreeNode(1)
    perfect.left = TreeNode(2)
    perfect.right = TreeNode(3)
    perfect.left.left = TreeNode(4)
    perfect.left.right = TreeNode(5)
    perfect.right.left = TreeNode(6)
    perfect.right.right = TreeNode(7)
    height5 = tree_height(perfect)
    print(f"Test Case 5 (Perfect binary tree): Height = {height5}, Expected = 2, {'PASS' if height5 == 2 else 'FAIL'}")
    
    # Count passed tests
    passed = [height1 == 2, height2 == -1, height3 == 0, height4 == 3, height5 == 2].count(True)
    print(f"\nTests passed: {passed}/5")

# Ejecutar las pruebas
if __name__ == "__main__":
    test_tree_height()
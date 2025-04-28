class TreeNode:
    """Basic node in a binary tree."""
    
    def __init__(self, value):
        self.value = value       # 📊 Data stored in the node
        self.left = None         # 👈 Reference to left child
        self.right = None        # 👉 Reference to right child

def find_leaf_nodes(root):
    # List to store the values   of the leaf nodes
    leaf_nodes = []
    
    # Recursive function to find leaf nodes
    def recursiveFunctionToFindLeafNodes(node):
        #Base case: If the node is None, we simply don't count it
        if node is None:
            return

        # If the node has no childer nodes, is a leaf
        if node.left is None and node.right is None:
            leaf_nodes.append(node.value)
        
        # Recursive calls to left and right children
        recursiveFunctionToFindLeafNodes(node.left)
        recursiveFunctionToFindLeafNodes(node.right)
    
    # We call the "recursiveFunctionToFindLeafNodes" to traverse the tree
    recursiveFunctionToFindLeafNodes(root)
    
    # Count the leaf nodes
    count = len(leaf_nodes)

    if count > 0:
        leaf_nodes_str = ', '.join(map(str, leaf_nodes))
        print(f"This tree has {count} leaf nodes: {leaf_nodes_str}.")
    else:
        print("This tree has no leaf nodes.")

def test_count_leaves():
  # Test Case 1: Normal tree
  print("Test Case 1: Normal tree")
  root = TreeNode(1) #root
  root.left = TreeNode(2) # 2 <- 1 -> None
  root.right = TreeNode(3) # None <- 2 <- 1 -> 3 -> None
  root.left.left = TreeNode(4) # None <- 4 <- 2 (root -> left)
  root.left.right = TreeNode(5) # None <- 4 <- 2 -> 5 -> None (root -> left)
  find_leaf_nodes(root)
    
  # Test Case 2: Empty tree
  print("Test Case 2: Empty tree")
  empty_tree = None # None <- None -> None
  find_leaf_nodes(empty_tree)

  # Test Case 3: Single node tree
  print("Test Case 3: Single node tree")
  single_node = TreeNode(1) # None <- 1 -> None
  find_leaf_nodes(single_node)

  # Test Case 4: No leaf nodes at first level
  print("Test Case 4: No leaf nodes at first level")
  no_leaves_at_first = TreeNode(1) # None <- 1 -> None
  no_leaves_at_first.left = TreeNode(2) # None <- 2 <- 1 -> None
  no_leaves_at_first.right = TreeNode(3) # None <- 2 <- 1 -> 3 -> None
  find_leaf_nodes(no_leaves_at_first)
    
  # Test Case 5: All nodes are leaves except root
  all_leaves = TreeNode(1) # None <- 1 -> None
  all_leaves.left = TreeNode(2) # None <- 2 <- 1 -> None
  all_leaves.right = TreeNode(3) # None <- 2 <- 1 -> 3 -> None
  all_leaves.left.left = TreeNode(4) # 4 <- 2 -> None (root -> left)
  all_leaves.left.right = TreeNode(5) # 4 <- 2 -> 5 (root -> left)
  all_leaves.right.left = TreeNode(6) # 6 <- 3 -> None (root -> right)
  all_leaves.right.right = TreeNode(7) # 6 <- 3 -> 7 (root -> right)
  find_leaf_nodes(all_leaves)

test_count_leaves()
class GenericTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

def tree_height(root):
    if root is None:
        return 0
    if not root.children:
        return 1
    return 1 + max(tree_height(child) for child in root.children)

def test_tree_height():
    print("===== Challenge 3: Generic Tree Height Tests =====")

    # Test 1: Empty tree
    print("Test 1: Empty tree → Expected: 0")
    print("Result:", tree_height(None), "\n")

    # Test 2: Single node
    root = GenericTreeNode('A')
    print("Test 2: Single node → Expected: 1")
    print("Result:", tree_height(root), "\n")

    # Test 3: Linear tree A -> B -> C -> D
    a = GenericTreeNode('A')
    b = GenericTreeNode('B')
    c = GenericTreeNode('C')
    d = GenericTreeNode('D')
    a.add_child(b)
    b.add_child(c)
    c.add_child(d)
    print("Test 3: Linear tree → Expected: 4")
    print("Result:", tree_height(a), "\n")

    # Test 4: Balanced tree
    a = GenericTreeNode('A')
    b = GenericTreeNode('B')
    c = GenericTreeNode('C')
    d = GenericTreeNode('D')
    e = GenericTreeNode('E')
    f = GenericTreeNode('F')
    g = GenericTreeNode('G')
    h = GenericTreeNode('H')
    a.add_child(b)
    a.add_child(c)
    a.add_child(d)
    b.add_child(e)
    b.add_child(f)
    b.add_child(g)
    d.add_child(h)
    print("Test 4: Balanced tree → Expected: 3")
    print("Result:", tree_height(a), "\n")

    # Test 5: Unbalanced tree
    a = GenericTreeNode('A')
    b = GenericTreeNode('B')
    c = GenericTreeNode('C')
    d = GenericTreeNode('D')
    e = GenericTreeNode('E')
    f = GenericTreeNode('F')
    g = GenericTreeNode('G')
    a.add_child(b)
    a.add_child(c)
    b.add_child(d)
    c.add_child(e)
    d.add_child(f)
    e.add_child(g)
    print("Test 5: Unbalanced tree → Expected: 4")
    print("Result:", tree_height(a), "\n")

if __name__ == "__main__":
    test_tree_height()
class GenericTreeNode:
    def __init__(self, value):  # ✅ Corregido aquí
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def find_leaves(root):
    if root is None:
        return []
    if not root.children:
        return [root.value]

    leaves = []
    for child in root.children:
        leaves.extend(find_leaves(child))
    return leaves

def test_find_leaves():
    """Test finding all leaf nodes. 🍃"""

    def print_result(case_num, result, expected):
        print(f"🔍 Test Case {case_num}:")
        print(f"    Resultado obtenido: {result}")
        print(f"    Esperado:           {expected}")
        print(f"    {'✅ PASÓ' if sorted(result) == sorted(expected) else '❌ FALLÓ'}\n")

    # Test Case 1: Empty tree
    test1_root = None
    test1_expected = []
    test1_result = find_leaves(test1_root)
    print_result(1, test1_result, test1_expected)
    assert test1_result == test1_expected

    # Test Case 2: Single node
    test2_root = GenericTreeNode('A')
    test2_expected = ['A']
    test2_result = find_leaves(test2_root)
    print_result(2, test2_result, test2_expected)
    assert test2_result == test2_expected

    # Test Case 3: Linear tree A -> B -> C
    test3_root = GenericTreeNode('A')
    test3_b = GenericTreeNode('B')
    test3_c = GenericTreeNode('C')
    test3_root.add_child(test3_b)
    test3_b.add_child(test3_c)
    test3_expected = ['C']
    test3_result = find_leaves(test3_root)
    print_result(3, test3_result, test3_expected)
    assert test3_result == test3_expected

    # Test Case 4: Balanced tree
    test4_root = GenericTreeNode('A')
    test4_b = GenericTreeNode('B')
    test4_c = GenericTreeNode('C')
    test4_d = GenericTreeNode('D')
    test4_e = GenericTreeNode('E')
    test4_f = GenericTreeNode('F')
    test4_g = GenericTreeNode('G')
    test4_h = GenericTreeNode('H')
    test4_root.add_child(test4_b)
    test4_root.add_child(test4_c)
    test4_root.add_child(test4_d)
    test4_b.add_child(test4_e)
    test4_b.add_child(test4_f)
    test4_b.add_child(test4_g)
    test4_d.add_child(test4_h)
    test4_expected = ['E', 'F', 'G', 'C', 'H']
    test4_result = find_leaves(test4_root)
    print_result(4, test4_result, test4_expected)
    assert sorted(test4_result) == sorted(test4_expected)

    # Test Case 5: Complex tree
    test5_root = GenericTreeNode('A')
    test5_b = GenericTreeNode('B')
    test5_c = GenericTreeNode('C')
    test5_d = GenericTreeNode('D')
    test5_e = GenericTreeNode('E')
    test5_f = GenericTreeNode('F')
    test5_g = GenericTreeNode('G')
    test5_h = GenericTreeNode('H')
    test5_i = GenericTreeNode('I')
    test5_j = GenericTreeNode('J')
    test5_k = GenericTreeNode('K')
    test5_root.add_child(test5_b)
    test5_root.add_child(test5_c)
    test5_root.add_child(test5_d)
    test5_b.add_child(test5_e)
    test5_b.add_child(test5_f)
    test5_d.add_child(test5_g)
    test5_e.add_child(test5_h)
    test5_f.add_child(test5_i)
    test5_f.add_child(test5_j)
    test5_f.add_child(test5_k)
    test5_expected = ['H', 'I', 'J', 'K', 'C', 'G']
    test5_result = find_leaves(test5_root)
    print_result(5, test5_result, test5_expected)
    assert sorted(test5_result) == sorted(test5_expected)

    print("🎉 Todos los casos de prueba pasaron.")

# Ejecutar pruebas
test_find_leaves()
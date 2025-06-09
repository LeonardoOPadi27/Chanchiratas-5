class Node:
    """Node for expression tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_number(s):
    """Checks if the string represents a number (int or float)"""
    try:
        float(s)
        return True
    except ValueError:
        return False

def apply_operator(op, left_val, right_val):
    """Applies the arithmetic operator to two values"""
    left = float(left_val)
    right = float(right_val)
    
    if op == '+':
        result = left + right
    elif op == '-':
        result = left - right
    elif op == '*':
        result = left * right
    elif op == '/':
        if right == 0:
            raise ZeroDivisionError("Division by zero")
        result = left / right
    else:
        raise ValueError(f"Unknown operator: {op}")
    
    # Devuelve como entero si no tiene decimales, sino como float
    return str(int(result)) if result.is_integer() else str(result)

def simplify_expression_tree(root):
    """Simplifies an expression tree by evaluating constant subtrees"""
    if root is None:
        return None

    # Recursively simplify both subtrees
    root.left = simplify_expression_tree(root.left)
    root.right = simplify_expression_tree(root.right)

    # If current node is an operator and both children are numbers
    if root.value in '+-*/' and root.left and root.right:
        if is_number(root.left.value) and is_number(root.right.value):
            try:
                simplified_value = apply_operator(
                    root.value, 
                    root.left.value, 
                    root.right.value
                )
                # Replace this node with the simplified value
                root.value = simplified_value
                root.left = None
                root.right = None
            except ZeroDivisionError:
                # Leave unchanged if division by zero
                pass

    return root
# --- TESTS ---
# Test 1: All constants
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
result1 = simplify_expression_tree(node1)
print(result1.value == '5' and result1.left is None and result1.right is None)  # True

# Test 2: Mixed variables and constants
node2 = Node('+')
node2.left = Node('x')
node2.right = Node('3')
result2 = simplify_expression_tree(node2)
print(result2.value == '+' and result2.left.value == 'x' and result2.right.value == '3')  # True

# Test 3: Partial simplification
node3 = Node('+')
node3.left = Node('*')
node3.right = Node('-')
node3.left.left = Node('2')
node3.left.right = Node('3')
node3.right.left = Node('8')
node3.right.right = Node('3')
result3 = simplify_expression_tree(node3)
print(result3.value == '+' and result3.left.value == '6' and result3.right.value == '5')  # True

# Test 4: All variables
node4 = Node('+')
node4.left = Node('x')
node4.right = Node('y')
result4 = simplify_expression_tree(node4)
print(result4.value == '+' and result4.left.value == 'x' and result4.right.value == 'y')  # True

# Test 5: Complex nested simplification
node5 = Node('+')
node5.left = Node('/')
node5.right = Node('*')
node5.left.left = Node('10')
node5.left.right = Node('2')
node5.right.left = Node('z')
node5.right.right = Node('4')
result5 = simplify_expression_tree(node5)
print(result5.value == '+' and result5.left.value == '5' and 
      result5.right.value == '*' and result5.right.left.value == 'z')  # True
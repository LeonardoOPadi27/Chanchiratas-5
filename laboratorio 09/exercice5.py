class ExpressionNode:
    """Node class for representing expression tree."""
    def __init__(self, value):
        self.value = value  # Value of the node (operator or operand)
        self.left = None    # Left child
        self.right = None   # Right child


def simplify_expression(root):
    """
    Simplifies an expression tree by evaluating constant subexpressions.
    
    Args:
        root: Root node of the expression tree
        
    Returns:
        Root node of the simplified expression tree
    """
    # Base case: if the node is None, return None
    if root is None:
        return None
    
    # Base case: if the node is a leaf (no children), return it as is
    if root.left is None and root.right is None:
        return root
    
    # Post-order traversal: first simplify the left and right subtrees
    root.left = simplify_expression(root.left)
    root.right = simplify_expression(root.right)
    
    # Check if both children are constants (can be evaluated)
    if is_constant(root.left) and is_constant(root.right):
        # Evaluate the expression based on the operator
        result = evaluate_expression(root.value, root.left.value, root.right.value)
        # Create a new node with the computed result
        return ExpressionNode(str(result))
    
    # If we can't simplify (e.g., one child is a variable), return the node as is
    return root


def is_constant(node):
    """
    Determines if a node represents a constant value (a number).
    
    Args:
        node: An expression tree node
        
    Returns:
        Boolean indicating if the node is a constant
    """
    # If the node is None, it's not a constant
    if node is None:
        return False
    
    # Try to convert the node's value to a float - if successful, it's a constant
    try:
        float(node.value)
        return True
    except ValueError:
        # If conversion fails, it's not a constant (likely a variable or operator)
        return False


def evaluate_expression(operator, left_value, right_value):
    """
    Evaluates a simple expression with one operator and two operands.
    
    Args:
        operator: String representing the operation ('+', '-', '*', '/')
        left_value: String representing the left operand
        right_value: String representing the right operand
        
    Returns:
        The result of the operation as a number
    """
    # Convert operand strings to numbers
    left_num = float(left_value)
    right_num = float(right_value)
    
    # Evaluate based on the operator
    if operator == '+':
        return left_num + right_num
    elif operator == '-':
        return left_num - right_num
    elif operator == '*':
        return left_num * right_num
    elif operator == '/':
        # Handle division by zero
        if right_num == 0:
            raise ValueError("Division by zero")
        return left_num / right_num
    else:
        # Handle unsupported operators
        raise ValueError(f"Unsupported operator: {operator}")

def test_simplify_expression():
    """Test expression tree simplification."""
    # Test Case 1: All constants
    # Input: (2 + 3) * 4
    # Expected: 20
    test1_root = ExpressionNode('*')
    test1_add = ExpressionNode('+')
    test1_2 = ExpressionNode('2')
    test1_3 = ExpressionNode('3')
    test1_4 = ExpressionNode('4')
    test1_add.left = test1_2
    test1_add.right = test1_3
    test1_root.left = test1_add
    test1_root.right = test1_4
    
    result1 = simplify_expression(test1_root)
    print(f"Test 1 Result: {result1.value}")  # Should print 20.0
    
    # Test Case 2: Partial simplification
    # Input: (2 + 3) * x
    # Expected: 5 * x
    test2_root = ExpressionNode('*')
    test2_add = ExpressionNode('+')
    test2_2 = ExpressionNode('2')
    test2_3 = ExpressionNode('3')
    test2_x = ExpressionNode('x')
    test2_add.left = test2_2
    test2_add.right = test2_3
    test2_root.left = test2_add
    test2_root.right = test2_x
    
    result2 = simplify_expression(test2_root)
    print(f"Test 2 Result: {result2.value} with left={result2.left.value} and right={result2.right.value}")
    
    # Test Case 3: No simplification possible
    # Input: (x + y) * z
    # Expected: (x + y) * z (unchanged)
    test3_root = ExpressionNode('*')
    test3_add = ExpressionNode('+')
    test3_x = ExpressionNode('x')
    test3_y = ExpressionNode('y')
    test3_z = ExpressionNode('z')
    test3_add.left = test3_x
    test3_add.right = test3_y
    test3_root.left = test3_add
    test3_root.right = test3_z
    
    result3 = simplify_expression(test3_root)
    print(f"Test 3 Result: {result3.value} with left={result3.left.value} and right={result3.right.value}")
    
    # Test Case 4: Nested simplification
    # Input: ((2 * 3) + (4 - 1)) * 5
    # Expected: 45
    test4_root = ExpressionNode('*')
    test4_add = ExpressionNode('+')
    test4_mult = ExpressionNode('*')
    test4_sub = ExpressionNode('-')
    test4_2 = ExpressionNode('2')
    test4_3 = ExpressionNode('3')
    test4_4 = ExpressionNode('4')
    test4_1 = ExpressionNode('1')
    test4_5 = ExpressionNode('5')
    test4_mult.left = test4_2
    test4_mult.right = test4_3
    test4_sub.left = test4_4
    test4_sub.right = test4_1
    test4_add.left = test4_mult
    test4_add.right = test4_sub
    test4_root.left = test4_add
    test4_root.right = test4_5
    
    result4 = simplify_expression(test4_root)
    print(f"Test 4 Result: {result4.value}")  # Should print 45.0
    
    # Test Case 5: Mixed variables and constants
    # Input: (x + 5) * (3 + 2)
    # Expected: (x + 5) * 5
    test5_root = ExpressionNode('*')
    test5_add1 = ExpressionNode('+')
    test5_add2 = ExpressionNode('+')
    test5_x = ExpressionNode('x')
    test5_5a = ExpressionNode('5')
    test5_3 = ExpressionNode('3')
    test5_2 = ExpressionNode('2')
    test5_add1.left = test5_x
    test5_add1.right = test5_5a
    test5_add2.left = test5_3
    test5_add2.right = test5_2
    test5_root.left = test5_add1
    test5_root.right = test5_add2
    
    result5 = simplify_expression(test5_root)
    print(f"Test 5 Result: {result5.value} with left node's value={result5.left.value} and right node's value={result5.right.value}")


# Run the tests
if __name__ == "__main__":
    test_simplify_expression()
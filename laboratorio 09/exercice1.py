class ExpressionNode:
    """
    Node class for representing a single node in an expression tree.
    Each node can be an operand (leaf) or an operator (with children).
    """
    def __init__(self, value, left=None, right=None):
        # Store the token value (could be an operator or operand)
        self.value = value
        # Left child node (for binary operators)
        self.left = left
        # Right child node (for binary operators)
        self.right = right

class ExpressionTree:
    """
    A comprehensive class for expression manipulation using tree-based operations.
    Supports conversion between different notations and expression evaluation.
    """
    def __init__(self):
        # Define operator precedence levels
        # Lower number = lower precedence
        self.precedence = {
            '+': 1,   # Addition has lowest precedence
            '-': 1,   # Subtraction has lowest precedence
            '*': 2,   # Multiplication has higher precedence
            '/': 2,   # Division has higher precedence
            '^': 3,   # Exponentiation has highest precedence
            '%': 2    # Modulo has same precedence as multiplication/division
        }
    
    def is_operator(self, token):
        """
        Determine if a given token is a mathematical operator.
        
        Args:
            token (str): Token to check
        
        Returns:
            bool: True if token is an operator, False otherwise
        """
        # Check if token exists in precedence dictionary (our list of known operators)
        return token in self.precedence
    
    def is_operand(self, token):
        """
        Check if a token is a valid numeric operand.
        
        Args:
            token (str): Token to check
        
        Returns:
            bool: True if token can be converted to a number, False otherwise
        """
        try:
            # Attempt to convert token to float
            # This covers integers, decimals, and scientific notation
            float(token)
            return True
        except ValueError:
            # If conversion fails, it's not a valid number
            return False
    
    def infix_to_postfix(self, tokens):
        """
        Convert infix notation (standard mathematical notation) to postfix notation.
        
        Args:
            tokens (list): List of tokens in infix notation
        
        Returns:
            list: Tokens converted to postfix notation
        """
        # List to store final postfix expression
        output = []
        # Stack to temporarily hold operators
        operator_stack = []
        
        # Process each token in the input
        for token in tokens:
            # If token is a number, immediately add to output
            if self.is_operand(token):
                output.append(token)
            
            # If token is an opening parenthesis, push to operator stack
            elif token == '(':
                operator_stack.append(token)
            
            # If token is a closing parenthesis
            elif token == ')':
                # Pop and output operators until matching opening parenthesis
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                
                # Remove the opening parenthesis
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()
            
            # If token is an operator
            elif self.is_operator(token):
                # Compare precedence with top of operator stack
                while (operator_stack and 
                       operator_stack[-1] != '(' and 
                       # Pop operators with higher or equal precedence
                       self.precedence.get(operator_stack[-1], 0) >= self.precedence.get(token, 0)):
                    output.append(operator_stack.pop())
                
                # Push current operator to stack
                operator_stack.append(token)
        
        # Pop any remaining operators to output
        while operator_stack:
            output.append(operator_stack.pop())
        
        return output
    
    def infix_to_prefix(self, tokens):
        """
        Convert infix notation to prefix notation.
        
        Args:
            tokens (list): List of tokens in infix notation
        
        Returns:
            list: Tokens converted to prefix notation
        """
        # Reverse the input, swapping parentheses
        reversed_tokens = []
        for token in reversed(tokens):
            # Swap parentheses when reversing
            if token == '(':
                reversed_tokens.append(')')
            elif token == ')':
                reversed_tokens.append('(')
            else:
                reversed_tokens.append(token)
        
        # Convert reversed tokens to postfix (which becomes prefix)
        postfix = self.infix_to_postfix(reversed_tokens)
        
        # Reverse back to get prefix notation
        return list(reversed(postfix))
    
    def postfix_to_tree(self, postfix_tokens):
        """
        Convert postfix expression to an expression tree.
        
        Args:
            postfix_tokens (list): List of tokens in postfix notation
        
        Returns:
            ExpressionNode: Root node of the expression tree
        """
        # Stack to build the tree
        stack = []
        
        # Process each token in postfix expression
        for token in postfix_tokens:
            # If token is a number, create a leaf node
            if self.is_operand(token):
                stack.append(ExpressionNode(token))
            
            # If token is an operator, create a tree node
            elif self.is_operator(token):
                # Ensure enough operands exist for binary operation
                if len(stack) < 2:
                    raise ValueError("Invalid postfix expression: not enough operands")
                
                # Pop two operands to become children
                # Note: Right operand is popped first
                right = stack.pop()
                left = stack.pop()
                
                # Create new node with operator and children
                node = ExpressionNode(token, left, right)
                
                # Push new node back to stack
                stack.append(node)
        
        # Final stack should have only the root node
        if len(stack) != 1:
            raise ValueError("Invalid postfix expression: too many operands")
        
        return stack[0]
    
    def prefix_to_tree(self, prefix_tokens):
        """
        Convert prefix expression to an expression tree.
        
        Args:
            prefix_tokens (list): List of tokens in prefix notation
        
        Returns:
            ExpressionNode: Root node of the expression tree
        """
        # Reverse tokens to process from right to left
        reversed_tokens = list(reversed(prefix_tokens))
        
        # Stack to build the tree
        stack = []
        
        # Process each token in reversed prefix expression
        for token in reversed_tokens:
            # If token is a number, create a leaf node
            if self.is_operand(token):
                stack.append(ExpressionNode(token))
            
            # If token is an operator, create a tree node
            elif self.is_operator(token):
                # Ensure enough operands exist for binary operation
                if len(stack) < 2:
                    raise ValueError("Invalid prefix expression: not enough operands")
                
                # Pop two operands to become children
                # Note: Order is different from postfix
                left = stack.pop()
                right = stack.pop()
                
                # Create new node with operator and children
                node = ExpressionNode(token, left, right)
                
                # Push new node back to stack
                stack.append(node)
        
        # Final stack should have only the root node
        if len(stack) != 1:
            raise ValueError("Invalid prefix expression: too many operands")
        
        return stack[0]
    
    def evaluate_tree(self, root):
        """
        Recursively evaluate an expression tree.
        
        Args:
            root (ExpressionNode): Root of the expression tree
        
        Returns:
            float: Computed result of the expression
        """
        # Base case: if node is a number (leaf node), return its value
        if not self.is_operator(root.value):
            return float(root.value)
        
        # Recursively evaluate left and right subtrees
        left_val = self.evaluate_tree(root.left)
        right_val = self.evaluate_tree(root.right)
        
        # Perform operation based on operator
        if root.value == '+':
            # Addition: sum of left and right values
            return left_val + right_val
        elif root.value == '-':
            # Subtraction: left value minus right value
            return left_val - right_val
        elif root.value == '*':
            # Multiplication: product of left and right values
            return left_val * right_val
        elif root.value == '/':
            # Division: left value divided by right value
            # Added check to prevent division by zero
            if right_val == 0:
                raise ValueError("Division by zero")
            return left_val / right_val
        elif root.value == '^':
            # Exponentiation: left value raised to right value
            return left_val ** right_val
        elif root.value == '%':
            # Modulo: remainder of left value divided by right value
            return left_val % right_val
        
        # Catch any unsupported operators
        raise ValueError(f"Unknown operator: {root.value}")
    
    def tree_to_infix(self, root):
        """
        Convert expression tree back to infix notation with parentheses.
        
        Args:
            root (ExpressionNode): Root of the expression tree
        
        Returns:
            str: Infix representation of the expression
        """
        # Base case: if node is a number (leaf node), return its value
        if not self.is_operator(root.value):
            return str(root.value)
        
        # Recursively convert left and right subtrees to infix
        left_expr = self.tree_to_infix(root.left)
        right_expr = self.tree_to_infix(root.right)
        
        # Combine with current operator, wrapped in parentheses
        return f"({left_expr} {root.value} {right_expr})"

def test_expression_tree():
    """
    Comprehensive test function to demonstrate all features of ExpressionTree.
    Shows conversion between notations, tree creation, and evaluation.
    """
    # Create an instance of ExpressionTree
    et = ExpressionTree()
    
    # Demonstration of Infix to Postfix conversion
    print("Infix to Postfix Conversion Tests:")
    # List of test cases in infix notation
    test_cases_infix_postfix = [
        ['2', '+', '3'],                   # Simple addition
        ['2', '+', '3', '*', '4'],         # With precedence
        ['(', '2', '+', '3', ')', '*', '4'],  # With parentheses
        ['(', '5', '+', '3', ')', '*', '(', '10', '-', '8', ')']  # Complex expression
    ]
    
    # Convert and print each test case
    for case in test_cases_infix_postfix:
        postfix = et.infix_to_postfix(case)
        print(f"Infix: {case} → Postfix: {postfix}")
    
    # Demonstration of Infix to Prefix conversion
    print("\nInfix to Prefix Conversion Tests:")
    # List of test cases in infix notation
    test_cases_infix_prefix = [
        ['2', '+', '3'],                   # Simple addition
        ['2', '+', '3', '*', '4'],         # With precedence
        ['(', '2', '+', '3', ')', '*', '4']  # With parentheses
    ]
    
    # Convert and print each test case
    for case in test_cases_infix_prefix:
        prefix = et.infix_to_prefix(case)
        print(f"Infix: {case} → Prefix: {prefix}")
    
    # Demonstration of Tree Creation and Evaluation
    print("\nTree Creation and Evaluation:")
    
    # Test Postfix to Tree
    print("Postfix to Tree:")
    postfix_expr = ['2', '3', '+', '4', '*']  # (2+3)*4
    tree = et.postfix_to_tree(postfix_expr)
    print(f"Postfix: {postfix_expr}")
    print(f"Tree Evaluation: {et.evaluate_tree(tree)}")
    print(f"Tree to Infix: {et.tree_to_infix(tree)}")
    
    # Test Prefix to Tree
    print("\nPrefix to Tree:")
    prefix_expr = ['*', '+', '2', '3', '4']  # *(+(2,3),4)
    tree = et.prefix_to_tree(prefix_expr)
    print(f"Prefix: {prefix_expr}")
    print(f"Tree Evaluation: {et.evaluate_tree(tree)}")
    print(f"Tree to Infix: {et.tree_to_infix(tree)}")

# Run the comprehensive test function
test_expression_tree()
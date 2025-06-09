class ExpressionNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def precedence(op):
    return {'+': 1, '-': 1, '*': 2, '/': 2}.get(op, 0)

def infix_to_postfix(tokens):
    output = []
    stack = []
    for token in tokens:
        if token.isnumeric() or token.isalpha():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(token):
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return output

def build_tree_from_infix(tokens):
    postfix = infix_to_postfix(tokens)
    stack = []
    for token in postfix:
        if token.isnumeric() or token.isalpha():
            stack.append(ExpressionNode(token))
        else:
            node = ExpressionNode(token)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    return stack[-1]

def print_expression_tree_test(expr_tokens):
    print("Input Infix:", expr_tokens)
    tree = build_tree_from_infix(expr_tokens)
    print("Root:", tree.value)
    if tree.left:
        print("  Left:", tree.left.value)
    if tree.right:
        print("  Right:", tree.right.value)
    if tree.left and tree.left.left:
        print("    Left.Left:", tree.left.left.value)
    if tree.left and tree.left.right:
        print("    Left.Right:", tree.left.right.value)
    print()

def test_build_tree_from_infix():
    print("===== Challenge 2: Expression Tree Tests =====")
    test_cases = [
        ['2', '+', '3'],
        ['2', '+', '3', '*', '4'],
        ['(', '2', '+', '3', ')', '*', '4'],
        ['(', '5', '+', '3', ')', '*', '(', '10', '-', '8', ')'],
        ['8', '/', '4', '/', '2']
    ]
    for tokens in test_cases:
        print_expression_tree_test(tokens)

if __name__ == "__main__":
    test_build_tree_from_infix()
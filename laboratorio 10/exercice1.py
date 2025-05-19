def infix_to_postfix(tokens):
    """Convert infix expression to postfix notation"""
    precedence = {'*': 3, '/': 3, '+': 2, '-': 2}
    stack = []
    output = []
    
    for token in tokens:
        if token.isalnum():  # Operando (número o variable)
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            # Desapilar hasta encontrar '('
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Eliminar '(' sin agregarlo a la salida
        else:  # Operador
            while (stack and stack[-1] != '(' and 
                   precedence.get(stack[-1], 0) >= precedence.get(token, 0)):
                output.append(stack.pop())
            stack.append(token)
    
    # Desapilar cualquier operador restante
    while stack:
        output.append(stack.pop())
    
    return output
# ✅ Test cases
# Test 1: Simple addition
# Input: 2 + 3
# Output: 2 3 +
print(infix_to_postfix(['2', '+', '3']) == ['2', '3', '+'])  # ➕ Simple operation

# Test 2: Operator precedence
# Input: 2 + 3 * 4
# Output: 2 3 4 * +
print(infix_to_postfix(['2', '+', '3', '*', '4']) == ['2', '3', '4', '*', '+'])  # 📊 Precedence test

# Test 3: Parentheses override precedence
# Input: (2 + 3) * 4
# Output: 2 3 + 4 *
print(infix_to_postfix(['(', '2', '+', '3', ')', '*', '4']) == ['2', '3', '+', '4', '*'])  # 🔗 Parentheses

# Test 4: Complex expression
# Input: (1 + 2) * (3 - 4)
# Output: 1 2 + 3 4 - *
print(infix_to_postfix(['(', '1', '+', '2', ')', '*', '(', '3', '-', '4', ')']) == ['1', '2', '+', '3', '4', '-', '*'])  # 🧮 Complex

# Test 5: Multiple operators
# Input: a + b * c / d
# Output: a b c * d / +
print(infix_to_postfix(['a', '+', 'b', '*', 'c', '/', 'd']) == ['a', 'b', 'c', '*', 'd', '/', '+'])  # 🔤 Variables

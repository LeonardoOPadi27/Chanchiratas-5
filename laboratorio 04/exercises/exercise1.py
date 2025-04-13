class ArrayStack:
    
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.capacity = capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1
    
    def push(self, item):
        if self.top == self.capacity - 1:
            raise OverflowError("Stack overflow - stack is full")
        self.top += 1
        self.data[self.top] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty")
        item = self.data[self.top]
        self.top -= 1
        return item
def reverse_string_with_array_stack(text):
    stack = ArrayStack(len(text)) 
    for char in text:
        stack.push(char)

    reversed_text = ''
    while not stack.is_empty():
        reversed_text += stack.pop()

    return reversed_text

if __name__ == "__main__":
#  ejemplo 1:
    original = "hola mundo"
    invertida = reverse_string_with_array_stack(original)
    print(f"Original: {original}")
    print(f"Invertida: {invertida}")
#  ejemplo 2:
    original = "con fe se pasa"
    invertida = reverse_string_with_array_stack(original)
    print(f"Original: {original}")
    print(f"Invertida: {invertida}")
#  ejemplo 3:
    original = "reconocer xd"
    invertida = reverse_string_with_array_stack(original)
    print(f"Original: {original}")
    print(f"Invertida: {invertida}")


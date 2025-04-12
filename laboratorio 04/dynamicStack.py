class DynamicArrayStack:
    """Stack implementation using a dynamic array that resizes when full."""
    
    def __init__(self, initial_capacity=10):
        """Initialize empty stack with dynamic capacity."""
        self.data = [None] * initial_capacity
        self.capacity = initial_capacity
        self.top = -1
    
    def is_empty(self):
        """Check if stack is empty."""
        return self.top == -1
    
    def resize(self, new_capacity):
        """Resize the stack to a new capacity."""
        new_data = [None] * new_capacity
        
        # Copy existing elements to the new array
        for i in range(self.top + 1):
            new_data[i] = self.data[i]
            
        self.data = new_data
        self.capacity = new_capacity
    
    def push(self, item):
        """Add item to the top of the stack."""
        if self.top == self.capacity - 1:
            # Double the capacity when full
            self.resize(2 * self.capacity)
        
        self.top += 1
        self.data[self.top] = item
        return True
    
    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty")
        
        item = self.data[self.top]
        self.data[self.top] = None  # Remove reference to the object
        self.top -= 1
        
        # Shrink the array if it's only 1/4 full
        if 0 < self.top + 1 <= self.capacity // 4 and self.capacity > 10:
            self.resize(self.capacity // 2)
            
        return item
    
    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty")
        
        return self.data[self.top]
    
    def size(self):
        """Return the number of items in the stack."""
        return self.top + 1
    
    def __str__(self):
        """Return a string representation of the stack."""
        if self.is_empty():
            return "Stack: []"
        
        items = [str(self.data[i]) for i in range(self.top + 1)]
        return f"Stack: [{', '.join(items)}]"


def test_dynamic_array_stack():
    """Test dynamic array stack with auto-resizing capability."""
    print("Test: Dynamic array stack with auto-resizing")
    stack = DynamicArrayStack(3)  # Start with small capacity
    
    print(f"Initial capacity: {stack.capacity}")
    
    # Push beyond initial capacity
    for i in range(1, 8):
        stack.push(i)
        print(f"After push({i}): size={stack.size()}, capacity={stack.capacity}")
    
    # Pop to trigger shrinking
    for _ in range(6):
        val = stack.pop()
        print(f"After pop -> {val}: size={stack.size()}, capacity={stack.capacity}")
    
    print("All dynamic array stack tests passed!")


# Example usage
if __name__ == "__main__":
    test_dynamic_array_stack()
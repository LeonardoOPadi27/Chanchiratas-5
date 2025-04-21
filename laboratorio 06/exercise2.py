class CircularQueue:
    """Queue implementation using a circular array."""
    
    def __init__(self, capacity=5):
        """Initialize an empty queue with a fixed capacity."""
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1  # Index of front element
        self.rear = -1   # Index of rear element
        self.size_count = 0
    
    def is_empty(self):
        """Check if the queue is empty."""
        return self.size_count == 0
    
    def is_full(self):
        """Check if the queue is full."""
        return self.size_count == self.capacity
    
    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        if self.is_full():
            raise IndexError("Overflow: Queue is full!")
        
        # If queue is empty, set front to 0
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            # Move rear circularly
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = item
        self.size_count += 1
    
    def dequeue(self):
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("Underflow: Queue is empty!")
        
        item = self.queue[self.front]
        self.queue[self.front] = None  # Clear reference
        
        # If this is the last item
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Move front circularly
            self.front = (self.front + 1) % self.capacity

        self.size_count -= 1
        return item

    def size(self):
        """Return the number of items in the queue."""
        return self.size_count

    def display(self):
        """Display the queue elements for debugging."""
        if self.is_empty():
            return "Queue: []"

        result = []
        index = self.front
        for _ in range(self.size_count):
            result.append(str(self.queue[index]))
            index = (index + 1) % self.capacity

        return f"Queue: [{', '.join(result)}]"

    def rotate_array(self, arr, steps):
        """Rotate array elements to the right by 'steps' positions."""
        length = len(arr)

        # "length == 0" -> If the array is empty it will return the same array
        # "steps == length" -> If steps is equal to length, it will return the same array because nothing is being altered
        if length == 0 or steps == length:
            return arr

        # Clear the queue first (in case it's not empty)
        self.__init__(length)

        # Enqueue the elements of the array
        for num in arr:
            self.enqueue(num)

        # Then dequeue and re-enqueue "steps" times
        for _ in range(steps):
            item = self.dequeue()
            self.enqueue(item)

        # Extract the elements in the new order
        return self.display()

# Example usage
if __name__ == "__main__":
    queue = CircularQueue(7)
    arr = [1, 2, 3, 4, 5, 6, 7]
    steps = 3
    
    rotated = queue.rotate_array(arr, steps)
    print(f"Original array: {arr}")
    print(f"Rotated {rotated}")
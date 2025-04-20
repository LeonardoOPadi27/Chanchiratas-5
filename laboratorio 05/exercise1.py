class QueueWithStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item):
        self.stack_in.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def is_empty(self):
        return not self.stack_in and not self.stack_out

    def size(self):
        return len(self.stack_in) + len(self.stack_out)
    
def test_queue():
    q = QueueWithStacks()

    print("Test 1: Enqueue and Dequeue")
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(q.dequeue())
    print(q.dequeue())  
    
    print("\nTest 2: Peek and Size")
    q.enqueue(40)
    print(q.peek())     
    print(q.size())     

    print("\nTest 3: Empty Check")
    q.dequeue()
    q.dequeue()
    print(q.is_empty())

if __name__ == "__main__":
    test_queue()

test_results = []

def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MinHeap:
    def __init__(self):
        """
        Initialize empty heap storage using a list.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Use list to store heap elements with index 0 as root
        self.heap = []
    
    def is_empty(self):
        """
        Return True if heap has no elements.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Check if the heap list is empty
        return len(self.heap) == 0
    
    def size(self):
        """
        Return number of elements in heap.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Return the length of the heap list
        return len(self.heap)
    
    def peek(self):
        """
        Return minimum element without removing it.
        In a min-heap, the minimum element is always at the root (index 0).
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Handle edge case: empty heap
        if self.is_empty():
            return None
        
        # In min-heap, root (index 0) contains minimum element
        return self.heap[0]

def test_1_1():
    # 1.1.1 Empty heap initialization
    heap = MinHeap()
    record_test("1.1.1 Empty heap initialization", heap.is_empty() == True)
    
    # 1.1.2 Size tracking
    heap.heap = [1, 3, 2]  # Simulate adding elements
    record_test("1.1.2 Size tracking", heap.size() == 3)
    
    # 1.1.3 Peek functionality
    record_test("1.1.3 Peek functionality", heap.peek() == 1)
    
    # 1.1.4 Empty heap edge case
    empty_heap = MinHeap()
    record_test("1.1.4 Empty heap edge case", empty_heap.peek() is None)
    
    # 1.1.5 Type validation
    record_test("1.1.5 Type validation", isinstance(heap.is_empty(), bool))

# 🚀 Run tests
test_1_1()

# 📋 Summary
print("TEST RESULTS:")
print("=" * 50)
for r in test_results:
    print(r)

print(f"\nTotal: {len([r for r in test_results if '✅' in r])}/{len(test_results)} tests passed")

# Demonstrate the implemented functionality
print("\n" + "=" * 50)
print("DEMONSTRATION:")
print("=" * 50)

# Create and test heap
demo_heap = MinHeap()
print(f"New heap is empty: {demo_heap.is_empty()}")
print(f"New heap size: {demo_heap.size()}")
print(f"Peek at empty heap: {demo_heap.peek()}")

# Simulate adding elements to demonstrate peek
demo_heap.heap = [5, 10, 15, 20, 25]
print(f"\nAfter adding elements [5, 10, 15, 20, 25]:")
print(f"Heap is empty: {demo_heap.is_empty()}")
print(f"Heap size: {demo_heap.size()}")
print(f"Minimum element (peek): {demo_heap.peek()}")
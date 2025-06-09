
class MinHeap:
    # 📦 MinHeap data structure using list
    def __init__(self):
        # Initialize empty list for heap
        self.heap = []
    
    def is_empty(self):
        # Return True if heap is empty
        return len(self.heap) == 0

# 🧪 Test cases
def test_min_heap_init_and_empty():
    h = MinHeap()
    # Test 1: Newly initialized heap is empty
    print("🌱 Test 1:", h.is_empty() == True)
    # Test 2: After appending an element, it's not empty
    h.heap.append(1)
    print("🌱 Test 2:", h.is_empty() == False)
    # Test 3: Manually clearing the heap returns to empty
    h.heap.clear()
    print("🌱 Test 3:", h.is_empty() == True)
    # Test 4: Appending multiple elements makes it not empty
    h.heap.extend([2, 3, 4])
    print("🌱 Test 4:", h.is_empty() == False)
    # Test 5: Removing all elements one by one returns to empty
    h.heap.pop()
    h.heap.pop()
    h.heap.pop()
    print("🌱 Test 5:", h.is_empty() == True)

test_min_heap_init_and_empty()
class MinHeap:
    # 📦 MinHeap data structure using list
    def __init__(self):
        # Initialize empty list for heap
        self.heap = []
    
    def is_empty(self):
        # Return True if heap is empty
        return len(self.heap) == 0
    
    def insert(self, value):
        # Insert value and maintain heap property
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    
    def heapify_up(self, index):
        # Move the value at index up to restore heap property
        if index == 0:  # Root element, no parent
            return
        
        parent_index = (index - 1) // 2
        
        # If parent is greater than current element, swap them
        if self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            # Recursively heapify up from the parent position
            self.heapify_up(parent_index)

# 🧪 Test cases
def test_min_heap_insert():
    h = MinHeap()
    h.insert(5)
    print("🍀 Test 1:", h.heap == [5])
    h.insert(3)
    print("🍀 Test 2:", h.heap == [3, 5])
    h.insert(4)
    print("🍀 Test 3:", h.heap == [3, 5, 4])
    h.insert(1)
    print("🍀 Test 4:", h.heap == [1, 3, 4, 5])
    # Heap property check: parent <= children
    valid = True
    for i in range(len(h.heap)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(h.heap) and h.heap[i] > h.heap[left]:
            valid = False
        if right < len(h.heap) and h.heap[i] > h.heap[right]:
            valid = False
    print("🍀 Test 5:", valid)

test_min_heap_insert()
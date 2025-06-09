class MinHeap:
    # 📦 MinHeap data structure using list
    def __init__(self):
        # Initialize empty list for heap
        self.heap = []
    
    def is_empty(self):
        # Return True if heap is empty
        return len(self.heap) == 0
    
    def build_heap(self, array):
        # Transform array into a min-heap
        self.heap = array.copy()  # Create a shallow copy
        
        # Start from the last non-leaf node and heapify down
        # Last non-leaf node is at index (n//2 - 1)
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)
    
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
    
    def delete_min(self):
        # Remove and return the smallest element
        if self.is_empty():
            return None
        
        # Store the minimum value (root)
        min_value = self.heap[0]
        
        # Replace root with last element
        self.heap[0] = self.heap[-1]
        
        # Remove the last element
        self.heap.pop()
        
        # Restore heap property if heap is not empty
        if not self.is_empty():
            self.heapify_down(0)
        
        return min_value
    
    def heapify_down(self, index):
        # Restore heap property from the root down
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        # Find the smallest among parent and children
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        
        # If smallest is not the current index, swap and continue heapifying
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

# 🧪 Test cases
def test_build_heap():
    h = MinHeap()
    h.build_heap([5, 3, 8, 1, 2])
    print("🔨 Test 1:", h.heap[0] == min([5, 3, 8, 1, 2]))
    h.build_heap([7, 6, 5, 4, 3, 2, 1])
    print("🔨 Test 2:", h.heap[0] == 1)
    h.build_heap([2, 1])
    print("🔨 Test 3:", h.heap == [1, 2])
    h.build_heap([10])
    print("🔨 Test 4:", h.heap == [10])
    h.build_heap([])
    print("🔨 Test 5:", h.heap == [])

test_build_heap()
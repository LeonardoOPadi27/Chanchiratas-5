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
def test_min_heap_delete_min():
    h = MinHeap()
    print("🧹 Test 1:", h.delete_min() is None)
    h.heap = [1]
    print("🧹 Test 2:", h.delete_min() == 1 and h.heap == [])
    h.heap = [1, 3, 2]
    print("🧹 Test 3:", h.delete_min() == 1 and h.heap == [2, 3])
    h.heap = [1, 3, 4, 5]
    print("🧹 Test 4:", h.delete_min() == 1 and h.heap == [3, 5, 4])
    h.heap = [1, 2, 3, 4, 5]
    min_val = min(h.heap)
    print("🧹 Test 5:", h.delete_min() == min_val)

test_min_heap_delete_min()
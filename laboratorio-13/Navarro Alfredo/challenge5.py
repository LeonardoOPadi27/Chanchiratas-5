class MaxHeap:
    # 🦁 MaxHeap data structure using list
    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        # Insert and heapify up for max-heap property
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    
    def heapify_up(self, index):
        # Move up while parent < current
        if index == 0:  # Root element, no parent
            return
        
        parent_index = (index - 1) // 2
        
        # If parent is less than current element, swap them
        if self.heap[parent_index] < self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            # Recursively heapify up from the parent position
            self.heapify_up(parent_index)
    
    def delete_max(self):
        # Remove and return the largest (root) element
        if len(self.heap) == 0:
            return None
        
        # Store the maximum value (root)
        max_value = self.heap[0]
        
        # Replace root with last element
        self.heap[0] = self.heap[-1]
        
        # Remove the last element
        self.heap.pop()
        
        # Restore heap property if heap is not empty
        if len(self.heap) > 0:
            self.heapify_down(0)
        
        return max_value
    
    def heapify_down(self, index):
        # Move down while current < child
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        # Find the largest among parent and children
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child
        
        # If largest is not the current index, swap and continue heapifying
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

# 🧪 Test cases
def test_max_heap():
    h = MaxHeap()
    h.insert(1)
    print("🦁 Test 1:", h.heap == [1])
    for val in [3, 2, 8, 5]:
        h.insert(val)
    print("🦁 Test 2:", h.heap[0] == max(h.heap))
    h.delete_max()
    print("🦁 Test 3:", h.heap[0] == max(h.heap))
    h = MaxHeap()
    for val in [5, 3, 1]:
        h.insert(val)
    h.delete_max()
    print("🦁 Test 4:", h.heap == [3, 1])
    h = MaxHeap()
    h.insert(10)
    print("🦁 Test 5:", h.delete_max() == 10 and h.heap == [])

test_max_heap()
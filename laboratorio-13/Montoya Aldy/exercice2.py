class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

# Test for Challenge 2
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

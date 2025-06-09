class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

# Test for Challenge 1
def test_min_heap_init_and_empty():
    h = MinHeap()
    print("🌱 Test 1:", h.is_empty() == True)
    h.heap.append(1)
    print("🌱 Test 2:", h.is_empty() == False)

test_min_heap_init_and_empty()

test_results = []

def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_val

    def build_heap(self, array):
        self.heap = array[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] <= self.heap[parent]:
                break
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent

    def _heapify_down(self, index):
        while 2 * index + 1 < len(self.heap):
            larger_child_index = 2 * index + 1
            right_index = 2 * index + 2

            if right_index < len(self.heap) and self.heap[right_index] > self.heap[larger_child_index]:
                larger_child_index = right_index

            if self.heap[index] >= self.heap[larger_child_index]:
                break

            self.heap[index], self.heap[larger_child_index] = self.heap[larger_child_index], self.heap[index]
            index = larger_child_index

def test_1_5():
    heap = MaxHeap()

    # 1.5.1 MaxHeap insertion
    heap.insert(3)
    heap.insert(1)
    heap.insert(5)
    record_test("1.5.1 MaxHeap insertion", heap.heap[0] == 5)

    # 1.5.2 MaxHeap deletion
    max_val = heap.delete_max()
    record_test("1.5.2 MaxHeap deletion", max_val == 5)

    # 1.5.3 Build heap from array
    heap.build_heap([3, 1, 4, 1, 5, 9, 2])
    record_test("1.5.3 Build heap from array", heap.heap[0] == max(heap.heap))

    # 1.5.4 Heap property verification
    valid_max_heap = all(
        (heap.heap[i] >= heap.heap[2 * i + 1] if 2 * i + 1 < len(heap.heap) else True) and
        (heap.heap[i] >= heap.heap[2 * i + 2] if 2 * i + 2 < len(heap.heap) else True)
        for i in range(len(heap.heap) // 2)
    )
    record_test("1.5.4 Heap property verification", valid_max_heap)

    # 1.5.5 Empty array handling
    heap.build_heap([])
    record_test("1.5.5 Empty array handling", len(heap.heap) == 0)

# 🚀 Run tests
test_1_5()

# 📋 Summary
for r in test_results:
    print(r)
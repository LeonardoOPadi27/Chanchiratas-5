class CircularDeque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue_back(self, value):
        if self.size == self.capacity:
            raise Exception("Deque is full")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1

    def dequeue_front(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def dequeue_back(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        value = self.queue[self.rear]
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return value

    def peek_front(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.queue[self.front]

    def peek_back(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.queue[self.rear]

    def get_items(self):
        # Devuelve los elementos en orden
        items = []
        idx = self.front
        for _ in range(self.size):
            items.append(self.queue[idx])
            idx = (idx + 1) % self.capacity
        return items

def sliding_window_max(nums, k):
    n = len(nums)
    if k == 0 or n == 0:
        return []

    result = []
    deque = CircularDeque(n)  # almacenar índices

    for i in range(n):
        # Eliminar desde el frente si está fuera del rango
        if not deque.is_empty() and deque.peek_front() <= i - k:
            deque.dequeue_front()

        # Eliminar desde atrás todos los menores que nums[i]
        while not deque.is_empty() and nums[deque.peek_back()] < nums[i]:
            deque.dequeue_back()

        # Insertar índice actual
        deque.enqueue_back(i)

        # Agregar el máximo actual a resultado
        if i >= k - 1:
            result.append(nums[deque.peek_front()])

    return result
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_max(nums, k))
# Salida esperada: [3, 3, 5, 5, 6, 7]

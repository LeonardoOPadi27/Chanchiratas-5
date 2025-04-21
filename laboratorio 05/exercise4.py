class Deque:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0] if self.items else None

def sliding_window_max(nums, k):
    if not nums:
        return []

    max_values = []
    deq = Deque()

    for i in range(len(nums)):
        # Eliminar elementos fuera de la ventana
        if deq.items and deq.peek() <= i - k:
            deq.pop()

        # Mantener la cola en orden decreciente
        while deq.items and nums[deq.items[-1]] < nums[i]:
            deq.pop()

        deq.append(i)

        # Guardar el máximo de la ventana
        if i >= k - 1:
            max_values.append(nums[deq.peek()])

    return max_values

# Casos de prueba
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_max(nums, k))  # Resultado esperado: [3, 3, 5, 5, 5, 6, 7]
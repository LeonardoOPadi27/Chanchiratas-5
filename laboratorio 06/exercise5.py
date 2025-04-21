class CircularBuffer:
    def __init__(self, size):
        # Inicializa el búfer circular con un tamaño fijo
        self.size = size
        self.buffer = [None] * size  # Búfer vacío
        self.head = 0  # Apunta al primer elemento
        self.tail = 0  # Apunta al siguiente lugar para insertar
        self.full = False  # Indica si el búfer está lleno

    def add(self, data):
        # Agrega datos al búfer
        self.buffer[self.tail] = data
        self.tail = (self.tail + 1) % self.size  # Mueve el puntero tail de forma circular

        if self.tail == self.head:
            self.head = (self.head + 1) % self.size  # Si el búfer está lleno, sobrescribe el elemento más antiguo

        if self.tail == self.head:
            self.full = True  # El búfer se ha llenado

    def get_recent(self):
        # Devuelve los N elementos más recientes
        if self.full:
            return self.buffer[self.head:] + self.buffer[:self.head]  # Si está lleno, devuelve todos los elementos
        return self.buffer[:self.tail]  # Si no está lleno, solo los elementos actuales

    def statistics(self):
        # Calcula estadísticas como el número de elementos en el búfer
        count = self.size if self.full else self.tail
        return {
            'count': count,
            'buffer': self.get_recent()
        }

# Ejemplo de uso
buf = CircularBuffer(5)  # Crear un búfer circular de tamaño 5

# Agregar algunos datos
buf.add(1)
buf.add(2)
buf.add(3)
buf.add(4)
buf.add(5)

# Agregar un dato más, esto sobrescribirá el más antiguo (1)
buf.add(6)

# Obtener los N elementos más recientes
print(buf.get_recent())  # Salida: [2, 3, 4, 5, 6]

# Ver estadísticas del búfer
print(buf.statistics())  # Salida: {'count': 5, 'buffer': [2, 3, 4, 5, 6]}
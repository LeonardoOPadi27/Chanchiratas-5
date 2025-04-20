import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

def hot_potato_game(players, max_passes):
    queue = Queue()
    
    # Encolar todos los jugadores
    for player in players:
        queue.enqueue(player)

    while len(queue.items) > 1:  # Mientras haya más de un jugador
        num_passes = random.randint(1, max_passes)  # Número aleatorio de pases
        print(f"Pasando la patata {num_passes} veces.")
    
        # Realizar los pases
        for _ in range(num_passes):
            player = queue.dequeue()  # Sacamos al jugador de la cola
            queue.enqueue(player)  # Lo volvemos a poner en la cola

        # El jugador con la "Patata Caliente" se elimina
        eliminated_player = queue.dequeue()
        print(f"{eliminated_player} ha sido eliminado.")

    # El único jugador restante es el ganador
    winner = queue.dequeue()
    return winner

# Casos de prueba

players = ["Alice", "Bob", "Charlie", "David", "Eve", "ccaihuari", "elliot", "jenxy"]
max_passes = 5
winner = hot_potato_game(players, max_passes)
print(f"El ganador es: {winner}")
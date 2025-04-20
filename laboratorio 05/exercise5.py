import random

class Cliente:
    def __init__(self, id_cliente, cantidad_articulos):
        self.id_cliente, self.cantidad_articulos = id_cliente, cantidad_articulos
        self.tiempo_llegada, self.tiempo_salida = None, None

class Caja:
    def __init__(self, tasa_procesamiento):
        self.tasa_procesamiento, self.cola = tasa_procesamiento, []

    def procesar_cliente(self, tiempo_transcurrido):
        if self.cola and (self.cola[0].cantidad_articulos / self.tasa_procesamiento) <= tiempo_transcurrido:
            cliente = self.cola.pop(0)
            cliente.tiempo_salida = tiempo_transcurrido

    def agregar_cliente(self, cliente):
        self.cola.append(cliente)

    def longitud_cola(self):
        return len(self.cola)

class Supermercado:
    def __init__(self, num_cajas, tasas_procesamiento):
        self.cajas = [Caja(tasa) for tasa in tasas_procesamiento]
        self.clientes_llegados = []

    def llegar_cliente(self, cliente):
        caja = min(self.cajas, key=lambda c: c.longitud_cola())
        caja.agregar_cliente(cliente)
        cliente.tiempo_llegada = 0
        self.clientes_llegados.append(cliente)

    def simular_tiempo(self, tiempo_maximo):
        for t in range(tiempo_maximo):
            for caja in self.cajas:
                caja.procesar_cliente(t)

    def calcular_estadisticas(self):
        total_espera = sum(c.tiempo_salida - c.tiempo_llegada for c in self.clientes_llegados if c.tiempo_salida)
        return total_espera / len(self.clientes_llegados), [len(c.cola) for c in self.cajas]

# Casos de prueba
def prueba(cajas, clientes):
    supermercado = Supermercado(len(cajas), cajas)
    for i, articulos in enumerate(clientes):
        cliente = Cliente(i, articulos)
        supermercado.llegar_cliente(cliente)
    supermercado.simular_tiempo(30)
    espera, rendimiento = supermercado.calcular_estadisticas()
    print(f"Tiempo promedio de espera: {espera:.2f}, Rendimiento de cajas: {rendimiento}")

# Ejecutar las pruebas
prueba([3, 4, 5], [random.randint(1, 20) for _ in range(10)])
prueba([2, 3], [random.randint(1, 10) for _ in range(5)])
prueba([1, 2, 3, 4], [random.randint(5, 15) for _ in range(8)])
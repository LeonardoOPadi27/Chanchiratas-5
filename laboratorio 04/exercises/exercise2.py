import sys
try:
    if sys.stdout.encoding.lower() != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass


class FixedStack:
    def __init__(self, capacidad):
        self.stack = [None] * capacidad
        self.top = -1
        self.capacidad = capacidad

    def push(self, dato):
        if self.top >= self.capacidad - 1:
            print("❌ [Fijo] Error: Pila llena")
            return
        self.top += 1
        self.stack[self.top] = dato
        print(f"✅ [Fijo] Push: {dato} (top = {self.top})")

    def pop(self):
        if self.top < 0:
            print("❌ [Fijo] Error: Pila vacía")
            return None
        valor = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        print(f"🔻 [Fijo] Pop: {valor} (top = {self.top})")
        return valor


class DynamicStack:
    def __init__(self):
        self.stack = []

    def push(self, dato):
        self.stack.append(dato)
        print(f"✅ [Dinámico] Push: {dato}")

    def pop(self):
        if not self.stack:
            print("❌ [Dinámico] Error: Pila vacía")
            return None
        valor = self.stack.pop()
        print(f"🔻 [Dinámico] Pop: {valor}")
        return valor


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.sig = self.top
        self.top = nuevo
        print(f"✅ [Enlazada] Push: {dato}")

    def pop(self):
        if not self.top:
            print("❌ [Enlazada] Error: Pila vacía")
            return None
        valor = self.top.dato
        self.top = self.top.sig
        print(f"🔻 [Enlazada] Pop: {valor}")
        return valor


if __name__ == "__main__":
    print("\n🔷 PRUEBA: PILA CON ARRAY FIJO")
    fs = FixedStack(3)
    fs.push(10)
    fs.push(20)
    fs.push(30)
    fs.push(40)  # Error
    fs.pop()
    fs.pop()
    fs.pop()
    fs.pop()     # Error

    print("\n🔷 PRUEBA: PILA CON ARRAY DINÁMICO")
    ds = DynamicStack()
    ds.push(5)
    ds.push(15)
    ds.push(25)
    ds.pop()
    ds.push(35)
    ds.pop()
    ds.pop()

    print("\n🔷 PRUEBA: PILA CON LISTA ENLAZADA")
    ls = LinkedListStack()
    ls.push(100)
    ls.push(200)
    ls.pop()
    ls.push(300)
    ls.pop()
    ls.pop()
    ls.pop()  # Error

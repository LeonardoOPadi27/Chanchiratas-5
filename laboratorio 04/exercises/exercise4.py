import sys
try:
    if sys.stdout.encoding.lower() != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass


# Variables globales
contenido = ""
historial = []


def escribir(texto):
    """Agrega texto al contenido y guarda la operación en el historial."""
    global contenido, historial
    contenido += texto
    historial.append(("eliminar", len(texto)))
    print(f"✍ Escribiendo: '{texto}'")


def eliminar(n):
    """Elimina los últimos n caracteres del contenido y guarda la operación."""
    global contenido, historial
    if n > len(contenido):
        n = len(contenido)
    texto_eliminado = contenido[-n:]
    contenido = contenido[:-n]
    historial.append(("escribir", texto_eliminado))
    print(f"❌ Eliminando últimos {n} caracteres")


def deshacer():
    """Deshace la última operación registrada en el historial."""
    global historial
    if not historial:
        print("🔁 Nada que deshacer.")
        return

    operacion, dato = historial.pop()
    if operacion == "eliminar":
        eliminar(dato)
    elif operacion == "escribir":
        escribir(dato)


def mostrar():
    """Muestra el contenido actual del texto."""
    print(f"📄 Contenido actual: '{contenido}'")


# Prueba del editor
if __name__ == "__main__":
    escribir("Hola")
    mostrar()

    escribir(" mundo")
    mostrar()

    eliminar(6)
    mostrar()

    deshacer()
    mostrar()

    deshacer()
    mostrar()

    deshacer()
    mostrar()
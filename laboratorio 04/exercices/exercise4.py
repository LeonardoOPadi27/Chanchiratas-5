contenido = ""
historial = []

# Por ejemplo, para escribir algo:
def escribir(texto):
    global contenido, historial
    contenido += texto
    historial.append(("eliminar", len(texto)))

# Para eliminar N caracteres:
def eliminar(n):
    global contenido, historial
    texto_eliminado = contenido[-n:]
    contenido = contenido[:-n]
    historial.append(("escribir", texto_eliminado))

# Para deshacer:
def deshacer():
    global historial
    if not historial:
        print("Nada que deshacer.")
        return

    operacion, dato = historial.pop()
    if operacion == "eliminar":
        eliminar(dato)
    elif operacion == "escribir":
        escribir(dato)

# Mostrar el contenido actual:
def mostrar():
    print(f"Contenido actual: '{contenido}'")
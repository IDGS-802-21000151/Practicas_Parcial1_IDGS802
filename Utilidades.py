# Solicitar cantidad de números
def solicitarCantidadNumeros(mensaje):
    return int(input(mensaje))

# Solicitar números
def solicitarNumeros(cantidadNumeros):
    listaNumeros = []

    for i in range(cantidadNumeros):
        listaNumeros.append(int(input(f"Ingresa el número {i + 1}: ")))
        
    return listaNumeros
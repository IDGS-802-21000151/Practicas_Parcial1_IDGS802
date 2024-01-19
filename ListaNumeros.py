import Utilidades

class ListaNumeros:
    listaNumeros = []
    
    # Inicializador
    def __init__(self, listaNumeros):
        self.listaNumeros = listaNumeros
    
    # Ordenar lista
    def ordenarLista(self):
        print("\nOrdenando lista")
        
        listaClon = self.listaNumeros
        listaClon.sort()
        
        print(listaClon)
        
    # Obtener pares
    def obtenerPares(self):
        print("\n\nObteniendo lista de pares")
        
        listaNumerosPares = []
    
        for numero in self.listaNumeros:
            if numero % 2 == 0:
                listaNumerosPares.append(numero)
        
        print(listaNumerosPares)
        
    # Obtener impares
    def obtenerImpares(self):
        print("\n\nObteniendo lista de impares")
        
        listaNumerosImpares = []
    
        for numero in self.listaNumeros:
            if numero % 2 != 0:
                listaNumerosImpares.append(numero)
                
        print(listaNumerosImpares)

    # Obtener números repetidos
    def obtenerRepetidos(self):
        print("\n\nObteniendo números repetidos")
        
        diccionarioNumerosRepetidos = {}
    
        for numero in self.listaNumeros:
            if numero in diccionarioNumerosRepetidos:
                diccionarioNumerosRepetidos[numero] += 1
            else:
                diccionarioNumerosRepetidos[numero] = 1
                
        print(diccionarioNumerosRepetidos)
                
        for numero_repetido in diccionarioNumerosRepetidos:
            veces_repetido = diccionarioNumerosRepetidos[numero_repetido]
            
            if veces_repetido > 1:
                print(f"El número {numero_repetido} se repitió {veces_repetido} veces.")
                
def main():
    print("Iniciando programa...\n\n")
    
    cantidadNumeros = Utilidades.solicitarCantidadNumeros("Cuantos números vas a ingresar: ")
    
    listaNumeros = Utilidades.solicitarNumeros(cantidadNumeros)
    
    objetoListaNumeros = ListaNumeros(listaNumeros)
    
    objetoListaNumeros.ordenarLista()
    objetoListaNumeros.obtenerPares()
    objetoListaNumeros.obtenerImpares()
    objetoListaNumeros.obtenerRepetidos()
                    
if __name__ == "__main__":
    main()
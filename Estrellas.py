import Utilidades

class Estrellas:
    def imprimirEstrellas(cantidadFilas):
        for fila in range(1, cantidadFilas + 1):
            estrellas = ""
            
            for columna in range(fila):
                estrellas += "*"
                
            print(estrellas)

def main():
    print("Iniciando programa...\n\n")
    
    cantidadFilas = Utilidades.solicitarCantidadNumeros("Cuantas filas de estrellas necesitas: ")
    
    Estrellas.imprimirEstrellas(cantidadFilas)

if __name__ == "__main__":
    main()
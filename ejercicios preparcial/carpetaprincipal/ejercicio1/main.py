from lista import Lista
class Main():
    def main():
        opcion= 999
        
        miLista = Lista()
        while opcion != 0:
            dato= 0
            opcion = int(input("Menú Lista Simple:\n"+
                               "1. Agregar al inicio.\n"+
                               "Ingrese la opción --> "))
            
            if opcion == 1:
                for i in range(6):
                    dato=int(input("Ingrese un dato para la lista: "))
                    miLista.agregarInicio(dato)
                miLista.imprimirLista()
            



    main()
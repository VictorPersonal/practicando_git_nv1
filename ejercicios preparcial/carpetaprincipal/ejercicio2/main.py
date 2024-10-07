from lista import Lista
class Main():
    def main():
        opcion= 999
        
        miLista = Lista()
        while opcion != 0:
            dato= 0
            opcion = int(input("Menú Lista Simple:\n"+
                               "1. Agregar al final.\n"+
                               "2. Eliminar al inicio.\n"+
                               "Ingrese la opción --> "))
            
            if opcion == 1:
                for i in range(16):
                    dato=int(input(f"Ingrese el dato {i+1} para la lista: "))
                    miLista.agregarFinal(dato)
                miLista.imprimirLista()

            elif opcion == 2:
                
                    miLista.eliminarInicio()
                    miLista.imprimirLista()
            



    main()